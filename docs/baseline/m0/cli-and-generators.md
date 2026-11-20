# M0 CLI and generator baseline

This report captures public CLI and generator behavior at source revision `476d9dba5647433c2362c67e35e246d0f0d23a23` (`2026-11-19` in the planning bundle). The source tree is unchanged by this capture. Exact CLI help text is stored under [`cli-help/`](cli-help/).

## Capture environment

- macOS 26.7.1, arm64
- CPython 3.12.16
- `uv 0.13.9`
- Installed package: `deepthought 0.1.0`, built from this source revision
- Runtime dependencies resolved by `uv` from `pyproject.toml`; the resolved versions are recorded below in [Resolved runtime dependencies](#resolved-runtime-dependencies).

Help snapshots were captured from the installed `deepthought` entry point. The documented sample paths below use `<repo>` and `<out>` for the source root and explicit output root; those placeholders replace only temporary-directory prefixes. CLI help text is unmodified.

## CLI surface

| Command | Observed behavior | Exit |
| --- | --- | ---: |
| `deepthought --help` | Lists `validate`, `schemas`, `test-schema`, and discovered `checks`, `docs`, `tests` generators. | 0 |
| `deepthought validate <root> [--schemas <dir>]` | Prints `all YAML in <root> validates against the meta-schemas` on success. A validation error returns 1. | 0 on valid input |
| `deepthought schemas` | Prints the canonical `meta-schema/` path in an editable/source checkout. | 0 in editable mode |
| `deepthought test-schema [--format path|json]` | Defaults to the schema file path; `--format json` prints the packaged JSON Schema. | 0 |

The `validate`, `schemas`, `test-schema`, and generator help snapshots preserve exact option text. In the installed wheel probe, `test-schema` resolves to the schema packaged under `site-packages`. The wheel does not contain the canonical meta-schemas at this revision: `deepthought schemas` and default `deepthought validate <root>` return 1 with `RuntimeError: deepthought: could not locate the meta-schema directory`. Passing `--schemas <repo>/meta-schema` allows installed `validate` and generator commands to run. This is recorded as existing behavior; M0 does not change package contents or runtime behavior.

## Generator discovery

`pyproject.toml` registers three built-in implementations in the `deepthought.generators` entry-point group: `checks`, `docs`, and `tests`. The installed entry point discovers those generators and displays them in top-level help.

The editable fallback was also run in a fresh Python 3.12 environment with dependencies installed but without installing the `deepthought` distribution. With `PYTHONPATH=<repo>/src`, `python -m deepthought --help` lists the same three built-ins. `python -m deepthought schemas` resolves `<repo>/meta-schema`, and `python -m deepthought validate <repo>/examples --schemas <repo>/meta-schema` returns 0. This exercises `_load_builtin_generators()` when the entry-point group is absent.

External discovery was exercised with the reproducible [temporary probe package](probes/external-generator/README.md), which registers `m0-probe` in `deepthought.generators`. Top-level help listed `m0-probe`; `deepthought m0-probe --help` listed its `build` subcommand; and `deepthought m0-probe build --out <out>/external` returned 0 and wrote `discovered.txt`. The probe package is documentation/test support and is not part of the installed product package.

## Generator commands and output paths

`docs build` supports `reference` and `spec` modes. `reference` is the default and writes a static site under `docs/` unless `--out` is supplied. `spec` requires `--spec` and also writes a site under the chosen output directory.

`checks build` requires `--spec`; it writes under `checks/` by default. With the existing inventory test fixture and explicit `--schemas`, it generated `index.json` and `checks/{invariants,permission_rules,scenarios,transitions}.json` under the output directory.

`tests build` requires `--spec`; supported `--format` values are `markdown`, `manifest`, `unittest`, `typescript`, `go`, and `rust`. The default is Markdown. Outputs from the inventory test fixture were:

| Format | Output paths below `<out>/` | Exit |
| --- | --- | ---: |
| `markdown` | `_config.yml`, `index.md`, `tests/invariants.md`, `tests/scenarios.md` | 0 |
| `manifest` | `test_manifest.json` | 0 |
| `unittest` | `generated_unittest/__init__.py`, `payloads.py`, `test_invariants.py`, `test_usecase_get_thing.py` | 0 |
| `typescript` / Vitest | `generated_typescript/get_thing.test.ts`, `invariants.test.ts`, `types.ts` | 0 |
| `typescript --typescript-runner jest` | Same three output paths, Jest-targeted contents | 0 |
| `go` | `generated_go/get_thing_test.go`, `invariants_test.go`, `types.go` | 0 |
| `rust` | `generated_rust/Cargo.toml`, `src/{get_thing,invariants,lib,types}.rs` | 0 |

These files are generated surfaces. No generated test stubs were executed by this capture.

## Input and output observations

`deepthought validate <repo>/examples --schemas <repo>/meta-schema` returned 0 for all 23 YAML examples. Reference documentation generation with the examples also returned 0 and wrote `_config.yml`, `index.md`, and `reference/{collection,constant,domain,error,event,expression,field,model,permission,scenario,state_machine,unit,usecase}.md`.

Catalog-based generators should use a catalog-valid fixture. Running `docs build --mode spec`, `checks build`, or any `tests build` format against the entire `examples/` directory returned 1 with the same catalog error: collection `standard_screen_resolutions` references missing model `resolution`. Using `_tests/spec_fixture.py` to generate the existing inventory fixture allowed the spec docs, checks, and each listed test format to complete with exit 0. The capture records both the valid-example validation result and the full-example catalog failure; it does not repair or omit either behavior.

## Reproduction commands

Run from the source root in a Python 3.12 environment with the project dependencies installed. The first group uses the editable/source fallback; the second uses an installed package and explicit schema paths because the wheel at the captured revision omits canonical meta-schemas. Use clean temporary directories for generated output.

```sh
M0_SPEC="$(mktemp -d)"
M0_OUT="$(mktemp -d)"

# Editable/source fallback
PYTHONPATH=src python -m deepthought --help
PYTHONPATH=src python -m deepthought schemas
PYTHONPATH=src python -m deepthought validate examples --schemas meta-schema

# Installed entry point
deepthought --help
deepthought validate examples --schemas meta-schema
deepthought test-schema
deepthought test-schema --format json

deepthought docs build --mode reference --schemas meta-schema \
  --examples examples --out "$M0_OUT/docs-reference"

PYTHONPATH=_tests python -c 'from pathlib import Path; import sys; from spec_fixture import write_catalog_fixture; write_catalog_fixture(Path(sys.argv[1]))' "$M0_SPEC"
deepthought docs build --mode spec --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/docs-spec"
deepthought checks build --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/checks"

deepthought tests build --format markdown --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/tests-markdown"
deepthought tests build --format manifest --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/tests-manifest"
deepthought tests build --format unittest --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/tests-unittest"
deepthought tests build --format typescript --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/tests-typescript"
deepthought tests build --format typescript --typescript-runner jest \
  --schemas meta-schema --spec "$M0_SPEC" \
  --out "$M0_OUT/tests-typescript-jest"
deepthought tests build --format go --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/tests-go"
deepthought tests build --format rust --schemas meta-schema \
  --spec "$M0_SPEC" --out "$M0_OUT/tests-rust"
```

The fixture helper depends on running from the repository root. Both fixture and output roots are disposable temporary directories, so the generation commands do not overwrite the repository's `docs/`, `checks/`, or default `test-plan/` directories.

## Resolved runtime dependencies

The installed capture environment resolved these packages from the project requirements. `pytest` and other quality tools are not project dependencies; their configured/available status is recorded separately by the M0 quality-gate report.

```text
attrs==26.1.0
certifi==2026.10.23
charset-normalizer==3.5.2
click==8.5.1
dataclasses-json==0.6.7
idna==3.20
jinja2==3.1.6
json-schema-for-humans==1.5.1
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
markdown2==2.5.5
markupsafe==3.0.4
marshmallow==3.26.2
mypy-extensions==1.2.0
packaging==26.3
pygments==2.21.0
pytz==2026.6
PyYAML==6.0.3
referencing==0.37.0
requests==2.34.2
rpds-py==2026.9.1
typing-extensions==4.16.0
typing-inspect==0.9.0
urllib3==2.8.0
```
