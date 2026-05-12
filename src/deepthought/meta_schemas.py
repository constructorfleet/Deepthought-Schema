"""Locate and load the DeepThought meta-schemas.

There is a single canonical location for the meta-schemas -- the
``meta-schema/`` directory at the repository root. The package does not
maintain a separate bundled copy; duplication would be exactly the kind
of doc-rot this project exists to prevent.

In editable / development installs the lookup walks up from this
module's ``__file__`` to find ``meta-schema/`` at the repo root. When
the project is published as a wheel, a build-time hook will copy the
canonical files into the package as ``deepthought/schemas/`` and
``bundled_schemas_dir`` will resolve to that location instead. The
fallback order in :func:`bundled_schemas_dir` makes both modes work
without configuration.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import yaml


META_SUFFIX = ".meta.yaml"

# Locations searched, in order, when no override is supplied.
_CANDIDATE_SUBPATHS = (
    # Wheel / sdist install: copied into the package at build time.
    Path("schemas"),
    # Editable / dev install: canonical location at the repo root.
    Path("..") / ".." / ".." / "meta-schema",
    Path("..") / ".." / "meta-schema",
)


def bundled_schemas_dir() -> Path:
    """Return the canonical directory holding the meta-schemas.

    Searches relative to this module's location for either a packaged
    ``schemas/`` directory (built distributions) or the canonical
    ``meta-schema/`` directory at the repo root (editable installs).
    Raises ``RuntimeError`` if neither location contains meta-schemas;
    callers can override the lookup by passing ``schemas_dir`` to the
    other functions in this module.
    """
    here = Path(__file__).resolve().parent
    for sub in _CANDIDATE_SUBPATHS:
        candidate = (here / sub).resolve()
        if candidate.is_dir() and any(candidate.glob(f"*{META_SUFFIX}")):
            return candidate
    raise RuntimeError(
        "deepthought: could not locate the meta-schema directory. "
        "Pass --schemas <dir> on the CLI, or set the schemas_dir argument."
    )


def iter_schema_paths(schemas_dir: Path | None = None) -> Iterable[Path]:
    """Yield every ``*.meta.yaml`` in the supplied (or default) directory."""
    base = schemas_dir or bundled_schemas_dir()
    yield from sorted(base.glob(f"*{META_SUFFIX}"))


def schema_name(path: Path) -> str:
    """Strip ``.meta.yaml`` to get the canonical schema name."""
    return path.name.removesuffix(META_SUFFIX)


def load_meta_schemas(schemas_dir: Path | None = None) -> dict[str, dict]:
    """Load all meta-schemas from ``schemas_dir`` (or the default location)
    keyed by every URI form ``$ref`` could reach them through.

    A meta-schema with ``$id: https://example.com/.../field`` containing
    ``$ref: "unit.meta.yaml"`` resolves the reference against the parent
    of its own ``$id``, producing a synthetic URL like
    ``https://example.com/.../unit.meta.yaml`` -- which is *not* the
    referenced schema's ``$id``. The store must include both forms or
    the validator falls through to HTTP fetching.

    Suitable for direct use as a :class:`jsonschema.RefResolver` store.
    """
    paths = list(iter_schema_paths(schemas_dir))
    by_name: dict[str, dict] = {}
    for path in paths:
        with path.open() as f:
            by_name[path.name] = yaml.safe_load(f)

    store: dict[str, dict] = {}
    id_parents: list[str] = []
    for path in paths:
        schema = by_name[path.name]
        store[path.resolve().as_uri()] = schema
        if isinstance(schema, dict) and "$id" in schema:
            store[schema["$id"]] = schema
            parent = schema["$id"].rsplit("/", 1)[0] + "/"
            if parent not in id_parents:
                id_parents.append(parent)

    for parent in id_parents:
        for filename, schema in by_name.items():
            store[parent + filename] = schema

    return store
