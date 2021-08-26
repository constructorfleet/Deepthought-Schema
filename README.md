# Deepthought-Schema
Specification schema for models, data types, and domain-interfacing operations that facilitate **Documentation Driven 
Development** for self-generated-code, self-validating, self-describing, auto-tested. and self-testing generated source code scaffolding for the Domain-Interfacing logic.

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
height:
  type: float
  name: Height
  description: How tall the person is
  unit: foot
  coerce: True
  constraints:
    - minimum: 0
    - maximum: 8
    - precision: 1 inch
```

Or, for the rest of the world:
```yaml
# person.fields.yml
height:
  type: float
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

For example, the units for the (Gravitational Constant)[https://en.wikipedia.org/wiki/Gravitational_constant] are
`m^3/(kg*s^2)`, to define this in DeepThought would look like this:

```yaml
id: gravitational_constant
name: Gravitational Constant Units
description: The units for G, the gravitational constant
label:
  single: meter^3 per (kilogram * second^2)
  plural: meters^3 per (kilogram * second^2)
  symbol: m^3/(kg*s^2)
unit:
  unit: meter
  exponent: 3
  dividedBy:
    group:
      unit: kilogram
      multipliedBy:
        unit: second
        exponent: 2
```

#### Built-in Units

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
