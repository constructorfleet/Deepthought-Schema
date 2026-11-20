# M0 quality and compatibility gate

This report records the tools configured at the M0 baseline and the checks run
for the M0 implementation. The baseline source revision is
`476d9dba5647433c2362c67e35e246d0f0d23a23` (`Add built-in generators for checks
and docs`). The integrated M0 implementation revision for the run below is
`277558320a09b033916145e7bdbd416025013b17`.

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
`8.4.2`. The commands were executed in disposable Python 3.12 virtual
environment `/tmp/deepthought-m0-final-venv` on integrated revision
`277558320a09b033916145e7bdbd416025013b17`. The install command exited 0; the
test command exited 0 with `23 passed, 1 warning in 3.26s`. The warning is the
existing `jsonschema.RefResolver` deprecation at `src/deepthought/validate.py:28`.

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

The following supplemental checks were run on the same integrated revision:

| Command | Tool version | Result |
| --- | --- | --- |
| `/tmp/deepthought-m0-final-venv/bin/python -m _tests.update_golden_fixtures` | CPython 3.12.16; project dependencies from editable install | Exit 0; double generation completed and updated zero tracked files |
| `actionlint .gitea/workflows/release.yml` | actionlint 1.7.12 (Homebrew build, Go 1.26.3, darwin/arm64) | Exit 0 |
| Python YAML parse of `.gitea/workflows/release.yml` | PyYAML 6.0.3 | Exit 0; all four jobs parsed |
| `bash -n` on the embedded release-detection script | system Bash | Exit 0 |
| `git diff --check -- ':(exclude)_tests/fixtures/golden/**'` | git from local environment | Exit 0 |

Evidence paths: `_tests/test_golden_compatibility.py`,
`_tests/fixtures/golden/`, `.gitea/workflows/release.yml`,
`_tests/test_release_version_sync.py`, and this report. `git diff --check`
over golden blobs reports generator-emitted trailing blank lines; see the
compatibility section above. These exact-output files are intentionally not
normalized.

The workflow itself has not run on a Gitea Actions runner. In particular, the
release action's authenticated PR/release operations remain unverified until
`GITEA_TOKEN` and the Gitea runner are available to that repository. Static
workflow validation and local Python tests do not claim that these remote
operations succeeded.

An independent review found no blocking fixture or implementation findings.
The reviewer confirmed exact byte and path comparison, two-generation fixture
stability checks, inert `.py.golden` generated test stubs, and representative
coverage across the current generators. The review also identified a hosting
boundary: the source upstream is GitHub `constructorfleet/Deepthought-Schema`,
but the configured `self:constructorfleet/release-please` action runs on
Gitea. The queried Gitea organization has no `Deepthought-Schema` repository;
`teagan42/Deepthought` is the separate planning/issues repository. Therefore a
GitHub PR can carry the Gitea workflow configuration, but GitHub Actions will
not execute it. The Gitea release flow becomes operational only when the code
is hosted on Gitea and the required runner/secret are configured.
