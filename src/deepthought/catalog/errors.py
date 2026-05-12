"""Catalog-specific exceptions."""

from __future__ import annotations

from dataclasses import dataclass

from deepthought.validate import ValidationError


class CatalogError(Exception):
    """Base class for catalog failures."""


@dataclass(frozen=True)
class DuplicateSpecError(CatalogError):
    kind: str
    identifier: str
    first_path: str
    second_path: str

    def __str__(self) -> str:
        return (
            f"duplicate {self.kind!r} spec {self.identifier!r}: "
            f"{self.first_path} and {self.second_path}"
        )


class CatalogValidationError(CatalogError):
    """Raised when YAML fails schema validation before catalog loading."""

    def __init__(self, errors: list[ValidationError]):
        self.errors = errors
        summary = f"catalog load failed validation with {len(errors)} error(s)"
        super().__init__(summary)


@dataclass(frozen=True)
class UnresolvedReferenceError(CatalogError):
    owner_kind: str
    owner_id: str
    reference_kind: str
    reference_id: str
    field_name: str

    def __str__(self) -> str:
        return (
            f"{self.owner_kind!r} {self.owner_id!r} references missing "
            f"{self.reference_kind!r} {self.reference_id!r} via {self.field_name!r}"
        )
