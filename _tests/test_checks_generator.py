import json
from argparse import Namespace
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from _tests.spec_fixture import write_catalog_fixture
from deepthought.generators.checks import ChecksGenerator
from deepthought.meta_schemas import bundled_schemas_dir


class ChecksGeneratorTest(unittest.TestCase):
    def test_build_writes_machine_readable_manifests(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "checks-out"
            write_catalog_fixture(spec_root)

            result = ChecksGenerator().run(
                Namespace(
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    clean=False,
                )
            )

            index_payload = json.loads((out_dir / "index.json").read_text())
            scenarios = json.loads((out_dir / "checks" / "scenarios.json").read_text())
            invariants = json.loads(
                (out_dir / "checks" / "invariants.json").read_text()
            )
            permission_rules = json.loads(
                (out_dir / "checks" / "permission_rules.json").read_text()
            )
            transitions = json.loads(
                (out_dir / "checks" / "transitions.json").read_text()
            )

        self.assertEqual(0, result)
        self.assertEqual(1, index_payload["counts"]["scenarios"])
        self.assertEqual(1, index_payload["counts"]["invariants"])
        self.assertEqual(1, index_payload["counts"]["permission_rules"])
        self.assertEqual(1, index_payload["counts"]["transitions"])
        self.assertEqual("get_thing", scenarios[0]["usecase"])
        self.assertEqual("thing", invariants[0]["model"])
        self.assertEqual("read_inventory", permission_rules[0]["permission"])
        self.assertEqual(["get_thing"], transitions[0]["via"])
        self.assertEqual(["thing_read"], transitions[0]["emits"])


if __name__ == "__main__":
    unittest.main()
