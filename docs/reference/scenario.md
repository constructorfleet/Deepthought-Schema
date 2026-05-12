# Scenario

- [1. Property `Scenario > id`](#id)
- [2. Property `Scenario > name`](#name)
- [3. Property `Scenario > description`](#description)
- [4. Property `Scenario > tags`](#tags)
  - [4.1. Scenario > tags > tags items](#tags_items)
- [5. Property `Scenario > usecase`](#usecase)
- [6. Property `Scenario > given`](#given)
  - [6.1. Scenario > given > Given clause](#given_items)
    - [6.1.1. Property `Scenario > given > Given clause > oneOf > Given - prose statement`](#given_items_oneOf_i0)
      - [6.1.1.1. Property `Scenario > given > Given clause > oneOf > Given - prose statement > statement`](#given_items_oneOf_i0_statement)
    - [6.1.2. Property `Scenario > given > Given clause > oneOf > Given - model is in state`](#given_items_oneOf_i1)
      - [6.1.2.1. Property `Scenario > given > Given clause > oneOf > Given - model is in state > model`](#given_items_oneOf_i1_model)
      - [6.1.2.2. Property `Scenario > given > Given clause > oneOf > Given - model is in state > state`](#given_items_oneOf_i1_state)
    - [6.1.3. Property `Scenario > given > Given clause > oneOf > Given - instance exists`](#given_items_oneOf_i2)
      - [6.1.3.1. Property `Scenario > given > Given clause > oneOf > Given - instance exists > exists`](#given_items_oneOf_i2_exists)
      - [6.1.3.2. Property `Scenario > given > Given clause > oneOf > Given - instance exists > values`](#given_items_oneOf_i2_values)
    - [6.1.4. Property `Scenario > given > Given clause > oneOf > Given - predicate`](#given_items_oneOf_i3)
      - [6.1.4.1. Property `Scenario > given > Given clause > oneOf > Given - predicate > assert`](#given_items_oneOf_i3_assert)
    - [6.1.5. Property `Scenario > given > Given clause > oneOf > Given - calling actor`](#given_items_oneOf_i4)
      - [6.1.5.1. Property `Scenario > given > Given clause > oneOf > Given - calling actor > actor`](#given_items_oneOf_i4_actor)
- [7. Property `Scenario > when`](#when)
  - [7.1. Property `Scenario > when > input`](#when_input)
    - [7.1.1. Property `Scenario > when > input > oneOf > item 0`](#when_input_oneOf_i0)
    - [7.1.2. Property `Scenario > when > input > oneOf > item 1`](#when_input_oneOf_i1)
      - [7.1.2.1. Scenario > when > input > oneOf > item 1 > item 1 items](#when_input_oneOf_i1_items)
  - [7.2. Property `Scenario > when > actor`](#when_actor)
- [8. Property `Scenario > then`](#then)
  - [8.1. Scenario > then > Then clause](#then_items)
    - [8.1.1. Property `Scenario > then > Then clause > oneOf > Then - expected output`](#then_items_oneOf_i0)
      - [8.1.1.1. Property `Scenario > then > Then clause > oneOf > Then - expected output > output`](#then_items_oneOf_i0_output)
        - [8.1.1.1.1. Property `Scenario > then > Then clause > oneOf > Then - expected output > output > oneOf > item 0`](#then_items_oneOf_i0_output_oneOf_i0)
        - [8.1.1.1.2. Property `Scenario > then > Then clause > oneOf > Then - expected output > output > oneOf > item 1`](#then_items_oneOf_i0_output_oneOf_i1)
    - [8.1.2. Property `Scenario > then > Then clause > oneOf > Then - error raised`](#then_items_oneOf_i1)
      - [8.1.2.1. Property `Scenario > then > Then clause > oneOf > Then - error raised > raises`](#then_items_oneOf_i1_raises)
      - [8.1.2.2. Property `Scenario > then > Then clause > oneOf > Then - error raised > payload`](#then_items_oneOf_i1_payload)
    - [8.1.3. Property `Scenario > then > Then clause > oneOf > Then - event emitted`](#then_items_oneOf_i2)
      - [8.1.3.1. Property `Scenario > then > Then clause > oneOf > Then - event emitted > emits`](#then_items_oneOf_i2_emits)
      - [8.1.3.2. Property `Scenario > then > Then clause > oneOf > Then - event emitted > payload`](#then_items_oneOf_i2_payload)
    - [8.1.4. Property `Scenario > then > Then clause > oneOf > Then - state transition`](#then_items_oneOf_i3)
      - [8.1.4.1. Property `Scenario > then > Then clause > oneOf > Then - state transition > transitions`](#then_items_oneOf_i3_transitions)
      - [8.1.4.2. Property `Scenario > then > Then clause > oneOf > Then - state transition > model`](#then_items_oneOf_i3_model)
      - [8.1.4.3. Property `Scenario > then > Then clause > oneOf > Then - state transition > to`](#then_items_oneOf_i3_to)
    - [8.1.5. Property `Scenario > then > Then clause > oneOf > Then - predicate`](#then_items_oneOf_i4)
      - [8.1.5.1. Property `Scenario > then > Then clause > oneOf > Then - predicate > assert`](#then_items_oneOf_i4_assert)
    - [8.1.6. Property `Scenario > then > Then clause > oneOf > Then - prose statement`](#then_items_oneOf_i5)
      - [8.1.6.1. Property `Scenario > then > Then clause > oneOf > Then - prose statement > statement`](#then_items_oneOf_i5_statement)
- [9. Property `Scenario > lifecycle`](#lifecycle)

**Title:** Scenario

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** Given/When/Then acceptance specification for a use case. Each scenario is simultaneously human-readable documentation, a generated BDD test, and a worked example for downstream consumers. Multiple scenarios per use case capture the happy path, edge cases, and error cases as a single contract.

| Property                       | Pattern | Type            | Deprecated | Definition                        | Title/Description       |
| ------------------------------ | ------- | --------------- | ---------- | --------------------------------- | ----------------------- |
| + [id](#id )                   | No      | string          | No         | In #/definitions/identifierSchema | Identifier              |
| + [name](#name )               | No      | string          | No         | -                                 | Scenario display name   |
| + [description](#description ) | No      | string          | No         | -                                 | Scenario description    |
| - [tags](#tags )               | No      | array of string | No         | -                                 | Suite tags              |
| - [usecase](#usecase )         | No      | string          | No         | In #/definitions/identifierSchema | Use case under test     |
| - [given](#given )             | No      | array           | No         | -                                 | Given clauses           |
| + [when](#when )               | No      | object          | No         | In #/definitions/whenSchema       | When clause             |
| + [then](#then )               | No      | array           | No         | -                                 | Then clauses            |
| - [lifecycle](#lifecycle )     | No      | object          | No         | -                                 | Field (lifecycleSchema) |

## <a name="id"></a>1. Property `Scenario > id`

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

## <a name="name"></a>2. Property `Scenario > name`

**Title:** Scenario display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `Scenario > description`

**Title:** Scenario description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What aspect of the use case this scenario pins down (happy path, specific edge case, specific error). Required so each scenario's intent stays inherent to the spec.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="tags"></a>4. Property `Scenario > tags`

**Title:** Suite tags

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Tags that organize generated test suites: smoke, regression, negative, security, golden, etc.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [tags items](#tags_items)       | -           |

### <a name="tags_items"></a>4.1. Scenario > tags > tags items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                         |
| --------------------------------- | --------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                       |
| **Must match regular expression** | ```^[a-z][a-z_-]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_-%5D%2A%24) |

## <a name="usecase"></a>5. Property `Scenario > usecase`

**Title:** Use case under test

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** The use case under test. Optional when the scenario is embedded inline on a use case definition; otherwise required.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="given"></a>6. Property `Scenario > given`

**Title:** Given clauses

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

| Each item of this array must be | Description                                                              |
| ------------------------------- | ------------------------------------------------------------------------ |
| [Given clause](#given_items)    | A single precondition. Compose multiple in the scenario's 'given' array. |

### <a name="given_items"></a>6.1. Scenario > given > Given clause

**Title:** Given clause

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `combining`               |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/definitions/givenSchema |

**Description:** A single precondition. Compose multiple in the scenario's `given` array.

| One of(Option)                                     |
| -------------------------------------------------- |
| [Given - prose statement](#given_items_oneOf_i0)   |
| [Given - model is in state](#given_items_oneOf_i1) |
| [Given - instance exists](#given_items_oneOf_i2)   |
| [Given - predicate](#given_items_oneOf_i3)         |
| [Given - calling actor](#given_items_oneOf_i4)     |

#### <a name="given_items_oneOf_i0"></a>6.1.1. Property `Scenario > given > Given clause > oneOf > Given - prose statement`

**Title:** Given - prose statement

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/givenStatementSchema |

**Description:** Free-form prose precondition for cases that don't lend themselves to structured assertions. Always allowed; structured forms are preferred where they fit.

| Property                                        | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [statement](#given_items_oneOf_i0_statement ) | No      | string | No         | -          | Statement         |

##### <a name="given_items_oneOf_i0_statement"></a>6.1.1.1. Property `Scenario > given > Given clause > oneOf > Given - prose statement > statement`

**Title:** Statement

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="given_items_oneOf_i1"></a>6.1.2. Property `Scenario > given > Given clause > oneOf > Given - model is in state`

**Title:** Given - model is in state

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/givenStateSchema |

**Description:** A model instance is currently in a particular state-machine state.

| Property                                | Pattern | Type   | Deprecated | Definition                        | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | --------------------------------- | ----------------- |
| + [model](#given_items_oneOf_i1_model ) | No      | string | No         | In #/definitions/identifierSchema | Model identifier  |
| + [state](#given_items_oneOf_i1_state ) | No      | string | No         | In #/definitions/identifierSchema | State identifier  |

##### <a name="given_items_oneOf_i1_model"></a>6.1.2.1. Property `Scenario > given > Given clause > oneOf > Given - model is in state > model`

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

##### <a name="given_items_oneOf_i1_state"></a>6.1.2.2. Property `Scenario > given > Given clause > oneOf > Given - model is in state > state`

**Title:** State identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="given_items_oneOf_i2"></a>6.1.3. Property `Scenario > given > Given clause > oneOf > Given - instance exists`

**Title:** Given - instance exists

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | #/definitions/givenExistsSchema |

**Description:** An instance of the named model exists with the supplied field values.

| Property                                  | Pattern | Type   | Deprecated | Definition                        | Title/Description |
| ----------------------------------------- | ------- | ------ | ---------- | --------------------------------- | ----------------- |
| + [exists](#given_items_oneOf_i2_exists ) | No      | string | No         | In #/definitions/identifierSchema | Model identifier  |
| - [values](#given_items_oneOf_i2_values ) | No      | object | No         | -                                 | Seed values       |

##### <a name="given_items_oneOf_i2_exists"></a>6.1.3.1. Property `Scenario > given > Given clause > oneOf > Given - instance exists > exists`

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

##### <a name="given_items_oneOf_i2_values"></a>6.1.3.2. Property `Scenario > given > Given clause > oneOf > Given - instance exists > values`

**Title:** Seed values

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Field values applied to the seeded instance.

#### <a name="given_items_oneOf_i3"></a>6.1.4. Property `Scenario > given > Given clause > oneOf > Given - predicate`

**Title:** Given - predicate

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | #/definitions/givenAssertSchema |

**Description:** An arbitrary predicate that must hold over the world state before the use case runs.

| Property                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [assert](#given_items_oneOf_i3_assert ) | No      | object | No         | -          | Expression        |

##### <a name="given_items_oneOf_i3_assert"></a>6.1.4.1. Property `Scenario > given > Given clause > oneOf > Given - predicate > assert`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

#### <a name="given_items_oneOf_i4"></a>6.1.5. Property `Scenario > given > Given clause > oneOf > Given - calling actor`

**Title:** Given - calling actor

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/givenActorSchema |

**Description:** The actor invoking the use case in this scenario.

| Property                                | Pattern | Type   | Deprecated | Definition                        | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | --------------------------------- | ----------------- |
| + [actor](#given_items_oneOf_i4_actor ) | No      | string | No         | In #/definitions/identifierSchema | Actor identifier  |

##### <a name="given_items_oneOf_i4_actor"></a>6.1.5.1. Property `Scenario > given > Given clause > oneOf > Given - calling actor > actor`

**Title:** Actor identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="when"></a>7. Property `Scenario > when`

**Title:** When clause

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | Yes                      |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/definitions/whenSchema |

**Description:** The input(s) supplied to the use case under test, plus the calling actor.

| Property                | Pattern | Type        | Deprecated | Definition                        | Title/Description        |
| ----------------------- | ------- | ----------- | ---------- | --------------------------------- | ------------------------ |
| + [input](#when_input ) | No      | Combination | No         | -                                 | Use-case input(s)        |
| - [actor](#when_actor ) | No      | string      | No         | In #/definitions/identifierSchema | Calling actor identifier |

### <a name="when_input"></a>7.1. Property `Scenario > when > input`

**Title:** Use-case input(s)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)                 |
| ------------------------------ |
| [item 0](#when_input_oneOf_i0) |
| [item 1](#when_input_oneOf_i1) |

#### <a name="when_input_oneOf_i0"></a>7.1.1. Property `Scenario > when > input > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

#### <a name="when_input_oneOf_i1"></a>7.1.2. Property `Scenario > when > input > oneOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [item 1 items](#when_input_oneOf_i1_items) | -           |

##### <a name="when_input_oneOf_i1_items"></a>7.1.2.1. Scenario > when > input > oneOf > item 1 > item 1 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

### <a name="when_actor"></a>7.2. Property `Scenario > when > actor`

**Title:** Calling actor identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="then"></a>8. Property `Scenario > then`

**Title:** Then clauses

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description                                                                 |
| ------------------------------- | --------------------------------------------------------------------------- |
| [Then clause](#then_items)      | A single expected outcome. Compose multiple in the scenario's 'then' array. |

### <a name="then_items"></a>8.1. Scenario > then > Then clause

**Title:** Then clause

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `combining`              |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/definitions/thenSchema |

**Description:** A single expected outcome. Compose multiple in the scenario's `then` array.

| One of(Option)                                  |
| ----------------------------------------------- |
| [Then - expected output](#then_items_oneOf_i0)  |
| [Then - error raised](#then_items_oneOf_i1)     |
| [Then - event emitted](#then_items_oneOf_i2)    |
| [Then - state transition](#then_items_oneOf_i3) |
| [Then - predicate](#then_items_oneOf_i4)        |
| [Then - prose statement](#then_items_oneOf_i5)  |

#### <a name="then_items_oneOf_i0"></a>8.1.1. Property `Scenario > then > Then clause > oneOf > Then - expected output`

**Title:** Then - expected output

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/thenOutputSchema |

**Description:** The output value(s) returned by the use case on success.

| Property                                 | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [output](#then_items_oneOf_i0_output ) | No      | Combination | No         | -          | -                 |

##### <a name="then_items_oneOf_i0_output"></a>8.1.1.1. Property `Scenario > then > Then clause > oneOf > Then - expected output > output`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#then_items_oneOf_i0_output_oneOf_i0) |
| [item 1](#then_items_oneOf_i0_output_oneOf_i1) |

###### <a name="then_items_oneOf_i0_output_oneOf_i0"></a>8.1.1.1.1. Property `Scenario > then > Then clause > oneOf > Then - expected output > output > oneOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="then_items_oneOf_i0_output_oneOf_i1"></a>8.1.1.1.2. Property `Scenario > then > Then clause > oneOf > Then - expected output > output > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

#### <a name="then_items_oneOf_i1"></a>8.1.2. Property `Scenario > then > Then clause > oneOf > Then - error raised`

**Title:** Then - error raised

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/thenRaisesSchema |

**Description:** An error is raised; payload optionally pinned for assertion.

| Property                                   | Pattern | Type   | Deprecated | Definition                        | Title/Description      |
| ------------------------------------------ | ------- | ------ | ---------- | --------------------------------- | ---------------------- |
| + [raises](#then_items_oneOf_i1_raises )   | No      | string | No         | In #/definitions/identifierSchema | Error identifier       |
| - [payload](#then_items_oneOf_i1_payload ) | No      | object | No         | -                                 | Expected error payload |

##### <a name="then_items_oneOf_i1_raises"></a>8.1.2.1. Property `Scenario > then > Then clause > oneOf > Then - error raised > raises`

**Title:** Error identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

##### <a name="then_items_oneOf_i1_payload"></a>8.1.2.2. Property `Scenario > then > Then clause > oneOf > Then - error raised > payload`

**Title:** Expected error payload

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

#### <a name="then_items_oneOf_i2"></a>8.1.3. Property `Scenario > then > Then clause > oneOf > Then - event emitted`

**Title:** Then - event emitted

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/thenEmitsSchema |

**Description:** An event is emitted by the use case; payload optionally pinned.

| Property                                   | Pattern | Type   | Deprecated | Definition                        | Title/Description      |
| ------------------------------------------ | ------- | ------ | ---------- | --------------------------------- | ---------------------- |
| + [emits](#then_items_oneOf_i2_emits )     | No      | string | No         | In #/definitions/identifierSchema | Event identifier       |
| - [payload](#then_items_oneOf_i2_payload ) | No      | object | No         | -                                 | Expected event payload |

##### <a name="then_items_oneOf_i2_emits"></a>8.1.3.1. Property `Scenario > then > Then clause > oneOf > Then - event emitted > emits`

**Title:** Event identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

##### <a name="then_items_oneOf_i2_payload"></a>8.1.3.2. Property `Scenario > then > Then clause > oneOf > Then - event emitted > payload`

**Title:** Expected event payload

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

#### <a name="then_items_oneOf_i3"></a>8.1.4. Property `Scenario > then > Then clause > oneOf > Then - state transition`

**Title:** Then - state transition

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Defined in**            | #/definitions/thenTransitionsSchema |

**Description:** A target model transitions from one lifecycle state to another.

| Property                                           | Pattern | Type   | Deprecated | Definition                        | Title/Description            |
| -------------------------------------------------- | ------- | ------ | ---------- | --------------------------------- | ---------------------------- |
| + [transitions](#then_items_oneOf_i3_transitions ) | No      | string | No         | In #/definitions/identifierSchema | Transition identifier        |
| - [model](#then_items_oneOf_i3_model )             | No      | string | No         | In #/definitions/identifierSchema | Affected model identifier    |
| + [to](#then_items_oneOf_i3_to )                   | No      | string | No         | In #/definitions/identifierSchema | Destination state identifier |

##### <a name="then_items_oneOf_i3_transitions"></a>8.1.4.1. Property `Scenario > then > Then clause > oneOf > Then - state transition > transitions`

**Title:** Transition identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

##### <a name="then_items_oneOf_i3_model"></a>8.1.4.2. Property `Scenario > then > Then clause > oneOf > Then - state transition > model`

**Title:** Affected model identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

##### <a name="then_items_oneOf_i3_to"></a>8.1.4.3. Property `Scenario > then > Then clause > oneOf > Then - state transition > to`

**Title:** Destination state identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="then_items_oneOf_i4"></a>8.1.5. Property `Scenario > then > Then clause > oneOf > Then - predicate`

**Title:** Then - predicate

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/thenAssertSchema |

**Description:** An arbitrary predicate that must hold after the use case runs.

| Property                                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [assert](#then_items_oneOf_i4_assert ) | No      | object | No         | -          | Expression        |

##### <a name="then_items_oneOf_i4_assert"></a>8.1.5.1. Property `Scenario > then > Then clause > oneOf > Then - predicate > assert`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

#### <a name="then_items_oneOf_i5"></a>8.1.6. Property `Scenario > then > Then clause > oneOf > Then - prose statement`

**Title:** Then - prose statement

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/definitions/thenStatementSchema |

**Description:** Free-form expected outcome.

| Property                                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [statement](#then_items_oneOf_i5_statement ) | No      | string | No         | -          | Statement         |

##### <a name="then_items_oneOf_i5_statement"></a>8.1.6.1. Property `Scenario > then > Then clause > oneOf > Then - prose statement > statement`

**Title:** Statement

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="lifecycle"></a>9. Property `Scenario > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

----------------------------------------------------------------------------------------------------------------------------
