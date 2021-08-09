# Deepthought-Schema
Specification schema for models, data types, and domain-interfacing operations that facilitate Documentation Oriented 
Development for self-coding, self-validation, self-describing and self-testing generated source code.

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
feet:
  type: int
  name: Feet
  description: The number of feet length units
  unit: feet
  coerce: True
  constraints:
    - minimum: 0
      maximum: 8
inches:
  type: int
  name: Inches
  description: The remaining inch length units
  unit: inches
  coerce: True
  constraints:
    - minimum: 0
    - maximum: 12
```

Or, for the rest of the world:
```yaml
# person.fields.yml
meters:
  type: float
  name: Meters
  description: The number of meter length units
  unit: meters
  coerce: True
  constrainst:
    - minimum: 0
    - maximum: 3
    - precision: 0.01
```

### Units

DeepThought comes bundled with the conversion factors for commonly used units - but allows for externally defined units.
Through the use of dimensional fields, DeepThought will also test and validate your calculation's correctness through
dimensional analysis. Of course, not every field or project has a need for units - unit-less scalars are just as valid.

To define custom units, provide a key that can be used in fields to refer to and a few other basic pieces of 
information:

```yaml
# units.yml
fathoms:
  name: Fathoms
  description: A length measure usually referring to a depth.
  label: fathom
  label_short: fm
  measures: length
  conversion_to_si: 1.8288
```

By specifying the conversion factor in relation to SI units, conversion between units is trivial and allows for wider,
easier adoption in more systems and projects.

### Data Types

While the field example above may appear verbose, just take a second to imagine writing code to handle all the 
various combinations of units, and the tests to validate those fields are within specification. True, this amount of
flexibility may not be required for every project, but with DeepThought, it's baked in with minimal-to-no performance
impact.

Data Types arise through the use of specified fields, and desired values (dimensional or scalar) of the Models that feed
the domain layer implementation of your project.

Returning to our previous example, we can now define the `height` Data Type:

```yaml
# datatypes.yml
height:
  name: Height
  description: The vertical length measurement of the Person model
  unit: feet
  fields:
    - feet
    - inches
```

The `meters` schema is far more simple:

```yaml
# datatypes.yml
height:
  name: Height
  description: The vertical length measurement of the Person model
  fields: meters
```

Since there is only a single field, the Data Type assumes the unit of the field unless otherwise specified:

```yaml
# datatypes.yml
height:
  name: Height
  description: The vertical length measurement of the Person model
  unit: fathoms
  fields: meters
```

### Models

Models are the data structures that are directly consumed, and returned by domain interfacing operations. Models 
comprise the necessary Data Types to fully describe that which the domain can consume, manipulate, transform, parse,
etc. and be passed to the next layer to Domain-Edge Interactors.

Assume, you had a use case for calculating the volumetric density of a can of pringles and created the following models:

```yaml
# models.yml
cylinder:
  name: Pringles Can
  description: Measurements of a can of Pringles
  attributes:
    - radius
    - mass
    - height
```

```yaml
# models.yml
pringles_can_density:
  name: Density of a Pringles Can
  description: The mean density of the measured Pringles can
  units: kg / m^3
```

### Domain-Interfacing Use Cases

When specifying Domain-Interfacing Use Cases, Deepthought has no knowledge of your implementation of the domain. Be it
a single method, a chain of methods - that is up to you. Specify the input model, and the output model - knowing you can
trust that your input is valid and tested and in the exact form that is expected. However, if your dimensional analysis
is incorrect, no scaffold for your use case will be generated.

Given the Use Case specification:

```yaml
# usecases.yml
calc_density:
  name: Calculate Density of Cylinder
  description: Calculates the density of a cylinder
  input: cylinder
  output: pringles_can_density
```

```yaml
# models.yml
cylinder:
  name: Pringles Can
  description: Measurements of a can of Pringles
  attributes:
    - radius
    - mass
    - height
```

```yaml
# models.yml
pringles_can_density:
  name: Density of a Pringles Can
  description: The mean density of the measured Pringles can
  units: m / s
```

There is no way that the input units, length and mass - could possibly generate meters per second based on the known
units in the system.

Use cases can also specify required permissions, (and more).

## Code Generation
See codegen README for how to generate the models, scaffolds, unit tests, and documentation from the schema