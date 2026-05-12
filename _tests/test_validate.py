from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import yaml

from deepthought.validate import validate_file


class ValidationMessageTest(unittest.TestCase):
    def test_one_of_error_message_names_each_attempted_branch_test(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            schemas = root / "schemas"
            specs = root / "specs"
            schemas.mkdir()
            specs.mkdir()

            (schemas / "thing.meta.yaml").write_text(
                yaml.safe_dump(
                    {
                        "$id": "https://example.test/thing.meta.yaml",
                        "oneOf": [
                            {
                                "title": "Scalar thing",
                                "type": "object",
                                "required": ["kind", "value"],
                                "properties": {
                                    "kind": {"const": "scalar"},
                                    "value": {"type": "number"},
                                },
                            },
                            {
                                "title": "Model thing",
                                "type": "object",
                                "required": ["kind", "model"],
                                "properties": {
                                    "kind": {"const": "model"},
                                    "model": {"type": "string"},
                                },
                            },
                        ],
                    },
                    sort_keys=False,
                )
            )
            spec = specs / "bad.thing.yaml"
            spec.write_text("kind: scalar\nvalue: nope\n")

            errors = validate_file(spec, schemas_dir=schemas)

        self.assertEqual(1, len(errors))
        self.assertIn("oneOf branch 0 (Scalar thing)", errors[0].message)
        self.assertIn("'nope' is not of type 'number'", errors[0].message)
        self.assertIn("oneOf branch 1 (Model thing)", errors[0].message)
        self.assertIn("'model' was expected", errors[0].message)


if __name__ == "__main__":
    unittest.main()
