from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from _tests.spec_fixture import write_catalog_fixture
from deepthought.cli import main


REPO_ROOT = Path(__file__).resolve().parents[1]
GOLDEN_ROOT = Path(__file__).resolve().parent / "fixtures" / "golden"
SCHEMAS = REPO_ROOT / "meta-schema"
EXAMPLES = REPO_ROOT / "examples"


OUTPUTS = {
    "docs-reference": [
        "docs",
        "build",
        "--mode",
        "reference",
        "--schemas",
        str(SCHEMAS),
        "--examples",
        str(EXAMPLES),
    ],
    "docs-spec": [
        "docs",
        "build",
        "--mode",
        "spec",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "checks": [
        "checks",
        "build",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "tests-markdown": [
        "tests",
        "build",
        "--format",
        "markdown",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "tests-manifest": [
        "tests",
        "build",
        "--format",
        "manifest",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "tests-unittest": [
        "tests",
        "build",
        "--format",
        "unittest",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "tests-typescript-vitest": [
        "tests",
        "build",
        "--format",
        "typescript",
        "--typescript-runner",
        "vitest",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "tests-typescript-jest": [
        "tests",
        "build",
        "--format",
        "typescript",
        "--typescript-runner",
        "jest",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "tests-go": [
        "tests",
        "build",
        "--format",
        "go",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
    "tests-rust": [
        "tests",
        "build",
        "--format",
        "rust",
        "--schemas",
        str(SCHEMAS),
        "--spec",
        str(EXAMPLES),
    ],
}

def generate_outputs(output_root: Path, catalog_fixture: Path) -> None:
    """Generate public surfaces using the declared corpus inputs."""
    output_root.mkdir(parents=True, exist_ok=True)
    for name, args in OUTPUTS.items():
        output_dir = output_root / name
        spec_root = EXAMPLES if name == "docs-reference" else catalog_fixture
        command_args = [
            str(spec_root) if argument == str(EXAMPLES) else argument
            for argument in args
        ]
        result = main([*command_args, "--out", str(output_dir), "--clean"])
        if result != 0:
            raise AssertionError(f"{name} generation returned exit status {result}")


def stored_path(relative: Path) -> Path:
    """Keep generated unittest stubs inert so pytest cannot collect them."""
    if relative.name.startswith("test_") and relative.suffix == ".py":
        return relative.with_name(f"{relative.name}.golden")
    return relative


def relative_files(root: Path) -> set[Path]:
    return {path.relative_to(root) for path in root.rglob("*") if path.is_file()}


class GoldenCompatibilityTest(unittest.TestCase):
    def test_generator_outputs_match_checked_in_goldens_exactly(self):
        with TemporaryDirectory() as tmp:
            actual_root = Path(tmp) / "actual"
            catalog_fixture = Path(tmp) / "catalog-fixture"
            write_catalog_fixture(catalog_fixture)
            generate_outputs(actual_root, catalog_fixture)

            expected_files = relative_files(GOLDEN_ROOT)
            actual_files = {stored_path(path) for path in relative_files(actual_root)}
            self.assertEqual(
                sorted(expected_files),
                sorted(actual_files),
                "golden output file inventory differs; see _tests/update_golden_fixtures.py",
            )
            for relative_path in sorted(expected_files):
                actual_relative_path = relative_path
                if relative_path.name.endswith(".py.golden"):
                    actual_relative_path = relative_path.with_suffix("")
                with self.subTest(path=str(relative_path)):
                    self.assertEqual(
                        (GOLDEN_ROOT / relative_path).read_bytes(),
                        (actual_root / actual_relative_path).read_bytes(),
                        f"golden output differs at {relative_path}",
                    )


if __name__ == "__main__":
    unittest.main()
