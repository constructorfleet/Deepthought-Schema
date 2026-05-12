# Event

- [1. Property `Event definition > id`](#id)
- [2. Property `Event definition > name`](#name)
- [3. Property `Event definition > description`](#description)
- [4. Property `Event definition > schema_version`](#schema_version)
- [5. Property `Event definition > payload`](#payload)
  - [5.1. Property `Event definition > payload > oneOf > item 0`](#payload_oneOf_i0)
  - [5.2. Property `Event definition > payload > oneOf > Identifier`](#payload_oneOf_i1)
  - [5.3. Property `Event definition > payload > oneOf > item 2`](#payload_oneOf_i2)
    - [5.3.1. Event definition > payload > oneOf > item 2 > Identifier](#payload_oneOf_i2_items)
- [6. Property `Event definition > delivery`](#delivery)
- [7. Property `Event definition > aggregate`](#aggregate)
- [8. Property `Event definition > topic`](#topic)
- [9. Property `Event definition > ordered`](#ordered)
- [10. Property `Event definition > lifecycle`](#lifecycle)

**Title:** Event

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** A fact -- something that happened in the domain -- emitted by a use case for downstream consumers (audit logs, event streams, projections, integrations). Declaring events makes the audit/event surface a first-class part of the contract instead of code archaeology.

| Property                             | Pattern | Type             | Deprecated | Definition                        | Title/Description       |
| ------------------------------------ | ------- | ---------------- | ---------- | --------------------------------- | ----------------------- |
| + [id](#id )                         | No      | string           | No         | In #/definitions/identifierSchema | Identifier              |
| + [name](#name )                     | No      | string           | No         | -                                 | Event display name      |
| + [description](#description )       | No      | string           | No         | -                                 | Event description       |
| + [schema_version](#schema_version ) | No      | integer          | No         | -                                 | Payload schema version  |
| + [payload](#payload )               | No      | Combination      | No         | -                                 | Event payload           |
| - [delivery](#delivery )             | No      | enum (of string) | No         | In #/definitions/deliverySchema   | Delivery semantics      |
| - [aggregate](#aggregate )           | No      | string           | No         | In #/definitions/identifierSchema | Aggregate root          |
| - [topic](#topic )                   | No      | string           | No         | -                                 | Routing topic           |
| - [ordered](#ordered )               | No      | boolean          | No         | -                                 | Ordering required       |
| - [lifecycle](#lifecycle )           | No      | object           | No         | -                                 | Field (lifecycleSchema) |

## <a name="id"></a>1. Property `Event definition > id`

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

## <a name="name"></a>2. Property `Event definition > name`

**Title:** Event display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `Event definition > description`

**Title:** Event description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What the event signals about the domain and the conditions under which it is emitted. Required so consumers can understand the event without reading producer code.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="schema_version"></a>4. Property `Event definition > schema_version`

**Title:** Payload schema version

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Monotonic integer incremented on breaking payload changes. Independent of the event's lifecycle metadata so consumers can version schema evolution without confusing it with deprecation.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

## <a name="payload"></a>5. Property `Event definition > payload`

**Title:** Event payload

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Payload model(s) carried by the event. Use the literal `none` for a marker event with no payload.

| One of(Option)                  |
| ------------------------------- |
| [item 0](#payload_oneOf_i0)     |
| [Identifier](#payload_oneOf_i1) |
| [item 2](#payload_oneOf_i2)     |

### <a name="payload_oneOf_i0"></a>5.1. Property `Event definition > payload > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"none"`

### <a name="payload_oneOf_i1"></a>5.2. Property `Event definition > payload > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="payload_oneOf_i2"></a>5.3. Property `Event definition > payload > oneOf > item 2`

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
| [Identifier](#payload_oneOf_i2_items) | -           |

#### <a name="payload_oneOf_i2_items"></a>5.3.1. Event definition > payload > oneOf > item 2 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="delivery"></a>6. Property `Event definition > delivery`

**Title:** Delivery semantics

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `enum (of string)`           |
| **Required**   | No                           |
| **Defined in** | #/definitions/deliverySchema |

**Description:** When the event is emitted relative to the use-case execution and what consistency guarantee the broker provides. The chosen mode shapes the generated producer / consumer scaffolding.

Must be one of:
* "synchronous"
* "transactional"
* "at_least_once"
* "at_most_once"
* "eventual"

## <a name="aggregate"></a>7. Property `Event definition > aggregate`

**Title:** Aggregate root

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** The aggregate / entity whose state change this event reports. Drives partition-key selection in generated stream producers.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="topic"></a>8. Property `Event definition > topic`

**Title:** Routing topic

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Routing topic / channel hint for generators that target a message broker (Kafka topic, NATS subject, SQS queue, etc.).

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="ordered"></a>9. Property `Event definition > ordered`

**Title:** Ordering required

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether subscribers must process this event in emission order within an aggregate. Drives partition + consumer config.

## <a name="lifecycle"></a>10. Property `Event definition > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

----------------------------------------------------------------------------------------------------------------------------
