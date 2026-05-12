"""In-memory catalog model for validated DeepThought specs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping


@dataclass(frozen=True)
class SpecEntry:
    """A single addressable spec item in the catalog."""

    kind: str
    identifier: str
    path: Path
    data: dict
    source_kind: str
    parent_identifier: str | None = None


@dataclass(frozen=True)
class Catalog:
    """Validated specs keyed by kind and identifier."""

    entries: Mapping[str, Mapping[str, SpecEntry]]

    def iter_kind(self, kind: str) -> Iterable[SpecEntry]:
        return self.entries.get(kind, {}).values()

    def resolve(self, kind: str, identifier: str) -> SpecEntry | None:
        return self.entries.get(kind, {}).get(identifier)

    def require(self, kind: str, identifier: str) -> SpecEntry:
        entry = self.resolve(kind, identifier)
        if entry is None:
            raise KeyError(f"unknown {kind!r} spec {identifier!r}")
        return entry

    @property
    def kinds(self) -> tuple[str, ...]:
        return tuple(sorted(self.entries))
