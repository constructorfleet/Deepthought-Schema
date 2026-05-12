# Error

- [1. Property `Error definition > id`](#id)
- [2. Property `Error definition > name`](#name)
- [3. Property `Error definition > description`](#description)
- [4. Property `Error definition > category`](#category)
- [5. Property `Error definition > payload`](#payload)
  - [5.1. Property `Error definition > payload > oneOf > Identifier`](#payload_oneOf_i0)
  - [5.2. Property `Error definition > payload > oneOf > item 1`](#payload_oneOf_i1)
    - [5.2.1. Error definition > payload > oneOf > item 1 > Identifier](#payload_oneOf_i1_items)
- [6. Property `Error definition > condition`](#condition)
- [7. Property `Error definition > retryable`](#retryable)
- [8. Property `Error definition > recovery`](#recovery)
  - [8.1. Error definition > recovery > Recovery hint](#recovery_items)
    - [8.1.1. Property `Error definition > recovery > Recovery hint > kind`](#recovery_items_kind)
    - [8.1.2. Property `Error definition > recovery > Recovery hint > target`](#recovery_items_target)
    - [8.1.3. Property `Error definition > recovery > Recovery hint > description`](#recovery_items_description)
- [9. Property `Error definition > lifecycle`](#lifecycle)

**Title:** Error

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** Typed failure mode of one or more use cases. Errors are first-class so generated code can produce typed error returns, exhaustive match arms, and negative-path tests instead of relying on string messages or unchecked exceptions. The condition under which a use case raises an error is part of the error's contract, not a comment in implementation code.

| Property                       | Pattern | Type             | Deprecated | Definition                           | Title/Description       |
| ------------------------------ | ------- | ---------------- | ---------- | ------------------------------------ | ----------------------- |
| + [id](#id )                   | No      | string           | No         | In #/definitions/identifierSchema    | Identifier              |
| + [name](#name )               | No      | string           | No         | -                                    | Error display name      |
| + [description](#description ) | No      | string           | No         | -                                    | Error description       |
| + [category](#category )       | No      | enum (of string) | No         | In #/definitions/errorCategorySchema | Error category          |
| - [payload](#payload )         | No      | Combination      | No         | -                                    | Error payload           |
| - [condition](#condition )     | No      | object           | No         | -                                    | Expression              |
| - [retryable](#retryable )     | No      | enum (of string) | No         | In #/definitions/retryabilitySchema  | Retry guidance          |
| - [recovery](#recovery )       | No      | array            | No         | -                                    | Recovery hints          |
| - [lifecycle](#lifecycle )     | No      | object           | No         | -                                    | Field (lifecycleSchema) |

## <a name="id"></a>1. Property `Error definition > id`

**Title:** Identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="name"></a>2. Property `Error definition > name`

**Title:** Error display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `Error definition > description`

**Title:** Error description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this error means and what state of the world produces it. Required so the failure surface is documented as part of the contract, not as implementation-side commentary.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="category"></a>4. Property `Error definition > category`

**Title:** Error category

|                |                                   |
| -------------- | --------------------------------- |
| **Type**       | `enum (of string)`                |
| **Required**   | Yes                               |
| **Defined in** | #/definitions/errorCategorySchema |

**Description:** Symbolic class of error. Drives default mapping in generators (HTTP status codes, gRPC codes, exception hierarchies) without forcing the schema to know about transport-layer details. Lets callers reason about retryability without parsing the id.

Must be one of:
* "not_found"
* "already_exists"
* "validation"
* "precondition_failed"
* "conflict"
* "unauthorized"
* "forbidden"
* "rate_limited"
* "quota_exceeded"
* "dependency_unavailable"
* "timeout"
* "internal"
* "cancelled"
* "unsupported"

## <a name="payload"></a>5. Property `Error definition > payload`

**Title:** Error payload

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Structured payload shipped with the error. Either a model id (or list of model ids) describing the payload's shape.

| One of(Option)                  |
| ------------------------------- |
| [Identifier](#payload_oneOf_i0) |
| [item 1](#payload_oneOf_i1)     |

### <a name="payload_oneOf_i0"></a>5.1. Property `Error definition > payload > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="payload_oneOf_i1"></a>5.2. Property `Error definition > payload > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be       | Description |
| ------------------------------------- | ----------- |
| [Identifier](#payload_oneOf_i1_items) | -           |

#### <a name="payload_oneOf_i1_items"></a>5.2.1. Error definition > payload > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="condition"></a>6. Property `Error definition > condition`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

## <a name="retryable"></a>7. Property `Error definition > retryable`

**Title:** Retry guidance

|                |                                  |
| -------------- | -------------------------------- |
| **Type**       | `enum (of string)`               |
| **Required**   | No                               |
| **Defined in** | #/definitions/retryabilitySchema |

**Description:** Caller-facing retry guidance. Drives generated retry policy and caller-visible documentation alike.

Must be one of:
* "never"
* "safe"
* "after_backoff"
* "manual"

## <a name="recovery"></a>8. Property `Error definition > recovery`

**Title:** Recovery hints

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Structured suggestions for callers responding to this error.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be  | Description                                                                                                                                                                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Recovery hint](#recovery_items) | Structured suggestion for how a caller should respond when this error is raised. Generators can lower these into typed retry, fallback, or escalation policies; documentation tooling can render them as caller-facing guidance. |

### <a name="recovery_items"></a>8.1. Error definition > recovery > Recovery hint

**Title:** Recovery hint

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `object`                     |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | #/definitions/recoverySchema |

**Description:** Structured suggestion for how a caller should respond when this error is raised. Generators can lower these into typed retry, fallback, or escalation policies; documentation tooling can render them as caller-facing guidance.

| Property                                      | Pattern | Type             | Deprecated | Definition                        | Title/Description          |
| --------------------------------------------- | ------- | ---------------- | ---------- | --------------------------------- | -------------------------- |
| + [kind](#recovery_items_kind )               | No      | enum (of string) | No         | -                                 | Recovery kind              |
| - [target](#recovery_items_target )           | No      | string           | No         | In #/definitions/identifierSchema | Recovery target identifier |
| + [description](#recovery_items_description ) | No      | string           | No         | -                                 | Recovery description       |

#### <a name="recovery_items_kind"></a>8.1.1. Property `Error definition > recovery > Recovery hint > kind`

**Title:** Recovery kind

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "retry"
* "fallback"
* "escalate"
* "wait_for_event"
* "use_alternative"

#### <a name="recovery_items_target"></a>8.1.2. Property `Error definition > recovery > Recovery hint > target`

**Title:** Recovery target identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Identifier referenced by the recovery hint. Interpretation depends on `kind` -- a use-case id for use_alternative, an event id for wait_for_event, etc.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="recovery_items_description"></a>8.1.3. Property `Error definition > recovery > Recovery hint > description`

**Title:** Recovery description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Human-readable rationale and instruction for the recovery action.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="lifecycle"></a>9. Property `Error definition > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

----------------------------------------------------------------------------------------------------------------------------
