"""Validate DeepThought YAML specifications against the meta-schemas.

Two modes of input are supported:

* **Subdirectory layout** -- ``examples/<schema>/*.yaml`` where each leaf
  YAML is validated against ``meta-schema/<schema>.meta.yaml``. This is
  the layout used inside the deepthought-schema repository itself.

* **Suffix layout** -- ``specs/foo.field.yaml``, ``specs/bar.model.yaml``,
  etc. The kind embedded in the filename selects the meta-schema. This
  is the layout most consumer projects use; it lets fields, models, and
  use cases coexist in a flat directory without sub-folders per kind.

A consumer can mix both layouts in the same root and the validator will
do the right thing -- subdirectory layout takes precedence when it is
present.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml
from jsonschema import Draft7Validator
from jsonschema.validators import RefResolver

from deepthought.meta_schemas import (
    META_SUFFIX,
    bundled_schemas_dir,
    iter_schema_paths,
    load_meta_schemas,
    schema_name,
)


KIND_FILENAME_RE = re.compile(r"\.(?P<kind>[a-z][a-z_]*)\.ya?ml$", re.IGNORECASE)


@dataclass(frozen=True)
class ValidationError:
    """A single validation failure -- file path, json-pointer, message."""

    path: Path
    pointer: str
    message: str

    def format(self, *, root: Path | None = None) -> str:
        rel = self.path.relative_to(root) if root else self.path
        return f"{rel} at {self.pointer}: {self.message}"


def _make_resolver(store: dict[str, dict], schemas_dir: Path) -> RefResolver:
    base = schemas_dir.resolve().as_uri() + "/"
    return RefResolver(base_uri=base, referrer={}, store=store)


def _kind_for_path(path: Path, root: Path) -> str | None:
    """Determine which meta-schema a YAML file targets.

    Subdirectory layout wins when applicable: a file at
    ``<root>/<kind>/<name>.yaml`` is treated as kind ``<kind>``.
    Otherwise the filename suffix ``.<kind>.yaml`` is consulted.
    """
    try:
        rel = path.relative_to(root)
    except ValueError:
        rel = path
    if len(rel.parts) > 1:
        candidate = rel.parts[0]
        if candidate.replace("_", "").isalpha():
            return candidate
    match = KIND_FILENAME_RE.search(path.name)
    if match:
        return match.group("kind")
    return None


def _branch_schema_name(schema: object) -> str | None:
    if not isinstance(schema, dict):
        return None
    title = schema.get("title")
    if isinstance(title, str) and title:
        return title
    ref = schema.get("$ref")
    if isinstance(ref, str) and ref:
        return ref.rstrip("/").rsplit("/", 1)[-1].removesuffix(META_SUFFIX)
    return None


def _branch_label(err, sub) -> str | None:
    if err.validator not in {"oneOf", "anyOf", "allOf"}:
        return None
    schema_path = tuple(sub.schema_path)
    if not schema_path or not isinstance(schema_path[0], int):
        return None
    branch_index = schema_path[0]
    label = f"{err.validator} branch {branch_index}"
    branch_schemas = err.schema.get(err.validator) if isinstance(err.schema, dict) else None
    branch_schema = None
    if isinstance(branch_schemas, list) and 0 <= branch_index < len(branch_schemas):
        branch_schema = branch_schemas[branch_index]
    name = _branch_schema_name(branch_schema) or _branch_schema_name(sub.schema)
    if name:
        label = f"{label} ({name})"
    return label


def _format_context_error(err, sub) -> str:
    label = _branch_label(err, sub)
    schema_path = "/".join(str(p) for p in sub.absolute_schema_path)
    message = f"[{schema_path}] {_flatten_error(sub)}"
    if label:
        return f"{label}: {message}"
    return message


def _flatten_error(err) -> str:
    """Render a jsonschema error with sub-context inline.

    ``oneOf``/``anyOf``/``allOf`` failures are uninformative on their own
    -- they say "no branch matched" without naming which branch failed
    where. Walking ``err.context`` and prepending the attempted branch plus
    schema-pointer of each sub-error makes the message actionable.
    """
    parts = [err.message]
    if err.context:
        details = [_format_context_error(err, sub) for sub in err.context]
        parts.append(" | ".join(details))
    return " :: ".join(parts)


def _validate_one(
    path: Path,
    meta: dict,
    resolver: RefResolver,
    *,
    root: Path,
) -> list[ValidationError]:
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        return [ValidationError(path=path, pointer="(root)", message=f"yaml parse error: {exc}")]
    validator = Draft7Validator(meta, resolver=resolver)
    errors: list[ValidationError] = []
    for err in validator.iter_errors(data):
        pointer = "/".join(str(p) for p in err.path) or "(root)"
        errors.append(ValidationError(path=path, pointer=pointer, message=_flatten_error(err)))
    return errors


def _candidate_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.yaml")):
        if path.is_file():
            yield path
    for path in sorted(root.rglob("*.yml")):
        if path.is_file():
            yield path


def validate_file(
    path: Path,
    *,
    kind: str | None = None,
    schemas_dir: Path | None = None,
) -> list[ValidationError]:
    """Validate a single YAML file. ``kind`` overrides the file's inferred
    meta-schema when supplied.
    """
    schemas_dir = schemas_dir or bundled_schemas_dir()
    store = load_meta_schemas(schemas_dir)
    resolver = _make_resolver(store, schemas_dir)
    inferred = kind or _kind_for_path(path, path.parent)
    if inferred is None:
        return [
            ValidationError(
                path=path,
                pointer="(root)",
                message=(
                    "could not infer meta-schema kind; expected a "
                    "<kind>/<file>.yaml subdirectory or a .<kind>.yaml suffix"
                ),
            )
        ]
    meta_path = schemas_dir / f"{inferred}{META_SUFFIX}"
    if not meta_path.exists():
        return [
            ValidationError(
                path=path,
                pointer="(root)",
                message=f"no meta-schema named {inferred!r}",
            )
        ]
    meta = store[meta_path.resolve().as_uri()]
    return _validate_one(path, meta, resolver, root=path.parent)


def validate_directory(
    root: Path,
    *,
    schemas_dir: Path | None = None,
) -> list[ValidationError]:
    """Recursively validate every ``*.yaml`` / ``*.yml`` file under ``root``.

    Files that don't match either the subdirectory or suffix conventions
    are skipped silently -- callers can pre-filter input or pass
    ``--strict`` at the CLI to surface skipped files.
    """
    schemas_dir = schemas_dir or bundled_schemas_dir()
    store = load_meta_schemas(schemas_dir)
    resolver = _make_resolver(store, schemas_dir)
    errors: list[ValidationError] = []
    known = {schema_name(p) for p in iter_schema_paths(schemas_dir)}
    for path in _candidate_files(root):
        kind = _kind_for_path(path, root)
        if kind is None or kind not in known:
            continue
        meta_path = schemas_dir / f"{kind}{META_SUFFIX}"
        meta = store[meta_path.resolve().as_uri()]
        errors.extend(_validate_one(path, meta, resolver, root=root))
    return errors
