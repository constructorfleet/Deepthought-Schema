"""Tests generator registration for the DeepThought CLI."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from deepthought.catalog import CatalogError, CatalogValidationError, load_catalog
from deepthought.meta_schemas import bundled_schemas_dir


class TestsGenerator:
    """Expose language-neutral and backend-specific test generation on the CLI."""

    name = "tests"
    summary = "Generated test plans and correctness checks."

    def register_cli(self, subparsers) -> None:
        tests_parser = subparsers.add_parser(
            self.name,
            help=self.summary,
            description=(
                "Generate catalog-backed test outputs from DeepThought "
                "specifications."
            ),
        )
        tests_subparsers = tests_parser.add_subparsers(
            dest="tests_command", required=True
        )

        build_parser = tests_subparsers.add_parser(
            "build",
            help="Generate test outputs from the validated catalog.",
            description=(
                "Generate language-neutral manifests or backend-specific test "
                "surfaces from the validated spec catalog, including Given/When/Then "
                "scenarios and model invariants."
            ),
        )
        build_parser.add_argument(
            "--format",
            choices=("go", "manifest", "markdown", "rust", "typescript", "unittest"),
            default="markdown",
            help=(
                "manifest: language-neutral JSON for generators in Go/TypeScript/Rust/etc.; "
                "markdown: human-readable plan; go: Go backend; rust: Rust backend; typescript: TypeScript backend; "
                "unittest: Python backend (default: markdown)"
            ),
        )
        build_parser.add_argument(
            "--typescript-runner",
            choices=("vitest", "jest"),
            default="vitest",
            help=(
                "TypeScript test runner to target when --format=typescript "
                "(default: vitest)"
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
            help="directory of consumer YAML to render into a test plan.",
        )
        build_parser.add_argument(
            "--out",
            type=Path,
            default=Path("test-plan"),
            help="output directory (default: ./test-plan)",
        )
        build_parser.add_argument(
            "--title",
            default="Generated Test Plan",
            help="page title (default: 'Generated Test Plan')",
        )
        build_parser.add_argument(
            "--clean",
            action="store_true",
            help="wipe <out> before building",
        )
        build_parser.set_defaults(func=self.run)

    def run(self, args) -> int:
        from deepthought.tests.render import (
            render_go_suite,
            render_rust_suite,
            render_test_manifest,
            render_test_plan,
            render_typescript_suite,
            render_unittest_suite,
        )

        if args.spec is None:
            print("tests build requires --spec <dir>", file=sys.stderr)
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

        if args.format == "manifest":
            render_test_manifest(catalog, args.spec, args.out)
            print(f"test manifest generated under {args.out}/")
            return 0

        if args.format == "unittest":
            render_unittest_suite(catalog, args.spec, args.out)
            print(f"unittest suite generated under {args.out}/")
            return 0

        if args.format == "go":
            render_go_suite(catalog, args.spec, args.out)
            print(f"go suite generated under {args.out}/")
            return 0

        if args.format == "rust":
            render_rust_suite(catalog, args.spec, args.out)
            print(f"rust suite generated under {args.out}/")
            return 0

        if args.format == "typescript":
            render_typescript_suite(
                catalog,
                args.spec,
                args.out,
                runner=args.typescript_runner,
            )
            print(f"typescript suite generated under {args.out}/")
            return 0

        render_test_plan(catalog, args.spec, args.out, title=args.title)
        print(f"test plan generated under {args.out}/")
        return 0
