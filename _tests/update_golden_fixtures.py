"""Regenerate the checked-in M0 public-output goldens after reviewed changes."""

from pathlib import Path
from shutil import copyfile, rmtree
from tempfile import TemporaryDirectory

from _tests.spec_fixture import write_catalog_fixture
from _tests.test_golden_compatibility import (
    GOLDEN_ROOT,
    generate_outputs,
    relative_files,
    stored_path,
)


def trees_match(left: Path, right: Path) -> bool:
    left_files = relative_files(left)
    right_files = relative_files(right)
    return left_files == right_files and all(
        (left / relative).read_bytes() == (right / relative).read_bytes()
        for relative in left_files
    )


def main() -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        catalog_fixture = root / "catalog-fixture"
        write_catalog_fixture(catalog_fixture)
        first = root / "first"
        second = root / "second"
        generate_outputs(first, catalog_fixture)
        generate_outputs(second, catalog_fixture)
        if not trees_match(first, second):
            raise SystemExit(
                "Repeated output generation differed; inspect the changed output "
                "before updating any golden fixture."
            )
        if GOLDEN_ROOT.exists():
            rmtree(GOLDEN_ROOT)
        GOLDEN_ROOT.parent.mkdir(parents=True, exist_ok=True)
        for relative in relative_files(first):
            target = GOLDEN_ROOT / stored_path(relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            copyfile(first / relative, target)

    print(f"Updated golden outputs in {GOLDEN_ROOT}")


if __name__ == "__main__":
    main()
