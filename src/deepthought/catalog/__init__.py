"""Validated, addressable spec catalog for generators."""

from deepthought.catalog.errors import (
    CatalogError,
    CatalogValidationError,
    DuplicateSpecError,
    UnresolvedReferenceError,
)
from deepthought.catalog.loader import load_catalog
from deepthought.catalog.model import Catalog, SpecEntry

__all__ = [
    "Catalog",
    "CatalogError",
    "CatalogValidationError",
    "DuplicateSpecError",
    "SpecEntry",
    "UnresolvedReferenceError",
    "load_catalog",
]
