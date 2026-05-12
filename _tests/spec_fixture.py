from pathlib import Path


def write_catalog_fixture(spec_root: Path) -> None:
    for name in (
        "domain",
        "field",
        "model",
        "permission",
        "usecase",
        "scenario",
        "event",
        "state_machine",
    ):
        (spec_root / name).mkdir(parents=True, exist_ok=True)

    (spec_root / "domain" / "inventory.yaml").write_text(
        "id: inventory\nname: Inventory\ndescription: Inventory domain.\n"
    )
    (spec_root / "field" / "thing_id.yaml").write_text(
        "id: thing_id\nname: Thing Id\ndescription: Thing identifier.\ndataType: string\n"
    )
    (spec_root / "field" / "thing_name.yaml").write_text(
        "id: thing_name\nname: Thing Name\ndescription: Thing name.\ndataType: string\n"
    )
    (spec_root / "field" / "thing_state.yaml").write_text(
        "id: thing_state\nname: Thing State\ndescription: Thing lifecycle state.\ndataType: string\n"
    )
    (spec_root / "model" / "thing.yaml").write_text("""
id: thing
name: Thing
description: A catalogued thing.
fields:
  - thing_id
  - thing_name
  - thing_state
key: thing_id
domain: inventory
invariants:
  - id: thing_name_present
    name: Thing Name Present
    description: Every thing has a name.
    assert:
      field: thing_name
    enforcement: always
""".lstrip())
    (spec_root / "permission" / "inventory_access.yaml").write_text("""
id: inventory_access
name: Inventory Access
description: Inventory access bundle.
actors:
  - id: pantry_owner
    name: Pantry Owner
    description: Pantry owner.
permissions:
  - id: read_inventory
    name: Read Inventory
    description: Read inventory.
    rules:
      - effect: allow
        actors: pantry_owner
        description: Owners may read inventory.
""".lstrip())
    (spec_root / "usecase" / "get_thing.yaml").write_text("""
id: get_thing
name: Get Thing
description: Fetch a thing.
input: thing
output: thing
domain: inventory
permissions: read_inventory
""".lstrip())
    (spec_root / "scenario" / "get_thing_happy_path.yaml").write_text("""
id: get_thing_happy_path
name: Get Thing Happy Path
description: Reading a known thing succeeds.
usecase: get_thing
tags:
  - smoke
given:
  - actor: pantry_owner
when:
  input:
    thing_id: abc
then:
  - output:
      thing_id: abc
      thing_name: Example
""".lstrip())
    (spec_root / "event" / "thing_read.yaml").write_text("""
id: thing_read
name: Thing Read
description: Emitted when a thing is read.
schema_version: 1
payload: thing
delivery: transactional
aggregate: thing
topic: inventory.thing
ordered: true
""".lstrip())
    (spec_root / "state_machine" / "thing_lifecycle.yaml").write_text("""
id: thing_lifecycle
name: Thing Lifecycle
description: Lifecycle for thing entities.
target: thing
stateField: thing_state
initial: draft
states:
  - id: draft
    name: Draft
    description: Thing is newly created.
    mutableFields:
      - thing_id
      - thing_name
      - thing_state
  - id: published
    name: Published
    description: Thing is visible.
    mutableFields:
      - thing_state
transitions:
  - id: publish_thing
    name: Publish Thing
    description: Publish a thing.
    from: draft
    to: published
    via: get_thing
    emits: thing_read
""".lstrip())
