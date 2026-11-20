"""Shared helper types for generated DeepThought unittest stubs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class GeneratedScenario:
    source: str
    given: list[Any]
    when: Any | None
    then: list[Any]


@dataclass(frozen=True)
class GeneratedInvariant:
    model: str
    source: str
    assertion: Any | None
    enforcement: Any | None
    raises: str | None
