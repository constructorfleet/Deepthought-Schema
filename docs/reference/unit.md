# Unit schema validating meta-schema

- [1. Property `Unit schema validating meta-schema > id`](#id)
- [2. Property `Unit schema validating meta-schema > name`](#name)
- [3. Property `Unit schema validating meta-schema > description`](#description)
- [4. Property `Unit schema validating meta-schema > label`](#label)
  - [4.1. Property `Unit schema validating meta-schema > label > single`](#label_single)
  - [4.2. Property `Unit schema validating meta-schema > label > plural`](#label_plural)
  - [4.3. Property `Unit schema validating meta-schema > label > symbol`](#label_symbol)
- [5. Property `Unit schema validating meta-schema > conversion`](#conversion)
  - [5.1. Property `Unit schema validating meta-schema > conversion > unit`](#conversion_unit)
  - [5.2. Property `Unit schema validating meta-schema > conversion > conversion`](#conversion_conversion)
- [6. Property `Unit schema validating meta-schema > unit`](#unit)
  - [6.1. Property `Unit schema validating meta-schema > unit > oneOf > unitIdentifierSchema`](#unit_oneOf_i0)
    - [6.1.1. Property `Unit schema validating meta-schema > unit > oneOf > item 0 > unit`](#unit_oneOf_i0_unit)
  - [6.2. Property `Unit schema validating meta-schema > unit > oneOf > unitSchema`](#unit_oneOf_i1)
    - [6.2.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > unit`](#unit_oneOf_i1_unit)
      - [6.2.1.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > unit > oneOf > unitSchema`](#unit_oneOf_i1_unit_oneOf_i0)
      - [6.2.1.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > unit > oneOf > unitIdentifierSchema`](#unit_oneOf_i1_unit_oneOf_i1)
    - [6.2.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > exponent`](#unit_oneOf_i1_exponent)
    - [6.2.3. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > multipliedBy`](#unit_oneOf_i1_multipliedBy)
      - [6.2.3.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > multipliedBy > oneOf > unitSchema`](#unit_oneOf_i1_multipliedBy_oneOf_i0)
      - [6.2.3.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > multipliedBy > oneOf > unitGroupSchema`](#unit_oneOf_i1_multipliedBy_oneOf_i1)
    - [6.2.4. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > dividedBy`](#unit_oneOf_i1_dividedBy)
      - [6.2.4.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > dividedBy > oneOf > unitSchema`](#unit_oneOf_i1_dividedBy_oneOf_i0)
      - [6.2.4.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > dividedBy > oneOf > unitGroupSchema`](#unit_oneOf_i1_dividedBy_oneOf_i1)
  - [6.3. Property `Unit schema validating meta-schema > unit > oneOf > unitGroupSchema`](#unit_oneOf_i2)
    - [6.3.1. Property `Unit schema validating meta-schema > unit > oneOf > item 2 > group`](#unit_oneOf_i2_group)
    - [6.3.2. Property `Unit schema validating meta-schema > unit > oneOf > item 2 > exponent`](#unit_oneOf_i2_exponent)

**Title:** Unit schema validating meta-schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |

| Property                       | Pattern | Type        | Deprecated | Definition                        | Title/Description |
| ------------------------------ | ------- | ----------- | ---------- | --------------------------------- | ----------------- |
| + [id](#id )                   | No      | string      | No         | -                                 | -                 |
| + [name](#name )               | No      | string      | No         | -                                 | -                 |
| + [description](#description ) | No      | string      | No         | -                                 | -                 |
| + [label](#label )             | No      | object      | No         | In #/definitions/labelSchema      | -                 |
| - [conversion](#conversion )   | No      | object      | No         | In #/definitions/conversionSchema | -                 |
| - [unit](#unit )               | No      | Combination | No         | -                                 | -                 |

## <a name="id"></a>1. Property `Unit schema validating meta-schema > id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

## <a name="name"></a>2. Property `Unit schema validating meta-schema > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `Unit schema validating meta-schema > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="label"></a>4. Property `Unit schema validating meta-schema > label`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | Yes                       |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/definitions/labelSchema |

| Property                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [single](#label_single ) | No      | string | No         | -          | -                 |
| + [plural](#label_plural ) | No      | string | No         | -          | -                 |
| + [symbol](#label_symbol ) | No      | string | No         | -          | -                 |

### <a name="label_single"></a>4.1. Property `Unit schema validating meta-schema > label > single`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="label_plural"></a>4.2. Property `Unit schema validating meta-schema > label > plural`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="label_symbol"></a>4.3. Property `Unit schema validating meta-schema > label > symbol`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="conversion"></a>5. Property `Unit schema validating meta-schema > conversion`

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/conversionSchema |

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [unit](#conversion_unit )             | No      | string | No         | -          | -                 |
| + [conversion](#conversion_conversion ) | No      | number | No         | -          | -                 |

### <a name="conversion_unit"></a>5.1. Property `Unit schema validating meta-schema > conversion > unit`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                         |
| --------------------------------- | ----------------------------------------------------------------------- |
| **Min length**                    | 1                                                                       |
| **Must match regular expression** | ```^[a-z_]+$``` [Test](https://regex101.com/?regex=%5E%5Ba-z_%5D%2B%24) |

### <a name="conversion_conversion"></a>5.2. Property `Unit schema validating meta-schema > conversion > conversion`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |
| **Format**   | `float`  |

## <a name="unit"></a>6. Property `Unit schema validating meta-schema > unit`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                         |
| -------------------------------------- |
| [unitIdentifierSchema](#unit_oneOf_i0) |
| [unitSchema](#unit_oneOf_i1)           |
| [unitGroupSchema](#unit_oneOf_i2)      |

### <a name="unit_oneOf_i0"></a>6.1. Property `Unit schema validating meta-schema > unit > oneOf > unitIdentifierSchema`

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/unitIdentifierSchema |

| Property                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [unit](#unit_oneOf_i0_unit ) | No      | string | No         | -          | -                 |

#### <a name="unit_oneOf_i0_unit"></a>6.1.1. Property `Unit schema validating meta-schema > unit > oneOf > item 0 > unit`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------- |
| **Must match regular expression** | ```[a-z][a-z_]+``` [Test](https://regex101.com/?regex=%5Ba-z%5D%5Ba-z_%5D%2B) |

### <a name="unit_oneOf_i1"></a>6.2. Property `Unit schema validating meta-schema > unit > oneOf > unitSchema`

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/definitions/unitSchema |

| Property                                       | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [unit](#unit_oneOf_i1_unit )                 | No      | Combination | No         | -          | -                 |
| - [exponent](#unit_oneOf_i1_exponent )         | No      | number      | No         | -          | -                 |
| - [multipliedBy](#unit_oneOf_i1_multipliedBy ) | No      | Combination | No         | -          | -                 |
| - [dividedBy](#unit_oneOf_i1_dividedBy )       | No      | Combination | No         | -          | -                 |

#### <a name="unit_oneOf_i1_unit"></a>6.2.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > unit`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)                                       |
| ---------------------------------------------------- |
| [unitSchema](#unit_oneOf_i1_unit_oneOf_i0)           |
| [unitIdentifierSchema](#unit_oneOf_i1_unit_oneOf_i1) |

##### <a name="unit_oneOf_i1_unit_oneOf_i0"></a>6.2.1.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > unit > oneOf > unitSchema`

**Title:** unitSchema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Recursive reference back to **unitSchema** -- see the `unitSchema` definition above for the full shape.

##### <a name="unit_oneOf_i1_unit_oneOf_i1"></a>6.2.1.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > unit > oneOf > unitIdentifierSchema`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Same definition as**    | [unit_oneOf_i0](#unit_oneOf_i0) |

#### <a name="unit_oneOf_i1_exponent"></a>6.2.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > exponent`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="unit_oneOf_i1_multipliedBy"></a>6.2.3. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > multipliedBy`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [unitSchema](#unit_oneOf_i1_multipliedBy_oneOf_i0)      |
| [unitGroupSchema](#unit_oneOf_i1_multipliedBy_oneOf_i1) |

##### <a name="unit_oneOf_i1_multipliedBy_oneOf_i0"></a>6.2.3.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > multipliedBy > oneOf > unitSchema`

**Title:** unitSchema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Recursive reference back to **unitSchema** -- see the `unitSchema` definition above for the full shape.

##### <a name="unit_oneOf_i1_multipliedBy_oneOf_i1"></a>6.2.3.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > multipliedBy > oneOf > unitGroupSchema`

**Title:** unitGroupSchema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Recursive reference back to **unitGroupSchema** -- see the `unitGroupSchema` definition above for the full shape.

#### <a name="unit_oneOf_i1_dividedBy"></a>6.2.4. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > dividedBy`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                       |
| ---------------------------------------------------- |
| [unitSchema](#unit_oneOf_i1_dividedBy_oneOf_i0)      |
| [unitGroupSchema](#unit_oneOf_i1_dividedBy_oneOf_i1) |

##### <a name="unit_oneOf_i1_dividedBy_oneOf_i0"></a>6.2.4.1. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > dividedBy > oneOf > unitSchema`

**Title:** unitSchema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Recursive reference back to **unitSchema** -- see the `unitSchema` definition above for the full shape.

##### <a name="unit_oneOf_i1_dividedBy_oneOf_i1"></a>6.2.4.2. Property `Unit schema validating meta-schema > unit > oneOf > item 1 > dividedBy > oneOf > unitGroupSchema`

**Title:** unitGroupSchema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Recursive reference back to **unitGroupSchema** -- see the `unitGroupSchema` definition above for the full shape.

### <a name="unit_oneOf_i2"></a>6.3. Property `Unit schema validating meta-schema > unit > oneOf > unitGroupSchema`

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/definitions/unitGroupSchema |

| Property                               | Pattern | Type   | Deprecated | Definition                               | Title/Description |
| -------------------------------------- | ------- | ------ | ---------- | ---------------------------------------- | ----------------- |
| + [group](#unit_oneOf_i2_group )       | No      | object | No         | Same as [unit_oneOf_i1](#unit_oneOf_i1 ) | -                 |
| - [exponent](#unit_oneOf_i2_exponent ) | No      | number | No         | -                                        | -                 |

#### <a name="unit_oneOf_i2_group"></a>6.3.1. Property `Unit schema validating meta-schema > unit > oneOf > item 2 > group`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | Yes                             |
| **Additional properties** | Any type allowed                |
| **Same definition as**    | [unit_oneOf_i1](#unit_oneOf_i1) |

#### <a name="unit_oneOf_i2_exponent"></a>6.3.2. Property `Unit schema validating meta-schema > unit > oneOf > item 2 > exponent`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
