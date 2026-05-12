# Model

- [1. Property `Model > id`](#id)
- [2. Property `Model > name`](#name)
- [3. Property `Model > description`](#description)
- [4. Property `Model > fields`](#fields)
  - [4.1. Property `Model > fields > oneOf > Field reference`](#fields_oneOf_i0)
  - [4.2. Property `Model > fields > oneOf > item 1`](#fields_oneOf_i1)
    - [4.2.1. Model > fields > oneOf > item 1 > Field reference](#fields_oneOf_i1_items)
- [5. Property `Model > key`](#key)
  - [5.1. Property `Model > fields > oneOf > Field reference`](#fields_oneOf_i0)
  - [5.2. Property `Model > fields > oneOf > item 1`](#fields_oneOf_i1)
    - [5.2.1. Model > fields > oneOf > item 1 > Field reference](#fields_oneOf_i1_items)
- [6. Property `Model > queryable`](#queryable)
  - [6.1. Property `Model > queryable > oneOf > Field list`](#queryable_oneOf_i0)
  - [6.2. Property `Model > queryable > oneOf > item 1`](#queryable_oneOf_i1)
- [7. Property `Model > extends`](#extends)
- [8. Property `Model > domain`](#domain)
- [9. Property `Model > references`](#references)
  - [9.1. Model > references > Cross-model reference](#references_items)
    - [9.1.1. Property `Model > references > Cross-model reference > id`](#references_items_id)
    - [9.1.2. Property `Model > references > Cross-model reference > target`](#references_items_target)
    - [9.1.3. Property `Model > references > Cross-model reference > cardinality`](#references_items_cardinality)
    - [9.1.4. Property `Model > references > Cross-model reference > via`](#references_items_via)
    - [9.1.5. Property `Model > references > Cross-model reference > inverseName`](#references_items_inverseName)
    - [9.1.6. Property `Model > references > Cross-model reference > onDelete`](#references_items_onDelete)
    - [9.1.7. Property `Model > references > Cross-model reference > eager`](#references_items_eager)
    - [9.1.8. Property `Model > references > Cross-model reference > description`](#references_items_description)
- [10. Property `Model > invariants`](#invariants)
  - [10.1. Model > invariants > Cross-field invariant](#invariants_items)
    - [10.1.1. Property `Model > invariants > Cross-field invariant > id`](#invariants_items_id)
    - [10.1.2. Property `Model > invariants > Cross-field invariant > name`](#invariants_items_name)
    - [10.1.3. Property `Model > invariants > Cross-field invariant > description`](#invariants_items_description)
    - [10.1.4. Property `Model > invariants > Cross-field invariant > assert`](#invariants_items_assert)
    - [10.1.5. Property `Model > invariants > Cross-field invariant > enforcement`](#invariants_items_enforcement)
      - [10.1.5.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 0`](#invariants_items_enforcement_oneOf_i0)
      - [10.1.5.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1`](#invariants_items_enforcement_oneOf_i1)
        - [10.1.5.2.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state`](#invariants_items_enforcement_oneOf_i1_in_state)
          - [10.1.5.2.1.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0)
          - [10.1.5.2.1.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)
            - [10.1.5.2.1.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items)
    - [10.1.6. Property `Model > invariants > Cross-field invariant > raises`](#invariants_items_raises)
- [11. Property `Model > stateMachine`](#stateMachine)
  - [11.1. Property `Model > stateMachine > oneOf > Identifier`](#stateMachine_oneOf_i0)
  - [11.2. Property `Model > stateMachine > oneOf > State Machine (stateMachineSchema)`](#stateMachine_oneOf_i1)
- [12. Property `Model > persistence`](#persistence)
  - [12.1. Property `Model > persistence > kind`](#persistence_kind)
  - [12.2. Property `Model > persistence > store`](#persistence_store)
  - [12.3. Property `Model > persistence > sourcedFrom`](#persistence_sourcedFrom)
    - [12.3.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0)
    - [12.3.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)
      - [12.3.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items)
  - [12.4. Property `Model > persistence > retention`](#persistence_retention)
  - [12.5. Property `Model > persistence > auditTrail`](#persistence_auditTrail)
- [13. Property `Model > readableBy`](#readableBy)
  - [13.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0)
  - [13.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)
    - [13.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items)
- [14. Property `Model > writableBy`](#writableBy)
  - [14.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0)
  - [14.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)
    - [14.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items)
- [15. Property `Model > fieldPolicies`](#fieldPolicies)
  - [15.1. Model > fieldPolicies > Field-level access policy](#fieldPolicies_items)
    - [15.1.1. Property `Model > fieldPolicies > Field-level access policy > field`](#fieldPolicies_items_field)
    - [15.1.2. Property `Model > fieldPolicies > Field-level access policy > readableBy`](#fieldPolicies_items_readableBy)
      - [15.1.2.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0)
      - [15.1.2.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)
        - [15.1.2.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items)
    - [15.1.3. Property `Model > fieldPolicies > Field-level access policy > writableBy`](#fieldPolicies_items_writableBy)
      - [15.1.3.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0)
      - [15.1.3.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)
        - [15.1.3.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items)
- [16. Property `Model > sensitivity`](#sensitivity)
- [17. Property `Model > lifecycle`](#lifecycle)

**Title:** Model

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** A data structure consumed or returned by a Domain-Interfacing Use Case. A model is the named composition of its fields together with the cross-field invariants, lifecycle, persistence, references, and policies that together describe its meaning -- everything a generator needs to scaffold the type, the storage layer, and its tests.

| Property                           | Pattern | Type        | Deprecated | Definition                            | Title/Description             |
| ---------------------------------- | ------- | ----------- | ---------- | ------------------------------------- | ----------------------------- |
| + [id](#id )                       | No      | string      | No         | In #/definitions/identifierSchema     | Model identifier              |
| + [name](#name )                   | No      | string      | No         | -                                     | Model display name            |
| + [description](#description )     | No      | string      | No         | -                                     | Model description             |
| + [fields](#fields )               | No      | object      | No         | In #/definitions/fieldListSchema      | Fields                        |
| - [key](#key )                     | No      | object      | No         | In #/definitions/fieldListSchema      | Identity field(s)             |
| - [queryable](#queryable )         | No      | Combination | No         | -                                     | Queryable fields              |
| - [extends](#extends )             | No      | string      | No         | In #/definitions/identifierSchema     | Parent model                  |
| - [domain](#domain )               | No      | string      | No         | In #/definitions/identifierSchema     | Bounded context               |
| - [references](#references )       | No      | array       | No         | -                                     | Cross-model references        |
| - [invariants](#invariants )       | No      | array       | No         | -                                     | Cross-field invariants        |
| - [stateMachine](#stateMachine )   | No      | Combination | No         | -                                     | Lifecycle state machine       |
| - [persistence](#persistence )     | No      | object      | No         | In #/definitions/persistenceSchema    | Persistence                   |
| - [readableBy](#readableBy )       | No      | object      | No         | In #/definitions/identifierListSchema | Model-level read permissions  |
| - [writableBy](#writableBy )       | No      | object      | No         | In #/definitions/identifierListSchema | Model-level write permissions |
| - [fieldPolicies](#fieldPolicies ) | No      | array       | No         | -                                     | Field-level access policies   |
| - [sensitivity](#sensitivity )     | No      | object      | No         | -                                     | Field (sensitivitySchema)     |
| - [lifecycle](#lifecycle )         | No      | object      | No         | -                                     | Field (lifecycleSchema)       |

## <a name="id"></a>1. Property `Model > id`

**Title:** Model identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="name"></a>2. Property `Model > name`

**Title:** Model display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `Model > description`

**Title:** Model description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this model represents in the domain. Required so the model's purpose is documented as part of its definition.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="fields"></a>4. Property `Model > fields`

**Title:** Fields

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | Yes                           |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/fieldListSchema |

**Description:** Field references composing the model.

| One of(Option)                      |
| ----------------------------------- |
| [Field reference](#fields_oneOf_i0) |
| [item 1](#fields_oneOf_i1)          |

### <a name="fields_oneOf_i0"></a>4.1. Property `Model > fields > oneOf > Field reference`

**Title:** Field reference

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `string`                           |
| **Required**   | No                                 |
| **Defined in** | #/definitions/fieldReferenceSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

### <a name="fields_oneOf_i1"></a>4.2. Property `Model > fields > oneOf > item 1`

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

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Field reference](#fields_oneOf_i1_items) | -           |

#### <a name="fields_oneOf_i1_items"></a>4.2.1. Model > fields > oneOf > item 1 > Field reference

**Title:** Field reference

|                        |                                     |
| ---------------------- | ----------------------------------- |
| **Type**               | `string`                            |
| **Required**           | No                                  |
| **Same definition as** | [Field reference](#fields_oneOf_i0) |

## <a name="key"></a>5. Property `Model > key`

**Title:** Identity field(s)

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/fieldListSchema |

**Description:** Field(s) that uniquely identify an instance. Use cases declared with relation: key resolve their inputKey/outputKey against this.

| One of(Option)                      |
| ----------------------------------- |
| [Field reference](#fields_oneOf_i0) |
| [item 1](#fields_oneOf_i1)          |

### <a name="fields_oneOf_i0"></a>5.1. Property `Model > fields > oneOf > Field reference`

**Title:** Field reference

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `string`                           |
| **Required**   | No                                 |
| **Defined in** | #/definitions/fieldReferenceSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

### <a name="fields_oneOf_i1"></a>5.2. Property `Model > fields > oneOf > item 1`

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

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Field reference](#fields_oneOf_i1_items) | -           |

#### <a name="fields_oneOf_i1_items"></a>5.2.1. Model > fields > oneOf > item 1 > Field reference

**Title:** Field reference

|                        |                                     |
| ---------------------- | ----------------------------------- |
| **Type**               | `string`                            |
| **Required**           | No                                  |
| **Same definition as** | [Field reference](#fields_oneOf_i0) |

## <a name="queryable"></a>6. Property `Model > queryable`

**Title:** Queryable fields

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Fields by which instances can be filtered but that don't uniquely identify an instance. Use cases declared with relation: query validate their filter fields against this. The literal `true` declares all fields queryable.

| One of(Option)                    |
| --------------------------------- |
| [Field list](#queryable_oneOf_i0) |
| [item 1](#queryable_oneOf_i1)     |

### <a name="queryable_oneOf_i0"></a>6.1. Property `Model > queryable > oneOf > Field list`

**Title:** Field list

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `combining`       |
| **Required**              | No                |
| **Additional properties** | Any type allowed  |
| **Same definition as**    | [fields](#fields) |

**Description:** One or more field identifiers from the surrounding model.

### <a name="queryable_oneOf_i1"></a>6.2. Property `Model > queryable > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `true`

## <a name="extends"></a>7. Property `Model > extends`

**Title:** Parent model

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Identifier of a model this one extends.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="domain"></a>8. Property `Model > domain`

**Title:** Bounded context

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Bounded context this model belongs to. Inherits from the surrounding document if omitted.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="references"></a>9. Property `Model > references`

**Title:** Cross-model references

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be            | Description                                                                                                                                                                                                                                                                                        |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Cross-model reference](#references_items) | Captures a relationship to another model: the cardinality, the local field that holds the foreign key (when applicable), the inverse relation name on the target, and the referential integrity policy. Without these, generated code can't reason about joins, cascades, or aggregate boundaries. |

### <a name="references_items"></a>9.1. Model > references > Cross-model reference

**Title:** Cross-model reference

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/referenceSchema |

**Description:** Captures a relationship to another model: the cardinality, the local field that holds the foreign key (when applicable), the inverse relation name on the target, and the referential integrity policy. Without these, generated code can't reason about joins, cascades, or aggregate boundaries.

| Property                                        | Pattern | Type             | Deprecated | Definition                            | Title/Description       |
| ----------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------- | ----------------------- |
| + [id](#references_items_id )                   | No      | string           | No         | In #/definitions/identifierSchema     | Reference identifier    |
| + [target](#references_items_target )           | No      | string           | No         | In #/definitions/identifierSchema     | Target model identifier |
| + [cardinality](#references_items_cardinality ) | No      | enum (of string) | No         | In #/definitions/cardinalitySchema    | Cardinality             |
| - [via](#references_items_via )                 | No      | string           | No         | In #/definitions/fieldReferenceSchema | Foreign key field       |
| - [inverseName](#references_items_inverseName ) | No      | string           | No         | In #/definitions/identifierSchema     | Inverse relation name   |
| - [onDelete](#references_items_onDelete )       | No      | enum (of string) | No         | -                                     | On-delete policy        |
| - [eager](#references_items_eager )             | No      | boolean          | No         | -                                     | Eager loading           |
| + [description](#references_items_description ) | No      | string           | No         | -                                     | Reference description   |

#### <a name="references_items_id"></a>9.1.1. Property `Model > references > Cross-model reference > id`

**Title:** Reference identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="references_items_target"></a>9.1.2. Property `Model > references > Cross-model reference > target`

**Title:** Target model identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="references_items_cardinality"></a>9.1.3. Property `Model > references > Cross-model reference > cardinality`

**Title:** Cardinality

|                |                                 |
| -------------- | ------------------------------- |
| **Type**       | `enum (of string)`              |
| **Required**   | Yes                             |
| **Defined in** | #/definitions/cardinalitySchema |

**Description:** The cardinality of a reference between two models.

Must be one of:
* "one_to_one"
* "one_to_many"
* "many_to_one"
* "many_to_many"

#### <a name="references_items_via"></a>9.1.4. Property `Model > references > Cross-model reference > via`

**Title:** Foreign key field

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `string`                           |
| **Required**   | No                                 |
| **Defined in** | #/definitions/fieldReferenceSchema |

**Description:** Local field holding the foreign key, when applicable.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="references_items_inverseName"></a>9.1.5. Property `Model > references > Cross-model reference > inverseName`

**Title:** Inverse relation name

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Name the target model uses to refer back to this one.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="references_items_onDelete"></a>9.1.6. Property `Model > references > Cross-model reference > onDelete`

**Title:** On-delete policy

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"restrict"`       |

**Description:** Referential integrity policy applied when the target is deleted.

Must be one of:
* "cascade"
* "restrict"
* "nullify"
* "no_action"

#### <a name="references_items_eager"></a>9.1.7. Property `Model > references > Cross-model reference > eager`

**Title:** Eager loading

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether navigating this reference loads the target automatically.

#### <a name="references_items_description"></a>9.1.8. Property `Model > references > Cross-model reference > description`

**Title:** Reference description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this relationship represents in the domain. Required so the relationship's meaning travels with the reference itself.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="invariants"></a>10. Property `Model > invariants`

**Title:** Cross-field invariants

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be            | Description                                                                                                                                                                                                                                                             |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Cross-field invariant](#invariants_items) | A domain rule that spans multiple fields ("shipped_at greater than or equal to ordered_at", "total equals sum of line_items.amount"). Single-field constraints can't express these; declaring them as invariants moves the rule out of code comments into the contract. |

### <a name="invariants_items"></a>10.1. Model > invariants > Cross-field invariant

**Title:** Cross-field invariant

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/invariantSchema |

**Description:** A domain rule that spans multiple fields ("shipped_at greater than or equal to ordered_at", "total equals sum of line_items.amount"). Single-field constraints can't express these; declaring them as invariants moves the rule out of code comments into the contract.

| Property                                        | Pattern | Type        | Deprecated | Definition                        | Title/Description         |
| ----------------------------------------------- | ------- | ----------- | ---------- | --------------------------------- | ------------------------- |
| + [id](#invariants_items_id )                   | No      | string      | No         | In #/definitions/identifierSchema | Invariant identifier      |
| - [name](#invariants_items_name )               | No      | string      | No         | -                                 | Invariant display name    |
| + [description](#invariants_items_description ) | No      | string      | No         | -                                 | Invariant description     |
| + [assert](#invariants_items_assert )           | No      | object      | No         | -                                 | Expression                |
| - [enforcement](#invariants_items_enforcement ) | No      | Combination | No         | -                                 | Enforcement window        |
| - [raises](#invariants_items_raises )           | No      | string      | No         | In #/definitions/identifierSchema | Error raised on violation |

#### <a name="invariants_items_id"></a>10.1.1. Property `Model > invariants > Cross-field invariant > id`

**Title:** Invariant identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="invariants_items_name"></a>10.1.2. Property `Model > invariants > Cross-field invariant > name`

**Title:** Invariant display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

#### <a name="invariants_items_description"></a>10.1.3. Property `Model > invariants > Cross-field invariant > description`

**Title:** Invariant description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this invariant guarantees and the domain rationale behind it. Required so the rule's intent stays inherent to the schema.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="invariants_items_assert"></a>10.1.4. Property `Model > invariants > Cross-field invariant > assert`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

#### <a name="invariants_items_enforcement"></a>10.1.5. Property `Model > invariants > Cross-field invariant > enforcement`

**Title:** Enforcement window

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** When the invariant must hold. `always` checks on every read and write. `on_write` skips validation for in-flight reads from legacy data. `in_state` restricts checks to specific lifecycle states.

| One of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#invariants_items_enforcement_oneOf_i0) |
| [item 1](#invariants_items_enforcement_oneOf_i1) |

##### <a name="invariants_items_enforcement_oneOf_i0"></a>10.1.5.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 0`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "always"
* "on_write"
* "on_read"

##### <a name="invariants_items_enforcement_oneOf_i1"></a>10.1.5.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                       | Pattern | Type   | Deprecated | Definition                            | Title/Description |
| -------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------------------- | ----------------- |
| + [in_state](#invariants_items_enforcement_oneOf_i1_in_state ) | No      | object | No         | In #/definitions/identifierListSchema | Identifier list   |

###### <a name="invariants_items_enforcement_oneOf_i1_in_state"></a>10.1.5.2.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state`

**Title:** Identifier list

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | Yes                                |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** One or more entity identifiers.

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0) |
| [item 1](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)     |

###### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0"></a>10.1.5.2.1.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

###### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1"></a>10.1.5.2.1.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`

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

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items) | -           |

###### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items"></a>10.1.5.2.1.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="invariants_items_raises"></a>10.1.6. Property `Model > invariants > Cross-field invariant > raises`

**Title:** Error raised on violation

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Error to raise if the invariant fails. If omitted, generators emit a default validation error type.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="stateMachine"></a>11. Property `Model > stateMachine`

**Title:** Lifecycle state machine

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Either an inline state machine or a reference to one defined in its own state_machine.meta.yaml document.

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [Identifier](#stateMachine_oneOf_i0)                         |
| [State Machine (stateMachineSchema)](#stateMachine_oneOf_i1) |

### <a name="stateMachine_oneOf_i0"></a>11.1. Property `Model > stateMachine > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="stateMachine_oneOf_i1"></a>11.2. Property `Model > stateMachine > oneOf > State Machine (stateMachineSchema)`

**Title:** State Machine (stateMachineSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [State Machine](./state_machine.md#statemachineschema).

## <a name="persistence"></a>12. Property `Model > persistence`

**Title:** Persistence

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | #/definitions/persistenceSchema |

**Description:** Where instances of this model live. Drives generator decisions about storage layer, repository scaffolding, and audit semantics.

| Property                                   | Pattern | Type             | Deprecated | Definition                            | Title/Description    |
| ------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------------- | -------------------- |
| + [kind](#persistence_kind )               | No      | enum (of string) | No         | -                                     | Persistence kind     |
| - [store](#persistence_store )             | No      | string           | No         | In #/definitions/identifierSchema     | Store identifier     |
| - [sourcedFrom](#persistence_sourcedFrom ) | No      | object           | No         | In #/definitions/identifierListSchema | Source models        |
| - [retention](#persistence_retention )     | No      | string           | No         | -                                     | Retention policy     |
| - [auditTrail](#persistence_auditTrail )   | No      | boolean          | No         | -                                     | Maintain audit trail |

### <a name="persistence_kind"></a>12.1. Property `Model > persistence > kind`

**Title:** Persistence kind

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** stored = durably persisted in a store of record; derived = projected from other models; ephemeral = in-memory DTO, never persisted; external = owned by an upstream system.

Must be one of:
* "stored"
* "derived"
* "ephemeral"
* "external"

### <a name="persistence_store"></a>12.2. Property `Model > persistence > store`

**Title:** Store identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Identifier of the store of record (for `stored`).

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

### <a name="persistence_sourcedFrom"></a>12.3. Property `Model > persistence > sourcedFrom`

**Title:** Source models

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** Source(s) the projection is built from (for `derived`).

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0) |
| [item 1](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)     |

#### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0"></a>12.3.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1"></a>12.3.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`

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

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items) | -           |

##### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items"></a>12.3.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="persistence_retention"></a>12.4. Property `Model > persistence > retention`

**Title:** Retention policy

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Free-form retention guidance for stored data.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="persistence_auditTrail"></a>12.5. Property `Model > persistence > auditTrail`

**Title:** Maintain audit trail

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether changes to instances are logged to an audit trail.

## <a name="readableBy"></a>13. Property `Model > readableBy`

**Title:** Model-level read permissions

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** One or more entity identifiers.

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0) |
| [item 1](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)     |

### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0"></a>13.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1"></a>13.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`

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

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items) | -           |

#### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items"></a>13.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="writableBy"></a>14. Property `Model > writableBy`

**Title:** Model-level write permissions

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** One or more entity identifiers.

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0) |
| [item 1](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)     |

### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0"></a>14.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1"></a>14.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`

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

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items) | -           |

#### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items"></a>14.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="fieldPolicies"></a>15. Property `Model > fieldPolicies`

**Title:** Field-level access policies

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                   | Description                                                                                                    |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [Field-level access policy](#fieldPolicies_items) | Per-field read / write visibility rules. References permission ids declared in permission.meta.yaml documents. |

### <a name="fieldPolicies_items"></a>15.1. Model > fieldPolicies > Field-level access policy

**Title:** Field-level access policy

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | #/definitions/fieldPolicySchema |

**Description:** Per-field read / write visibility rules. References permission ids declared in permission.meta.yaml documents.

| Property                                         | Pattern | Type   | Deprecated | Definition                                   | Title/Description |
| ------------------------------------------------ | ------- | ------ | ---------- | -------------------------------------------- | ----------------- |
| + [field](#fieldPolicies_items_field )           | No      | string | No         | Same as [Field reference](#fields_oneOf_i0 ) | Field reference   |
| - [readableBy](#fieldPolicies_items_readableBy ) | No      | object | No         | In #/definitions/identifierListSchema        | Read permissions  |
| - [writableBy](#fieldPolicies_items_writableBy ) | No      | object | No         | In #/definitions/identifierListSchema        | Write permissions |

#### <a name="fieldPolicies_items_field"></a>15.1.1. Property `Model > fieldPolicies > Field-level access policy > field`

**Title:** Field reference

|                        |                                     |
| ---------------------- | ----------------------------------- |
| **Type**               | `string`                            |
| **Required**           | Yes                                 |
| **Same definition as** | [Field reference](#fields_oneOf_i0) |

#### <a name="fieldPolicies_items_readableBy"></a>15.1.2. Property `Model > fieldPolicies > Field-level access policy > readableBy`

**Title:** Read permissions

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** One or more entity identifiers.

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0) |
| [item 1](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)     |

##### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0"></a>15.1.2.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

##### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1"></a>15.1.2.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`

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

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items) | -           |

###### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items"></a>15.1.2.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="fieldPolicies_items_writableBy"></a>15.1.3. Property `Model > fieldPolicies > Field-level access policy > writableBy`

**Title:** Write permissions

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** One or more entity identifiers.

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0) |
| [item 1](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1)     |

##### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i0"></a>15.1.3.1. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

##### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1"></a>15.1.3.2. Property `Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1`

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

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [Identifier](#invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items) | -           |

###### <a name="invariants_items_enforcement_oneOf_i1_in_state_oneOf_i1_items"></a>15.1.3.2.1. Model > invariants > Cross-field invariant > enforcement > oneOf > item 1 > in_state > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="sensitivity"></a>16. Property `Model > sensitivity`

**Title:** Field (sensitivitySchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#sensitivityschema).

## <a name="lifecycle"></a>17. Property `Model > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

----------------------------------------------------------------------------------------------------------------------------
