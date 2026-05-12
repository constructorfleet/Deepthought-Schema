"""Docs generator registration for the DeepThought CLI."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from deepthought.catalog import CatalogError, CatalogValidationError, load_catalog
from deepthought.meta_schemas import bundled_schemas_dir
from deepthought.validate import validate_directory


class DocsGenerator:
    """Expose documentation generation on the CLI."""

    name = "docs"
    summary = "Documentation generation."

    def register_cli(self, subparsers) -> None:
        docs_parser = subparsers.add_parser(
            self.name,
            help=self.summary,
            description="Generate Markdown documentation from meta-schemas or specs.",
        )
        docs_subparsers = docs_parser.add_subparsers(dest="docs_command", required=True)

        build_parser = docs_subparsers.add_parser(
            "build",
            help="Generate a Markdown documentation site.",
            description=(
                "Generate a static site under <out>. In `reference` mode the "
                "input is a directory of JSON Schema documents; in `spec` mode "
                "the input is a directory of consumer YAML conforming to the "
                "DeepThought meta-schemas."
            ),
        )
        build_parser.add_argument(
            "--mode",
            choices=("reference", "spec"),
            default="reference",
            help="reference: render schema docs (default). spec: render domain docs.",
        )
        build_parser.add_argument(
            "--schemas",
            type=Path,
            default=None,
            help=(
                "reference mode: directory of meta-schemas to render. spec mode: "
                "directory of meta-schemas to validate against. Defaults to the "
                "canonical meta-schema directory."
            ),
        )
        build_parser.add_argument(
            "--examples",
            type=Path,
            default=None,
            help="reference mode: directory of YAML examples to validate and embed.",
        )
        build_parser.add_argument(
            "--spec",
            type=Path,
            default=None,
            help="spec mode: directory of consumer YAML to render.",
        )
        build_parser.add_argument(
            "--out",
            type=Path,
            default=Path("docs"),
            help="output directory (default: ./docs)",
        )
        build_parser.add_argument(
            "--title",
            default=None,
            help="page title (default: 'DeepThought Schema' in reference mode)",
        )
        build_parser.add_argument(
            "--clean",
            action="store_true",
            help="wipe <out> before building",
        )
        build_parser.set_defaults(func=self.run)

    def run(self, args) -> int:
        from deepthought.docs.render import render_catalog, render_reference

        schemas_dir = args.schemas or bundled_schemas_dir()

        if args.mode == "reference":
            if args.examples is not None:
                errors = validate_directory(args.examples, schemas_dir=schemas_dir)
                if errors:
                    print(
                        f"example validation failed ({len(errors)} error(s)):",
                        file=sys.stderr,
                    )
                    for err in errors:
                        print(f"  {err.format(root=args.examples)}", file=sys.stderr)
                    return 1
            kwargs: dict = {
                "examples_dir": args.examples,
                "clean": args.clean,
            }
            if args.title:
                kwargs["title"] = args.title
            render_reference(schemas_dir, args.out, **kwargs)
            print(f"reference docs generated under {args.out}/")
            return 0

        if args.spec is None:
            print("spec mode requires --spec <dir>", file=sys.stderr)
            return 2
        try:
            catalog = load_catalog(args.spec, schemas_dir=schemas_dir)
        except CatalogValidationError as exc:
            print(
                f"spec validation failed ({len(exc.errors)} error(s)):",
                file=sys.stderr,
            )
            for err in exc.errors:
                print(f"  {err.format(root=args.spec)}", file=sys.stderr)
            return 1
        except CatalogError as exc:
            print(f"spec catalog load failed: {exc}", file=sys.stderr)
            return 1
        if args.clean and args.out.exists():
            shutil.rmtree(args.out)
        render_catalog(
            catalog, args.spec, args.out, title=args.title or "Domain Reference"
        )
        print(f"spec docs generated under {args.out}/")
        return 0
