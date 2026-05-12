"""Generator discovery for DeepThought CLI subcommands.

Generators are the output-producing surfaces of the toolkit: docs today,
tests/code/checks next. They register themselves on the
``deepthought.generators`` entry-point group so the CLI can enumerate them
without hardcoding each subcommand.
"""

from __future__ import annotations

from importlib.metadata import entry_points
from typing import Protocol, runtime_checkable

ENTRY_POINT_GROUP = "deepthought.generators"


@runtime_checkable
class Generator(Protocol):
    """CLI-pluggable generator surface."""

    name: str
    summary: str

    def register_cli(self, subparsers) -> None:
        """Attach this generator's parser(s) to the top-level CLI."""


def _materialize_generator(candidate) -> Generator:
    if isinstance(candidate, type):
        candidate = candidate()
    if not isinstance(candidate, Generator):
        raise TypeError(
            "deepthought generator entry points must resolve to a Generator "
            "instance or a Generator class"
        )
    return candidate


def _load_builtin_generators() -> list[Generator]:
    from deepthought.generators.checks import ChecksGenerator
    from deepthought.generators.docs import DocsGenerator
    from deepthought.generators.tests import TestsGenerator

    return [ChecksGenerator(), DocsGenerator(), TestsGenerator()]


def discover_generators() -> list[Generator]:
    """Load every registered generator.

    Editable checkouts may not have package metadata yet, so if the entry-point
    group is absent we fall back to the built-in generators.
    """

    loaded: dict[str, Generator] = {}
    candidates = entry_points()
    if hasattr(candidates, "select"):
        matches = candidates.select(group=ENTRY_POINT_GROUP)
    elif isinstance(candidates, list):
        matches = candidates
    else:
        matches = candidates.get(ENTRY_POINT_GROUP, [])
    for item in matches:
        generator = _materialize_generator(item.load())
        loaded[generator.name] = generator
    for generator in _load_builtin_generators():
        loaded.setdefault(generator.name, generator)
    return sorted(loaded.values(), key=lambda generator: generator.name)
