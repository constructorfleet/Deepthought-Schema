"""Render Markdown documentation from DeepThought meta-schemas and specs.

Two render modes are exposed:

* :func:`render_reference` -- reference docs for a directory of JSON
  Schemas. Used by the deepthought-schema repo itself to publish the
  language reference; also useful for projects that ship their own
  meta-schemas alongside their domain specs.
* :func:`render_spec` -- per-entity domain docs for a directory of YAML
  specs (fields, models, use cases, ...). Cross-references are rendered
  as inline links between pages.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import yaml
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

from deepthought._refs import prepare_for_rendering
from deepthought.catalog import Catalog, load_catalog
from deepthought.meta_schemas import (
    META_SUFFIX,
    iter_schema_paths,
    schema_name,
)

# json-schema-for-humans walks recursively defined schemas (the
# expression AST in particular) deeper than CPython's default limit.
# Bumping the limit here keeps the work bounded; the cycle-breaker in
# `_refs.py` prevents the actual recursion from being unbounded.
sys.setrecursionlimit(50000)


def _render_one(json_path: Path, out_path: Path) -> None:
    cfg = GenerationConfiguration(
        template_name="md",
        show_toc=True,
        with_footer=False,
        copy_css=False,
        copy_js=False,
        recursive_detection_depth=3,
        link_to_reused_ref=True,
        description_is_markdown=True,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    generate_from_filename(str(json_path), str(out_path), config=cfg)


def _example_block(path: Path) -> str:
    return "```yaml\n" + path.read_text().rstrip() + "\n```\n"


def _append_examples(
    name: str,
    page_path: Path,
    examples_root: Path | None,
) -> int:
    if examples_root is None:
        return 0
    candidates: list[Path] = []
    sub_dir = examples_root / name
    if sub_dir.is_dir():
        candidates.extend(sorted(sub_dir.glob("*.yaml")))
        candidates.extend(sorted(sub_dir.glob("*.yml")))
    suffix_glob = f"*.{name}.yaml"
    candidates.extend(sorted(examples_root.glob(suffix_glob)))
    candidates.extend(sorted(examples_root.glob(f"*.{name}.yml")))
    candidates = sorted(set(candidates))
    if not candidates:
        return 0
    parts = ["\n\n---\n\n## Examples\n\n"]
    parts.append(
        "Every example below is validated against this schema as part of "
        "the docs build; if a build ships these examples, they still "
        "describe the schema correctly.\n\n"
    )
    for path in candidates:
        title = path.stem.replace(f".{name}", "").replace("_", " ").title()
        rel = path.name
        try:
            rel = str(path.relative_to(examples_root))
        except ValueError:
            pass
        parts.append(f"### {title}\n\n*Source: `{rel}`*\n\n")
        parts.append(_example_block(path))
        parts.append("\n")
    with page_path.open("a") as f:
        f.write("".join(parts))
    return len(candidates)


def _index_page(
    title: str,
    schema_paths: list[Path],
    example_counts: dict[str, int],
    *,
    intro: str,
) -> str:
    lines: list[str] = [
        "---",
        f"title: {title}",
        "layout: default",
        "---",
        "",
        f"# {title}",
        "",
        intro,
        "",
        "## Reference pages",
        "",
        "| Schema | Examples |",
        "| --- | --- |",
    ]
    for path in sorted(schema_paths):
        name = schema_name(path)
        n = example_counts.get(name, 0)
        ex_label = f"{n}" if n else "—"
        lines.append(f"| [{name}](./reference/{name}.md) | {ex_label} |")
    return "\n".join(lines) + "\n"


def _jekyll_config(title: str, description: str) -> str:
    return (
        f"title: {title}\n"
        f"description: {description}\n"
        "theme: jekyll-theme-cayman\n"
        "markdown: kramdown\n"
        "kramdown:\n"
        "  syntax_highlighter: rouge\n"
        "  parse_block_html: true\n"
    )


def _display_kind(kind: str) -> str:
    return kind.replace("_", " ").title()


def _entry_source_label(entry, spec_root: Path) -> str:
    try:
        rel = entry.path.relative_to(spec_root)
    except ValueError:
        rel = entry.path
    source = f"source: `{rel}`"
    if entry.parent_identifier is not None:
        source += f"; nested under `{entry.parent_identifier}`"
    return source


def render_catalog(
    catalog: Catalog,
    spec_root: Path,
    out_dir: Path,
    *,
    title: str = "Domain Reference",
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    reference_dir = out_dir / "spec"
    reference_dir.mkdir(parents=True, exist_ok=True)

    for kind in catalog.kinds:
        entries = sorted(catalog.iter_kind(kind), key=lambda entry: entry.identifier)
        page_lines = [
            "---",
            f"title: {_display_kind(kind)}",
            "layout: default",
            "---",
            "",
            f"# {_display_kind(kind)}",
            "",
        ]
        for entry in entries:
            data = entry.data
            name = data.get("name", entry.identifier)
            description = data.get("description", "")
            page_lines.append(f"## {name}")
            page_lines.append("")
            page_lines.append(
                f"`{entry.identifier}`  *({_entry_source_label(entry, spec_root)})*"
            )
            page_lines.append("")
            if description:
                page_lines.append(description)
                page_lines.append("")
        (reference_dir / f"{kind}.md").write_text("\n".join(page_lines) + "\n")

    index_lines = [
        "---",
        f"title: {title}",
        "layout: default",
        "---",
        "",
        f"# {title}",
        "",
        "Per-kind indexes generated from the validated DeepThought catalog.",
        "",
    ]
    for kind in catalog.kinds:
        index_lines.append(
            f"- [{_display_kind(kind)}](./spec/{kind}.md) "
            f"({len(tuple(catalog.iter_kind(kind)))} entries)"
        )
    (out_dir / "index.md").write_text("\n".join(index_lines) + "\n")

    config_path = out_dir / "_config.yml"
    if not config_path.exists():
        config_path.write_text(_jekyll_config(title, "DeepThought domain spec"))


def render_reference(
    schemas_dir: Path,
    out_dir: Path,
    *,
    examples_dir: Path | None = None,
    title: str = "DeepThought Schema",
    intro: str = (
        "DeepThought is a Documentation-Driven Development specification "
        "language: every concept its meta-schemas describe is documented "
        "*inherent* to the schema (via `title` and `description`), so the "
        "reference pages below are generated directly from the YAML in "
        "`meta-schema/`. Examples are validated against those schemas on "
        "every build, so the worked examples on the reference pages can't "
        "rot away from the contracts they illustrate."
    ),
    clean: bool = False,
) -> dict[str, int]:
    """Generate Markdown reference pages for every meta-schema in
    ``schemas_dir`` under ``out_dir``. Returns a mapping of schema name to
    example count rendered alongside that schema.
    """
    if clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    reference_dir = out_dir / "reference"
    reference_dir.mkdir(parents=True, exist_ok=True)
    tmp_dir = out_dir / ".tmp"
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir()

    schema_paths = list(iter_schema_paths(schemas_dir))
    example_counts: dict[str, int] = {}
    for path in schema_paths:
        name = schema_name(path)
        with path.open() as f:
            raw = yaml.safe_load(f)
        prepared = prepare_for_rendering(raw)
        json_path = tmp_dir / f"{name}.json"
        with json_path.open("w") as f:
            json.dump(prepared, f, indent=2)
        out = reference_dir / f"{name}.md"
        _render_one(json_path, out)
        example_counts[name] = _append_examples(name, out, examples_dir)

    (out_dir / "index.md").write_text(
        _index_page(title, schema_paths, example_counts, intro=intro)
    )
    config_path = out_dir / "_config.yml"
    if not config_path.exists():
        config_path.write_text(
            _jekyll_config(
                title,
                "Documentation-Driven Development specification language",
            )
        )

    shutil.rmtree(tmp_dir)
    return example_counts


def render_spec(
    spec_dir: Path,
    out_dir: Path,
    *,
    schemas_dir: Path | None = None,
    title: str = "Domain Reference",
) -> None:
    """Render per-entity documentation for a consumer's validated spec directory."""

    catalog = load_catalog(spec_dir, schemas_dir=schemas_dir)
    render_catalog(catalog, spec_dir, out_dir, title=title)
