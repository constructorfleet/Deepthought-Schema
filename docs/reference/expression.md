# Expression

- [1. Property `Expression > oneOf > String-shorthand expression`](#oneOf_i0)
  - [1.1. Property `Expression > oneOf > String-shorthand expression > expr`](#oneOf_i0_expr)
- [2. Property `Expression > oneOf > Comparison expression`](#oneOf_i1)
  - [2.1. Property `Expression > oneOf > Comparison expression > op`](#oneOf_i1_op)
  - [2.2. Property `Expression > oneOf > Comparison expression > args`](#oneOf_i1_args)
    - [2.2.1. Expression > oneOf > Comparison expression > args > Expression term](#oneOf_i1_args_items)
      - [2.2.1.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value`](#oneOf_i1_args_items_oneOf_i0)
        - [2.2.1.1.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal`](#oneOf_i1_args_items_oneOf_i0_literal)
          - [2.2.1.1.1.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 0`](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i0)
          - [2.2.1.1.1.2. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 1`](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i1)
          - [2.2.1.1.1.3. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 2`](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i2)
          - [2.2.1.1.1.4. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 3`](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i3)
          - [2.2.1.1.1.5. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 4`](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i4)
          - [2.2.1.1.1.6. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 5`](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i5)
            - [2.2.1.1.1.6.1. Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 5 > item 5 items](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i5_items)
        - [2.2.1.1.2. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > unit`](#oneOf_i1_args_items_oneOf_i0_unit)
      - [2.2.1.2. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Field reference term`](#oneOf_i1_args_items_oneOf_i1)
        - [2.2.1.2.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Field reference term > field`](#oneOf_i1_args_items_oneOf_i1_field)
      - [2.2.1.3. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Constant reference term`](#oneOf_i1_args_items_oneOf_i2)
        - [2.2.1.3.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Constant reference term > constant`](#oneOf_i1_args_items_oneOf_i2_constant)
      - [2.2.1.4. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > expressionSchema`](#oneOf_i1_args_items_oneOf_i3)
- [3. Property `Expression > oneOf > Logical expression`](#oneOf_i2)
  - [3.1. Property `Expression > oneOf > Logical expression > op`](#oneOf_i2_op)
  - [3.2. Property `Expression > oneOf > Logical expression > args`](#oneOf_i2_args)
    - [3.2.1. Expression > oneOf > Logical expression > args > Expression term](#oneOf_i2_args_items)
- [4. Property `Expression > oneOf > Arithmetic expression`](#oneOf_i3)
  - [4.1. Property `Expression > oneOf > Arithmetic expression > op`](#oneOf_i3_op)
  - [4.2. Property `Expression > oneOf > Arithmetic expression > args`](#oneOf_i3_args)
    - [4.2.1. Expression > oneOf > Arithmetic expression > args > Expression term](#oneOf_i3_args_items)
- [5. Property `Expression > oneOf > aggregateExpressionSchema`](#oneOf_i4)
- [6. Property `Expression > oneOf > Function-call expression`](#oneOf_i5)
  - [6.1. Property `Expression > oneOf > Function-call expression > call`](#oneOf_i5_call)
  - [6.2. Property `Expression > oneOf > Function-call expression > args`](#oneOf_i5_args)
    - [6.2.1. Expression > oneOf > Function-call expression > args > Expression term](#oneOf_i5_args_items)
- [7. Property `Expression > oneOf > Literal value`](#oneOf_i6)
- [8. Property `Expression > oneOf > Field reference term`](#oneOf_i7)
- [9. Property `Expression > oneOf > Constant reference term`](#oneOf_i8)

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** The shared evaluation language used wherever a DeepThought specification needs to express a value or a predicate at the spec layer rather than in code: cross-field invariants on a model, computed/derived fields, guards on state-machine transitions, conditional permissions, error-raise conditions, and assertions in scenario "then" clauses. Two surface syntaxes are accepted -- a structured AST (always machine-walkable, lower-able into any target language) and a string shorthand (concise, parsed by tooling).

| One of(Option)                           |
| ---------------------------------------- |
| [String-shorthand expression](#oneOf_i0) |
| [Comparison expression](#oneOf_i1)       |
| [Logical expression](#oneOf_i2)          |
| [Arithmetic expression](#oneOf_i3)       |
| [aggregateExpressionSchema](#oneOf_i4)   |
| [Function-call expression](#oneOf_i5)    |
| [Literal value](#oneOf_i6)               |
| [Field reference term](#oneOf_i7)        |
| [Constant reference term](#oneOf_i8)     |

## <a name="oneOf_i0"></a>1. Property `Expression > oneOf > String-shorthand expression`

**Title:** String-shorthand expression

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Defined in**            | #/definitions/shorthandExpressionSchema |

**Description:** Concise hand-authored surface syntax (e.g. "status == 'shipped' && total > 0"). Parsing into the AST is left to tooling; this layer just enforces non-empty.

| Property                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [expr](#oneOf_i0_expr ) | No      | string | No         | -          | Expression source |

### <a name="oneOf_i0_expr"></a>1.1. Property `Expression > oneOf > String-shorthand expression > expr`

**Title:** Expression source

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="oneOf_i1"></a>2. Property `Expression > oneOf > Comparison expression`

**Title:** Comparison expression

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | #/definitions/comparisonExpressionSchema |

**Description:** Predicate built from a comparison operator and one or more operands. Example structured form for "status equals shipped": {op: equals, args: [{field: status}, {literal: shipped}]}.

| Property                  | Pattern | Type             | Deprecated | Definition                                | Title/Description   |
| ------------------------- | ------- | ---------------- | ---------- | ----------------------------------------- | ------------------- |
| + [op](#oneOf_i1_op )     | No      | enum (of string) | No         | In #/definitions/comparisonOperatorSchema | Comparison operator |
| + [args](#oneOf_i1_args ) | No      | array            | No         | -                                         | -                   |

### <a name="oneOf_i1_op"></a>2.1. Property `Expression > oneOf > Comparison expression > op`

**Title:** Comparison operator

|                |                                        |
| -------------- | -------------------------------------- |
| **Type**       | `enum (of string)`                     |
| **Required**   | Yes                                    |
| **Defined in** | #/definitions/comparisonOperatorSchema |

**Description:** Predicate operators that compare two or more terms.

Must be one of:
* "equals"
* "not_equals"
* "greater_than"
* "greater_than_or_equal"
* "less_than"
* "less_than_or_equal"
* "in"
* "not_in"
* "matches"
* "contains"
* "starts_with"
* "ends_with"
* "exists"
* "is_null"

### <a name="oneOf_i1_args"></a>2.2. Property `Expression > oneOf > Comparison expression > args`

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

| Each item of this array must be         | Description                                                                                                                        |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [Expression term](#oneOf_i1_args_items) | Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression. |

#### <a name="oneOf_i1_args_items"></a>2.2.1. Expression > oneOf > Comparison expression > args > Expression term

**Title:** Expression term

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `combining`              |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/definitions/termSchema |

**Description:** Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression.

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Literal value](#oneOf_i1_args_items_oneOf_i0)           |
| [Field reference term](#oneOf_i1_args_items_oneOf_i1)    |
| [Constant reference term](#oneOf_i1_args_items_oneOf_i2) |
| [expressionSchema](#oneOf_i1_args_items_oneOf_i3)        |

##### <a name="oneOf_i1_args_items_oneOf_i0"></a>2.2.1.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value`

**Title:** Literal value

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/definitions/literalSchema |

**Description:** A literal scalar, array, or null value. May carry a unit so that dimensional analysis still applies inside expressions (e.g. comparing a field in millimeters against a literal {literal: 10, unit: centimeter}).

| Property                                            | Pattern | Type        | Deprecated | Definition | Title/Description |
| --------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [literal](#oneOf_i1_args_items_oneOf_i0_literal ) | No      | Combination | No         | -          | Literal value     |
| - [unit](#oneOf_i1_args_items_oneOf_i0_unit )       | No      | string      | No         | -          | Unit identifier   |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal"></a>2.2.1.1.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal`

**Title:** Literal value

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The constant value itself. Any JSON-representable scalar or array.

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i0) |
| [item 1](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i1) |
| [item 2](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i2) |
| [item 3](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i3) |
| [item 4](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i4) |
| [item 5](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i5) |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal_anyOf_i0"></a>2.2.1.1.1.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal_anyOf_i1"></a>2.2.1.1.1.2. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal_anyOf_i2"></a>2.2.1.1.1.3. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 2`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal_anyOf_i3"></a>2.2.1.1.1.4. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 3`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal_anyOf_i4"></a>2.2.1.1.1.5. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 4`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal_anyOf_i5"></a>2.2.1.1.1.6. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 5`

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
| **Tuple validation** | See below          |

| Each item of this array must be                                      | Description |
| -------------------------------------------------------------------- | ----------- |
| [item 5 items](#oneOf_i1_args_items_oneOf_i0_literal_anyOf_i5_items) | -           |

###### <a name="oneOf_i1_args_items_oneOf_i0_literal_anyOf_i5_items"></a>2.2.1.1.1.6.1. Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > literal > anyOf > item 5 > item 5 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="oneOf_i1_args_items_oneOf_i0_unit"></a>2.2.1.1.2. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Literal value > unit`

**Title:** Unit identifier

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Optional unit attached to the literal. When present, dimensional analysis treats the literal as a quantity in this unit.

| Restrictions                      |                                                                         |
| --------------------------------- | ----------------------------------------------------------------------- |
| **Must match regular expression** | ```^[a-z_]+$``` [Test](https://regex101.com/?regex=%5E%5Ba-z_%5D%2B%24) |

##### <a name="oneOf_i1_args_items_oneOf_i1"></a>2.2.1.2. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Field reference term`

**Title:** Field reference term

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `object`                     |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | #/definitions/fieldRefSchema |

**Description:** Reference to a field by path. Resolves to the value of that field on the entity the expression is evaluated against.

| Property                                        | Pattern | Type   | Deprecated | Definition                       | Title/Description |
| ----------------------------------------------- | ------- | ------ | ---------- | -------------------------------- | ----------------- |
| + [field](#oneOf_i1_args_items_oneOf_i1_field ) | No      | string | No         | In #/definitions/fieldPathSchema | Field path        |

###### <a name="oneOf_i1_args_items_oneOf_i1_field"></a>2.2.1.2.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Field reference term > field`

**Title:** Field path

|                |                               |
| -------------- | ----------------------------- |
| **Type**       | `string`                      |
| **Required**   | Yes                           |
| **Defined in** | #/definitions/fieldPathSchema |

**Description:** Reference to a field on the current model, or on a related model via dot-path. Examples: "shipped_at", "items.amount", "owner.id".

| Restrictions                      |                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                         |
| **Must match regular expression** | ```^[a-z][a-z_]*(\.[a-z][a-z_]*)*$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2A%28%5C.%5Ba-z%5D%5Ba-z_%5D%2A%29%2A%24) |

##### <a name="oneOf_i1_args_items_oneOf_i2"></a>2.2.1.3. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Constant reference term`

**Title:** Constant reference term

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | #/definitions/constantRefSchema |

**Description:** Reference to a named constant declared in a constant.meta.yaml document. Resolves to the constant's typed value at evaluation time.

| Property                                              | Pattern | Type   | Deprecated | Definition                        | Title/Description |
| ----------------------------------------------------- | ------- | ------ | ---------- | --------------------------------- | ----------------- |
| + [constant](#oneOf_i1_args_items_oneOf_i2_constant ) | No      | string | No         | In #/definitions/identifierSchema | Identifier        |

###### <a name="oneOf_i1_args_items_oneOf_i2_constant"></a>2.2.1.3.1. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > Constant reference term > constant`

**Title:** Identifier

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

**Description:** Snake-case identifier used to name domain entities. Stable, lowercase, underscore-separated, never starting or ending with an underscore.

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

##### <a name="oneOf_i1_args_items_oneOf_i3"></a>2.2.1.4. Property `Expression > oneOf > Comparison expression > args > Expression term > oneOf > expressionSchema`

**Title:** expressionSchema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Recursive reference back to **expressionSchema** -- see the `expressionSchema` definition above for the full shape.

## <a name="oneOf_i2"></a>3. Property `Expression > oneOf > Logical expression`

**Title:** Logical expression

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Defined in**            | #/definitions/logicalExpressionSchema |

**Description:** Boolean connective applied to one or more sub-predicates.

| Property                  | Pattern | Type             | Deprecated | Definition                             | Title/Description |
| ------------------------- | ------- | ---------------- | ---------- | -------------------------------------- | ----------------- |
| + [op](#oneOf_i2_op )     | No      | enum (of string) | No         | In #/definitions/logicalOperatorSchema | Logical operator  |
| + [args](#oneOf_i2_args ) | No      | array            | No         | -                                      | -                 |

### <a name="oneOf_i2_op"></a>3.1. Property `Expression > oneOf > Logical expression > op`

**Title:** Logical operator

|                |                                     |
| -------------- | ----------------------------------- |
| **Type**       | `enum (of string)`                  |
| **Required**   | Yes                                 |
| **Defined in** | #/definitions/logicalOperatorSchema |

**Description:** Boolean connectives that combine sub-predicates.

Must be one of:
* "and"
* "or"
* "not"
* "implies"
* "iff"

### <a name="oneOf_i2_args"></a>3.2. Property `Expression > oneOf > Logical expression > args`

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

| Each item of this array must be         | Description                                                                                                                        |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [Expression term](#oneOf_i2_args_items) | Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression. |

#### <a name="oneOf_i2_args_items"></a>3.2.1. Expression > oneOf > Logical expression > args > Expression term

**Title:** Expression term

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `combining`                             |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [Expression term](#oneOf_i1_args_items) |

**Description:** Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression.

## <a name="oneOf_i3"></a>4. Property `Expression > oneOf > Arithmetic expression`

**Title:** Arithmetic expression

|                           |                                          |
| ------------------------- | ---------------------------------------- |
| **Type**                  | `object`                                 |
| **Required**              | No                                       |
| **Additional properties** | Any type allowed                         |
| **Defined in**            | #/definitions/arithmeticExpressionSchema |

**Description:** Numeric computation built from an arithmetic operator and operands.

| Property                  | Pattern | Type             | Deprecated | Definition                                | Title/Description   |
| ------------------------- | ------- | ---------------- | ---------- | ----------------------------------------- | ------------------- |
| + [op](#oneOf_i3_op )     | No      | enum (of string) | No         | In #/definitions/arithmeticOperatorSchema | Arithmetic operator |
| + [args](#oneOf_i3_args ) | No      | array            | No         | -                                         | -                   |

### <a name="oneOf_i3_op"></a>4.1. Property `Expression > oneOf > Arithmetic expression > op`

**Title:** Arithmetic operator

|                |                                        |
| -------------- | -------------------------------------- |
| **Type**       | `enum (of string)`                     |
| **Required**   | Yes                                    |
| **Defined in** | #/definitions/arithmeticOperatorSchema |

**Description:** Numeric value operators. Dimensional analysis is enforced for the operators that apply to dimensioned quantities.

Must be one of:
* "add"
* "subtract"
* "multiply"
* "divide"
* "modulo"
* "power"
* "negate"
* "abs"
* "round"
* "ceil"
* "floor"

### <a name="oneOf_i3_args"></a>4.2. Property `Expression > oneOf > Arithmetic expression > args`

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

| Each item of this array must be         | Description                                                                                                                        |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [Expression term](#oneOf_i3_args_items) | Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression. |

#### <a name="oneOf_i3_args_items"></a>4.2.1. Expression > oneOf > Arithmetic expression > args > Expression term

**Title:** Expression term

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `combining`                             |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [Expression term](#oneOf_i1_args_items) |

**Description:** Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression.

## <a name="oneOf_i4"></a>5. Property `Expression > oneOf > aggregateExpressionSchema`

**Title:** aggregateExpressionSchema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Recursive reference back to **aggregateExpressionSchema** -- see the `aggregateExpressionSchema` definition above for the full shape.

## <a name="oneOf_i5"></a>6. Property `Expression > oneOf > Function-call expression`

**Title:** Function-call expression

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/callExpressionSchema |

**Description:** Escape hatch for domain-specific functions a generator knows how to lower (e.g. now(), uuid(), hash(...)). Function name and arity are part of the spec; their semantics are documented separately.

| Property                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [call](#oneOf_i5_call ) | No      | string | No         | -          | Function name     |
| - [args](#oneOf_i5_args ) | No      | array  | No         | -          | Argument list     |

### <a name="oneOf_i5_call"></a>6.1. Property `Expression > oneOf > Function-call expression > call`

**Title:** Function name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[a-z][a-z_0-9]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_0-9%5D%2A%24) |

### <a name="oneOf_i5_args"></a>6.2. Property `Expression > oneOf > Function-call expression > args`

**Title:** Argument list

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
| **Tuple validation** | See below          |

| Each item of this array must be         | Description                                                                                                                        |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [Expression term](#oneOf_i5_args_items) | Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression. |

#### <a name="oneOf_i5_args_items"></a>6.2.1. Expression > oneOf > Function-call expression > args > Expression term

**Title:** Expression term

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `combining`                             |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [Expression term](#oneOf_i1_args_items) |

**Description:** Any leaf or sub-expression usable as an operand: a literal, a field reference, a constant reference, or another nested expression.

## <a name="oneOf_i6"></a>7. Property `Expression > oneOf > Literal value`

**Title:** Literal value

|                           |                                                |
| ------------------------- | ---------------------------------------------- |
| **Type**                  | `object`                                       |
| **Required**              | No                                             |
| **Additional properties** | Any type allowed                               |
| **Same definition as**    | [Literal value](#oneOf_i1_args_items_oneOf_i0) |

**Description:** A literal scalar, array, or null value. May carry a unit so that dimensional analysis still applies inside expressions (e.g. comparing a field in millimeters against a literal {literal: 10, unit: centimeter}).

## <a name="oneOf_i7"></a>8. Property `Expression > oneOf > Field reference term`

**Title:** Field reference term

|                           |                                                       |
| ------------------------- | ----------------------------------------------------- |
| **Type**                  | `object`                                              |
| **Required**              | No                                                    |
| **Additional properties** | Any type allowed                                      |
| **Same definition as**    | [Field reference term](#oneOf_i1_args_items_oneOf_i1) |

**Description:** Reference to a field by path. Resolves to the value of that field on the entity the expression is evaluated against.

## <a name="oneOf_i8"></a>9. Property `Expression > oneOf > Constant reference term`

**Title:** Constant reference term

|                           |                                                          |
| ------------------------- | -------------------------------------------------------- |
| **Type**                  | `object`                                                 |
| **Required**              | No                                                       |
| **Additional properties** | Any type allowed                                         |
| **Same definition as**    | [Constant reference term](#oneOf_i1_args_items_oneOf_i2) |

**Description:** Reference to a named constant declared in a constant.meta.yaml document. Resolves to the constant's typed value at evaluation time.

----------------------------------------------------------------------------------------------------------------------------
