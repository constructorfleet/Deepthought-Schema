"""Checks generator registration for the DeepThought CLI."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from deepthought.catalog import CatalogError, CatalogValidationError, load_catalog
from deepthought.meta_schemas import bundled_schemas_dir


class ChecksGenerator:
    """Expose machine-readable correctness manifests on the CLI."""

    name = "checks"
    summary = "Machine-readable correctness manifests."

    def register_cli(self, subparsers) -> None:
        checks_parser = subparsers.add_parser(
            self.name,
            help=self.summary,
            description=(
                "Generate catalog-backed JSON manifests for correctness checks, "
                "including scenarios, invariants, permission rules, and state "
                "machine transitions."
            ),
        )
        checks_subparsers = checks_parser.add_subparsers(
            dest="checks_command", required=True
        )

        build_parser = checks_subparsers.add_parser(
            "build",
            help="Generate JSON correctness manifests.",
            description=(
                "Generate JSON manifests from the validated spec catalog so downstream "
                "tooling can consume correctness checks without reparsing YAML."
            ),
        )
        build_parser.add_argument(
            "--schemas",
            type=Path,
            default=None,
            help=(
                "directory of meta-schemas to validate against. Defaults to the "
                "canonical meta-schema directory."
            ),
        )
        build_parser.add_argument(
            "--spec",
            type=Path,
            default=None,
            help="directory of consumer YAML to render into correctness manifests.",
        )
        build_parser.add_argument(
            "--out",
            type=Path,
            default=Path("checks"),
            help="output directory (default: ./checks)",
        )
        build_parser.add_argument(
            "--clean",
            action="store_true",
            help="wipe <out> before building",
        )
        build_parser.set_defaults(func=self.run)

    def run(self, args) -> int:
        from deepthought.checks.render import render_checks_manifest

        if args.spec is None:
            print("checks build requires --spec <dir>", file=sys.stderr)
            return 2

        schemas_dir = args.schemas or bundled_schemas_dir()
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

        render_checks_manifest(catalog, args.spec, args.out)
        print(f"checks manifest generated under {args.out}/")
        return 0
