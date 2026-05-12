"""Render language-neutral and backend-specific test outputs from a catalog."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
import re

import yaml

from deepthought.catalog import Catalog, SpecEntry

_TEST_MANIFEST_SCHEMA_PATH = Path(__file__).with_name("test_manifest.schema.json")


def test_manifest_schema_path() -> Path:
    return _TEST_MANIFEST_SCHEMA_PATH


def _jekyll_config(title: str, description: str) -> str:
    return (
        f"title: {title}\n"
        f"description: {description}\n"
        "theme: jekyll-theme-cayman\n"
        "markdown: kramdown\n"
        "kramdown:\n"
        "  syntax_highlighter: rouge\n"
        "  parse_block_html: true\n"
    )


def _yaml_block(value: object) -> list[str]:
    rendered = yaml.safe_dump(value, sort_keys=False).rstrip()
    return ["```yaml", rendered, "```", ""]


def _scenario_usecase_id(entry: SpecEntry) -> str | None:
    usecase = entry.data.get("usecase")
    if isinstance(usecase, str):
        return usecase
    return entry.parent_identifier


def _code_identifier(value: str) -> str:
    normalized = re.sub(r"[^0-9a-zA-Z_]+", "_", value)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    if not normalized:
        normalized = "generated"
    if normalized[0].isdigit():
        normalized = f"_{normalized}"
    return normalized.lower()


def _entry_source_label(entry: SpecEntry, spec_root: Path) -> str:
    try:
        rel = entry.path.relative_to(spec_root)
    except ValueError:
        rel = entry.path
    source = f"source: `{rel}`"
    if entry.parent_identifier is not None:
        source += f"; nested under `{entry.parent_identifier}`"
    return source


def _scenario_manifest(catalog: Catalog, spec_root: Path) -> list[dict[str, object]]:
    scenarios: list[dict[str, object]] = []
    for entry in sorted(
        catalog.iter_kind("scenario"), key=lambda item: item.identifier
    ):
        scenarios.append(
            {
                "id": entry.identifier,
                "name": entry.data.get("name", entry.identifier),
                "description": entry.data.get("description", ""),
                "usecase": _scenario_usecase_id(entry) or "unassigned",
                "tags": entry.data.get("tags") or [],
                "source": _entry_source_label(entry, spec_root),
                "given": entry.data.get("given") or [],
                "when": entry.data.get("when"),
                "then": entry.data.get("then") or [],
            }
        )
    return scenarios


def _invariant_manifest(catalog: Catalog, spec_root: Path) -> list[dict[str, object]]:
    invariants: list[dict[str, object]] = []
    for model in sorted(catalog.iter_kind("model"), key=lambda item: item.identifier):
        model_invariants = model.data.get("invariants")
        if not isinstance(model_invariants, list):
            continue
        for invariant in model_invariants:
            if not isinstance(invariant, dict):
                continue
            identifier = invariant.get("id", "(no id)")
            invariants.append(
                {
                    "id": identifier,
                    "name": invariant.get("name", identifier),
                    "description": invariant.get("description", ""),
                    "model": model.identifier,
                    "source": _entry_source_label(model, spec_root),
                    "assert": invariant.get("assert"),
                    "enforcement": invariant.get("enforcement"),
                    "raises": invariant.get("raises"),
                }
            )
    return invariants


def build_test_manifest(catalog: Catalog, spec_root: Path) -> dict[str, object]:
    scenarios = _scenario_manifest(catalog, spec_root)
    invariants = _invariant_manifest(catalog, spec_root)
    return {
        "counts": {
            "scenarios": len(scenarios),
            "invariants": len(invariants),
        },
        "scenarios": scenarios,
        "invariants": invariants,
    }


def load_test_manifest_schema() -> dict[str, object]:
    return json.loads(_TEST_MANIFEST_SCHEMA_PATH.read_text())


def _render_scenarios_page(catalog: Catalog, spec_root: Path) -> str:
    grouped: dict[str, list[dict[str, object]]] = {}
    for scenario in _scenario_manifest(catalog, spec_root):
        grouped.setdefault(str(scenario["usecase"]), []).append(scenario)

    lines = [
        "---",
        "title: Scenarios",
        "layout: default",
        "---",
        "",
        "# Scenarios",
        "",
        "Generated Given/When/Then suites grouped by use case.",
        "",
    ]
    if not grouped:
        lines.extend(["No scenarios were found in the catalog.", ""])
        return "\n".join(lines) + "\n"

    for usecase_id in sorted(grouped):
        usecase_entry = catalog.resolve("usecase", usecase_id)
        usecase_name = (
            usecase_entry.data.get("name", usecase_id) if usecase_entry else usecase_id
        )
        lines.extend([f"## {usecase_name}", ""])
        if usecase_entry is not None:
            lines.append(f"`{usecase_entry.identifier}`")
            lines.append("")
        for scenario in sorted(grouped[usecase_id], key=lambda item: str(item["id"])):
            name = str(scenario["name"])
            description = str(scenario["description"])
            lines.extend([f"### {name}", ""])
            lines.append(f"`{scenario['id']}`  *(source: `{scenario['source']}`)*")
            lines.append("")
            if description:
                lines.extend([description, ""])
            tags = scenario.get("tags")
            if isinstance(tags, list) and tags:
                lines.extend([f"Tags: {', '.join(tags)}", ""])
            given = scenario.get("given") or []
            if isinstance(given, list) and given:
                lines.extend(["#### Given", ""])
                for clause in given:
                    lines.extend(_yaml_block(clause))
            when = scenario.get("when")
            if when is not None:
                lines.extend(["#### When", ""])
                lines.extend(_yaml_block(when))
            then = scenario.get("then") or []
            if isinstance(then, list) and then:
                lines.extend(["#### Then", ""])
                for clause in then:
                    lines.extend(_yaml_block(clause))
    return "\n".join(lines) + "\n"


def _render_invariants_page(catalog: Catalog, spec_root: Path) -> str:
    lines = [
        "---",
        "title: Invariants",
        "layout: default",
        "---",
        "",
        "# Invariants",
        "",
        "Generated correctness checks derived from model invariants.",
        "",
    ]

    grouped: dict[str, list[dict[str, object]]] = {}
    for invariant in _invariant_manifest(catalog, spec_root):
        grouped.setdefault(str(invariant["model"]), []).append(invariant)

    found = False
    for model in sorted(catalog.iter_kind("model"), key=lambda entry: entry.identifier):
        invariants = grouped.get(model.identifier, [])
        if not invariants:
            continue
        found = True
        model_name = model.data.get("name", model.identifier)
        lines.extend([f"## {model_name}", ""])
        lines.append(
            f"`{model.identifier}`  *({_entry_source_label(model, spec_root)})*"
        )
        lines.append("")
        for invariant in invariants:
            identifier = str(invariant["id"])
            name = str(invariant["name"])
            description = str(invariant["description"])
            lines.extend([f"### {name}", ""])
            lines.append(f"`{identifier}`")
            lines.append("")
            if description:
                lines.extend([description, ""])
            enforcement = invariant.get("enforcement")
            if enforcement is not None:
                lines.extend(["Enforcement:", ""])
                lines.extend(_yaml_block(enforcement))
            raises = invariant.get("raises")
            if raises is not None:
                lines.extend([f"Raises: `{raises}`", ""])
            assertion = invariant.get("assert")
            if assertion is not None:
                lines.extend(["Assertion:", ""])
                lines.extend(_yaml_block(assertion))
    if not found:
        lines.extend(["No model invariants were found in the catalog.", ""])
    return "\n".join(lines) + "\n"


def render_test_plan(
    catalog: Catalog,
    spec_root: Path,
    out_dir: Path,
    *,
    title: str = "Generated Test Plan",
    clean: bool = False,
) -> None:
    if clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tests_dir = out_dir / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)

    scenario_count = len(tuple(catalog.iter_kind("scenario")))
    invariant_count = sum(
        len(model.data.get("invariants") or [])
        for model in catalog.iter_kind("model")
        if isinstance(model.data.get("invariants"), list)
    )

    (tests_dir / "scenarios.md").write_text(_render_scenarios_page(catalog, spec_root))
    (tests_dir / "invariants.md").write_text(
        _render_invariants_page(catalog, spec_root)
    )

    index_lines = [
        "---",
        f"title: {title}",
        "layout: default",
        "---",
        "",
        f"# {title}",
        "",
        "Generated test surfaces and correctness checks derived from the validated DeepThought catalog.",
        "",
        f"- [Scenarios](./tests/scenarios.md) ({scenario_count} scenarios)",
        f"- [Invariants](./tests/invariants.md) ({invariant_count} invariants)",
        "",
    ]
    (out_dir / "index.md").write_text("\n".join(index_lines) + "\n")

    config_path = out_dir / "_config.yml"
    if not config_path.exists():
        config_path.write_text(_jekyll_config(title, "DeepThought generated test plan"))


def render_test_manifest(catalog: Catalog, spec_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = build_test_manifest(catalog, spec_root)
    (out_dir / "test_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


def _typescript_test_import(runner: str) -> str:
    if runner == "jest":
        return 'import { describe, test } from "@jest/globals";'
    return 'import { describe, test } from "vitest";'


def _go_test_name(prefix: str, value: str) -> str:
    segments = [segment for segment in re.split(r"[^0-9a-zA-Z]+", value) if segment]
    if not segments:
        suffix = "Generated"
    else:
        suffix = "".join(segment[:1].upper() + segment[1:] for segment in segments)
    if suffix and suffix[0].isdigit():
        suffix = f"_{suffix}"
    return f"{prefix}{suffix}"


def _typescript_types_module() -> str:
    lines = [
        "// Shared helper types for generated DeepThought TypeScript stubs.",
        "",
        "export type JsonValue =",
        "  | null",
        "  | boolean",
        "  | number",
        "  | string",
        "  | JsonValue[]",
        "  | { [key: string]: JsonValue };",
        "",
        "export interface GeneratedScenario {",
        "  source: string;",
        "  given: JsonValue[];",
        "  when: JsonValue | null;",
        "  then: JsonValue[];",
        "}",
        "",
        "export interface GeneratedInvariant {",
        "  model: string;",
        "  source: string;",
        "  assertion: JsonValue | null;",
        "  enforcement: JsonValue | null;",
        "  raises: string | null;",
        "}",
        "",
    ]
    return "\n".join(lines)


def _go_json_string(value: object) -> str:
    return f"`{json.dumps(value, separators=(',', ':'))}`"


def _go_string_list(values: object) -> str:
    if not isinstance(values, list) or not values:
        return "nil"
    rendered = ", ".join(_go_json_string(item) for item in values)
    return f"[]string{{{rendered}}}"


def _go_optional_json_string(value: object) -> str:
    if value is None:
        return "nil"
    return f"stringPtr({_go_json_string(value)})"


def _go_optional_string(value: object) -> str:
    if value is None:
        return "nil"
    return f"stringPtr({json.dumps(str(value))})"


def _go_types_module() -> str:
    lines = [
        "// Shared helper types for generated DeepThought Go stubs.",
        "package generatedtests",
        "",
        "type GeneratedScenario struct {",
        "\tSource string",
        "\tGiven  []string",
        "\tWhen   *string",
        "\tThen   []string",
        "}",
        "",
        "type GeneratedInvariant struct {",
        "\tModel       string",
        "\tSource      string",
        "\tAssertion   *string",
        "\tEnforcement *string",
        "\tRaises      *string",
        "}",
        "",
        "func stringPtr(value string) *string {",
        "\treturn &value",
        "}",
        "",
    ]
    return "\n".join(lines)


def _rust_string(value: object) -> str:
    return f"r#{json.dumps(str(value))}#.to_string()"


def _rust_json_string(value: object) -> str:
    return f"r#{json.dumps(value, separators=(',', ':'))}#.to_string()"


def _rust_string_list(values: object) -> str:
    if not isinstance(values, list) or not values:
        return "Vec::new()"
    rendered = ", ".join(_rust_json_string(item) for item in values)
    return f"vec![{rendered}]"


def _rust_optional_json_string(value: object) -> str:
    if value is None:
        return "None"
    return f"Some({_rust_json_string(value)})"


def _rust_optional_string(value: object) -> str:
    if value is None:
        return "None"
    return f"Some({_rust_string(value)})"


def _rust_types_module() -> str:
    lines = [
        "// Shared helper types for generated DeepThought Rust stubs.",
        "#[derive(Debug, Clone)]",
        "pub struct GeneratedScenario {",
        "    pub source: String,",
        "    pub given: Vec<String>,",
        "    pub when: Option<String>,",
        "    pub then: Vec<String>,",
        "}",
        "",
        "#[derive(Debug, Clone)]",
        "pub struct GeneratedInvariant {",
        "    pub model: String,",
        "    pub source: String,",
        "    pub assertion: Option<String>,",
        "    pub enforcement: Option<String>,",
        "    pub raises: Option<String>,",
        "}",
        "",
    ]
    return "\n".join(lines)


def _rust_cargo_toml() -> str:
    return "\n".join(
        [
            "[package]",
            'name = "generated-deepthought-tests"',
            'version = "0.1.0"',
            'edition = "2021"',
            "",
        ]
    )


def _rust_lib_rs(module_names: list[str]) -> str:
    lines = ["// Generated crate root for DeepThought Rust test scaffolds.", ""]
    for module_name in module_names:
        lines.append(f"mod {module_name};")
    lines.append("")
    return "\n".join(lines)


def _python_payloads_module() -> str:
    lines = [
        '"""Shared helper types for generated DeepThought unittest stubs."""',
        "",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from typing import Any",
        "",
        "",
        "@dataclass(frozen=True)",
        "class GeneratedScenario:",
        "    source: str",
        "    given: list[Any]",
        "    when: Any | None",
        "    then: list[Any]",
        "",
        "",
        "@dataclass(frozen=True)",
        "class GeneratedInvariant:",
        "    model: str",
        "    source: str",
        "    assertion: Any | None",
        "    enforcement: Any | None",
        "    raises: str | None",
        "",
    ]
    return "\n".join(lines)


def render_typescript_suite(
    catalog: Catalog,
    spec_root: Path,
    out_dir: Path,
    *,
    runner: str = "vitest",
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    suite_dir = out_dir / "generated_typescript"
    suite_dir.mkdir(parents=True, exist_ok=True)
    (suite_dir / "types.ts").write_text(_typescript_types_module())

    manifest = build_test_manifest(catalog, spec_root)
    import_line = _typescript_test_import(runner)
    scenario_groups: dict[str, list[dict[str, object]]] = {}
    for scenario in manifest["scenarios"]:
        scenario_groups.setdefault(str(scenario["usecase"]), []).append(scenario)

    if scenario_groups:
        for usecase_id in sorted(scenario_groups):
            lines = [
                f"// Generated TypeScript {runner} stubs from a validated DeepThought catalog.",
                import_line,
                'import type { GeneratedScenario } from "./types";',
                "",
                f"describe.skip({json.dumps(usecase_id)}, () => {{",
            ]
            for entry in sorted(
                scenario_groups[usecase_id], key=lambda item: str(item["id"])
            ):
                payload = {
                    "source": entry["source"],
                    "given": entry.get("given") or [],
                    "when": entry.get("when"),
                    "then": entry.get("then") or [],
                }
                lines.extend(
                    [
                        f"  test.skip({json.dumps(str(entry['name']))}, () => {{",
                        f"    const scenario: GeneratedScenario = {json.dumps(payload, indent=2)};",
                        "    void scenario;",
                        "    throw new Error('Generated scenario stub: connect this to a concrete use-case runner');",
                        "  });",
                        "",
                    ]
                )
            lines.append("});")
            lines.append("")
            file_name = f"{_code_identifier(usecase_id)}.test.ts"
            (suite_dir / file_name).write_text("\n".join(lines))
    else:
        (suite_dir / "unassigned.test.ts").write_text(
            "\n".join(
                [
                    f"// Generated TypeScript {runner} stubs from a validated DeepThought catalog.",
                    import_line,
                    'import type { GeneratedScenario } from "./types";',
                    "",
                    "describe.skip('unassigned', () => {",
                    "  test.skip('no scenarios declared', () => {",
                    "    const scenario: GeneratedScenario | null = null;",
                    "    void scenario;",
                    "    throw new Error('No scenarios were present in the catalog');",
                    "  });",
                    "});",
                    "",
                ]
            )
        )

    lines = [
        f"// Generated TypeScript {runner} invariant stubs from a validated DeepThought catalog.",
        import_line,
        'import type { GeneratedInvariant } from "./types";',
        "",
        "describe.skip('invariants', () => {",
    ]
    if manifest["invariants"]:
        for invariant in manifest["invariants"]:
            payload = {
                "model": invariant["model"],
                "source": invariant["source"],
                "assertion": invariant.get("assert"),
                "enforcement": invariant.get("enforcement"),
                "raises": invariant.get("raises"),
            }
            lines.extend(
                [
                    f"  test.skip({json.dumps(str(invariant['name']))}, () => {{",
                    f"    const invariant: GeneratedInvariant = {json.dumps(payload, indent=2)};",
                    "    void invariant;",
                    "    throw new Error('Generated invariant stub: connect this to a concrete model validator');",
                    "  });",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "  test.skip('no invariants declared', () => {",
                "    const invariant: GeneratedInvariant | null = null;",
                "    void invariant;",
                "    throw new Error('No invariants were present in the catalog');",
                "  });",
                "",
            ]
        )
    lines.append("});")
    lines.append("")
    (suite_dir / "invariants.test.ts").write_text("\n".join(lines))


def render_go_suite(catalog: Catalog, spec_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    suite_dir = out_dir / "generated_go"
    suite_dir.mkdir(parents=True, exist_ok=True)
    (suite_dir / "types.go").write_text(_go_types_module())

    manifest = build_test_manifest(catalog, spec_root)
    scenario_groups: dict[str, list[dict[str, object]]] = {}
    for scenario in manifest["scenarios"]:
        scenario_groups.setdefault(str(scenario["usecase"]), []).append(scenario)

    if scenario_groups:
        for usecase_id in sorted(scenario_groups):
            lines = [
                "// Generated Go test stubs from a validated DeepThought catalog.",
                "package generatedtests",
                "",
                'import "testing"',
                "",
            ]
            for entry in sorted(
                scenario_groups[usecase_id], key=lambda item: str(item["id"])
            ):
                payload = {
                    "source": entry["source"],
                    "given": entry.get("given") or [],
                    "when": entry.get("when"),
                    "then": entry.get("then") or [],
                }
                lines.extend(
                    [
                        f"func {_go_test_name('TestScenario', str(entry['id']))}(t *testing.T) {{",
                        "\tscenario := GeneratedScenario{",
                        f"\t\tSource: {json.dumps(str(payload['source']))},",
                        f"\t\tGiven: {_go_string_list(payload['given'])},",
                        f"\t\tWhen: {_go_optional_json_string(payload['when'])},",
                        f"\t\tThen: {_go_string_list(payload['then'])},",
                        "\t}",
                        "\t_ = scenario",
                        '\tt.Skip("Generated scenario stub: connect this to a concrete use-case runner")',
                        "}",
                        "",
                    ]
                )
            file_name = f"{_code_identifier(usecase_id)}_test.go"
            (suite_dir / file_name).write_text("\n".join(lines))
    else:
        (suite_dir / "unassigned_test.go").write_text(
            "\n".join(
                [
                    "// Generated Go test stubs from a validated DeepThought catalog.",
                    "package generatedtests",
                    "",
                    'import "testing"',
                    "",
                    "func TestNoScenariosDeclared(t *testing.T) {",
                    "\tscenario := (*GeneratedScenario)(nil)",
                    "\t_ = scenario",
                    '\tt.Skip("No scenarios were present in the catalog")',
                    "}",
                    "",
                ]
            )
        )

    lines = [
        "// Generated Go invariant stubs from a validated DeepThought catalog.",
        "package generatedtests",
        "",
        'import "testing"',
        "",
    ]
    if manifest["invariants"]:
        for invariant in manifest["invariants"]:
            payload = {
                "model": invariant["model"],
                "source": invariant["source"],
                "assertion": invariant.get("assert"),
                "enforcement": invariant.get("enforcement"),
                "raises": invariant.get("raises"),
            }
            lines.extend(
                [
                    f"func {_go_test_name('TestInvariant', f'{invariant['model']}_{invariant['id']}')}(t *testing.T) {{",
                    "\tinvariant := GeneratedInvariant{",
                    f"\t\tModel: {json.dumps(str(payload['model']))},",
                    f"\t\tSource: {json.dumps(str(payload['source']))},",
                    f"\t\tAssertion: {_go_optional_json_string(payload['assertion'])},",
                    f"\t\tEnforcement: {_go_optional_json_string(payload['enforcement'])},",
                    f"\t\tRaises: {_go_optional_string(payload['raises'])},",
                    "\t}",
                    "\t_ = invariant",
                    '\tt.Skip("Generated invariant stub: connect this to a concrete model validator")',
                    "}",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "func TestNoInvariantsDeclared(t *testing.T) {",
                "\tinvariant := (*GeneratedInvariant)(nil)",
                "\t_ = invariant",
                '\tt.Skip("No invariants were present in the catalog")',
                "}",
                "",
            ]
        )
    (suite_dir / "invariants_test.go").write_text("\n".join(lines))


def render_rust_suite(catalog: Catalog, spec_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    suite_dir = out_dir / "generated_rust"
    suite_dir.mkdir(parents=True, exist_ok=True)
    src_dir = suite_dir / "src"
    src_dir.mkdir(parents=True, exist_ok=True)
    (suite_dir / "Cargo.toml").write_text(_rust_cargo_toml())
    (src_dir / "types.rs").write_text(_rust_types_module())

    manifest = build_test_manifest(catalog, spec_root)
    scenario_groups: dict[str, list[dict[str, object]]] = {}
    for scenario in manifest["scenarios"]:
        scenario_groups.setdefault(str(scenario["usecase"]), []).append(scenario)
    module_names = ["types"]

    if scenario_groups:
        for usecase_id in sorted(scenario_groups):
            module_name = _code_identifier(usecase_id)
            module_names.append(module_name)
            lines = [
                "// Generated Rust test stubs from a validated DeepThought catalog.",
                "use crate::types::GeneratedScenario;",
                "",
            ]
            for entry in sorted(
                scenario_groups[usecase_id], key=lambda item: str(item["id"])
            ):
                payload = {
                    "source": entry["source"],
                    "given": entry.get("given") or [],
                    "when": entry.get("when"),
                    "then": entry.get("then") or [],
                }
                lines.extend(
                    [
                        "#[test]",
                        "#[ignore = \"Generated scenario stub: connect this to a concrete use-case runner\"]",
                        f"fn {_code_identifier(str(entry['id']))}() {{",
                        "    let scenario = GeneratedScenario {",
                        f"        source: {_rust_string(payload['source'])},",
                        f"        given: {_rust_string_list(payload['given'])},",
                        f"        when: {_rust_optional_json_string(payload['when'])},",
                        f"        then: {_rust_string_list(payload['then'])},",
                        "    };",
                        "    let _ = scenario;",
                        "    unreachable!(\"Generated scenario stub\");",
                        "}",
                        "",
                    ]
                )
            file_name = f"{module_name}.rs"
            (src_dir / file_name).write_text("\n".join(lines))
    else:
        module_names.append("unassigned")
        (src_dir / "unassigned.rs").write_text(
            "\n".join(
                [
                    "// Generated Rust test stubs from a validated DeepThought catalog.",
                    "use crate::types::GeneratedScenario;",
                    "",
                    "#[test]",
                    "#[ignore = \"No scenarios were present in the catalog\"]",
                    "fn no_scenarios_declared() {",
                    "    let scenario: Option<GeneratedScenario> = None;",
                    "    let _ = scenario;",
                    "    unreachable!(\"No scenarios were present in the catalog\");",
                    "}",
                    "",
                ]
            )
        )

    module_names.append("invariants")
    lines = [
        "// Generated Rust invariant stubs from a validated DeepThought catalog.",
        "use crate::types::GeneratedInvariant;",
        "",
    ]
    if manifest["invariants"]:
        for invariant in manifest["invariants"]:
            payload = {
                "model": invariant["model"],
                "source": invariant["source"],
                "assertion": invariant.get("assert"),
                "enforcement": invariant.get("enforcement"),
                "raises": invariant.get("raises"),
            }
            lines.extend(
                [
                    "#[test]",
                    "#[ignore = \"Generated invariant stub: connect this to a concrete model validator\"]",
                    f"fn {_code_identifier(f'{invariant['model']}_{invariant['id']}')}() {{",
                    "    let invariant = GeneratedInvariant {",
                    f"        model: {_rust_string(payload['model'])},",
                    f"        source: {_rust_string(payload['source'])},",
                    f"        assertion: {_rust_optional_json_string(payload['assertion'])},",
                    f"        enforcement: {_rust_optional_json_string(payload['enforcement'])},",
                    f"        raises: {_rust_optional_string(payload['raises'])},",
                    "    };",
                    "    let _ = invariant;",
                    "    unreachable!(\"Generated invariant stub\");",
                    "}",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "#[test]",
                "#[ignore = \"No invariants were present in the catalog\"]",
                "fn no_invariants_declared() {",
                "    let invariant: Option<GeneratedInvariant> = None;",
                "    let _ = invariant;",
                "    unreachable!(\"No invariants were present in the catalog\");",
                "}",
                "",
            ]
        )
    (src_dir / "invariants.rs").write_text("\n".join(lines))
    (src_dir / "lib.rs").write_text(_rust_lib_rs(module_names))


def _quoted_yaml(value: object) -> str:
    return yaml.safe_dump(value, sort_keys=False).rstrip()


def _unittest_method_block(name: str, body_lines: list[str]) -> list[str]:
    return [f"    def {name}(self):", *[f"        {line}" for line in body_lines], ""]


def render_unittest_suite(catalog: Catalog, spec_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    suite_dir = out_dir / "generated_unittest"
    suite_dir.mkdir(parents=True, exist_ok=True)
    (suite_dir / "__init__.py").write_text('"""Generated unittest stubs."""\n')
    (suite_dir / "payloads.py").write_text(_python_payloads_module())

    manifest = build_test_manifest(catalog, spec_root)
    scenario_groups: dict[str, list[dict[str, object]]] = {}
    for scenario in manifest["scenarios"]:
        scenario_groups.setdefault(str(scenario["usecase"]), []).append(scenario)

    if scenario_groups:
        for usecase_id in sorted(scenario_groups):
            lines = [
                '"""Generated unittest stubs from a validated DeepThought catalog."""',
                "",
                "from generated_unittest.payloads import GeneratedScenario",
                "import unittest",
                "",
                "",
                "class GeneratedScenarioTests(unittest.TestCase):",
            ]
            for entry in sorted(
                scenario_groups[usecase_id], key=lambda item: str(item["id"])
            ):
                payload = {
                    "source": entry["source"],
                    "given": entry.get("given") or [],
                    "when": entry.get("when"),
                    "then": entry.get("then") or [],
                }
                body_lines = [
                    f'"""Scenario: {entry["name"]}\n\n{_quoted_yaml(payload)}\n"""',
                    "scenario = GeneratedScenario(",
                    f"    source={payload['source']!r},",
                    f"    given={payload['given']!r},",
                    f"    when={payload['when']!r},",
                    f"    then={payload['then']!r},",
                    ")",
                    "self.assertIsNotNone(scenario)",
                    'self.skipTest("Generated scenario stub: connect this to a concrete use-case runner")',
                ]
                lines.extend(
                    _unittest_method_block(
                        f"test_scenario_{_code_identifier(str(entry['id']))}",
                        body_lines,
                    )
                )
            lines.extend(
                [
                    "",
                    'if __name__ == "__main__":',
                    "    unittest.main()",
                    "",
                ]
            )
            file_name = f"test_usecase_{_code_identifier(usecase_id)}.py"
            (suite_dir / file_name).write_text("\n".join(lines))
    else:
        lines = [
            '"""Generated unittest stubs from a validated DeepThought catalog."""',
            "",
            "from generated_unittest.payloads import GeneratedScenario",
            "import unittest",
            "",
            "",
            "class GeneratedScenarioTests(unittest.TestCase):",
        ]
        lines.extend(
            _unittest_method_block(
                "test_no_scenarios_declared",
                [
                    "scenario = None",
                    "self.assertIsNone(scenario)",
                    'self.skipTest("No scenarios were present in the catalog")',
                ],
            )
        )
        lines.extend(
            [
                "",
                'if __name__ == "__main__":',
                "    unittest.main()",
                "",
            ]
        )
        (suite_dir / "test_usecase_unassigned.py").write_text("\n".join(lines))

    lines = [
        '"""Generated unittest stubs from a validated DeepThought catalog."""',
        "",
        "from generated_unittest.payloads import GeneratedInvariant",
        "import unittest",
        "",
        "",
        "class GeneratedInvariantTests(unittest.TestCase):",
    ]

    invariant_methods = 0
    for invariant in manifest["invariants"]:
        invariant_methods += 1
        model = str(invariant["model"])
        identifier = str(invariant["id"])
        payload = {
            "model": model,
            "source": invariant["source"],
            "assertion": invariant.get("assert"),
            "enforcement": invariant.get("enforcement"),
            "raises": invariant.get("raises"),
        }
        body_lines = [
            f'"""Invariant: {invariant["name"]}\n\n{_quoted_yaml(payload)}\n"""',
            "invariant = GeneratedInvariant(",
            f"    model={payload['model']!r},",
            f"    source={payload['source']!r},",
            f"    assertion={payload['assertion']!r},",
            f"    enforcement={payload['enforcement']!r},",
            f"    raises={payload['raises']!r},",
            ")",
            "self.assertIsNotNone(invariant)",
            'self.skipTest("Generated invariant stub: connect this to a concrete model validator")',
        ]
        lines.extend(
            _unittest_method_block(
                f"test_invariant_{_code_identifier(model)}_{_code_identifier(identifier)}",
                body_lines,
            )
        )
    if invariant_methods == 0:
        lines.extend(
            _unittest_method_block(
                "test_no_invariants_declared",
                [
                    "invariant = None",
                    "self.assertIsNone(invariant)",
                    'self.skipTest("No invariants were present in the catalog")',
                ],
            )
        )
    lines.extend(
        [
            "",
            'if __name__ == "__main__":',
            "    unittest.main()",
            "",
        ]
    )
    (suite_dir / "test_invariants.py").write_text("\n".join(lines))
