# State Machine

- [1. Property `State machine > id`](#id)
- [2. Property `State machine > name`](#name)
- [3. Property `State machine > description`](#description)
- [4. Property `State machine > target`](#target)
- [5. Property `State machine > stateField`](#stateField)
- [6. Property `State machine > initial`](#initial)
- [7. Property `State machine > states`](#states)
  - [7.1. State machine > states > State](#states_items)
    - [7.1.1. Property `State machine > states > State > id`](#states_items_id)
    - [7.1.2. Property `State machine > states > State > name`](#states_items_name)
    - [7.1.3. Property `State machine > states > State > description`](#states_items_description)
    - [7.1.4. Property `State machine > states > State > mutableFields`](#states_items_mutableFields)
      - [7.1.4.1. Property `State machine > states > State > mutableFields > oneOf > item 0`](#states_items_mutableFields_oneOf_i0)
      - [7.1.4.2. Property `State machine > states > State > mutableFields > oneOf > item 1`](#states_items_mutableFields_oneOf_i1)
      - [7.1.4.3. Property `State machine > states > State > mutableFields > oneOf > Field list`](#states_items_mutableFields_oneOf_i2)
        - [7.1.4.3.1. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > Field reference`](#states_items_mutableFields_oneOf_i2_oneOf_i0)
        - [7.1.4.3.2. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1`](#states_items_mutableFields_oneOf_i2_oneOf_i1)
          - [7.1.4.3.2.1. State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1 > Field reference](#states_items_mutableFields_oneOf_i2_oneOf_i1_items)
    - [7.1.5. Property `State machine > states > State > requiredFields`](#states_items_requiredFields)
      - [7.1.5.1. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > Field reference`](#states_items_mutableFields_oneOf_i2_oneOf_i0)
      - [7.1.5.2. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1`](#states_items_mutableFields_oneOf_i2_oneOf_i1)
        - [7.1.5.2.1. State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1 > Field reference](#states_items_mutableFields_oneOf_i2_oneOf_i1_items)
    - [7.1.6. Property `State machine > states > State > terminal`](#states_items_terminal)
- [8. Property `State machine > transitions`](#transitions)
  - [8.1. State machine > transitions > Transition](#transitions_items)
    - [8.1.1. Property `State machine > transitions > Transition > id`](#transitions_items_id)
    - [8.1.2. Property `State machine > transitions > Transition > name`](#transitions_items_name)
    - [8.1.3. Property `State machine > transitions > Transition > description`](#transitions_items_description)
    - [8.1.4. Property `State machine > transitions > Transition > from`](#transitions_items_from)
      - [8.1.4.1. Property `State machine > transitions > Transition > from > oneOf > item 0`](#transitions_items_from_oneOf_i0)
      - [8.1.4.2. Property `State machine > transitions > Transition > from > oneOf > Identifier`](#transitions_items_from_oneOf_i1)
      - [8.1.4.3. Property `State machine > transitions > Transition > from > oneOf > item 2`](#transitions_items_from_oneOf_i2)
        - [8.1.4.3.1. State machine > transitions > Transition > from > oneOf > item 2 > Identifier](#transitions_items_from_oneOf_i2_items)
    - [8.1.5. Property `State machine > transitions > Transition > to`](#transitions_items_to)
    - [8.1.6. Property `State machine > transitions > Transition > via`](#transitions_items_via)
      - [8.1.6.1. Property `State machine > transitions > Transition > via > oneOf > Identifier`](#transitions_items_via_oneOf_i0)
      - [8.1.6.2. Property `State machine > transitions > Transition > via > oneOf > item 1`](#transitions_items_via_oneOf_i1)
        - [8.1.6.2.1. State machine > transitions > Transition > via > oneOf > item 1 > Identifier](#transitions_items_via_oneOf_i1_items)
    - [8.1.7. Property `State machine > transitions > Transition > guard`](#transitions_items_guard)
    - [8.1.8. Property `State machine > transitions > Transition > emits`](#transitions_items_emits)
      - [8.1.8.1. Property `State machine > transitions > Transition > emits > oneOf > Identifier`](#transitions_items_emits_oneOf_i0)
      - [8.1.8.2. Property `State machine > transitions > Transition > emits > oneOf > item 1`](#transitions_items_emits_oneOf_i1)
        - [8.1.8.2.1. State machine > transitions > Transition > emits > oneOf > item 1 > Identifier](#transitions_items_emits_oneOf_i1_items)
- [9. Property `State machine > lifecycle`](#lifecycle)

**Title:** State Machine

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** Legal lifecycle of an entity: which states it can occupy, which transitions are legal between them, what triggers each transition, and which fields are mutable in which state. State machines are referenced from a model and generate both the runtime state-validation code and the illegal-transition test cases.

| Property                       | Pattern | Type   | Deprecated | Definition                            | Title/Description          |
| ------------------------------ | ------- | ------ | ---------- | ------------------------------------- | -------------------------- |
| + [id](#id )                   | No      | string | No         | In #/definitions/identifierSchema     | Identifier                 |
| + [name](#name )               | No      | string | No         | -                                     | State machine display name |
| + [description](#description ) | No      | string | No         | -                                     | State machine description  |
| + [target](#target )           | No      | string | No         | In #/definitions/identifierSchema     | Target model               |
| - [stateField](#stateField )   | No      | string | No         | In #/definitions/fieldReferenceSchema | State field                |
| + [initial](#initial )         | No      | string | No         | In #/definitions/identifierSchema     | Initial state              |
| + [states](#states )           | No      | array  | No         | -                                     | States                     |
| + [transitions](#transitions ) | No      | array  | No         | -                                     | Transitions                |
| - [lifecycle](#lifecycle )     | No      | object | No         | -                                     | Field (lifecycleSchema)    |

## <a name="id"></a>1. Property `State machine > id`

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

## <a name="name"></a>2. Property `State machine > name`

**Title:** State machine display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `State machine > description`

**Title:** State machine description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What entity lifecycle this state machine governs and why.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="target"></a>4. Property `State machine > target`

**Title:** Target model

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

**Description:** The model whose lifecycle this state machine governs. The stateField on that model holds the current state id.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="stateField"></a>5. Property `State machine > stateField`

**Title:** State field

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `string`                           |
| **Required**   | No                                 |
| **Defined in** | #/definitions/fieldReferenceSchema |

**Description:** Field on the target model that records the current state. Defaults to `state` when omitted; declare explicitly when the model uses a different name.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="initial"></a>6. Property `State machine > initial`

**Title:** Initial state

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

**Description:** The state newly created instances enter.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="states"></a>7. Property `State machine > states`

**Title:** States

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description                                 |
| ------------------------------- | ------------------------------------------- |
| [State](#states_items)          | A named state the target entity may occupy. |

### <a name="states_items"></a>7.1. State machine > states > State

**Title:** State

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/definitions/stateSchema |

**Description:** A named state the target entity may occupy.

| Property                                          | Pattern | Type        | Deprecated | Definition                       | Title/Description  |
| ------------------------------------------------- | ------- | ----------- | ---------- | -------------------------------- | ------------------ |
| + [id](#states_items_id )                         | No      | string      | No         | Same as [id](#id )               | Identifier         |
| + [name](#states_items_name )                     | No      | string      | No         | -                                | State display name |
| + [description](#states_items_description )       | No      | string      | No         | -                                | State description  |
| - [mutableFields](#states_items_mutableFields )   | No      | Combination | No         | -                                | Mutable fields     |
| - [requiredFields](#states_items_requiredFields ) | No      | object      | No         | In #/definitions/fieldListSchema | Required fields    |
| - [terminal](#states_items_terminal )             | No      | boolean     | No         | -                                | Terminal state     |

#### <a name="states_items_id"></a>7.1.1. Property `State machine > states > State > id`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | Yes       |
| **Same definition as** | [id](#id) |

#### <a name="states_items_name"></a>7.1.2. Property `State machine > states > State > name`

**Title:** State display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

#### <a name="states_items_description"></a>7.1.3. Property `State machine > states > State > description`

**Title:** State description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this state represents in the domain and what an entity is observable as while occupying it. Required so the meaning of each state is documented as part of the lifecycle, not in surrounding code.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="states_items_mutableFields"></a>7.1.4. Property `State machine > states > State > mutableFields`

**Title:** Mutable fields

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Fields the entity is allowed to mutate while in this state. Use the literal `none` to declare the state immutable, `all` to allow any field, or list specific fields.

| One of(Option)                                     |
| -------------------------------------------------- |
| [item 0](#states_items_mutableFields_oneOf_i0)     |
| [item 1](#states_items_mutableFields_oneOf_i1)     |
| [Field list](#states_items_mutableFields_oneOf_i2) |

##### <a name="states_items_mutableFields_oneOf_i0"></a>7.1.4.1. Property `State machine > states > State > mutableFields > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"none"`

##### <a name="states_items_mutableFields_oneOf_i1"></a>7.1.4.2. Property `State machine > states > State > mutableFields > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"all"`

##### <a name="states_items_mutableFields_oneOf_i2"></a>7.1.4.3. Property `State machine > states > State > mutableFields > oneOf > Field list`

**Title:** Field list

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/fieldListSchema |

**Description:** One or more field references on the target model.

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Field reference](#states_items_mutableFields_oneOf_i2_oneOf_i0) |
| [item 1](#states_items_mutableFields_oneOf_i2_oneOf_i1)          |

###### <a name="states_items_mutableFields_oneOf_i2_oneOf_i0"></a>7.1.4.3.1. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > Field reference`

**Title:** Field reference

|                        |                           |
| ---------------------- | ------------------------- |
| **Type**               | `string`                  |
| **Required**           | No                        |
| **Same definition as** | [stateField](#stateField) |

###### <a name="states_items_mutableFields_oneOf_i2_oneOf_i1"></a>7.1.4.3.2. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1`

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

| Each item of this array must be                                        | Description |
| ---------------------------------------------------------------------- | ----------- |
| [Field reference](#states_items_mutableFields_oneOf_i2_oneOf_i1_items) | -           |

###### <a name="states_items_mutableFields_oneOf_i2_oneOf_i1_items"></a>7.1.4.3.2.1. State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1 > Field reference

**Title:** Field reference

|                        |                           |
| ---------------------- | ------------------------- |
| **Type**               | `string`                  |
| **Required**           | No                        |
| **Same definition as** | [stateField](#stateField) |

#### <a name="states_items_requiredFields"></a>7.1.5. Property `State machine > states > State > requiredFields`

**Title:** Required fields

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/fieldListSchema |

**Description:** Fields that must be non-null while in this state. Example: a shipped order requires shipped_at and tracking_number.

| One of(Option)                                                   |
| ---------------------------------------------------------------- |
| [Field reference](#states_items_mutableFields_oneOf_i2_oneOf_i0) |
| [item 1](#states_items_mutableFields_oneOf_i2_oneOf_i1)          |

##### <a name="states_items_mutableFields_oneOf_i2_oneOf_i0"></a>7.1.5.1. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > Field reference`

**Title:** Field reference

|                        |                           |
| ---------------------- | ------------------------- |
| **Type**               | `string`                  |
| **Required**           | No                        |
| **Same definition as** | [stateField](#stateField) |

##### <a name="states_items_mutableFields_oneOf_i2_oneOf_i1"></a>7.1.5.2. Property `State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1`

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

| Each item of this array must be                                        | Description |
| ---------------------------------------------------------------------- | ----------- |
| [Field reference](#states_items_mutableFields_oneOf_i2_oneOf_i1_items) | -           |

###### <a name="states_items_mutableFields_oneOf_i2_oneOf_i1_items"></a>7.1.5.2.1. State machine > states > State > mutableFields > oneOf > Field list > oneOf > item 1 > Field reference

**Title:** Field reference

|                        |                           |
| ---------------------- | ------------------------- |
| **Type**               | `string`                  |
| **Required**           | No                        |
| **Same definition as** | [stateField](#stateField) |

#### <a name="states_items_terminal"></a>7.1.6. Property `State machine > states > State > terminal`

**Title:** Terminal state

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Marks a state as final / absorbing -- no transitions may leave it. Generators emit assertions accordingly.

## <a name="transitions"></a>8. Property `State machine > transitions`

**Title:** Transitions

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

| Each item of this array must be  | Description                                                          |
| -------------------------------- | -------------------------------------------------------------------- |
| [Transition](#transitions_items) | A legal move between states, scoped to the use case that effects it. |

### <a name="transitions_items"></a>8.1. State machine > transitions > Transition

**Title:** Transition

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/transitionSchema |

**Description:** A legal move between states, scoped to the use case that effects it.

| Property                                         | Pattern | Type        | Deprecated | Definition                        | Title/Description       |
| ------------------------------------------------ | ------- | ----------- | ---------- | --------------------------------- | ----------------------- |
| + [id](#transitions_items_id )                   | No      | string      | No         | Same as [id](#id )                | Identifier              |
| - [name](#transitions_items_name )               | No      | string      | No         | -                                 | Transition display name |
| + [description](#transitions_items_description ) | No      | string      | No         | -                                 | Transition description  |
| + [from](#transitions_items_from )               | No      | Combination | No         | -                                 | Source state(s)         |
| + [to](#transitions_items_to )                   | No      | string      | No         | In #/definitions/identifierSchema | Destination state       |
| - [via](#transitions_items_via )                 | No      | Combination | No         | -                                 | Triggering use case     |
| - [guard](#transitions_items_guard )             | No      | object      | No         | -                                 | Expression              |
| - [emits](#transitions_items_emits )             | No      | Combination | No         | -                                 | Emitted events          |

#### <a name="transitions_items_id"></a>8.1.1. Property `State machine > transitions > Transition > id`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | Yes       |
| **Same definition as** | [id](#id) |

#### <a name="transitions_items_name"></a>8.1.2. Property `State machine > transitions > Transition > name`

**Title:** Transition display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

#### <a name="transitions_items_description"></a>8.1.3. Property `State machine > transitions > Transition > description`

**Title:** Transition description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What changes when this transition fires and why it exists. Required so the lifecycle event is documented inherent to the transition.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="transitions_items_from"></a>8.1.4. Property `State machine > transitions > Transition > from`

**Title:** Source state(s)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** State or states the transition may originate from. The literal `any` permits the transition from any non-terminal state.

| One of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#transitions_items_from_oneOf_i0)     |
| [Identifier](#transitions_items_from_oneOf_i1) |
| [item 2](#transitions_items_from_oneOf_i2)     |

##### <a name="transitions_items_from_oneOf_i0"></a>8.1.4.1. Property `State machine > transitions > Transition > from > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"any"`

##### <a name="transitions_items_from_oneOf_i1"></a>8.1.4.2. Property `State machine > transitions > Transition > from > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

##### <a name="transitions_items_from_oneOf_i2"></a>8.1.4.3. Property `State machine > transitions > Transition > from > oneOf > item 2`

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

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [Identifier](#transitions_items_from_oneOf_i2_items) | -           |

###### <a name="transitions_items_from_oneOf_i2_items"></a>8.1.4.3.1. State machine > transitions > Transition > from > oneOf > item 2 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="transitions_items_to"></a>8.1.5. Property `State machine > transitions > Transition > to`

**Title:** Destination state

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="transitions_items_via"></a>8.1.6. Property `State machine > transitions > Transition > via`

**Title:** Triggering use case

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The use case that effects this transition. Wires the state machine to the operation contract so generated code can assert "calling `ship_order` is the only path to `shipped`".

| One of(Option)                                |
| --------------------------------------------- |
| [Identifier](#transitions_items_via_oneOf_i0) |
| [item 1](#transitions_items_via_oneOf_i1)     |

##### <a name="transitions_items_via_oneOf_i0"></a>8.1.6.1. Property `State machine > transitions > Transition > via > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

##### <a name="transitions_items_via_oneOf_i1"></a>8.1.6.2. Property `State machine > transitions > Transition > via > oneOf > item 1`

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

| Each item of this array must be                     | Description |
| --------------------------------------------------- | ----------- |
| [Identifier](#transitions_items_via_oneOf_i1_items) | -           |

###### <a name="transitions_items_via_oneOf_i1_items"></a>8.1.6.2.1. State machine > transitions > Transition > via > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="transitions_items_guard"></a>8.1.7. Property `State machine > transitions > Transition > guard`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

#### <a name="transitions_items_emits"></a>8.1.8. Property `State machine > transitions > Transition > emits`

**Title:** Emitted events

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Events emitted when this transition fires.

| One of(Option)                                  |
| ----------------------------------------------- |
| [Identifier](#transitions_items_emits_oneOf_i0) |
| [item 1](#transitions_items_emits_oneOf_i1)     |

##### <a name="transitions_items_emits_oneOf_i0"></a>8.1.8.1. Property `State machine > transitions > Transition > emits > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

##### <a name="transitions_items_emits_oneOf_i1"></a>8.1.8.2. Property `State machine > transitions > Transition > emits > oneOf > item 1`

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

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [Identifier](#transitions_items_emits_oneOf_i1_items) | -           |

###### <a name="transitions_items_emits_oneOf_i1_items"></a>8.1.8.2.1. State machine > transitions > Transition > emits > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="lifecycle"></a>9. Property `State machine > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

----------------------------------------------------------------------------------------------------------------------------
