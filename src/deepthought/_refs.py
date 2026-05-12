"""Reference rewriting for documentation rendering.

The renderer cannot follow deeply mutually recursive schemas without
exhausting the Python stack, so before handing a meta-schema to
``json-schema-for-humans`` we (a) replace every cross-file ``$ref`` with
a description-stub linking to the referenced schema's page and (b) break
same-file cycles by stubbing the back-edges of the local ``$ref`` graph.

Validation of consumer YAML is unaffected -- it operates on the original
schemas with full ``$ref`` resolution. The rewrites here only shape the
documentation surface.
"""

from __future__ import annotations

from typing import Any


def stub_external_refs(node: Any) -> Any:
    """Replace every cross-file ``$ref`` in ``node`` with a description stub.

    Cross-file refs are values like ``"field.meta.yaml"`` or
    ``"field.meta.yaml#/definitions/lifecycleSchema"``. They are replaced
    with a small object carrying a ``title`` and a Markdown ``description``
    that links to the rendered page for the referenced schema.
    """
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and not ref.startswith("#"):
            file_part, _, anchor = ref.partition("#")
            target = file_part.removesuffix(".meta.yaml")
            link = f"./{target}.md"
            anchor_label = ""
            if anchor:
                tail = anchor.rsplit("/", 1)[-1]
                anchor_label = f" ({tail})"
                link += f"#{tail.lower()}"
            display = target.replace("_", " ").title()
            return {
                "title": f"{display}{anchor_label}",
                "description": f"See [{display}]({link}).",
            }
        return {k: stub_external_refs(v) for k, v in node.items()}
    if isinstance(node, list):
        return [stub_external_refs(item) for item in node]
    return node


def _collect_local_refs(node: Any) -> set[str]:
    """All ``#/definitions/<name>`` references reachable from ``node``."""
    out: set[str] = set()
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/definitions/"):
            out.add(ref.removeprefix("#/definitions/"))
        for value in node.values():
            out |= _collect_local_refs(value)
    elif isinstance(node, list):
        for item in node:
            out |= _collect_local_refs(item)
    return out


def _find_back_edges(graph: dict[str, set[str]]) -> set[tuple[str, str]]:
    """DFS over a definition reference graph; return edges that close
    cycles. Stubbing one edge per cycle is sufficient to break the
    recursive rendering loop without losing any individual definition.
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color: dict[str, int] = {}
    back_edges: set[tuple[str, str]] = set()

    def dfs(node: str) -> None:
        color[node] = GRAY
        for child in sorted(graph.get(node, set())):
            c = color.get(child, WHITE)
            if c == GRAY:
                back_edges.add((node, child))
            elif c == WHITE:
                dfs(child)
        color[node] = BLACK

    for name in sorted(graph):
        if color.get(name, WHITE) == WHITE:
            dfs(name)
    return back_edges


def break_internal_cycles(schema: dict) -> dict:
    """Detect cycles among same-file ``definitions`` and stub the back-edges.

    Returns a new schema; the input is not mutated.
    """
    defs = schema.get("definitions") or {}
    if not defs:
        return schema

    graph: dict[str, set[str]] = {
        name: _collect_local_refs(defn) for name, defn in defs.items()
    }
    back_edges = _find_back_edges(graph)
    if not back_edges:
        return schema

    def stub(target: str) -> dict:
        return {
            "title": target,
            "description": (
                f"Recursive reference back to **{target}** -- see the "
                f"`{target}` definition above for the full shape."
            ),
        }

    def walk(node: Any, owner: str) -> Any:
        if isinstance(node, dict):
            ref = node.get("$ref")
            if isinstance(ref, str) and ref.startswith("#/definitions/"):
                target = ref.removeprefix("#/definitions/")
                if (owner, target) in back_edges:
                    return stub(target)
            return {k: walk(v, owner) for k, v in node.items()}
        if isinstance(node, list):
            return [walk(item, owner) for item in node]
        return node

    rewritten = {name: walk(defn, name) for name, defn in defs.items()}
    new_schema = dict(schema)
    new_schema["definitions"] = rewritten
    return new_schema


def prepare_for_rendering(schema: dict) -> dict:
    """Apply both rewrites: external-ref stubbing then cycle-breaking."""
    return break_internal_cycles(stub_external_refs(schema))
