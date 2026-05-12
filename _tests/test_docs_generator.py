from argparse import Namespace
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from deepthought.generators.docs import DocsGenerator
from deepthought.meta_schemas import bundled_schemas_dir


class DocsGeneratorSpecModeTest(unittest.TestCase):
    def test_spec_mode_renders_nested_catalog_entities(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "site"
            for name in (
                "domain",
                "field",
                "model",
                "permission",
                "usecase",
                "scenario",
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
            (spec_root / "model" / "thing.yaml").write_text("""
id: thing
name: Thing
description: A catalogued thing.
fields:
  - thing_id
  - thing_name
key: thing_id
domain: inventory
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

            result = DocsGenerator().run(
                Namespace(
                    mode="spec",
                    schemas=bundled_schemas_dir(),
                    examples=None,
                    spec=spec_root,
                    out=out_dir,
                    title="Domain Reference",
                    clean=False,
                )
            )

            actor_page = (out_dir / "spec" / "actor.md").read_text()
            permission_page = (out_dir / "spec" / "permission.md").read_text()
            index_page = (out_dir / "index.md").read_text()

        self.assertEqual(0, result)
        self.assertIn("Pantry Owner", actor_page)
        self.assertIn("nested under `inventory_access`", actor_page)
        self.assertIn("Read Inventory", permission_page)
        self.assertIn("Actor", index_page)
        self.assertIn("Permission Set", index_page)


if __name__ == "__main__":
    unittest.main()
