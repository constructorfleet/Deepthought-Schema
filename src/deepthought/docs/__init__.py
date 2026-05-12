"""Documentation generation for DeepThought specifications.

Two render modes are exposed:

* :func:`render_reference` -- reference docs for a directory of JSON
  Schemas. Used by the deepthought-schema repo itself to publish the
  language reference.
* :func:`render_spec` -- per-entity domain docs for a directory of YAML
  consumer specs (fields, models, use cases, ...).
"""

from deepthought.docs.render import render_reference, render_spec

__all__ = ["render_reference", "render_spec"]
