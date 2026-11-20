---
title: Scenarios
layout: default
---

# Scenarios

Generated Given/When/Then suites grouped by use case.

## Get Thing

`get_thing`

### Get Thing Happy Path

`get_thing_happy_path`  *(source: `source: `scenario/get_thing_happy_path.yaml``)*

Reading a known thing succeeds.

Tags: smoke

#### Given

```yaml
actor: pantry_owner
```

#### When

```yaml
input:
  thing_id: abc
```

#### Then

```yaml
output:
  thing_id: abc
  thing_name: Example
```

