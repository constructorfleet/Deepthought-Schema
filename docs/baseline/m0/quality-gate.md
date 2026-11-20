# M0 quality and compatibility gate

This report records the tools configured at the M0 baseline and the checks run
for the M0 implementation. The baseline source revision is
`476d9dba5647433c2362c67e35e246d0f0d23a23` (`Add built-in generators for checks
and docs`). The report's implementation revision is filled in when the M0
branches are integrated.

## Configured checks at baseline

The baseline repository configures pytest in `pytest.ini`:

- Discovery root: `_tests`
- File pattern: `test_*.py`
- Function pattern: `*_test`
- Logging formatting and date options are configured there as well.

`pyproject.toml` uses setuptools (`setuptools>=64`, `wheel`) as the build
backend. There was no repository CI workflow, formatter, type checker, security
scanner, dependency scanner, or packaging verification job at the pinned
baseline. Those checks therefore have no baseline command or result. M0 adds a
Gitea Actions Python 3.12 quality job; this is a new configured check, not a
pre-existing baseline gate.

## Exact M0 quality commands

The release workflow runs these commands on pushes and pull requests using
Python 3.12:

```sh
python -m pip install --editable . pytest==8.4.2
python -m pytest -q
```

Recorded local runner environment: CPython `3.12.16`, pip `26.2.2`, pytest
`8.4.2`. The commands were executed in a disposable Python 3.12 virtual
environment. Result on the M0 release-flow branch before final integration:
`22 passed, 1 warning` (exit status 0). The warning is the existing
`jsonschema.RefResolver` deprecation. The final integrated run and commit are
recorded below after integration.

No formatter, type checker, build/package, security, or dependency scan is
configured by the repository or the M0 workflow. Their status is **not
configured / not run**, not passed. No generated test stubs are counted as
executed or passing tests: only pytest runner output is reported as test
results.

## Compatibility checks

`_tests/test_golden_compatibility.py` compares generated file paths and bytes
exactly against checked-in goldens. It permits no normalization. The fixture
updater runs each inventory twice into separate temporary directories and
requires identical inventories and bytes before writing. Generator-produced
Python test files are stored with `.py.golden` suffixes and are data, not
imported test modules.

The two generator inputs are deliberately distinct: schema-valid existing
examples provide reference documentation coverage, while the complete catalog
fixture provides representative output for built-in checks and language test
backends. The CLI/external-generator report records commands, versions,
outputs, and the pre-existing collection failure for the incomplete
`standard_screen_resolutions` example set.

Generator output contains blank lines at end-of-file. Consequently, a generic
`git diff --check` over golden blobs reports those trailing blank lines; this
is preserved byte-for-byte for compatibility. The non-golden diff check is
clean. This is an evidence limitation of whitespace lint on exact output, not
a fixture normalization.

## Release-flow verification boundary

The Gitea workflow uses
`self:constructorfleet/release-please@v17.1.3`. Its quality job runs before
release automation. The action uses a `GITEA_TOKEN` repository secret to open
or update the release pull request and synchronize the Gitea release. The
release action runtime was not exercised against the live Gitea repository in
local verification; the workflow was statically checked and its helper was
unit tested. Do not treat that as a live release-flow pass.

## Final integrated verification

This section is to be completed against the integration commit and records the
exact runner output, command exit codes, tool versions, and evidence location.
