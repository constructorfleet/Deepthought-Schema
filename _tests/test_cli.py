from io import StringIO
import contextlib
import json
import unittest
from unittest.mock import patch

from deepthought.cli import main
from deepthought.generators import discover_generators
from deepthought.tests import load_test_manifest_schema, test_manifest_schema_path


class GeneratorDiscoveryTest(unittest.TestCase):
    def test_discover_generators_falls_back_to_builtins_when_no_metadata_exists(self):
        with patch("deepthought.generators.entry_points", return_value=[]):
            generators = discover_generators()

        self.assertEqual(
            ["checks", "docs", "tests"], [generator.name for generator in generators]
        )


class CliHelpTest(unittest.TestCase):
    def test_top_level_help_lists_discovered_generators(self):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            with self.assertRaises(SystemExit) as exc:
                main(["--help"])

        self.assertEqual(0, exc.exception.code)
        self.assertIn("checks", stdout.getvalue())
        self.assertIn("docs", stdout.getvalue())
        self.assertIn("tests", stdout.getvalue())

    def test_top_level_help_lists_test_schema_command(self):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            with self.assertRaises(SystemExit) as exc:
                main(["--help"])

        self.assertEqual(0, exc.exception.code)
        self.assertIn("test-schema", stdout.getvalue())


class TestSchemaCommandTest(unittest.TestCase):
    def test_test_schema_prints_packaged_schema_path(self):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            result = main(["test-schema"])

        self.assertEqual(0, result)
        self.assertEqual(str(test_manifest_schema_path()), stdout.getvalue().strip())

    def test_test_schema_can_print_json_schema(self):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            result = main(["test-schema", "--format", "json"])

        self.assertEqual(0, result)
        self.assertEqual(load_test_manifest_schema(), json.loads(stdout.getvalue()))


if __name__ == "__main__":
    unittest.main()
