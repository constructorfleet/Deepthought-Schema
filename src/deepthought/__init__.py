"""DeepThought toolkit.

DeepThought is a Documentation-Driven Development specification language.
This package bundles the meta-schemas alongside the tooling that operates
on them: validation as framework infrastructure plus discovered generators
for output-producing workflows such as documentation, tests, code, and
correctness checks. First-party generators ship with the package; future
generators can register through the ``deepthought.generators`` entry-point
group.

Public API:
    from deepthought import validate_directory, load_meta_schemas
    from deepthought.docs import render_reference, render_spec
"""

from deepthought.catalog import Catalog, SpecEntry, load_catalog
from deepthought.meta_schemas import bundled_schemas_dir, load_meta_schemas
from deepthought.validate import (
    ValidationError,
    validate_directory,
    validate_file,
)

__all__ = [
    "Catalog",
    "SpecEntry",
    "ValidationError",
    "bundled_schemas_dir",
    "load_catalog",
    "load_meta_schemas",
    "validate_directory",
    "validate_file",
]

__version__ = "0.1.0"
