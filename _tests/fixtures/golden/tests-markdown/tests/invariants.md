---
title: Invariants
layout: default
---

# Invariants

Generated correctness checks derived from model invariants.

## Thing

`thing`  *(source: `model/thing.yaml`)*

### Thing Name Present

`thing_name_present`

Every thing has a name.

Enforcement:

```yaml
always
...
```

Assertion:

```yaml
field: thing_name
```

