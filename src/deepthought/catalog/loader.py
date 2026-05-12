"""Validated loading of DeepThought specs into a generator-facing catalog."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Iterable

import yaml

from deepthought.catalog.errors import (
    CatalogValidationError,
    DuplicateSpecError,
    UnresolvedReferenceError,
)
from deepthought.catalog.model import Catalog, SpecEntry
from deepthought.meta_schemas import bundled_schemas_dir, iter_schema_paths, schema_name
from deepthought.validate import _candidate_files, _kind_for_path, validate_directory


def _iter_entities(kind: str, path: Path, data: object) -> Iterable[SpecEntry]:
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                yield SpecEntry(
                    kind=kind,
                    identifier=item["id"],
                    path=path,
                    data=item,
                    source_kind=kind,
                )
        return

    if not isinstance(data, dict) or not isinstance(data.get("id"), str):
        return

    identifier = data["id"]

    if kind == "permission":
        if isinstance(data.get("rules"), list):
            yield SpecEntry(
                kind="permission",
                identifier=identifier,
                path=path,
                data=data,
                source_kind=kind,
            )
            return
        if "actors" in data or "permissions" in data:
            yield SpecEntry(
                kind="permission_set",
                identifier=identifier,
                path=path,
                data=data,
                source_kind=kind,
            )
            actors = data.get("actors") or []
            if isinstance(actors, list):
                for actor in actors:
                    if isinstance(actor, dict) and isinstance(actor.get("id"), str):
                        yield SpecEntry(
                            kind="actor",
                            identifier=actor["id"],
                            path=path,
                            data=actor,
                            source_kind=kind,
                            parent_identifier=identifier,
                        )
            permissions = data.get("permissions") or []
            if isinstance(permissions, list):
                for permission in permissions:
                    if isinstance(permission, dict) and isinstance(
                        permission.get("id"), str
                    ):
                        yield SpecEntry(
                            kind="permission",
                            identifier=permission["id"],
                            path=path,
                            data=permission,
                            source_kind=kind,
                            parent_identifier=identifier,
                        )
            return
        if any(key in data for key in ("anonymous", "extends")):
            yield SpecEntry(
                kind="actor",
                identifier=identifier,
                path=path,
                data=data,
                source_kind=kind,
            )
            return

    yield SpecEntry(
        kind=kind,
        identifier=identifier,
        path=path,
        data=data,
        source_kind=kind,
    )

    if kind == "usecase":
        scenarios = data.get("scenarios") or []
        if isinstance(scenarios, list):
            for scenario in scenarios:
                if isinstance(scenario, dict) and isinstance(scenario.get("id"), str):
                    yield SpecEntry(
                        kind="scenario",
                        identifier=scenario["id"],
                        path=path,
                        data=scenario,
                        source_kind=kind,
                        parent_identifier=identifier,
                    )
    if kind == "model":
        state_machine = data.get("stateMachine")
        if isinstance(state_machine, dict) and isinstance(state_machine.get("id"), str):
            yield SpecEntry(
                kind="state_machine",
                identifier=state_machine["id"],
                path=path,
                data=state_machine,
                source_kind=kind,
                parent_identifier=identifier,
            )


def _normalize_reference_targets(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def _iter_reference_checks(entry: SpecEntry) -> Iterable[tuple[str, str, str]]:
    data = entry.data
    kind = entry.kind

    if kind == "model":
        for field_name in ("fields", "key", "queryable"):
            value = data.get(field_name)
            if value is True:
                continue
            for identifier in _normalize_reference_targets(value):
                yield (field_name, "field", identifier)
        domain = data.get("domain")
        if isinstance(domain, str):
            yield ("domain", "domain", domain)
        for reference in data.get("references") or []:
            if isinstance(reference, dict):
                target = reference.get("target")
                if isinstance(target, str):
                    yield ("references.target", "model", target)

    elif kind == "usecase":
        for field_name in ("input", "output"):
            for identifier in _normalize_reference_targets(data.get(field_name)):
                yield (field_name, "entity", identifier)
        for identifier in _normalize_reference_targets(data.get("permissions")):
            yield ("permissions", "permission", identifier)
        for error_ref in data.get("errors") or []:
            if isinstance(error_ref, str):
                yield ("errors", "error", error_ref)
            elif isinstance(error_ref, dict) and isinstance(
                error_ref.get("error"), str
            ):
                yield ("errors.error", "error", error_ref["error"])
        for emits_ref in data.get("emits") or []:
            if isinstance(emits_ref, str):
                yield ("emits", "event", emits_ref)
            elif isinstance(emits_ref, dict) and isinstance(
                emits_ref.get("event"), str
            ):
                yield ("emits.event", "event", emits_ref["event"])
        domain = data.get("domain")
        if isinstance(domain, str):
            yield ("domain", "domain", domain)
        for scenario in data.get("scenarios") or []:
            if isinstance(scenario, str):
                yield ("scenarios", "scenario", scenario)

    elif kind == "scenario":
        usecase = data.get("usecase")
        if isinstance(usecase, str):
            yield ("usecase", "usecase", usecase)
        given = data.get("given") or []
        if isinstance(given, list):
            for clause in given:
                if not isinstance(clause, dict):
                    continue
                actor = clause.get("actor")
                if isinstance(actor, str):
                    yield ("given.actor", "actor", actor)
                exists = clause.get("exists")
                if isinstance(exists, str):
                    yield ("given.exists", "model", exists)
                model = clause.get("model")
                if isinstance(model, str):
                    yield ("given.model", "model", model)
        when = data.get("when")
        if isinstance(when, dict) and isinstance(when.get("actor"), str):
            yield ("when.actor", "actor", when["actor"])
        then = data.get("then") or []
        if isinstance(then, list):
            for clause in then:
                if not isinstance(clause, dict):
                    continue
                raises = clause.get("raises")
                if isinstance(raises, str):
                    yield ("then.raises", "error", raises)
                emits = clause.get("emits")
                if isinstance(emits, str):
                    yield ("then.emits", "event", emits)
                model = clause.get("model")
                if isinstance(model, str):
                    yield ("then.model", "model", model)

    elif kind == "permission":
        for rule in data.get("rules") or []:
            if not isinstance(rule, dict):
                continue
            actors = rule.get("actors")
            if actors == "any":
                continue
            for identifier in _normalize_reference_targets(actors):
                yield ("rules.actors", "actor", identifier)

    elif kind == "actor":
        for identifier in _normalize_reference_targets(data.get("extends")):
            yield ("extends", "actor", identifier)

    elif kind == "error":
        for identifier in _normalize_reference_targets(data.get("payload")):
            yield ("payload", "entity", identifier)

    elif kind == "event":
        payload = data.get("payload")
        if payload != "none":
            for identifier in _normalize_reference_targets(payload):
                yield ("payload", "entity", identifier)
        aggregate = data.get("aggregate")
        if isinstance(aggregate, str):
            yield ("aggregate", "entity", aggregate)

    elif kind == "state_machine":
        target = data.get("target")
        if isinstance(target, str):
            yield ("target", "model", target)
        for transition in data.get("transitions") or []:
            if isinstance(transition, dict):
                for identifier in _normalize_reference_targets(transition.get("via")):
                    yield ("transitions.via", "usecase", identifier)
                for identifier in _normalize_reference_targets(transition.get("emits")):
                    yield ("transitions.emits", "event", identifier)

    elif kind == "collection":
        model = data.get("model")
        if isinstance(model, str):
            yield ("model", "model", model)


def _entry_satisfies_kind(entry: SpecEntry, expected_kind: str) -> bool:
    if expected_kind == "entity":
        return entry.kind in {"model", "collection"}
    return entry.kind == expected_kind


def _ensure_reference(
    catalog: Catalog,
    owner: SpecEntry,
    field_name: str,
    expected_kind: str,
    identifier: str,
) -> None:
    if expected_kind == "entity":
        for candidate_kind in ("model", "collection"):
            if catalog.resolve(candidate_kind, identifier) is not None:
                return
    elif catalog.resolve(expected_kind, identifier) is not None:
        return
    raise UnresolvedReferenceError(
        owner_kind=owner.kind,
        owner_id=owner.identifier,
        reference_kind=expected_kind,
        reference_id=identifier,
        field_name=field_name,
    )


def _validate_references(catalog: Catalog) -> None:
    for entries in catalog.entries.values():
        for entry in entries.values():
            for field_name, expected_kind, identifier in _iter_reference_checks(entry):
                _ensure_reference(catalog, entry, field_name, expected_kind, identifier)


def load_catalog(root: Path, *, schemas_dir: Path | None = None) -> Catalog:
    """Load every valid DeepThought spec under ``root`` into an addressable catalog."""

    schemas_dir = schemas_dir or bundled_schemas_dir()
    errors = validate_directory(root, schemas_dir=schemas_dir)
    if errors:
        raise CatalogValidationError(errors)

    known_kinds = {schema_name(path) for path in iter_schema_paths(schemas_dir)}
    grouped: dict[str, dict[str, SpecEntry]] = defaultdict(dict)
    for path in _candidate_files(root):
        kind = _kind_for_path(path, root)
        if kind is None or kind not in known_kinds:
            continue
        data = yaml.safe_load(path.read_text())
        for entry in _iter_entities(kind, path, data):
            existing = grouped[entry.kind].get(entry.identifier)
            if existing is not None:
                raise DuplicateSpecError(
                    kind=entry.kind,
                    identifier=entry.identifier,
                    first_path=str(existing.path),
                    second_path=str(entry.path),
                )
            grouped[entry.kind][entry.identifier] = entry

    catalog = Catalog(
        entries={kind: dict(entries) for kind, entries in grouped.items()}
    )
    _validate_references(catalog)
    return catalog
