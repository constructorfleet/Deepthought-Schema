import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / ".gitea" / "scripts" / "sync_project_version.py"
SPEC = importlib.util.spec_from_file_location("sync_project_version", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def updates_only_project_version_test(tmp_path):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        '[build-system]\nrequires = ["setuptools>=64"]\n\n'
        '[project]\nname = "deepthought"\nversion = "0.1.0"\n'
        'description = "tooling"\n\n[tool.example]\nversion = "8.0.0"\n'
    )

    changed = MODULE.sync_project_version(pyproject, "0.2.0")

    assert changed is True
    assert pyproject.read_text() == (
        '[build-system]\nrequires = ["setuptools>=64"]\n\n'
        '[project]\nname = "deepthought"\nversion = "0.2.0"\n'
        'description = "tooling"\n\n[tool.example]\nversion = "8.0.0"\n'
    )


def is_idempotent_when_version_already_matches_test(tmp_path):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text('[project]\nname = "deepthought"\nversion = "0.2.0"\n')

    assert MODULE.sync_project_version(pyproject, "0.2.0") is False
    assert pyproject.read_text().endswith('version = "0.2.0"\n')


def rejects_non_semver_release_version_test(tmp_path):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text('[project]\nname = "deepthought"\nversion = "0.1.0"\n')

    try:
        MODULE.sync_project_version(pyproject, "0.2")
    except ValueError as exc:
        assert "semantic version" in str(exc)
    else:
        raise AssertionError("invalid version should be rejected")


def requires_exactly_one_project_version_test(tmp_path):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text('[project]\nname = "deepthought"\n')

    try:
        MODULE.sync_project_version(pyproject, "0.2.0")
    except ValueError as exc:
        assert "exactly one" in str(exc)
    else:
        raise AssertionError("missing project version should be rejected")
