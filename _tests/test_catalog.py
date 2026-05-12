from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from deepthought.catalog import (
    DuplicateSpecError,
    UnresolvedReferenceError,
    load_catalog,
)
from deepthought.meta_schemas import bundled_schemas_dir


class CatalogLoadTest(unittest.TestCase):
    def test_load_catalog_indexes_valid_specs_and_nested_permission_members(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "domain").mkdir()
            (root / "field").mkdir()
            (root / "model").mkdir()
            (root / "permission").mkdir()
            (root / "usecase").mkdir()
            (root / "scenario").mkdir()

            (root / "domain" / "inventory.yaml").write_text(
                "id: inventory\nname: Inventory\ndescription: Inventory domain.\n"
            )
            (root / "field" / "thing_id.yaml").write_text(
                "id: thing_id\nname: Thing Id\ndescription: Thing identifier.\ndataType: string\n"
            )
            (root / "field" / "thing_name.yaml").write_text(
                "id: thing_name\nname: Thing Name\ndescription: Thing name.\ndataType: string\n"
            )
            (root / "model" / "thing.yaml").write_text("""
id: thing
name: Thing
description: A catalogued thing.
fields:
  - thing_id
  - thing_name
key: thing_id
domain: inventory
""".lstrip())
            (root / "permission" / "inventory_access.yaml").write_text("""
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
            (root / "usecase" / "get_thing.yaml").write_text("""
id: get_thing
name: Get Thing
description: Fetch a thing.
input: thing
output: thing
domain: inventory
permissions: read_inventory
""".lstrip())
            (root / "scenario" / "get_thing_happy_path.yaml").write_text("""
id: get_thing_happy_path
name: Get Thing Happy Path
description: Reading a known thing succeeds.
usecase: get_thing
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

            catalog = load_catalog(root, schemas_dir=bundled_schemas_dir())

        self.assertEqual("thing", catalog.require("model", "thing").identifier)
        self.assertEqual(
            "inventory_access",
            catalog.require("permission_set", "inventory_access").identifier,
        )
        self.assertEqual(
            "read_inventory", catalog.require("permission", "read_inventory").identifier
        )
        self.assertEqual(
            "pantry_owner", catalog.require("actor", "pantry_owner").identifier
        )
        self.assertEqual(
            "get_thing", catalog.require("usecase", "get_thing").identifier
        )
        self.assertEqual(
            "get_thing_happy_path",
            catalog.require("scenario", "get_thing_happy_path").identifier,
        )

    def test_load_catalog_raises_for_duplicate_ids_within_kind(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            domain_dir = root / "domain"
            domain_dir.mkdir()
            (domain_dir / "first.yaml").write_text(
                "id: shared\nname: Shared\ndescription: first\n"
            )
            (domain_dir / "second.yaml").write_text(
                "id: shared\nname: Shared Again\ndescription: second\n"
            )

            with self.assertRaises(DuplicateSpecError):
                load_catalog(root, schemas_dir=bundled_schemas_dir())

    def test_load_catalog_raises_for_unresolved_reference(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "domain").mkdir()
            (root / "field").mkdir()
            (root / "model").mkdir()
            permission_dir = root / "permission"
            permission_dir.mkdir()
            (root / "domain" / "inventory.yaml").write_text(
                "id: inventory\nname: Inventory\ndescription: Inventory domain.\n"
            )
            (root / "field" / "thing_id.yaml").write_text(
                "id: thing_id\nname: Thing Id\ndescription: Thing identifier.\ndataType: string\n"
            )
            (root / "model" / "thing.yaml").write_text("""
id: thing
name: Thing
description: A catalogued thing.
fields:
  - thing_id
domain: inventory
""".lstrip())
            (permission_dir / "read_inventory.yaml").write_text("""
id: read_inventory
name: Read Inventory
description: Read inventory.
rules:
  - effect: allow
    actors: missing_actor
    description: Broken actor reference.
""".lstrip())

            with self.assertRaises(UnresolvedReferenceError):
                load_catalog(root, schemas_dir=bundled_schemas_dir())


if __name__ == "__main__":
    unittest.main()
