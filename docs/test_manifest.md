---
title: Test Manifest
layout: default
---

# Test Manifest

DeepThought's test generators share a single language-neutral manifest contract. Instead of reparsing YAML per backend, the built-in Python, TypeScript, Go, and Rust generators all consume the same `test_manifest.json` structure.

The canonical schema for that contract lives in `src/deepthought/tests/test_manifest.schema.json`.

You can print the packaged schema path with `deepthought test-schema`, or print the schema JSON directly with `deepthought test-schema --format json`.

## Top-level shape

The manifest contains three top-level keys:

- `counts`: summary counts for generated scenarios and invariants.
- `scenarios`: Given/When/Then scenario payloads grouped by use case by downstream generators.
- `invariants`: model invariant payloads for generated correctness checks.

## Scenario entries

Each scenario entry includes:

- `id`: stable scenario identifier.
- `name`: human-readable scenario name.
- `description`: optional description text.
- `usecase`: owning use case identifier.
- `tags`: scenario tags.
- `source`: source file label relative to the spec root.
- `given`: preconditions as structured JSON/YAML-compatible values.
- `when`: action under test as a structured JSON/YAML-compatible value or `null`.
- `then`: expected outcomes as structured JSON/YAML-compatible values.

## Invariant entries

Each invariant entry includes:

- `id`: stable invariant identifier.
- `name`: human-readable invariant name.
- `description`: optional description text.
- `model`: owning model identifier.
- `source`: source file label relative to the spec root.
- `assert`: invariant assertion payload from the source spec.
- `enforcement`: enforcement payload from the source spec.
- `raises`: optional error identifier raised when the invariant fails.

## Consumer guidance

Backends should treat the manifest as the contract boundary and map it into language-specific helper types rather than walking the original YAML specs directly.

- Python emits generated unittest stubs plus helper dataclasses.
- TypeScript emits generated Vitest or Jest stubs plus helper interfaces.
- Go emits generated `_test.go` stubs plus helper structs.
- Rust emits a generated crate layout with helper structs and ignored test scaffolds.