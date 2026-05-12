# Use Case

- [1. Property `Use case > id`](#id)
- [2. Property `Use case > name`](#name)
- [3. Property `Use case > description`](#description)
- [4. Property `Use case > input`](#input)
  - [4.1. Property `Use case > input > oneOf > Identifier`](#input_oneOf_i0)
  - [4.2. Property `Use case > input > oneOf > item 1`](#input_oneOf_i1)
    - [4.2.1. Use case > input > oneOf > item 1 > Identifier](#input_oneOf_i1_items)
- [5. Property `Use case > output`](#output)
  - [5.1. Property `Use case > input > oneOf > Identifier`](#input_oneOf_i0)
  - [5.2. Property `Use case > input > oneOf > item 1`](#input_oneOf_i1)
    - [5.2.1. Use case > input > oneOf > item 1 > Identifier](#input_oneOf_i1_items)
- [6. Property `Use case > relation`](#relation)
  - [6.1. Property `Use case > relation > oneOf > Dimensional relation`](#relation_oneOf_i0)
    - [6.1.1. Property `Use case > relation > oneOf > Dimensional relation > kind`](#relation_oneOf_i0_kind)
    - [6.1.2. Property `Use case > relation > oneOf > Dimensional relation > cardinality`](#relation_oneOf_i0_cardinality)
  - [6.2. Property `Use case > relation > oneOf > Key relation`](#relation_oneOf_i1)
    - [6.2.1. Property `Use case > relation > oneOf > Key relation > kind`](#relation_oneOf_i1_kind)
    - [6.2.2. Property `Use case > relation > oneOf > Key relation > inputKey`](#relation_oneOf_i1_inputKey)
      - [6.2.2.1. Property `Use case > relation > oneOf > Key relation > inputKey > oneOf > Field reference`](#relation_oneOf_i1_inputKey_oneOf_i0)
      - [6.2.2.2. Property `Use case > relation > oneOf > Key relation > inputKey > oneOf > item 1`](#relation_oneOf_i1_inputKey_oneOf_i1)
        - [6.2.2.2.1. Use case > relation > oneOf > Key relation > inputKey > oneOf > item 1 > Field reference](#relation_oneOf_i1_inputKey_oneOf_i1_items)
    - [6.2.3. Property `Use case > relation > oneOf > Key relation > outputKey`](#relation_oneOf_i1_outputKey)
      - [6.2.3.1. Property `Use case > relation > oneOf > Key relation > outputKey > oneOf > Field reference`](#relation_oneOf_i1_outputKey_oneOf_i0)
      - [6.2.3.2. Property `Use case > relation > oneOf > Key relation > outputKey > oneOf > item 1`](#relation_oneOf_i1_outputKey_oneOf_i1)
        - [6.2.3.2.1. Use case > relation > oneOf > Key relation > outputKey > oneOf > item 1 > Field reference](#relation_oneOf_i1_outputKey_oneOf_i1_items)
    - [6.2.4. Property `Use case > relation > oneOf > Key relation > cardinality`](#relation_oneOf_i1_cardinality)
  - [6.3. Property `Use case > relation > oneOf > Query relation`](#relation_oneOf_i2)
    - [6.3.1. Property `Use case > relation > oneOf > Query relation > kind`](#relation_oneOf_i2_kind)
    - [6.3.2. Property `Use case > relation > oneOf > Query relation > filters`](#relation_oneOf_i2_filters)
      - [6.3.2.1. Use case > relation > oneOf > Query relation > filters > filters items](#relation_oneOf_i2_filters_items)
        - [6.3.2.1.1. Property `Use case > relation > oneOf > Query relation > filters > filters items > inputField`](#relation_oneOf_i2_filters_items_inputField)
        - [6.3.2.1.2. Property `Use case > relation > oneOf > Query relation > filters > filters items > outputField`](#relation_oneOf_i2_filters_items_outputField)
        - [6.3.2.1.3. Property `Use case > relation > oneOf > Query relation > filters > filters items > operator`](#relation_oneOf_i2_filters_items_operator)
    - [6.3.3. Property `Use case > relation > oneOf > Query relation > cardinality`](#relation_oneOf_i2_cardinality)
  - [6.4. Property `Use case > relation > oneOf > Opaque relation`](#relation_oneOf_i3)
    - [6.4.1. Property `Use case > relation > oneOf > Opaque relation > kind`](#relation_oneOf_i3_kind)
    - [6.4.2. Property `Use case > relation > oneOf > Opaque relation > reason`](#relation_oneOf_i3_reason)
    - [6.4.3. Property `Use case > relation > oneOf > Opaque relation > pure`](#relation_oneOf_i3_pure)
    - [6.4.4. Property `Use case > relation > oneOf > Opaque relation > cardinality`](#relation_oneOf_i3_cardinality)
- [7. Property `Use case > next`](#next)
  - [7.1. Property `Use case > next > oneOf > Identifier`](#next_oneOf_i0)
  - [7.2. Property `Use case > next > oneOf > item 1`](#next_oneOf_i1)
    - [7.2.1. Use case > next > oneOf > item 1 > Identifier](#next_oneOf_i1_items)
- [8. Property `Use case > extends`](#extends)
- [9. Property `Use case > focus`](#focus)
- [10. Property `Use case > domain`](#domain)
- [11. Property `Use case > errors`](#errors)
  - [11.1. Use case > errors > Error reference](#errors_items)
    - [11.1.1. Property `Use case > errors > Error reference > oneOf > Identifier`](#errors_items_oneOf_i0)
    - [11.1.2. Property `Use case > errors > Error reference > oneOf > item 1`](#errors_items_oneOf_i1)
      - [11.1.2.1. Property `Use case > errors > Error reference > oneOf > item 1 > error`](#errors_items_oneOf_i1_error)
      - [11.1.2.2. Property `Use case > errors > Error reference > oneOf > item 1 > when`](#errors_items_oneOf_i1_when)
      - [11.1.2.3. Property `Use case > errors > Error reference > oneOf > item 1 > observed`](#errors_items_oneOf_i1_observed)
- [12. Property `Use case > permissions`](#permissions)
  - [12.1. Property `Use case > next > oneOf > Identifier`](#next_oneOf_i0)
  - [12.2. Property `Use case > next > oneOf > item 1`](#next_oneOf_i1)
    - [12.2.1. Use case > next > oneOf > item 1 > Identifier](#next_oneOf_i1_items)
- [13. Property `Use case > emits`](#emits)
  - [13.1. Use case > emits > Emitted event reference](#emits_items)
    - [13.1.1. Property `Use case > emits > Emitted event reference > oneOf > Identifier`](#emits_items_oneOf_i0)
    - [13.1.2. Property `Use case > emits > Emitted event reference > oneOf > item 1`](#emits_items_oneOf_i1)
      - [13.1.2.1. Property `Use case > emits > Emitted event reference > oneOf > item 1 > event`](#emits_items_oneOf_i1_event)
      - [13.1.2.2. Property `Use case > emits > Emitted event reference > oneOf > item 1 > when`](#emits_items_oneOf_i1_when)
- [14. Property `Use case > transitions`](#transitions)
  - [14.1. Use case > transitions > Lifecycle transition reference](#transitions_items)
    - [14.1.1. Property `Use case > transitions > Lifecycle transition reference > model`](#transitions_items_model)
    - [14.1.2. Property `Use case > transitions > Lifecycle transition reference > transition`](#transitions_items_transition)
    - [14.1.3. Property `Use case > transitions > Lifecycle transition reference > from`](#transitions_items_from)
    - [14.1.4. Property `Use case > transitions > Lifecycle transition reference > to`](#transitions_items_to)
- [15. Property `Use case > safety`](#safety)
  - [15.1. Property `Use case > safety > mutates`](#safety_mutates)
  - [15.2. Property `Use case > safety > idempotent`](#safety_idempotent)
  - [15.3. Property `Use case > safety > cacheable`](#safety_cacheable)
    - [15.3.1. Property `Use case > safety > cacheable > oneOf > item 0`](#safety_cacheable_oneOf_i0)
    - [15.3.2. Property `Use case > safety > cacheable > oneOf > item 1`](#safety_cacheable_oneOf_i1)
      - [15.3.2.1. Property `Use case > safety > cacheable > oneOf > item 1 > ttl`](#safety_cacheable_oneOf_i1_ttl)
      - [15.3.2.2. Property `Use case > safety > cacheable > oneOf > item 1 > vary`](#safety_cacheable_oneOf_i1_vary)
        - [15.3.2.2.1. Use case > safety > cacheable > oneOf > item 1 > vary > Field reference](#safety_cacheable_oneOf_i1_vary_items)
  - [15.4. Property `Use case > safety > latencyTarget`](#safety_latencyTarget)
  - [15.5. Property `Use case > safety > availabilityTarget`](#safety_availabilityTarget)
  - [15.6. Property `Use case > safety > throughputTarget`](#safety_throughputTarget)
  - [15.7. Property `Use case > safety > rateLimit`](#safety_rateLimit)
    - [15.7.1. Property `Use case > safety > rateLimit > limit`](#safety_rateLimit_limit)
    - [15.7.2. Property `Use case > safety > rateLimit > window`](#safety_rateLimit_window)
    - [15.7.3. Property `Use case > safety > rateLimit > per`](#safety_rateLimit_per)
  - [15.8. Property `Use case > safety > timeout`](#safety_timeout)
- [16. Property `Use case > observability`](#observability)
  - [16.1. Property `Use case > observability > metrics`](#observability_metrics)
    - [16.1.1. Use case > observability > metrics > Metric](#observability_metrics_items)
      - [16.1.1.1. Property `Use case > observability > metrics > Metric > name`](#observability_metrics_items_name)
      - [16.1.1.2. Property `Use case > observability > metrics > Metric > kind`](#observability_metrics_items_kind)
      - [16.1.1.3. Property `Use case > observability > metrics > Metric > description`](#observability_metrics_items_description)
      - [16.1.1.4. Property `Use case > observability > metrics > Metric > labels`](#observability_metrics_items_labels)
        - [16.1.1.4.1. Use case > observability > metrics > Metric > labels > labels items](#observability_metrics_items_labels_items)
  - [16.2. Property `Use case > observability > traces`](#observability_traces)
    - [16.2.1. Property `Use case > observability > traces > spanName`](#observability_traces_spanName)
    - [16.2.2. Property `Use case > observability > traces > description`](#observability_traces_description)
    - [16.2.3. Property `Use case > observability > traces > attributes`](#observability_traces_attributes)
      - [16.2.3.1. Use case > observability > traces > attributes > attributes items](#observability_traces_attributes_items)
  - [16.3. Property `Use case > observability > logs`](#observability_logs)
    - [16.3.1. Use case > observability > logs > Log event](#observability_logs_items)
      - [16.3.1.1. Property `Use case > observability > logs > Log event > event`](#observability_logs_items_event)
      - [16.3.1.2. Property `Use case > observability > logs > Log event > level`](#observability_logs_items_level)
      - [16.3.1.3. Property `Use case > observability > logs > Log event > description`](#observability_logs_items_description)
- [17. Property `Use case > scenarios`](#scenarios)
  - [17.1. Use case > scenarios > scenarios items](#scenarios_items)
    - [17.1.1. Property `Use case > scenarios > scenarios items > oneOf > Identifier`](#scenarios_items_oneOf_i0)
    - [17.1.2. Property `Use case > scenarios > scenarios items > oneOf > Scenario (scenarioSchema)`](#scenarios_items_oneOf_i1)
- [18. Property `Use case > lifecycle`](#lifecycle)

**Title:** Use Case

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** A Domain-Interfacing Use Case: a contract between an input model (or collection) and an output model (or collection), augmented with the permissions, errors, events, lifecycle transitions, safety guarantees, observability surface, and acceptance criteria that together describe exactly what the operation does. The relation discriminator says how the output is produced from the input -- by dimensional combination, by key lookup, by query / filter, or as an explicitly opaque external call.

| Property                           | Pattern | Type   | Deprecated | Definition                            | Title/Description                  |
| ---------------------------------- | ------- | ------ | ---------- | ------------------------------------- | ---------------------------------- |
| + [id](#id )                       | No      | string | No         | In #/definitions/identifierSchema     | Use case identifier                |
| + [name](#name )                   | No      | string | No         | -                                     | Use case display name              |
| + [description](#description )     | No      | string | No         | -                                     | Use case description               |
| + [input](#input )                 | No      | object | No         | In #/definitions/modelReferenceSchema | Input model(s)                     |
| + [output](#output )               | No      | object | No         | In #/definitions/modelReferenceSchema | Output model(s)                    |
| - [relation](#relation )           | No      | object | No         | In #/definitions/relationSchema       | Input-output relation              |
| - [next](#next )                   | No      | object | No         | In #/definitions/identifierListSchema | Subsequent use case(s)             |
| - [extends](#extends )             | No      | string | No         | In #/definitions/identifierSchema     | Parent use case                    |
| - [focus](#focus )                 | No      | string | No         | -                                     | Template focus                     |
| - [domain](#domain )               | No      | string | No         | In #/definitions/identifierSchema     | Bounded context                    |
| - [errors](#errors )               | No      | array  | No         | -                                     | Typed errors raised                |
| - [permissions](#permissions )     | No      | object | No         | In #/definitions/identifierListSchema | Required permissions               |
| - [emits](#emits )                 | No      | array  | No         | -                                     | Events emitted                     |
| - [transitions](#transitions )     | No      | array  | No         | -                                     | Lifecycle transitions effected     |
| - [safety](#safety )               | No      | object | No         | In #/definitions/safetySchema         | Safety / invocation classification |
| - [observability](#observability ) | No      | object | No         | In #/definitions/observabilitySchema  | Observability surface              |
| - [scenarios](#scenarios )         | No      | array  | No         | -                                     | Acceptance scenarios               |
| - [lifecycle](#lifecycle )         | No      | object | No         | -                                     | Field (lifecycleSchema)            |

## <a name="id"></a>1. Property `Use case > id`

**Title:** Use case identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="name"></a>2. Property `Use case > name`

**Title:** Use case display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `Use case > description`

**Title:** Use case description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this use case does and the domain intent behind it. Required at every site so the operation's purpose is documented inherent to its definition.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="input"></a>4. Property `Use case > input`

**Title:** Input model(s)

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | Yes                                |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/modelReferenceSchema |

**Description:** One or more model or collection identifiers used as input or output.

| One of(Option)                |
| ----------------------------- |
| [Identifier](#input_oneOf_i0) |
| [item 1](#input_oneOf_i1)     |

### <a name="input_oneOf_i0"></a>4.1. Property `Use case > input > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="input_oneOf_i1"></a>4.2. Property `Use case > input > oneOf > item 1`

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

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [Identifier](#input_oneOf_i1_items) | -           |

#### <a name="input_oneOf_i1_items"></a>4.2.1. Use case > input > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="output"></a>5. Property `Use case > output`

**Title:** Output model(s)

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | Yes                                |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/modelReferenceSchema |

**Description:** One or more model or collection identifiers used as input or output.

| One of(Option)                |
| ----------------------------- |
| [Identifier](#input_oneOf_i0) |
| [item 1](#input_oneOf_i1)     |

### <a name="input_oneOf_i0"></a>5.1. Property `Use case > input > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="input_oneOf_i1"></a>5.2. Property `Use case > input > oneOf > item 1`

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

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [Identifier](#input_oneOf_i1_items) | -           |

#### <a name="input_oneOf_i1_items"></a>5.2.1. Use case > input > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="relation"></a>6. Property `Use case > relation`

**Title:** Input-output relation

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `combining`                  |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | #/definitions/relationSchema |

**Description:** Defaults to { kind: dimensional } when omitted, preserving the historical compute-style contract for use cases that don't declare a relation.

| One of(Option)                             |
| ------------------------------------------ |
| [Dimensional relation](#relation_oneOf_i0) |
| [Key relation](#relation_oneOf_i1)         |
| [Query relation](#relation_oneOf_i2)       |
| [Opaque relation](#relation_oneOf_i3)      |

### <a name="relation_oneOf_i0"></a>6.1. Property `Use case > relation > oneOf > Dimensional relation`

**Title:** Dimensional relation

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | #/definitions/dimensionalRelationSchema |

**Description:** The unit-bearing fields on the input model(s) must be dimensionally combinable to yield the unit-bearing fields on the output model. The original DeepThought contract for compute-style use cases (e.g. density = mass / volume).

| Property                                         | Pattern | Type             | Deprecated | Definition                         | Title/Description  |
| ------------------------------------------------ | ------- | ---------------- | ---------- | ---------------------------------- | ------------------ |
| + [kind](#relation_oneOf_i0_kind )               | No      | const            | No         | -                                  | -                  |
| - [cardinality](#relation_oneOf_i0_cardinality ) | No      | enum (of string) | No         | In #/definitions/cardinalitySchema | Output cardinality |

#### <a name="relation_oneOf_i0_kind"></a>6.1.1. Property `Use case > relation > oneOf > Dimensional relation > kind`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"dimensional"`

#### <a name="relation_oneOf_i0_cardinality"></a>6.1.2. Property `Use case > relation > oneOf > Dimensional relation > cardinality`

**Title:** Output cardinality

|                |                                 |
| -------------- | ------------------------------- |
| **Type**       | `enum (of string)`              |
| **Required**   | No                              |
| **Defined in** | #/definitions/cardinalitySchema |

**Description:** Whether the use case returns one record or many.

Must be one of:
* "one"
* "many"

### <a name="relation_oneOf_i1"></a>6.2. Property `Use case > relation > oneOf > Key relation`

**Title:** Key relation

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | #/definitions/keyRelationSchema |

**Description:** Data-retrieval style. The input supplies a lookup key (an id, slug, etc.) and the output is the record identified by that key. Dimensional analysis is bypassed because the input key and output payload do not share a dimension -- they relate by identity.

| Property                                         | Pattern | Type             | Deprecated | Definition                                             | Title/Description   |
| ------------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------------------------------ | ------------------- |
| + [kind](#relation_oneOf_i1_kind )               | No      | const            | No         | -                                                      | -                   |
| + [inputKey](#relation_oneOf_i1_inputKey )       | No      | Combination      | No         | -                                                      | Input key field(s)  |
| - [outputKey](#relation_oneOf_i1_outputKey )     | No      | Combination      | No         | -                                                      | Output key field(s) |
| - [cardinality](#relation_oneOf_i1_cardinality ) | No      | enum (of string) | No         | Same as [cardinality](#relation_oneOf_i0_cardinality ) | Output cardinality  |

#### <a name="relation_oneOf_i1_kind"></a>6.2.1. Property `Use case > relation > oneOf > Key relation > kind`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"key"`

#### <a name="relation_oneOf_i1_inputKey"></a>6.2.2. Property `Use case > relation > oneOf > Key relation > inputKey`

**Title:** Input key field(s)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Field(s) on the input model whose values supply the lookup key.

| One of(Option)                                          |
| ------------------------------------------------------- |
| [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0) |
| [item 1](#relation_oneOf_i1_inputKey_oneOf_i1)          |

##### <a name="relation_oneOf_i1_inputKey_oneOf_i0"></a>6.2.2.1. Property `Use case > relation > oneOf > Key relation > inputKey > oneOf > Field reference`

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

##### <a name="relation_oneOf_i1_inputKey_oneOf_i1"></a>6.2.2.2. Property `Use case > relation > oneOf > Key relation > inputKey > oneOf > item 1`

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

| Each item of this array must be                               | Description |
| ------------------------------------------------------------- | ----------- |
| [Field reference](#relation_oneOf_i1_inputKey_oneOf_i1_items) | -           |

###### <a name="relation_oneOf_i1_inputKey_oneOf_i1_items"></a>6.2.2.2.1. Use case > relation > oneOf > Key relation > inputKey > oneOf > item 1 > Field reference

**Title:** Field reference

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| **Type**               | `string`                                                |
| **Required**           | No                                                      |
| **Same definition as** | [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0) |

#### <a name="relation_oneOf_i1_outputKey"></a>6.2.3. Property `Use case > relation > oneOf > Key relation > outputKey`

**Title:** Output key field(s)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Field(s) on the output model that the inputKey resolves against. Defaults to the output model's declared `key`.

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Field reference](#relation_oneOf_i1_outputKey_oneOf_i0) |
| [item 1](#relation_oneOf_i1_outputKey_oneOf_i1)          |

##### <a name="relation_oneOf_i1_outputKey_oneOf_i0"></a>6.2.3.1. Property `Use case > relation > oneOf > Key relation > outputKey > oneOf > Field reference`

**Title:** Field reference

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| **Type**               | `string`                                                |
| **Required**           | No                                                      |
| **Same definition as** | [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0) |

##### <a name="relation_oneOf_i1_outputKey_oneOf_i1"></a>6.2.3.2. Property `Use case > relation > oneOf > Key relation > outputKey > oneOf > item 1`

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

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [Field reference](#relation_oneOf_i1_outputKey_oneOf_i1_items) | -           |

###### <a name="relation_oneOf_i1_outputKey_oneOf_i1_items"></a>6.2.3.2.1. Use case > relation > oneOf > Key relation > outputKey > oneOf > item 1 > Field reference

**Title:** Field reference

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| **Type**               | `string`                                                |
| **Required**           | No                                                      |
| **Same definition as** | [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0) |

#### <a name="relation_oneOf_i1_cardinality"></a>6.2.4. Property `Use case > relation > oneOf > Key relation > cardinality`

**Title:** Output cardinality

|                        |                                               |
| ---------------------- | --------------------------------------------- |
| **Type**               | `enum (of string)`                            |
| **Required**           | No                                            |
| **Same definition as** | [cardinality](#relation_oneOf_i0_cardinality) |

**Description:** Whether the use case returns one record or many.

### <a name="relation_oneOf_i2"></a>6.3. Property `Use case > relation > oneOf > Query relation`

**Title:** Query relation

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/definitions/queryRelationSchema |

**Description:** Data-retrieval style with a filter / predicate as the input. The output is zero, one, or many records that match. Each filter pairs an input field with the output field it constrains; if `filters` is omitted, every input field is assumed to filter the same-named field on the output.

| Property                                         | Pattern | Type             | Deprecated | Definition                                             | Title/Description  |
| ------------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------------------------------ | ------------------ |
| + [kind](#relation_oneOf_i2_kind )               | No      | const            | No         | -                                                      | -                  |
| - [filters](#relation_oneOf_i2_filters )         | No      | array of object  | No         | -                                                      | Filter clauses     |
| - [cardinality](#relation_oneOf_i2_cardinality ) | No      | enum (of string) | No         | Same as [cardinality](#relation_oneOf_i0_cardinality ) | Output cardinality |

#### <a name="relation_oneOf_i2_kind"></a>6.3.1. Property `Use case > relation > oneOf > Query relation > kind`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"query"`

#### <a name="relation_oneOf_i2_filters"></a>6.3.2. Property `Use case > relation > oneOf > Query relation > filters`

**Title:** Filter clauses

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

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [filters items](#relation_oneOf_i2_filters_items) | -           |

##### <a name="relation_oneOf_i2_filters_items"></a>6.3.2.1. Use case > relation > oneOf > Query relation > filters > filters items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                       | Title/Description |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------------------------------------------------------------- | ----------------- |
| + [inputField](#relation_oneOf_i2_filters_items_inputField )   | No      | string           | No         | Same as [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0 ) | Field reference   |
| + [outputField](#relation_oneOf_i2_filters_items_outputField ) | No      | string           | No         | Same as [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0 ) | Field reference   |
| - [operator](#relation_oneOf_i2_filters_items_operator )       | No      | enum (of string) | No         | -                                                                | Filter operator   |

###### <a name="relation_oneOf_i2_filters_items_inputField"></a>6.3.2.1.1. Property `Use case > relation > oneOf > Query relation > filters > filters items > inputField`

**Title:** Field reference

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| **Type**               | `string`                                                |
| **Required**           | Yes                                                     |
| **Same definition as** | [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0) |

###### <a name="relation_oneOf_i2_filters_items_outputField"></a>6.3.2.1.2. Property `Use case > relation > oneOf > Query relation > filters > filters items > outputField`

**Title:** Field reference

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| **Type**               | `string`                                                |
| **Required**           | Yes                                                     |
| **Same definition as** | [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0) |

###### <a name="relation_oneOf_i2_filters_items_operator"></a>6.3.2.1.3. Property `Use case > relation > oneOf > Query relation > filters > filters items > operator`

**Title:** Filter operator

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"equals"`         |

Must be one of:
* "equals"
* "not_equals"
* "contains"
* "starts_with"
* "ends_with"
* "greater_than"
* "greater_than_or_equal"
* "less_than"
* "less_than_or_equal"
* "in"
* "matches"

#### <a name="relation_oneOf_i2_cardinality"></a>6.3.3. Property `Use case > relation > oneOf > Query relation > cardinality`

**Title:** Output cardinality

|                        |                                               |
| ---------------------- | --------------------------------------------- |
| **Type**               | `enum (of string)`                            |
| **Required**           | No                                            |
| **Same definition as** | [cardinality](#relation_oneOf_i0_cardinality) |

**Description:** Whether the use case returns one record or many.

### <a name="relation_oneOf_i3"></a>6.4. Property `Use case > relation > oneOf > Opaque relation`

**Title:** Opaque relation

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/opaqueRelationSchema |

**Description:** Explicit escape hatch. The author asserts that the input/output contract cannot be validated by DeepThought -- external API calls, side-effecting operations, hashes, encryptions, translations. `reason` is required so opting out is always accompanied by a documented justification rather than silent abuse.

| Property                                         | Pattern | Type             | Deprecated | Definition                                             | Title/Description     |
| ------------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------------------------------ | --------------------- |
| + [kind](#relation_oneOf_i3_kind )               | No      | const            | No         | -                                                      | -                     |
| + [reason](#relation_oneOf_i3_reason )           | No      | string           | No         | -                                                      | Opt-out justification |
| - [pure](#relation_oneOf_i3_pure )               | No      | boolean          | No         | -                                                      | Pure operation        |
| - [cardinality](#relation_oneOf_i3_cardinality ) | No      | enum (of string) | No         | Same as [cardinality](#relation_oneOf_i0_cardinality ) | Output cardinality    |

#### <a name="relation_oneOf_i3_kind"></a>6.4.1. Property `Use case > relation > oneOf > Opaque relation > kind`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"opaque"`

#### <a name="relation_oneOf_i3_reason"></a>6.4.2. Property `Use case > relation > oneOf > Opaque relation > reason`

**Title:** Opt-out justification

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Why structured analysis is being bypassed for this use case.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="relation_oneOf_i3_pure"></a>6.4.3. Property `Use case > relation > oneOf > Opaque relation > pure`

**Title:** Pure operation

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether the operation has observable side effects. Drives generated retry / memoization decisions.

#### <a name="relation_oneOf_i3_cardinality"></a>6.4.4. Property `Use case > relation > oneOf > Opaque relation > cardinality`

**Title:** Output cardinality

|                        |                                               |
| ---------------------- | --------------------------------------------- |
| **Type**               | `enum (of string)`                            |
| **Required**           | No                                            |
| **Same definition as** | [cardinality](#relation_oneOf_i0_cardinality) |

**Description:** Whether the use case returns one record or many.

## <a name="next"></a>7. Property `Use case > next`

**Title:** Subsequent use case(s)

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** Use case(s) chained after this one.

| One of(Option)               |
| ---------------------------- |
| [Identifier](#next_oneOf_i0) |
| [item 1](#next_oneOf_i1)     |

### <a name="next_oneOf_i0"></a>7.1. Property `Use case > next > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="next_oneOf_i1"></a>7.2. Property `Use case > next > oneOf > item 1`

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

| Each item of this array must be    | Description |
| ---------------------------------- | ----------- |
| [Identifier](#next_oneOf_i1_items) | -           |

#### <a name="next_oneOf_i1_items"></a>7.2.1. Use case > next > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="extends"></a>8. Property `Use case > extends`

**Title:** Parent use case

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Identifier of a use case this one extends.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="focus"></a>9. Property `Use case > focus`

**Title:** Template focus

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Subject value that fills `{{ this.focus }}` in templated names and descriptions.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="domain"></a>10. Property `Use case > domain`

**Title:** Bounded context

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Bounded context this use case lives in. Inherits from the surrounding document if omitted.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="errors"></a>11. Property `Use case > errors`

**Title:** Typed errors raised

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

| Each item of this array must be  | Description                                                                                                                                                                                           |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Error reference](#errors_items) | A typed failure mode of this use case. Either a bare error id or an object overriding the raise condition for this specific call site (the canonical condition lives on the error definition itself). |

### <a name="errors_items"></a>11.1. Use case > errors > Error reference

**Title:** Error reference

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `combining`                  |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | #/definitions/errorRefSchema |

**Description:** A typed failure mode of this use case. Either a bare error id or an object overriding the raise condition for this specific call site (the canonical condition lives on the error definition itself).

| One of(Option)                       |
| ------------------------------------ |
| [Identifier](#errors_items_oneOf_i0) |
| [item 1](#errors_items_oneOf_i1)     |

#### <a name="errors_items_oneOf_i0"></a>11.1.1. Property `Use case > errors > Error reference > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="errors_items_oneOf_i1"></a>11.1.2. Property `Use case > errors > Error reference > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                       | Pattern | Type    | Deprecated | Definition         | Title/Description      |
| ---------------------------------------------- | ------- | ------- | ---------- | ------------------ | ---------------------- |
| + [error](#errors_items_oneOf_i1_error )       | No      | string  | No         | Same as [id](#id ) | Identifier             |
| - [when](#errors_items_oneOf_i1_when )         | No      | object  | No         | -                  | Expression             |
| - [observed](#errors_items_oneOf_i1_observed ) | No      | boolean | No         | -                  | Observed in production |

##### <a name="errors_items_oneOf_i1_error"></a>11.1.2.1. Property `Use case > errors > Error reference > oneOf > item 1 > error`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | Yes       |
| **Same definition as** | [id](#id) |

##### <a name="errors_items_oneOf_i1_when"></a>11.1.2.2. Property `Use case > errors > Error reference > oneOf > item 1 > when`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

##### <a name="errors_items_oneOf_i1_observed"></a>11.1.2.3. Property `Use case > errors > Error reference > oneOf > item 1 > observed`

**Title:** Observed in production

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Whether this failure has been observed in production. Lets generators tag tests as "documented but unobserved".

## <a name="permissions"></a>12. Property `Use case > permissions`

**Title:** Required permissions

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `combining`                        |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/identifierListSchema |

**Description:** Permission identifiers required to invoke the use case.

| One of(Option)               |
| ---------------------------- |
| [Identifier](#next_oneOf_i0) |
| [item 1](#next_oneOf_i1)     |

### <a name="next_oneOf_i0"></a>12.1. Property `Use case > next > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="next_oneOf_i1"></a>12.2. Property `Use case > next > oneOf > item 1`

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

| Each item of this array must be    | Description |
| ---------------------------------- | ----------- |
| [Identifier](#next_oneOf_i1_items) | -           |

#### <a name="next_oneOf_i1_items"></a>12.2.1. Use case > next > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="emits"></a>13. Property `Use case > emits`

**Title:** Events emitted

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

| Each item of this array must be         | Description                                                           |
| --------------------------------------- | --------------------------------------------------------------------- |
| [Emitted event reference](#emits_items) | An event emitted by this use case, optionally guarded by a predicate. |

### <a name="emits_items"></a>13.1. Use case > emits > Emitted event reference

**Title:** Emitted event reference

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/emitsEventSchema |

**Description:** An event emitted by this use case, optionally guarded by a predicate.

| One of(Option)                      |
| ----------------------------------- |
| [Identifier](#emits_items_oneOf_i0) |
| [item 1](#emits_items_oneOf_i1)     |

#### <a name="emits_items_oneOf_i0"></a>13.1.1. Property `Use case > emits > Emitted event reference > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="emits_items_oneOf_i1"></a>13.1.2. Property `Use case > emits > Emitted event reference > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                | Pattern | Type   | Deprecated | Definition         | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ------------------ | ----------------- |
| + [event](#emits_items_oneOf_i1_event ) | No      | string | No         | Same as [id](#id ) | Identifier        |
| - [when](#emits_items_oneOf_i1_when )   | No      | object | No         | -                  | Expression        |

##### <a name="emits_items_oneOf_i1_event"></a>13.1.2.1. Property `Use case > emits > Emitted event reference > oneOf > item 1 > event`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | Yes       |
| **Same definition as** | [id](#id) |

##### <a name="emits_items_oneOf_i1_when"></a>13.1.2.2. Property `Use case > emits > Emitted event reference > oneOf > item 1 > when`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

## <a name="transitions"></a>14. Property `Use case > transitions`

**Title:** Lifecycle transitions effected

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

| Each item of this array must be                      | Description                                                                                                                                                                                                                                    |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Lifecycle transition reference](#transitions_items) | A state-machine transition effected by this use case. Wires the operation contract back to the entity lifecycle declared on the affected model so generated code can assert "calling this use case is the only path to the destination state". |

### <a name="transitions_items"></a>14.1. Use case > transitions > Lifecycle transition reference

**Title:** Lifecycle transition reference

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/definitions/transitionRefSchema |

**Description:** A state-machine transition effected by this use case. Wires the operation contract back to the entity lifecycle declared on the affected model so generated code can assert "calling this use case is the only path to the destination state".

| Property                                       | Pattern | Type   | Deprecated | Definition                        | Title/Description            |
| ---------------------------------------------- | ------- | ------ | ---------- | --------------------------------- | ---------------------------- |
| + [model](#transitions_items_model )           | No      | string | No         | In #/definitions/identifierSchema | Affected model identifier    |
| - [transition](#transitions_items_transition ) | No      | string | No         | In #/definitions/identifierSchema | Transition identifier        |
| - [from](#transitions_items_from )             | No      | string | No         | In #/definitions/identifierSchema | Source state identifier      |
| - [to](#transitions_items_to )                 | No      | string | No         | In #/definitions/identifierSchema | Destination state identifier |

#### <a name="transitions_items_model"></a>14.1.1. Property `Use case > transitions > Lifecycle transition reference > model`

**Title:** Affected model identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="transitions_items_transition"></a>14.1.2. Property `Use case > transitions > Lifecycle transition reference > transition`

**Title:** Transition identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Identifier of the transition declared on the model's state machine.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="transitions_items_from"></a>14.1.3. Property `Use case > transitions > Lifecycle transition reference > from`

**Title:** Source state identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Optional shorthand when the transition isn't formally declared.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="transitions_items_to"></a>14.1.4. Property `Use case > transitions > Lifecycle transition reference > to`

**Title:** Destination state identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="safety"></a>15. Property `Use case > safety`

**Title:** Safety / invocation classification

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/definitions/safetySchema |

**Description:** Classification that drives generator decisions about HTTP method, retry policy, cache headers, and the test suite (read-only ops should be safe to call repeatedly; mutating ops shouldn't be retried blindly).

| Property                                            | Pattern | Type    | Deprecated | Definition                       | Title/Description |
| --------------------------------------------------- | ------- | ------- | ---------- | -------------------------------- | ----------------- |
| - [mutates](#safety_mutates )                       | No      | boolean | No         | -                                | Mutates state     |
| - [idempotent](#safety_idempotent )                 | No      | boolean | No         | -                                | Idempotent        |
| - [cacheable](#safety_cacheable )                   | No      | object  | No         | In #/definitions/cacheableSchema | Cacheability      |
| - [latencyTarget](#safety_latencyTarget )           | No      | string  | No         | -                                | Latency SLO       |
| - [availabilityTarget](#safety_availabilityTarget ) | No      | string  | No         | -                                | Availability SLO  |
| - [throughputTarget](#safety_throughputTarget )     | No      | string  | No         | -                                | Throughput SLO    |
| - [rateLimit](#safety_rateLimit )                   | No      | object  | No         | In #/definitions/rateLimitSchema | Rate limit        |
| - [timeout](#safety_timeout )                       | No      | string  | No         | -                                | Timeout           |

### <a name="safety_mutates"></a>15.1. Property `Use case > safety > mutates`

**Title:** Mutates state

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether the use case modifies persistent state.

### <a name="safety_idempotent"></a>15.2. Property `Use case > safety > idempotent`

**Title:** Idempotent

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether repeating the call with the same input yields the same effect.

### <a name="safety_cacheable"></a>15.3. Property `Use case > safety > cacheable`

**Title:** Cacheability

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/cacheableSchema |

**Description:** Either a boolean (cacheable / not) or a structured policy with TTL and varying-by-field rules.

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#safety_cacheable_oneOf_i0) |
| [item 1](#safety_cacheable_oneOf_i1) |

#### <a name="safety_cacheable_oneOf_i0"></a>15.3.1. Property `Use case > safety > cacheable > oneOf > item 0`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

#### <a name="safety_cacheable_oneOf_i1"></a>15.3.2. Property `Use case > safety > cacheable > oneOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [ttl](#safety_cacheable_oneOf_i1_ttl )   | No      | string | No         | -          | Time-to-live      |
| - [vary](#safety_cacheable_oneOf_i1_vary ) | No      | array  | No         | -          | Cache key fields  |

##### <a name="safety_cacheable_oneOf_i1_ttl"></a>15.3.2.1. Property `Use case > safety > cacheable > oneOf > item 1 > ttl`

**Title:** Time-to-live

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Cache lifetime as a duration string (e.g. "5m").

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="safety_cacheable_oneOf_i1_vary"></a>15.3.2.2. Property `Use case > safety > cacheable > oneOf > item 1 > vary`

**Title:** Cache key fields

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Fields that contribute to the cache key.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                          | Description |
| -------------------------------------------------------- | ----------- |
| [Field reference](#safety_cacheable_oneOf_i1_vary_items) | -           |

###### <a name="safety_cacheable_oneOf_i1_vary_items"></a>15.3.2.2.1. Use case > safety > cacheable > oneOf > item 1 > vary > Field reference

**Title:** Field reference

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| **Type**               | `string`                                                |
| **Required**           | No                                                      |
| **Same definition as** | [Field reference](#relation_oneOf_i1_inputKey_oneOf_i0) |

### <a name="safety_latencyTarget"></a>15.4. Property `Use case > safety > latencyTarget`

**Title:** Latency SLO

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Target latency (e.g. "200ms"). Optional.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="safety_availabilityTarget"></a>15.5. Property `Use case > safety > availabilityTarget`

**Title:** Availability SLO

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Target availability (e.g. "99.9"). Optional.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="safety_throughputTarget"></a>15.6. Property `Use case > safety > throughputTarget`

**Title:** Throughput SLO

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Target throughput (e.g. "1000rps"). Optional.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="safety_rateLimit"></a>15.7. Property `Use case > safety > rateLimit`

**Title:** Rate limit

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/rateLimitSchema |

**Description:** Maximum invocation rate for this use case.

| Property                              | Pattern | Type    | Deprecated | Definition                        | Title/Description |
| ------------------------------------- | ------- | ------- | ---------- | --------------------------------- | ----------------- |
| + [limit](#safety_rateLimit_limit )   | No      | integer | No         | -                                 | Limit count       |
| + [window](#safety_rateLimit_window ) | No      | string  | No         | -                                 | Window duration   |
| - [per](#safety_rateLimit_per )       | No      | string  | No         | In #/definitions/identifierSchema | Limit subject     |

#### <a name="safety_rateLimit_limit"></a>15.7.1. Property `Use case > safety > rateLimit > limit`

**Title:** Limit count

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Maximum number of invocations within the window.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

#### <a name="safety_rateLimit_window"></a>15.7.2. Property `Use case > safety > rateLimit > window`

**Title:** Window duration

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Time window the limit applies over (e.g. "1m", "1h").

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="safety_rateLimit_per"></a>15.7.3. Property `Use case > safety > rateLimit > per`

**Title:** Limit subject

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Identifier the limit is keyed by (actor, tenant, etc.).

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

### <a name="safety_timeout"></a>15.8. Property `Use case > safety > timeout`

**Title:** Timeout

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Hard timeout for the call (e.g. "5s").

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="observability"></a>16. Property `Use case > observability`

**Title:** Observability surface

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/definitions/observabilitySchema |

**Description:** Signals the use case is expected to emit. Capturing metrics, traces, and logs in the spec keeps Grafana dashboards and alert rules from drifting away from the contract they describe.

| Property                             | Pattern | Type   | Deprecated | Definition                   | Title/Description |
| ------------------------------------ | ------- | ------ | ---------- | ---------------------------- | ----------------- |
| - [metrics](#observability_metrics ) | No      | array  | No         | -                            | Metrics           |
| - [traces](#observability_traces )   | No      | object | No         | In #/definitions/traceSchema | Trace             |
| - [logs](#observability_logs )       | No      | array  | No         | -                            | Log events        |

### <a name="observability_metrics"></a>16.1. Property `Use case > observability > metrics`

**Title:** Metrics

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

| Each item of this array must be        | Description                                |
| -------------------------------------- | ------------------------------------------ |
| [Metric](#observability_metrics_items) | A signal the use case is expected to emit. |

#### <a name="observability_metrics_items"></a>16.1.1. Use case > observability > metrics > Metric

**Title:** Metric

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/definitions/metricSchema |

**Description:** A signal the use case is expected to emit.

| Property                                                   | Pattern | Type             | Deprecated | Definition | Title/Description  |
| ---------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------ |
| + [name](#observability_metrics_items_name )               | No      | string           | No         | -          | Metric name        |
| + [kind](#observability_metrics_items_kind )               | No      | enum (of string) | No         | -          | Metric kind        |
| + [description](#observability_metrics_items_description ) | No      | string           | No         | -          | Metric description |
| - [labels](#observability_metrics_items_labels )           | No      | array of string  | No         | -          | Metric labels      |

##### <a name="observability_metrics_items_name"></a>16.1.1.1. Property `Use case > observability > metrics > Metric > name`

**Title:** Metric name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="observability_metrics_items_kind"></a>16.1.1.2. Property `Use case > observability > metrics > Metric > kind`

**Title:** Metric kind

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "counter"
* "gauge"
* "histogram"
* "summary"

##### <a name="observability_metrics_items_description"></a>16.1.1.3. Property `Use case > observability > metrics > Metric > description`

**Title:** Metric description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What the metric measures and how it should be interpreted.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="observability_metrics_items_labels"></a>16.1.1.4. Property `Use case > observability > metrics > Metric > labels`

**Title:** Metric labels

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Label dimensions attached to the metric.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [labels items](#observability_metrics_items_labels_items) | -           |

###### <a name="observability_metrics_items_labels_items"></a>16.1.1.4.1. Use case > observability > metrics > Metric > labels > labels items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="observability_traces"></a>16.2. Property `Use case > observability > traces`

**Title:** Trace

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/definitions/traceSchema |

**Description:** Tracing surface emitted by the use case.

| Property                                            | Pattern | Type            | Deprecated | Definition | Title/Description |
| --------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [spanName](#observability_traces_spanName )       | No      | string          | No         | -          | Span name         |
| + [description](#observability_traces_description ) | No      | string          | No         | -          | Span description  |
| - [attributes](#observability_traces_attributes )   | No      | array of string | No         | -          | Span attributes   |

#### <a name="observability_traces_spanName"></a>16.2.1. Property `Use case > observability > traces > spanName`

**Title:** Span name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="observability_traces_description"></a>16.2.2. Property `Use case > observability > traces > description`

**Title:** Span description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What the span represents and how it should be interpreted in a trace tree.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="observability_traces_attributes"></a>16.2.3. Property `Use case > observability > traces > attributes`

**Title:** Span attributes

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Attribute names attached to the span.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                            | Description |
| ---------------------------------------------------------- | ----------- |
| [attributes items](#observability_traces_attributes_items) | -           |

##### <a name="observability_traces_attributes_items"></a>16.2.3.1. Use case > observability > traces > attributes > attributes items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="observability_logs"></a>16.3. Property `Use case > observability > logs`

**Title:** Log events

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

| Each item of this array must be        | Description                                     |
| -------------------------------------- | ----------------------------------------------- |
| [Log event](#observability_logs_items) | A structured log event emitted by the use case. |

#### <a name="observability_logs_items"></a>16.3.1. Use case > observability > logs > Log event

**Title:** Log event

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `object`                     |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | #/definitions/logEntrySchema |

**Description:** A structured log event emitted by the use case.

| Property                                                | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [event](#observability_logs_items_event )             | No      | string           | No         | -          | Event name        |
| + [level](#observability_logs_items_level )             | No      | enum (of string) | No         | -          | Log level         |
| + [description](#observability_logs_items_description ) | No      | string           | No         | -          | Event description |

##### <a name="observability_logs_items_event"></a>16.3.1.1. Property `Use case > observability > logs > Log event > event`

**Title:** Event name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Stable event name -- the equivalent of a metric name.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="observability_logs_items_level"></a>16.3.1.2. Property `Use case > observability > logs > Log event > level`

**Title:** Log level

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "debug"
* "info"
* "warn"
* "error"

##### <a name="observability_logs_items_description"></a>16.3.1.3. Property `Use case > observability > logs > Log event > description`

**Title:** Event description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this log event signals and when it is emitted.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="scenarios"></a>17. Property `Use case > scenarios`

**Title:** Acceptance scenarios

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Given/When/Then scenarios exercising this use case. Inline scenarios live alongside the use case; identifier references point to scenarios declared in their own documents.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [scenarios items](#scenarios_items) | -           |

### <a name="scenarios_items"></a>17.1. Use case > scenarios > scenarios items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                         |
| ------------------------------------------------------ |
| [Identifier](#scenarios_items_oneOf_i0)                |
| [Scenario (scenarioSchema)](#scenarios_items_oneOf_i1) |

#### <a name="scenarios_items_oneOf_i0"></a>17.1.1. Property `Use case > scenarios > scenarios items > oneOf > Identifier`

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="scenarios_items_oneOf_i1"></a>17.1.2. Property `Use case > scenarios > scenarios items > oneOf > Scenario (scenarioSchema)`

**Title:** Scenario (scenarioSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Scenario](./scenario.md#scenarioschema).

## <a name="lifecycle"></a>18. Property `Use case > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

----------------------------------------------------------------------------------------------------------------------------
