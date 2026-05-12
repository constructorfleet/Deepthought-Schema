# Permission

- [1. Property `Permission > oneOf > Permission set`](#oneOf_i0)
  - [1.1. Property `Permission > oneOf > Permission set > id`](#oneOf_i0_id)
  - [1.2. Property `Permission > oneOf > Permission set > name`](#oneOf_i0_name)
  - [1.3. Property `Permission > oneOf > Permission set > description`](#oneOf_i0_description)
  - [1.4. Property `Permission > oneOf > Permission set > actors`](#oneOf_i0_actors)
    - [1.4.1. Permission > oneOf > Permission set > actors > Actor](#oneOf_i0_actors_items)
      - [1.4.1.1. Property `Permission > oneOf > Permission set > actors > Actor > id`](#oneOf_i0_actors_items_id)
      - [1.4.1.2. Property `Permission > oneOf > Permission set > actors > Actor > name`](#oneOf_i0_actors_items_name)
      - [1.4.1.3. Property `Permission > oneOf > Permission set > actors > Actor > description`](#oneOf_i0_actors_items_description)
      - [1.4.1.4. Property `Permission > oneOf > Permission set > actors > Actor > extends`](#oneOf_i0_actors_items_extends)
        - [1.4.1.4.1. Property `Permission > oneOf > Permission set > actors > Actor > extends > oneOf > Identifier`](#oneOf_i0_actors_items_extends_oneOf_i0)
        - [1.4.1.4.2. Property `Permission > oneOf > Permission set > actors > Actor > extends > oneOf > item 1`](#oneOf_i0_actors_items_extends_oneOf_i1)
          - [1.4.1.4.2.1. Permission > oneOf > Permission set > actors > Actor > extends > oneOf > item 1 > Identifier](#oneOf_i0_actors_items_extends_oneOf_i1_items)
      - [1.4.1.5. Property `Permission > oneOf > Permission set > actors > Actor > anonymous`](#oneOf_i0_actors_items_anonymous)
      - [1.4.1.6. Property `Permission > oneOf > Permission set > actors > Actor > lifecycle`](#oneOf_i0_actors_items_lifecycle)
  - [1.5. Property `Permission > oneOf > Permission set > permissions`](#oneOf_i0_permissions)
    - [1.5.1. Permission > oneOf > Permission set > permissions > Permission](#oneOf_i0_permissions_items)
      - [1.5.1.1. Property `Permission > oneOf > Permission set > permissions > Permission > id`](#oneOf_i0_permissions_items_id)
      - [1.5.1.2. Property `Permission > oneOf > Permission set > permissions > Permission > name`](#oneOf_i0_permissions_items_name)
      - [1.5.1.3. Property `Permission > oneOf > Permission set > permissions > Permission > description`](#oneOf_i0_permissions_items_description)
      - [1.5.1.4. Property `Permission > oneOf > Permission set > permissions > Permission > rules`](#oneOf_i0_permissions_items_rules)
        - [1.5.1.4.1. Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule](#oneOf_i0_permissions_items_rules_items)
          - [1.5.1.4.1.1. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > effect`](#oneOf_i0_permissions_items_rules_items_effect)
          - [1.5.1.4.1.2. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors`](#oneOf_i0_permissions_items_rules_items_actors)
            - [1.5.1.4.1.2.1. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > item 0`](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i0)
            - [1.5.1.4.1.2.2. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > Identifier`](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i1)
            - [1.5.1.4.1.2.3. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > item 2`](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i2)
              - [1.5.1.4.1.2.3.1. Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > item 2 > Identifier](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i2_items)
          - [1.5.1.4.1.3. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > condition`](#oneOf_i0_permissions_items_rules_items_condition)
          - [1.5.1.4.1.4. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > description`](#oneOf_i0_permissions_items_rules_items_description)
      - [1.5.1.5. Property `Permission > oneOf > Permission set > permissions > Permission > lifecycle`](#oneOf_i0_permissions_items_lifecycle)
  - [1.6. Property `Permission > oneOf > Permission set > lifecycle`](#oneOf_i0_lifecycle)
- [2. Property `Permission > oneOf > Permission`](#oneOf_i1)
- [3. Property `Permission > oneOf > Actor`](#oneOf_i2)

**Title:** Permission

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |

**Description:** Who may invoke a use case (or read/write a model field) and under what conditions. Permissions are split across two concepts. Actors are classes of caller (admin, customer, service-account, anonymous) -- domain-level roles, not transport-layer auth tokens. Permissions are named capabilities that grant one or more actors the right to perform an action, optionally gated by a conditional expression. Use cases reference permissions; models can reference permissions at field-level granularity for read/write visibility.

| One of(Option)              |
| --------------------------- |
| [Permission set](#oneOf_i0) |
| [Permission](#oneOf_i1)     |
| [Actor](#oneOf_i2)          |

## <a name="oneOf_i0"></a>1. Property `Permission > oneOf > Permission set`

**Title:** Permission set

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/definitions/permissionSetSchema |

**Description:** A bundle of related actors and permissions defined together. Useful when a domain owns several actors and the permissions that connect them; otherwise individual actor or permission documents are fine.

| Property                                | Pattern | Type   | Deprecated | Definition                        | Title/Description       |
| --------------------------------------- | ------- | ------ | ---------- | --------------------------------- | ----------------------- |
| + [id](#oneOf_i0_id )                   | No      | string | No         | In #/definitions/identifierSchema | Identifier              |
| + [name](#oneOf_i0_name )               | No      | string | No         | -                                 | Set display name        |
| + [description](#oneOf_i0_description ) | No      | string | No         | -                                 | Set description         |
| - [actors](#oneOf_i0_actors )           | No      | array  | No         | -                                 | Actors in this set      |
| - [permissions](#oneOf_i0_permissions ) | No      | array  | No         | -                                 | Permissions in this set |
| - [lifecycle](#oneOf_i0_lifecycle )     | No      | object | No         | -                                 | Field (lifecycleSchema) |

### <a name="oneOf_i0_id"></a>1.1. Property `Permission > oneOf > Permission set > id`

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

### <a name="oneOf_i0_name"></a>1.2. Property `Permission > oneOf > Permission set > name`

**Title:** Set display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

### <a name="oneOf_i0_description"></a>1.3. Property `Permission > oneOf > Permission set > description`

**Title:** Set description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this bundle of actors and permissions models in the domain.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="oneOf_i0_actors"></a>1.4. Property `Permission > oneOf > Permission set > actors`

**Title:** Actors in this set

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

| Each item of this array must be | Description                                                                                                                                                             |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Actor](#oneOf_i0_actors_items) | A class of caller. Actors are domain-level roles that exist independently of any specific authentication mechanism, so the same actor model survives transport changes. |

#### <a name="oneOf_i0_actors_items"></a>1.4.1. Permission > oneOf > Permission set > actors > Actor

**Title:** Actor

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/definitions/actorSchema |

**Description:** A class of caller. Actors are domain-level roles that exist independently of any specific authentication mechanism, so the same actor model survives transport changes.

| Property                                             | Pattern | Type        | Deprecated | Definition                  | Title/Description              |
| ---------------------------------------------------- | ------- | ----------- | ---------- | --------------------------- | ------------------------------ |
| + [id](#oneOf_i0_actors_items_id )                   | No      | string      | No         | Same as [id](#oneOf_i0_id ) | Identifier                     |
| + [name](#oneOf_i0_actors_items_name )               | No      | string      | No         | -                           | Actor display name             |
| + [description](#oneOf_i0_actors_items_description ) | No      | string      | No         | -                           | Actor description              |
| - [extends](#oneOf_i0_actors_items_extends )         | No      | Combination | No         | -                           | Inherited actors               |
| - [anonymous](#oneOf_i0_actors_items_anonymous )     | No      | boolean     | No         | -                           | Represents an anonymous caller |
| - [lifecycle](#oneOf_i0_actors_items_lifecycle )     | No      | object      | No         | -                           | Field (lifecycleSchema)        |

##### <a name="oneOf_i0_actors_items_id"></a>1.4.1.1. Property `Permission > oneOf > Permission set > actors > Actor > id`

**Title:** Identifier

|                        |                    |
| ---------------------- | ------------------ |
| **Type**               | `string`           |
| **Required**           | Yes                |
| **Same definition as** | [id](#oneOf_i0_id) |

##### <a name="oneOf_i0_actors_items_name"></a>1.4.1.2. Property `Permission > oneOf > Permission set > actors > Actor > name`

**Title:** Actor display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

##### <a name="oneOf_i0_actors_items_description"></a>1.4.1.3. Property `Permission > oneOf > Permission set > actors > Actor > description`

**Title:** Actor description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this actor represents in the domain and what real-world subject(s) typically map to it. Required so the role's purpose is documented alongside its definition.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="oneOf_i0_actors_items_extends"></a>1.4.1.4. Property `Permission > oneOf > Permission set > actors > Actor > extends`

**Title:** Inherited actors

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Actors this actor subsumes. The current actor is granted every permission held by each of the listed actors.

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Identifier](#oneOf_i0_actors_items_extends_oneOf_i0) |
| [item 1](#oneOf_i0_actors_items_extends_oneOf_i1)     |

###### <a name="oneOf_i0_actors_items_extends_oneOf_i0"></a>1.4.1.4.1. Property `Permission > oneOf > Permission set > actors > Actor > extends > oneOf > Identifier`

**Title:** Identifier

|                        |                    |
| ---------------------- | ------------------ |
| **Type**               | `string`           |
| **Required**           | No                 |
| **Same definition as** | [id](#oneOf_i0_id) |

###### <a name="oneOf_i0_actors_items_extends_oneOf_i1"></a>1.4.1.4.2. Property `Permission > oneOf > Permission set > actors > Actor > extends > oneOf > item 1`

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

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [Identifier](#oneOf_i0_actors_items_extends_oneOf_i1_items) | -           |

###### <a name="oneOf_i0_actors_items_extends_oneOf_i1_items"></a>1.4.1.4.2.1. Permission > oneOf > Permission set > actors > Actor > extends > oneOf > item 1 > Identifier

**Title:** Identifier

|                        |                    |
| ---------------------- | ------------------ |
| **Type**               | `string`           |
| **Required**           | No                 |
| **Same definition as** | [id](#oneOf_i0_id) |

##### <a name="oneOf_i0_actors_items_anonymous"></a>1.4.1.5. Property `Permission > oneOf > Permission set > actors > Actor > anonymous`

**Title:** Represents an anonymous caller

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether this actor represents an unauthenticated caller. Drives generators' anonymous-access middleware decisions.

##### <a name="oneOf_i0_actors_items_lifecycle"></a>1.4.1.6. Property `Permission > oneOf > Permission set > actors > Actor > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

### <a name="oneOf_i0_permissions"></a>1.5. Property `Permission > oneOf > Permission set > permissions`

**Title:** Permissions in this set

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

| Each item of this array must be           | Description                                       |
| ----------------------------------------- | ------------------------------------------------- |
| [Permission](#oneOf_i0_permissions_items) | A named capability composed of one or more rules. |

#### <a name="oneOf_i0_permissions_items"></a>1.5.1. Permission > oneOf > Permission set > permissions > Permission

**Title:** Permission

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/definitions/permissionSchema |

**Description:** A named capability composed of one or more rules.

| Property                                                  | Pattern | Type   | Deprecated | Definition                  | Title/Description       |
| --------------------------------------------------------- | ------- | ------ | ---------- | --------------------------- | ----------------------- |
| + [id](#oneOf_i0_permissions_items_id )                   | No      | string | No         | Same as [id](#oneOf_i0_id ) | Identifier              |
| + [name](#oneOf_i0_permissions_items_name )               | No      | string | No         | -                           | Permission display name |
| + [description](#oneOf_i0_permissions_items_description ) | No      | string | No         | -                           | Permission description  |
| + [rules](#oneOf_i0_permissions_items_rules )             | No      | array  | No         | -                           | Rules                   |
| - [lifecycle](#oneOf_i0_permissions_items_lifecycle )     | No      | object | No         | -                           | Field (lifecycleSchema) |

##### <a name="oneOf_i0_permissions_items_id"></a>1.5.1.1. Property `Permission > oneOf > Permission set > permissions > Permission > id`

**Title:** Identifier

|                        |                    |
| ---------------------- | ------------------ |
| **Type**               | `string`           |
| **Required**           | Yes                |
| **Same definition as** | [id](#oneOf_i0_id) |

##### <a name="oneOf_i0_permissions_items_name"></a>1.5.1.2. Property `Permission > oneOf > Permission set > permissions > Permission > name`

**Title:** Permission display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

##### <a name="oneOf_i0_permissions_items_description"></a>1.5.1.3. Property `Permission > oneOf > Permission set > permissions > Permission > description`

**Title:** Permission description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What the capability authorizes and the policy intent behind it.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="oneOf_i0_permissions_items_rules"></a>1.5.1.4. Property `Permission > oneOf > Permission set > permissions > Permission > rules`

**Title:** Rules

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** Ordered rules. First match wins; an implicit deny applies if none match.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                            | Description                                                                                                                                                           |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Permission rule](#oneOf_i0_permissions_items_rules_items) | A single grant or denial. Rules in a permission are evaluated top-to-bottom; the first matching rule wins. A trailing implicit "deny any" applies if no rule matches. |

###### <a name="oneOf_i0_permissions_items_rules_items"></a>1.5.1.4.1. Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule

**Title:** Permission rule

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Defined in**            | #/definitions/permissionRuleSchema |

**Description:** A single grant or denial. Rules in a permission are evaluated top-to-bottom; the first matching rule wins. A trailing implicit "deny any" applies if no rule matches.

| Property                                                              | Pattern | Type             | Deprecated | Definition                    | Title/Description |
| --------------------------------------------------------------------- | ------- | ---------------- | ---------- | ----------------------------- | ----------------- |
| + [effect](#oneOf_i0_permissions_items_rules_items_effect )           | No      | enum (of string) | No         | In #/definitions/effectSchema | Rule effect       |
| + [actors](#oneOf_i0_permissions_items_rules_items_actors )           | No      | Combination      | No         | -                             | Subject actors    |
| - [condition](#oneOf_i0_permissions_items_rules_items_condition )     | No      | object           | No         | -                             | Expression        |
| + [description](#oneOf_i0_permissions_items_rules_items_description ) | No      | string           | No         | -                             | Rule description  |

###### <a name="oneOf_i0_permissions_items_rules_items_effect"></a>1.5.1.4.1.1. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > effect`

**Title:** Rule effect

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `enum (of string)`         |
| **Required**   | Yes                        |
| **Defined in** | #/definitions/effectSchema |

**Description:** Whether the matching rule grants or denies the action.

Must be one of:
* "allow"
* "deny"

###### <a name="oneOf_i0_permissions_items_rules_items_actors"></a>1.5.1.4.1.2. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors`

**Title:** Subject actors

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Actors this rule applies to. The literal `any` matches every actor (including anonymous).

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [item 0](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i0)     |
| [Identifier](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i1) |
| [item 2](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i2)     |

###### <a name="oneOf_i0_permissions_items_rules_items_actors_oneOf_i0"></a>1.5.1.4.1.2.1. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"any"`

###### <a name="oneOf_i0_permissions_items_rules_items_actors_oneOf_i1"></a>1.5.1.4.1.2.2. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > Identifier`

**Title:** Identifier

|                        |                    |
| ---------------------- | ------------------ |
| **Type**               | `string`           |
| **Required**           | No                 |
| **Same definition as** | [id](#oneOf_i0_id) |

###### <a name="oneOf_i0_permissions_items_rules_items_actors_oneOf_i2"></a>1.5.1.4.1.2.3. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > item 2`

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

| Each item of this array must be                                             | Description |
| --------------------------------------------------------------------------- | ----------- |
| [Identifier](#oneOf_i0_permissions_items_rules_items_actors_oneOf_i2_items) | -           |

###### <a name="oneOf_i0_permissions_items_rules_items_actors_oneOf_i2_items"></a>1.5.1.4.1.2.3.1. Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > actors > oneOf > item 2 > Identifier

**Title:** Identifier

|                        |                    |
| ---------------------- | ------------------ |
| **Type**               | `string`           |
| **Required**           | No                 |
| **Same definition as** | [id](#oneOf_i0_id) |

###### <a name="oneOf_i0_permissions_items_rules_items_condition"></a>1.5.1.4.1.3. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > condition`

**Title:** Expression

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Expression](./expression.md).

###### <a name="oneOf_i0_permissions_items_rules_items_description"></a>1.5.1.4.1.4. Property `Permission > oneOf > Permission set > permissions > Permission > rules > Permission rule > description`

**Title:** Rule description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Why this rule exists. Required so authorization intent stays inherent to the rule.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="oneOf_i0_permissions_items_lifecycle"></a>1.5.1.5. Property `Permission > oneOf > Permission set > permissions > Permission > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

### <a name="oneOf_i0_lifecycle"></a>1.6. Property `Permission > oneOf > Permission set > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

## <a name="oneOf_i1"></a>2. Property `Permission > oneOf > Permission`

**Title:** Permission

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `object`                                  |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Same definition as**    | [Permission](#oneOf_i0_permissions_items) |

**Description:** A named capability composed of one or more rules.

## <a name="oneOf_i2"></a>3. Property `Permission > oneOf > Actor`

**Title:** Actor

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Same definition as**    | [Actor](#oneOf_i0_actors_items) |

**Description:** A class of caller. Actors are domain-level roles that exist independently of any specific authentication mechanism, so the same actor model survives transport changes.

----------------------------------------------------------------------------------------------------------------------------
