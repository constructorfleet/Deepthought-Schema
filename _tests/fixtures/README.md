# M0 golden outputs

Snapshots under `golden/` pin current generated public surfaces at the M0
baseline. Reference documentation uses the checked-in `meta-schema/` and all
schema-valid files under `examples/`. Catalog-backed outputs use
`_tests/spec_fixture.py`, the repository's complete catalog fixture, because
some standalone examples are schema-valid but contain unresolved catalog
references.

The comparison is exact by relative file path and bytes. No normalization is
applied. Generator-emitted Markdown blank lines at end of file are retained byte for byte.
Repeated generation in two distinct temporary output directories must
produce identical files before the updater replaces these snapshots. Generated
`test_*.py` stubs are stored with a `.golden` suffix so pytest cannot discover
them as runnable tests.

Run from the repository root with project dependencies installed:

```sh
python -m _tests.update_golden_fixtures
python -m pytest _tests/test_golden_compatibility.py
```

The snapshots include reference and spec docs, checks, Markdown, the language
neutral test manifest, Python unittest, TypeScript Vitest and Jest, Go, and Rust
outputs. Generated test stubs remain templates; their presence in the snapshots
is not evidence that generated tests were executed or passed.
