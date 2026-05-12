"""Render JSON correctness manifests from a validated DeepThought catalog."""

from __future__ import annotations

import json
from pathlib import Path

from deepthought.catalog import Catalog, SpecEntry


def _entry_source_label(entry: SpecEntry, spec_root: Path) -> str:
    try:
        rel = entry.path.relative_to(spec_root)
    except ValueError:
        rel = entry.path
    source = str(rel)
    if entry.parent_identifier is not None:
        return f"{source}#{entry.parent_identifier}"
    return source


def _scenario_usecase_id(entry: SpecEntry) -> str | None:
    usecase = entry.data.get("usecase")
    if isinstance(usecase, str):
        return usecase
    return entry.parent_identifier


def _normalize_targets(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def _scenario_manifest(catalog: Catalog, spec_root: Path) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for entry in sorted(
        catalog.iter_kind("scenario"), key=lambda item: item.identifier
    ):
        entries.append(
            {
                "id": entry.identifier,
                "name": entry.data.get("name", entry.identifier),
                "usecase": _scenario_usecase_id(entry),
                "tags": entry.data.get("tags") or [],
                "given": entry.data.get("given") or [],
                "when": entry.data.get("when"),
                "then": entry.data.get("then") or [],
                "source": _entry_source_label(entry, spec_root),
            }
        )
    return entries


def _invariant_manifest(catalog: Catalog, spec_root: Path) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for model in sorted(catalog.iter_kind("model"), key=lambda item: item.identifier):
        invariants = model.data.get("invariants")
        if not isinstance(invariants, list):
            continue
        for invariant in invariants:
            if not isinstance(invariant, dict):
                continue
            entries.append(
                {
                    "id": invariant.get("id"),
                    "name": invariant.get("name", invariant.get("id")),
                    "model": model.identifier,
                    "description": invariant.get("description"),
                    "assert": invariant.get("assert"),
                    "enforcement": invariant.get("enforcement"),
                    "raises": invariant.get("raises"),
                    "source": _entry_source_label(model, spec_root),
                }
            )
    return entries


def _permission_rule_manifest(
    catalog: Catalog, spec_root: Path
) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for permission in sorted(
        catalog.iter_kind("permission"), key=lambda item: item.identifier
    ):
        rules = permission.data.get("rules")
        if not isinstance(rules, list):
            continue
        for index, rule in enumerate(rules, start=1):
            if not isinstance(rule, dict):
                continue
            entries.append(
                {
                    "permission": permission.identifier,
                    "permission_set": permission.parent_identifier,
                    "rule_index": index,
                    "effect": rule.get("effect"),
                    "actors": rule.get("actors"),
                    "condition": rule.get("condition"),
                    "description": rule.get("description"),
                    "source": _entry_source_label(permission, spec_root),
                }
            )
    return entries


def _transition_manifest(catalog: Catalog, spec_root: Path) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for state_machine in sorted(
        catalog.iter_kind("state_machine"), key=lambda item: item.identifier
    ):
        transitions = state_machine.data.get("transitions")
        if not isinstance(transitions, list):
            continue
        for transition in transitions:
            if not isinstance(transition, dict):
                continue
            entries.append(
                {
                    "id": transition.get("id"),
                    "name": transition.get("name", transition.get("id")),
                    "state_machine": state_machine.identifier,
                    "target": state_machine.data.get("target"),
                    "description": transition.get("description"),
                    "from": transition.get("from"),
                    "to": transition.get("to"),
                    "via": _normalize_targets(transition.get("via")),
                    "guard": transition.get("guard"),
                    "emits": _normalize_targets(transition.get("emits")),
                    "source": _entry_source_label(state_machine, spec_root),
                }
            )
    return entries


def render_checks_manifest(catalog: Catalog, spec_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    checks_dir = out_dir / "checks"
    checks_dir.mkdir(parents=True, exist_ok=True)

    scenarios = _scenario_manifest(catalog, spec_root)
    invariants = _invariant_manifest(catalog, spec_root)
    permission_rules = _permission_rule_manifest(catalog, spec_root)
    transitions = _transition_manifest(catalog, spec_root)

    payloads = {
        "invariants.json": invariants,
        "permission_rules.json": permission_rules,
        "scenarios.json": scenarios,
        "transitions.json": transitions,
    }
    for file_name, payload in payloads.items():
        (checks_dir / file_name).write_text(json.dumps(payload, indent=2) + "\n")

    index = {
        "counts": {
            "scenarios": len(scenarios),
            "invariants": len(invariants),
            "permission_rules": len(permission_rules),
            "transitions": len(transitions),
        },
        "files": sorted(payloads),
    }
    (out_dir / "index.json").write_text(json.dumps(index, indent=2) + "\n")
