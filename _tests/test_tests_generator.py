from argparse import Namespace
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys
import unittest
import json

from jsonschema import Draft7Validator

from _tests.spec_fixture import write_catalog_fixture
from deepthought.generators.tests import TestsGenerator
from deepthought.meta_schemas import bundled_schemas_dir
from deepthought.tests import load_test_manifest_schema


class TestsGeneratorSpecModeTest(unittest.TestCase):
    def test_spec_mode_can_generate_language_neutral_manifest(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "test-manifest"
            write_catalog_fixture(spec_root)

            result = TestsGenerator().run(
                Namespace(
                    format="manifest",
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    title="Ignored In Manifest Mode",
                    clean=False,
                )
            )

            manifest = json.loads((out_dir / "test_manifest.json").read_text())
            schema = load_test_manifest_schema()
            errors = sorted(
                Draft7Validator(schema).iter_errors(manifest),
                key=lambda error: list(error.path),
            )

        self.assertEqual(0, result)
        self.assertEqual([], errors)
        self.assertEqual(1, manifest["counts"]["scenarios"])
        self.assertEqual(1, manifest["counts"]["invariants"])
        self.assertEqual("get_thing", manifest["scenarios"][0]["usecase"])
        self.assertEqual("thing", manifest["invariants"][0]["model"])

    def test_spec_mode_can_generate_typescript_stubs(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "generated-typescript"
            write_catalog_fixture(spec_root)

            result = TestsGenerator().run(
                Namespace(
                    format="typescript",
                    typescript_runner="vitest",
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    title="Ignored In Typescript Mode",
                    clean=False,
                )
            )

            suite_dir = out_dir / "generated_typescript"
            types_text = (suite_dir / "types.ts").read_text()
            scenario_text = (suite_dir / "get_thing.test.ts").read_text()
            invariant_text = (suite_dir / "invariants.test.ts").read_text()

        self.assertEqual(0, result)
        self.assertIn("export interface GeneratedScenario", types_text)
        self.assertIn("export interface GeneratedInvariant", types_text)
        self.assertIn("assertion: JsonValue | null;", types_text)
        self.assertIn('import { describe, test } from "vitest";', scenario_text)
        self.assertIn('import type { GeneratedScenario } from "./types";', scenario_text)
        self.assertIn("describe.skip", scenario_text)
        self.assertIn("test.skip", scenario_text)
        self.assertIn("const scenario: GeneratedScenario", scenario_text)
        self.assertIn("Generated scenario stub", scenario_text)
        self.assertIn('import type { GeneratedInvariant } from "./types";', invariant_text)
        self.assertIn("const invariant: GeneratedInvariant", invariant_text)
        self.assertIn('"assertion":', invariant_text)
        self.assertIn("Thing Name Present", invariant_text)
        self.assertIn("Generated invariant stub", invariant_text)

    def test_spec_mode_can_generate_jest_stubs(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "generated-jest"
            write_catalog_fixture(spec_root)

            result = TestsGenerator().run(
                Namespace(
                    format="typescript",
                    typescript_runner="jest",
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    title="Ignored In Jest Mode",
                    clean=False,
                )
            )

            scenario_text = (
                out_dir / "generated_typescript" / "get_thing.test.ts"
            ).read_text()

        self.assertEqual(0, result)
        self.assertIn('import { describe, test } from "@jest/globals";', scenario_text)

    def test_spec_mode_can_generate_go_stubs(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "generated-go"
            write_catalog_fixture(spec_root)

            result = TestsGenerator().run(
                Namespace(
                    format="go",
                    typescript_runner="vitest",
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    title="Ignored In Go Mode",
                    clean=False,
                )
            )

            suite_dir = out_dir / "generated_go"
            types_text = (suite_dir / "types.go").read_text()
            scenario_text = (suite_dir / "get_thing_test.go").read_text()
            invariant_text = (suite_dir / "invariants_test.go").read_text()

        self.assertEqual(0, result)
        self.assertIn("type GeneratedScenario struct", types_text)
        self.assertIn("type GeneratedInvariant struct", types_text)
        self.assertIn("Assertion   *string", types_text)
        self.assertIn("package generatedtests", scenario_text)
        self.assertIn('import "testing"', scenario_text)
        self.assertIn("func TestScenarioGetThingHappyPath", scenario_text)
        self.assertIn("scenario := GeneratedScenario{", scenario_text)
        self.assertIn("Generated scenario stub", scenario_text)
        self.assertIn("func TestInvariantThingThingNamePresent", invariant_text)
        self.assertIn("invariant := GeneratedInvariant{", invariant_text)
        self.assertIn("Assertion:", invariant_text)
        self.assertIn("Generated invariant stub", invariant_text)

    def test_spec_mode_can_generate_rust_stubs(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "generated-rust"
            write_catalog_fixture(spec_root)

            result = TestsGenerator().run(
                Namespace(
                    format="rust",
                    typescript_runner="vitest",
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    title="Ignored In Rust Mode",
                    clean=False,
                )
            )

            suite_dir = out_dir / "generated_rust"
            cargo_text = (suite_dir / "Cargo.toml").read_text()
            lib_text = (suite_dir / "src" / "lib.rs").read_text()
            types_text = (suite_dir / "src" / "types.rs").read_text()
            scenario_text = (suite_dir / "src" / "get_thing.rs").read_text()
            invariant_text = (suite_dir / "src" / "invariants.rs").read_text()

        self.assertEqual(0, result)
        self.assertIn('[package]', cargo_text)
        self.assertIn('name = "generated-deepthought-tests"', cargo_text)
        self.assertIn('mod types;', lib_text)
        self.assertIn('mod get_thing;', lib_text)
        self.assertIn('mod invariants;', lib_text)
        self.assertIn("pub struct GeneratedScenario", types_text)
        self.assertIn("pub struct GeneratedInvariant", types_text)
        self.assertIn("pub assertion: Option<String>", types_text)
        self.assertIn("use crate::types::GeneratedScenario;", scenario_text)
        self.assertIn("#[test]", scenario_text)
        self.assertIn("#[ignore = \"Generated scenario stub: connect this to a concrete use-case runner\"]", scenario_text)
        self.assertIn("let scenario = GeneratedScenario {", scenario_text)
        self.assertIn("Generated scenario stub", scenario_text)
        self.assertIn("use crate::types::GeneratedInvariant;", invariant_text)
        self.assertIn("let invariant = GeneratedInvariant {", invariant_text)
        self.assertIn("assertion:", invariant_text)
        self.assertIn("Generated invariant stub", invariant_text)

    def test_spec_mode_renders_scenarios_and_invariants(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "test-plan"
            write_catalog_fixture(spec_root)

            result = TestsGenerator().run(
                Namespace(
                    format="markdown",
                    typescript_runner="vitest",
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    title="Generated Test Plan",
                    clean=False,
                )
            )

            scenario_page = (out_dir / "tests" / "scenarios.md").read_text()
            invariant_page = (out_dir / "tests" / "invariants.md").read_text()
            index_page = (out_dir / "index.md").read_text()

        self.assertEqual(0, result)
        self.assertIn("Get Thing Happy Path", scenario_page)
        self.assertIn("smoke", scenario_page)
        self.assertIn("thing_id: abc", scenario_page)
        self.assertIn("Thing Name Present", invariant_page)
        self.assertIn("field: thing_name", invariant_page)
        self.assertIn("Scenarios", index_page)
        self.assertIn("Invariants", index_page)

    def test_spec_mode_can_generate_runnable_unittest_stubs(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_root = root / "spec"
            out_dir = root / "generated-tests"
            write_catalog_fixture(spec_root)

            result = TestsGenerator().run(
                Namespace(
                    format="unittest",
                    typescript_runner="vitest",
                    schemas=bundled_schemas_dir(),
                    spec=spec_root,
                    out=out_dir,
                    title="Ignored In Unittest Mode",
                    clean=False,
                )
            )

            suite_dir = out_dir / "generated_unittest"
            scenario_path = suite_dir / "test_usecase_get_thing.py"
            invariant_path = suite_dir / "test_invariants.py"
            payloads_path = suite_dir / "payloads.py"
            init_exists = (suite_dir / "__init__.py").exists()
            payloads_text = payloads_path.read_text()
            scenario_text = scenario_path.read_text()
            invariant_text = invariant_path.read_text()
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    "generated_unittest",
                    "-p",
                    "test_*.py",
                ],
                capture_output=True,
                text=True,
                check=False,
                cwd=out_dir,
            )

        self.assertEqual(0, result)
        self.assertTrue(init_exists)
        self.assertIn("class GeneratedScenario", payloads_text)
        self.assertIn("class GeneratedInvariant", payloads_text)
        self.assertIn("assertion: Any | None", payloads_text)
        self.assertIn("from generated_unittest.payloads import GeneratedScenario", scenario_text)
        self.assertIn("class GeneratedScenarioTests", scenario_text)
        self.assertIn("scenario = GeneratedScenario(", scenario_text)
        self.assertIn("test_scenario_get_thing_happy_path", scenario_text)
        self.assertIn("Generated scenario stub", scenario_text)
        self.assertIn("from generated_unittest.payloads import GeneratedInvariant", invariant_text)
        self.assertIn("invariant = GeneratedInvariant(", invariant_text)
        self.assertIn("assertion=", invariant_text)
        self.assertIn("test_invariant_thing_thing_name_present", invariant_text)
        self.assertEqual(0, completed.returncode)
        self.assertIn("OK (skipped=2)", completed.stderr)


if __name__ == "__main__":
    unittest.main()
