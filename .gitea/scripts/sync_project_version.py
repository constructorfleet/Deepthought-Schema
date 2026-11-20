"""Synchronize the Python package version with release-please's planned version."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SEMVER = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\Z")
PROJECT_HEADER = re.compile(r"^\s*\[([^]]+)\]\s*(?:#.*)?(?:\r?\n)?$")
VERSION_LINE = re.compile(r"^(\s*version\s*=\s*)(['\"])([^'\"]+)\2(\s*(?:#.*)?)(\r?\n)?$")


def sync_project_version(pyproject_path: Path, version: str) -> bool:
    """Set exactly one `[project].version` to a stable semantic version.

    Return whether the file changed. Refuse ambiguous or unsupported TOML
    layouts instead of modifying a different version field.
    """
    if not SEMVER.fullmatch(version):
        raise ValueError(f"release version must be a stable semantic version: {version}")

    lines = pyproject_path.read_text().splitlines(keepends=True)
    in_project = False
    version_indexes: list[int] = []
    for index, line in enumerate(lines):
        header = PROJECT_HEADER.match(line)
        if header:
            in_project = header.group(1).strip() == "project"
            continue
        if in_project and re.match(r"^\s*version\s*=", line):
            version_indexes.append(index)

    if len(version_indexes) != 1:
        raise ValueError(
            "pyproject.toml must contain exactly one version field in [project]"
        )

    index = version_indexes[0]
    match = VERSION_LINE.fullmatch(lines[index])
    if not match:
        raise ValueError("[project].version must be a quoted string")
    if match.group(3) == version:
        return False

    lines[index] = (
        match.group(1)
        + match.group(2)
        + version
        + match.group(2)
        + match.group(4)
        + (match.group(5) or "")
    )
    pyproject_path.write_text("".join(lines))
    return True


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("usage: sync_project_version.py VERSION", file=sys.stderr)
        return 2
    try:
        changed = sync_project_version(Path("pyproject.toml"), args[0])
    except (OSError, ValueError) as exc:
        print(f"version sync failed: {exc}", file=sys.stderr)
        return 1
    print("pyproject.toml version updated" if changed else "pyproject.toml version already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
