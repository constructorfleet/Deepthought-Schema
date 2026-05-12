---
title: DeepThought Schema
layout: default
---

# DeepThought Schema

DeepThought is a Documentation-Driven Development specification language: every concept its meta-schemas describe is documented *inherent* to the schema (via `title` and `description`), so the reference pages below are generated directly from the YAML in `meta-schema/`. Examples are validated against those schemas on every build, so the worked examples on the reference pages can't rot away from the contracts they illustrate.

## Generator contracts

- [Test manifest](./test_manifest.md): language-neutral scenarios and invariants consumed by the generated Python, TypeScript, Go, and Rust backends.

## Reference pages

| Schema | Examples |
| --- | --- |
| [collection](./reference/collection.md) | — |
| [constant](./reference/constant.md) | — |
| [domain](./reference/domain.md) | — |
| [error](./reference/error.md) | — |
| [event](./reference/event.md) | — |
| [expression](./reference/expression.md) | — |
| [field](./reference/field.md) | 3 |
| [model](./reference/model.md) | — |
| [permission](./reference/permission.md) | — |
| [scenario](./reference/scenario.md) | — |
| [state_machine](./reference/state_machine.md) | — |
| [unit](./reference/unit.md) | — |
| [usecase](./reference/usecase.md) | — |
