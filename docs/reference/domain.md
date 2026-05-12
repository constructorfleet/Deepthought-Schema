# Domain

- [1. Property `Domain > id`](#id)
- [2. Property `Domain > name`](#name)
- [3. Property `Domain > description`](#description)
- [4. Property `Domain > owner`](#owner)
- [5. Property `Domain > classification`](#classification)
- [6. Property `Domain > glossary`](#glossary)
  - [6.1. Domain > glossary > Glossary entry](#glossary_items)
    - [6.1.1. Property `Domain > glossary > Glossary entry > term`](#glossary_items_term)
    - [6.1.2. Property `Domain > glossary > Glossary entry > definition`](#glossary_items_definition)
    - [6.1.3. Property `Domain > glossary > Glossary entry > synonyms`](#glossary_items_synonyms)
      - [6.1.3.1. Domain > glossary > Glossary entry > synonyms > synonyms items](#glossary_items_synonyms_items)
    - [6.1.4. Property `Domain > glossary > Glossary entry > relatedTerms`](#glossary_items_relatedTerms)
      - [6.1.4.1. Domain > glossary > Glossary entry > relatedTerms > relatedTerms items](#glossary_items_relatedTerms_items)
- [7. Property `Domain > imports`](#imports)
  - [7.1. Domain > imports > Domain import](#imports_items)
    - [7.1.1. Property `Domain > imports > Domain import > from`](#imports_items_from)
    - [7.1.2. Property `Domain > imports > Domain import > models`](#imports_items_models)
      - [7.1.2.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
    - [7.1.3. Property `Domain > imports > Domain import > usecases`](#imports_items_usecases)
      - [7.1.3.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
    - [7.1.4. Property `Domain > imports > Domain import > events`](#imports_items_events)
      - [7.1.4.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
    - [7.1.5. Property `Domain > imports > Domain import > collections`](#imports_items_collections)
      - [7.1.5.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
    - [7.1.6. Property `Domain > imports > Domain import > errors`](#imports_items_errors)
      - [7.1.6.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
- [8. Property `Domain > exports`](#exports)
  - [8.1. Property `Domain > exports > models`](#exports_models)
    - [8.1.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
  - [8.2. Property `Domain > exports > usecases`](#exports_usecases)
    - [8.2.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
  - [8.3. Property `Domain > exports > events`](#exports_events)
    - [8.3.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
  - [8.4. Property `Domain > exports > collections`](#exports_collections)
    - [8.4.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
  - [8.5. Property `Domain > exports > errors`](#exports_errors)
    - [8.5.1. Domain > imports > Domain import > models > Identifier](#imports_items_models_items)
- [9. Property `Domain > lifecycle`](#lifecycle)

**Title:** Domain

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `true`           |
| **Defined in**            |                  |

**Description:** A bounded context (in the Eric Evans sense): a named slice of the larger system whose vocabulary, models, use cases, events, and permissions form a coherent whole. Domains keep large DeepThought specifications navigable by giving every entity a home and making cross-domain dependencies explicit.

| Property                             | Pattern | Type             | Deprecated | Definition                        | Title/Description        |
| ------------------------------------ | ------- | ---------------- | ---------- | --------------------------------- | ------------------------ |
| + [id](#id )                         | No      | string           | No         | In #/definitions/identifierSchema | Identifier               |
| + [name](#name )                     | No      | string           | No         | -                                 | Domain display name      |
| + [description](#description )       | No      | string           | No         | -                                 | Domain description       |
| - [owner](#owner )                   | No      | string           | No         | -                                 | Owner                    |
| - [classification](#classification ) | No      | enum (of string) | No         | -                                 | Strategic classification |
| - [glossary](#glossary )             | No      | array            | No         | -                                 | Glossary                 |
| - [imports](#imports )               | No      | array            | No         | -                                 | Imports                  |
| - [exports](#exports )               | No      | object           | No         | In #/definitions/exportSchema     | Domain exports           |
| - [lifecycle](#lifecycle )           | No      | object           | No         | -                                 | Field (lifecycleSchema)  |

## <a name="id"></a>1. Property `Domain > id`

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

## <a name="name"></a>2. Property `Domain > name`

**Title:** Domain display name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                           |
| **Must match regular expression** | ```^[A-Z][a-zA-Z ]+$``` [Test](https://regex101.com/?regex=%5E%5BA-Z%5D%5Ba-zA-Z+%5D%2B%24) |

## <a name="description"></a>3. Property `Domain > description`

**Title:** Domain description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** What this bounded context is responsible for and the slice of the system its language and entities cover. Required so every domain carries its own purpose statement inherent to its definition.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="owner"></a>4. Property `Domain > owner`

**Title:** Owner

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Team or individual accountable for this bounded context. Drives CODEOWNERS-style routing and on-call surface area.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="classification"></a>5. Property `Domain > classification`

**Title:** Strategic classification

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Subdomain classification in the Evans taxonomy: core (the thing the business wins on), supporting (necessary but not differentiating), generic (commodity / off-the-shelf candidate).

Must be one of:
* "core"
* "supporting"
* "generic"

## <a name="glossary"></a>6. Property `Domain > glossary`

**Title:** Glossary

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Authoritative definitions of domain terms.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be   | Description                                                                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Glossary entry](#glossary_items) | Pins the meaning of a domain term so prose documentation, code, and tests share one definition. The antidote to "what does X mean here?". |

### <a name="glossary_items"></a>6.1. Domain > glossary > Glossary entry

**Title:** Glossary entry

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/definitions/glossaryEntrySchema |

**Description:** Pins the meaning of a domain term so prose documentation, code, and tests share one definition. The antidote to "what does X mean here?".

| Property                                        | Pattern | Type            | Deprecated | Definition | Title/Description |
| ----------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [term](#glossary_items_term )                 | No      | string          | No         | -          | Term              |
| + [definition](#glossary_items_definition )     | No      | string          | No         | -          | Definition        |
| - [synonyms](#glossary_items_synonyms )         | No      | array of string | No         | -          | Synonyms          |
| - [relatedTerms](#glossary_items_relatedTerms ) | No      | array of string | No         | -          | Related terms     |

#### <a name="glossary_items_term"></a>6.1.1. Property `Domain > glossary > Glossary entry > term`

**Title:** Term

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="glossary_items_definition"></a>6.1.2. Property `Domain > glossary > Glossary entry > definition`

**Title:** Definition

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Authoritative meaning of the term within this domain.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="glossary_items_synonyms"></a>6.1.3. Property `Domain > glossary > Glossary entry > synonyms`

**Title:** Synonyms

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Alternate names for the same concept.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                  | Description |
| ------------------------------------------------ | ----------- |
| [synonyms items](#glossary_items_synonyms_items) | -           |

##### <a name="glossary_items_synonyms_items"></a>6.1.3.1. Domain > glossary > Glossary entry > synonyms > synonyms items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="glossary_items_relatedTerms"></a>6.1.4. Property `Domain > glossary > Glossary entry > relatedTerms`

**Title:** Related terms

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Adjacent terms that frequently co-occur with this one.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                          | Description |
| -------------------------------------------------------- | ----------- |
| [relatedTerms items](#glossary_items_relatedTerms_items) | -           |

##### <a name="glossary_items_relatedTerms_items"></a>6.1.4.1. Domain > glossary > Glossary entry > relatedTerms > relatedTerms items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="imports"></a>7. Property `Domain > imports`

**Title:** Imports

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Cross-domain dependencies this domain takes on.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description                                                                                                                                                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Domain import](#imports_items) | Names what this domain consumes from another domain. Only entities explicitly exported by the source domain may be imported -- this is how cross-context dependencies are made explicit and reviewable. |

### <a name="imports_items"></a>7.1. Domain > imports > Domain import

**Title:** Domain import

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/definitions/importSchema |

**Description:** Names what this domain consumes from another domain. Only entities explicitly exported by the source domain may be imported -- this is how cross-context dependencies are made explicit and reviewable.

| Property                                     | Pattern | Type   | Deprecated | Definition                            | Title/Description    |
| -------------------------------------------- | ------- | ------ | ---------- | ------------------------------------- | -------------------- |
| + [from](#imports_items_from )               | No      | string | No         | In #/definitions/identifierSchema     | Source domain        |
| - [models](#imports_items_models )           | No      | array  | No         | In #/definitions/identifierListSchema | Imported models      |
| - [usecases](#imports_items_usecases )       | No      | array  | No         | In #/definitions/identifierListSchema | Imported use cases   |
| - [events](#imports_items_events )           | No      | array  | No         | In #/definitions/identifierListSchema | Imported events      |
| - [collections](#imports_items_collections ) | No      | array  | No         | In #/definitions/identifierListSchema | Imported collections |
| - [errors](#imports_items_errors )           | No      | array  | No         | In #/definitions/identifierListSchema | Imported errors      |

#### <a name="imports_items_from"></a>7.1.1. Property `Domain > imports > Domain import > from`

**Title:** Source domain

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/identifierSchema |

| Restrictions                      |                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                   |
| **Must match regular expression** | ```^[a-z][a-z_]+[a-z]$``` [Test](https://regex101.com/?regex=%5E%5Ba-z%5D%5Ba-z_%5D%2B%5Ba-z%5D%24) |

#### <a name="imports_items_models"></a>7.1.2. Property `Domain > imports > Domain import > models`

**Title:** Imported models

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

##### <a name="imports_items_models_items"></a>7.1.2.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="imports_items_usecases"></a>7.1.3. Property `Domain > imports > Domain import > usecases`

**Title:** Imported use cases

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

##### <a name="imports_items_models_items"></a>7.1.3.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="imports_items_events"></a>7.1.4. Property `Domain > imports > Domain import > events`

**Title:** Imported events

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

##### <a name="imports_items_models_items"></a>7.1.4.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="imports_items_collections"></a>7.1.5. Property `Domain > imports > Domain import > collections`

**Title:** Imported collections

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

##### <a name="imports_items_models_items"></a>7.1.5.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

#### <a name="imports_items_errors"></a>7.1.6. Property `Domain > imports > Domain import > errors`

**Title:** Imported errors

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

##### <a name="imports_items_models_items"></a>7.1.6.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="exports"></a>8. Property `Domain > exports`

**Title:** Domain exports

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/definitions/exportSchema |

**Description:** The public surface of this domain. Anything not listed is private to the domain and may not be referenced from outside it.

| Property                               | Pattern | Type  | Deprecated | Definition                            | Title/Description    |
| -------------------------------------- | ------- | ----- | ---------- | ------------------------------------- | -------------------- |
| - [models](#exports_models )           | No      | array | No         | In #/definitions/identifierListSchema | Exported models      |
| - [usecases](#exports_usecases )       | No      | array | No         | In #/definitions/identifierListSchema | Exported use cases   |
| - [events](#exports_events )           | No      | array | No         | In #/definitions/identifierListSchema | Exported events      |
| - [collections](#exports_collections ) | No      | array | No         | In #/definitions/identifierListSchema | Exported collections |
| - [errors](#exports_errors )           | No      | array | No         | In #/definitions/identifierListSchema | Exported errors      |

### <a name="exports_models"></a>8.1. Property `Domain > exports > models`

**Title:** Exported models

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

#### <a name="imports_items_models_items"></a>8.1.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="exports_usecases"></a>8.2. Property `Domain > exports > usecases`

**Title:** Exported use cases

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

#### <a name="imports_items_models_items"></a>8.2.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="exports_events"></a>8.3. Property `Domain > exports > events`

**Title:** Exported events

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

#### <a name="imports_items_models_items"></a>8.3.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="exports_collections"></a>8.4. Property `Domain > exports > collections`

**Title:** Exported collections

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

#### <a name="imports_items_models_items"></a>8.4.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

### <a name="exports_errors"></a>8.5. Property `Domain > exports > errors`

**Title:** Exported errors

|                |                                    |
| -------------- | ---------------------------------- |
| **Type**       | `array`                            |
| **Required**   | No                                 |
| **Defined in** | #/definitions/identifierListSchema |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [Identifier](#imports_items_models_items) | -           |

#### <a name="imports_items_models_items"></a>8.5.1. Domain > imports > Domain import > models > Identifier

**Title:** Identifier

|                        |           |
| ---------------------- | --------- |
| **Type**               | `string`  |
| **Required**           | No        |
| **Same definition as** | [id](#id) |

## <a name="lifecycle"></a>9. Property `Domain > lifecycle`

**Title:** Field (lifecycleSchema)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** See [Field](./field.md#lifecycleschema).

----------------------------------------------------------------------------------------------------------------------------
