"""Top-level command-line entry point for ``deepthought``.

The CLI exposes built-in framework commands (validation, schema lookup)
plus every discovered output generator. Generators register themselves
via the ``deepthought.generators`` entry-point group instead of being
hardcoded here.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from deepthought.generators import discover_generators
from deepthought.meta_schemas import bundled_schemas_dir
from deepthought.tests import load_test_manifest_schema, test_manifest_schema_path
from deepthought.validate import validate_directory


def _add_validate_subcommand(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "validate",
        help="Validate a directory of DeepThought YAML against the meta-schemas.",
        description=(
            "Validate every YAML file under <root> against the appropriate "
            "meta-schema. The kind is inferred from a containing subdirectory "
            "name (examples/field/...) or a filename suffix (foo.field.yaml)."
        ),
    )
    parser.add_argument("root", type=Path, help="directory of YAML to validate")
    parser.add_argument(
        "--schemas",
        type=Path,
        default=None,
        help=(
            "directory of meta-schemas to validate against; defaults to the "
            "canonical meta-schema/ directory bundled with deepthought"
        ),
    )
    parser.set_defaults(func=_run_validate)


def _add_schemas_subcommand(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "schemas",
        help="Print the path of the canonical meta-schema directory.",
        description=(
            "Print the directory containing every DeepThought meta-schema. "
            "Useful for editor LSP integration and external validators."
        ),
    )
    parser.set_defaults(func=_run_schemas)


def _add_test_schema_subcommand(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "test-schema",
        help="Print the packaged test-manifest schema path or JSON.",
        description=(
            "Print the packaged JSON schema that defines DeepThought's "
            "language-neutral test manifest contract."
        ),
    )
    parser.add_argument(
        "--format",
        choices=("json", "path"),
        default="path",
        help="output format (default: path)",
    )
    parser.set_defaults(func=_run_test_schema)


def _run_validate(args: argparse.Namespace) -> int:
    errors = validate_directory(args.root, schemas_dir=args.schemas)
    if errors:
        print(f"validation failed ({len(errors)} error(s)):", file=sys.stderr)
        for err in errors:
            print(f"  {err.format(root=args.root)}", file=sys.stderr)
        return 1
    print(f"all YAML in {args.root} validates against the meta-schemas")
    return 0


def _run_schemas(_: argparse.Namespace) -> int:
    print(bundled_schemas_dir())
    return 0


def _run_test_schema(args: argparse.Namespace) -> int:
    if args.format == "json":
        print(json.dumps(load_test_manifest_schema(), indent=2))
        return 0
    print(test_manifest_schema_path())
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="deepthought",
        description=(
            "DeepThought toolkit: validate specifications and generate "
            "documentation, tests, and code from them."
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    _add_validate_subcommand(subparsers)
    _add_schemas_subcommand(subparsers)
    _add_test_schema_subcommand(subparsers)
    for generator in discover_generators():
        generator.register_cli(subparsers)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
