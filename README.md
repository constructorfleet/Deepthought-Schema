# Deepthought-Schema
Specification schemas and tooling for models, data types, and domain-interfacing operations that facilitate **Documentation Driven
Development**: living documentation, generated test surfaces, generated correctness checks, and generated code scaffolding derived from the same source specifications.

The `deepthought` package is the execution surface for that idea. Validation remains a built-in framework command, and output-producing workflows are moving behind a generator interface so docs, tests, code, and future correctness-check generators can be discovered and invoked consistently from the CLI.

The `tests` generator now exposes a language-neutral manifest backend intended for downstream generators in Python, TypeScript, Go, Rust, and other ecosystems. That contract is defined in `src/deepthought/tests/test_manifest.schema.json`, and backend-specific emitters should target the manifest rather than reparsing the source YAML directly. The built-in backends now include Python `unittest` stubs with generated helper dataclasses, TypeScript for explicit Vitest or Jest stubs with generated helper interfaces, Go `_test.go` scaffolds with generated helper structs, and Rust scaffolds with generated helper structs plus a `Cargo.toml`/`src/` crate layout, all emitted from that shared manifest and aligned on the same helper field names where the host language allows it.

You can print the packaged test-manifest schema path with `deepthought test-schema`, or print the schema JSON directly with `deepthought test-schema --format json`.

## Schema Types

### Fields

Traditionally, a field's specification is broad, abstract, or meaningless which leads to writing documentation that
attempts to provide meaning to the consumer of the code. We know what an Integer, Float, Byte, String, etc. are - but 
these are just labels we apply to varying ways of storing and manipulating data. If the author provides sufficient 
information regarding the acceptable values, ranges, and edge case - there is still the matter of writing a slew of 
tests to ensure the fields lie within the specifications. Not to mention, hoping the documentation remains in line with
the implementation as teams, features, and requirements change and grow.  

While still using the same underlying storage and manipulations considered familiar across the landscape, fields in
DeepThought attempt to remove the tediousness, prevent stale documentation, as well as describing what is. Each field 
specifies a code-friendly reference name, a human-readable meaningful name, description, constraints, coercive 
manipulations of the underlying data type - plus units if applicable.  

Assume you need a field that represents the height of something, maybe a person:  

Traditionally, this would be a field of type `int` - if you're lucky or forward thinking, the variable name might be 
`heightFt` - more often than not it's named `height`.  

With DeepThought, this field could be specified as:
```yaml
# person.fields.yml
id: height
type: number
name: Height
description: How tall the person is
unit: foot
coerce: True
constraints:
- minimum: 0
- maximum: 8
- precision: 
    value: 1
    unit: inch
```

Or, for the rest of the world:
```yaml
# person.fields.yml
id:
type: number
name: Height
description: How tall the person is
unit: meter
coerce: True
constraints:
- minimum: 0
- maximum: 3
- precision: 0.01
```

You tell DeepThought the unit to present to the Domain-Interfacing Use Case.

### Constraints

The constraints placed on a field, as seen above, can be expressed with inferred or explicit units. Constraints apply to
a set of underlying types: `minimum` is not a meaningful constraint to a `string` or `byte`.

#### Built-in Constraints

TODO

### Units

DeepThought's extensible unit system comes bundled with commonly used units. Through the use of dimensional fields, 
DeepThought will also test and validate correctness through dimensional analysis. Of course, not every field has a need 
for units - unit-less scalars are just as valid.

To define custom units, provide a key that can be used in fields to refer to and a few other basic pieces of 
information:

```yaml
# units.yml
id: fathom
name: Fathom
description: A length measure usually referring to a depth.
label:
  single: Fathom
  plural: Fathoms
  symbol: fm
conversion:
  unit: meter
  factor: 1.8288
```

While any unit can be specified in the conversion attribute, specifying the conversion factor in relation to 
[International System Units](https://en.wikipedia.org/wiki/International_System_of_Units) (SI), allows for wider, easier
adoption in more systems and projects.

To specify an entirely new dimensional unit, simply omit the conversion attribute:

```yaml
# units.yml
id: click
name: Click
description: The click count of something.
label:
  single: Click
  plural: Clicks
  symbol: clicks
```
```yaml
id: slam  # This may be meaningful to someone...
name: Slams
description: Count of something clicked being broken.
label:
    single: Slam
    plural: Slams
    symbol: slams
conversion:
    unit: click
    factor: .001  # If clicked 1000 times, must be broken
```

DeepThought also supports defining multi-dimensional units, or compound units, even complex units.

For example, velocity is distance over time, acceleration is the change in velocity over time:
```yaml
id: velocity
name: Velocity
description: The change in physical position per unit time.
label:
  single: meter per second
  plural: meters per second
  symbom: m/s
unit:
  unit: meter
  dividedBy:
    unit: second
```

```yaml
id: acceleration
name: Acceleration
description: The rate of change in velocity per unit time.
label:
  single: meter per second^2
  plural: meters per second^2
  symbol: m/s^2
unit:
  unit: meter
  dividedBy:
    unit: second
    exponent: 2
```

#### Built-in Units

* bps, Bps, kbps, kBps, mbps, mBps  
* bit, byte, kilobit, kilobyte, megabit, megabyte, gigabyte  
* ampere  
* Couloumb, joule  
* acceleration, velocity, force, presssure  
* foot, inch, mile, yard  
* centimeter, millimeter, meter, kilometer  
* ounce, pound, gram, kilogram, microgram  
* second, minute, hour  
* hertz  

#### Built-in Constants

* Elementary Charge  
* Gravitational Constant  
* Lightspeed  
* Planck  

### Models

Models are the data structures that are directly consumed, or returned by, Domain-Interfacing Use Cases. Models 
comprise the necessary Fields to fully describe that which the domain can consume, manipulate, transform, parse, or
return.

Assume, you had a use case for calculating the volumetric density of a can of Pringles and created the following models:

```yaml
# pringles.fields.yml
- id: radius
  type: number
  name: Radius
  description: Distance from edge to center of a Pringles can
  unit: centimeter
  coerce: True
  constraints:
    - minimum: 0
    - maximum:
        value: 1
        unit: meter
- id: height
  type: float
  name: Height
  description: Distance from bottom to top of a Pringles can
  unit: inches
  coerce: True
  constraints:
    - exclusiveMinimum: 0
- id: mass
  type: number
  name: Mass
  description: The amount of matter contained in a Pringles can
  unit: grams
  coerce: True
- id: density
  type: number
  name: Pringles Can Density 
  description: The mean density of the a Pringles can
  unit: si_density
      
# pringles.models.yml
pringles_can_dimensions:
  name: Pringles Can Dimensions
  description: The physical measurements of a can of Pringles
  fields:
    - radius
    - mass
    - height

pringles_can_density:
  fields: density
```

### Domain-Interfacing Use Cases

When specifying Domain-Interfacing Use Cases, Deepthought has no knowledge of your implementation. Be it a single 
method, a chain of methods - that is up to you. Specify the input Model, and the output Model - knowing you can trust 
that your input is valid, tested, and in the exact form that is expected. If dimensionally correct, DeepThought will
generate the scaffolded code for you to implement - if incorrect, you will know before you even start coding.

Correct:

```yaml
# pringles.usecases.yml
calculate_can_density:
  name: Calculate Density of Cylinder
  description: Calculates the density of a cylinder
  input: pringles_can_dimensions
  output: pringles_can_density
```

Incorrect:
```yaml
# pringles.fields.yml
pringles_can_density:
  name: Pringles Can Density 
  description: The mean density of the a Pringles can
  unit: meter / second
  
# pringles.usecases.yml
calculate_can_density:
  name: Calculate Density of Cylinder
  description: Calculates the density of a cylinder
  input: pringles_can_dimensions
  output: pringles_can_density
```

There is no way that the input units (`inches`/`centimeter` and `grams`) - could possibly be yield to the expected
units (`meter / second`) specified in the `density` model based on the known units in the system.

Use Cases can be chained, accept multiple models, provide permission validation and are completely reusable.

#### Use Case Relations

By default, a Use Case asserts a **dimensional** relation between its inputs and its output: the units on the
input fields, when combined dimensionally, must yield the units of the output. That contract is exactly right
for compute-style work (`density = mass / volume`) but it is the *wrong* contract for data-retrieval work, where
the input is a lookup key and the output is the record identified by that key. The two never share a dimension.

To support both, every Use Case may declare an explicit `relation`:

| `relation.kind` | When to use it | Match contract |
|-----------------|----------------|----------------|
| `dimensional` (default) | Compute / transform / derive | Units of input fields are dimensionally combinable into the units of the output fields |
| `key`                   | "Get by id" / "Get by slug" lookups | An input field value is matched against the output model's `key` field (or the explicit `outputKey`) |
| `query`                 | Filter / search / list endpoints | Each input field constrains a named output field; output cardinality is typically `many` |
| `opaque`                | External APIs, side effects, hashes, translations, anything DeepThought can't reason about | None — the author asserts a contract DeepThought cannot validate. A `reason` is required so the escape hatch is always documented. |

**Key relation — data retrieval by id:**

```yaml
# pringles.fields.yml
- id: pringles_can_id
  type: string
  name: Pringles Can Id
  description: Stable identifier for a specific Pringles can on the shelf
- id: stocked_at
  type: string
  name: Stocked At
  description: ISO-8601 timestamp the can was stocked

# pringles.models.yml
pringles_can_lookup:
  name: Pringles Can Lookup
  description: Looks up a single Pringles can by id
  fields:
    - pringles_can_id

pringles_can:
  name: Pringles Can
  description: A specific Pringles can on the shelf
  fields:
    - pringles_can_id
    - radius
    - height
    - mass
    - stocked_at
  key: pringles_can_id

# pringles.usecases.yml
get_pringles_can:
  name: Get Pringles Can
  description: Retrieves a Pringles can by its id
  input: pringles_can_lookup
  output: pringles_can
  relation:
    kind: key
    inputKey: pringles_can_id
    cardinality: one
```

The `pringles_can_id` on the input does not — and cannot — combine dimensionally into the `radius`,
`height`, or `mass` of the output. Declaring `relation.kind: key` tells DeepThought to skip dimensional
analysis and instead check that `inputKey` resolves against the output model's `key`.

**Query relation — filter / search:**

```yaml
# pringles.models.yml
pringles_can_filter:
  name: Pringles Can Filter
  description: Filter for searching the stocked-can inventory
  fields:
    - flavor
    - stocked_after

# pringles.usecases.yml
list_pringles_cans:
  name: List Pringles Cans
  description: Returns every can matching the supplied filter
  input: pringles_can_filter
  output: pringles_can
  relation:
    kind: query
    cardinality: many
    filters:
      - inputField: flavor
        outputField: flavor
        operator: equals
      - inputField: stocked_after
        outputField: stocked_at
        operator: greater_than_or_equal
```

`relation.kind: query` lets the input model be a *predicate* against the output model rather than a
dimensional precursor of it. Each `filters` entry maps an input field to the output field it constrains
and the comparison operator to apply.

**Opaque relation — explicit escape hatch:**

Some Use Cases genuinely cannot be validated by DeepThought: an external API call, a cryptographic hash, a
translation service, a notification dispatch. The input doesn't combine into the output dimensionally, the
output isn't a record looked up by an input key, and the input isn't a query over the output. Rather than
torture one of the structured relations into "kind of fitting," declare the contract opaque:

```yaml
hash_pringles_can:
  name: Hash Pringles Can
  description: Computes a stable content hash of a Pringles can record
  input: pringles_can
  output: pringles_can_hash
  relation:
    kind: opaque
    reason: One-way SHA-256; output bytes have no dimensional or key relationship to the input fields
    pure: true
```

```yaml
notify_pantry_owner:
  name: Notify Pantry Owner
  description: Sends a push notification when the pantry is below threshold
  input:
    - pantry_dimensions
    - notification_settings
  output: notification_dispatch_receipt
  relation:
    kind: opaque
    reason: External notification provider; receipt is provider-assigned and unrelated to input units
    pure: false
```

`relation.kind: opaque` tells DeepThought to skip both dimensional analysis and key/query resolution, but
`reason` is **required** so opting out is always accompanied by a documented justification — the escape
hatch should be visible in code review, not silent. The optional `pure` flag signals whether the use case
has observable side effects (defaults to `false`), which downstream tooling can use to decide whether the
operation is safe to retry or memoize.

### Collections

A **Collection** is a named, finite set of typed values that share a common kind — think *enums, but where
every member shares a dimension or a model*. Collections compose with Use Cases: a `relation.kind: key` use
case can resolve its lookup against a Collection just as easily as against a stored model.

There are two flavors:

**Scalar collection** — every entry is a single value of the same `dataType` and (optionally) `unit`:

```yaml
# paper_sizes.collection.yaml
id: a_series_paper_widths
name: A Series Paper Widths
description: ISO 216 A-series paper widths, longest edge
kind: scalar
dataType: number
unit: millimeter
values:
  - id: a3
    name: A3
    value: 420
  - id: a4
    name: A4
    value: 297
  - id: a5
    name: A5
    value: 210
```

Because every entry shares `unit: millimeter`, the collection itself is dimensionally meaningful — it can be
the output of a use case that resolves a paper size to its width and pass dimensional analysis the same way
a single field would.

**Model collection** — every entry is an instance of the same model:

```yaml
# screen_resolutions.collection.yaml
id: standard_screen_resolutions
name: Standard Screen Resolutions
description: Common named display resolutions
kind: model
model: resolution
key: id
values:
  - id: hd
    name: HD
    value:
      width: 1280
      height: 720
  - id: full_hd
    name: Full HD
    value:
      width: 1920
      height: 1080
  - id: uhd_4k
    name: UHD 4K
    value:
      width: 3840
      height: 2160
```

A model collection is the natural target for a key-relation use case:

```yaml
get_resolution:
  name: Get Standard Resolution
  description: Resolves a named standard resolution to its width / height
  input: resolution_lookup     # has a single `id` field
  output: standard_screen_resolutions
  relation:
    kind: key
    inputKey: id
    cardinality: one
```

## Chained Use Cases with Multiple Input Models

Most architectural philosophies preach of the "ATOMIC!": Atomic commits, atomic classes, atomic use cases. It makes 
sense to reuse Use Cases, and put them together like Legos or microservices. Using the Use Case schema, you can specify 
the next use case in the chain. Inputs can be trusted, and output models must be dimensionally possible from the input
models for the code-generated scaffolding to work.

```yaml
# usecases.yml
calculate_cylinder_density:
  name: Calculate the Density of a Cylinder
  description: Calculates the density of a cylinder
  input: pringles_can_dimensions
  output: pringles_can_density
  next: calculate_time_to_empty

calculate_time_to_empty:
  name: Calculate the time to empty a can of Pringles
  description: Calculates the time it will take to consume an entire Pringles can. Once You Pop, You Can't Stop!
  input:
    - pringles_can_dimensions
    - density_consumption_rate
  output: time_to_empty_can
  next: extrapolate_emptying_pantry

extrapolate_emptying_pantry:
  name: Calculate the time to empty the pantry
  description: Extrapolates the time it takes to empty a can of Pringles to approximate the time to devour the pantry full of Pringles.
  input:
    - time_to_empty_can
    - pringles_can_density
    - pantry_dimensions
  output: time_to_obesity
```

## Re-usability Of Schemas

Hard-coding names and descriptions, as above, doesn't facilitate portability or re-usability. To rectify Units, 
Field, Data Types can utilize template replacers of the containing structures.

```yaml
# fields.yml
radius:
  type: float
  name: Radius
  description: Radial dimension of {{ model.name }}
  unit: centimeter
  coerce: True
height:
  type: float
  name: Height
  description: Top to bottom dimension of {{ model.name }}
  unit: inches
  coerce: True
mass:
  type: float
  name: Mass
  description: Physical quantity of matter in {{ model.usecase.focus }}
  unit: grams
  coerce: True
density:
  type: float
  name: Density of {{ model.usecase.focus }} 
  description: The mean density of {{ model.usecase.focus }}
  unit: kilogram / (meter ^ 3)
  
# models.yml
dimensions:
  name: Dimensions of {{ usecase.focus }}
  description: The physical measurements of {{ usecase.focus }}
  fields:
    - radius
    - mass
    - height

# usecases.yml
get_cylinder_density:
  name: Get Density of {{ this.focus }}
  description: Calculates mean density of {{ this.focus }} 
  input: dimensions
  output: density

get_pringles_can_density:
  extends: get_cylinder_density
  focus: Pringles Can
  next: calculate_time_to_empty
```

### MORE TO COME

TODO

## Where's the value? I don't get it - Editorial

I have always been drawn to software architectural design. I also am one of those blatantly guilty of focusing on code, 
not the documentation - and if you know me, I'm lazy. I don't write a lot of APIs, which seems to be the focus of
GraphQL and Swagger - but the idea of schema-first, validated, self-describing... resonated with me. Take Ansible, with well-defined
YAML formatted documentation, the ArgSpec must still be implemented; allowing for divergence in implementation and documentation.

The goal here is to create a specification that is simple, scalable and consistent enough for non-developers to 
maintain. A specification that can drive and generate human-readable documentation (Swagger). Automatically generate descriptive and meaningful 
classes in almost any language (GraphQL). Testing is a natural consequence of the specification and constraints therein (TTD).

Is this complete? Not by a long shot. If you see the benefit, join me! Because, for me, this will completely change how
I approach software development.
