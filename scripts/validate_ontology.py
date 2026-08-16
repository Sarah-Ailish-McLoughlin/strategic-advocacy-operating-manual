#!/usr/bin/env python3
"""Parse ontology artefacts and test positive and negative SHACL fixtures."""
from pathlib import Path
import json
import sys

from rdflib import Graph
from pyshacl import validate

ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / "ontology" / "strategic-advocacy.ttl"
SHAPES = ROOT / "ontology" / "shapes.ttl"
CONTEXT = ROOT / "ontology" / "context.jsonld"
VALID_EXAMPLE = ROOT / "ontology" / "examples" / "minimal-valid.ttl"
INVALID_EXAMPLE = ROOT / "ontology" / "examples" / "invalid-missing-goal.ttl"


def parse_rdf(path: Path, fmt: str = "turtle") -> Graph:
    graph = Graph()
    graph.parse(path, format=fmt)
    print(f"parsed {path.relative_to(ROOT)}: {len(graph)} triples")
    return graph


def run_shacl(data_graph: Graph, shapes_graph: Graph, ontology_graph: Graph):
    return validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        ont_graph=ontology_graph,
        inference="rdfs",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
    )


def main() -> int:
    ontology_graph = parse_rdf(ONTOLOGY)
    shapes_graph = parse_rdf(SHAPES)

    with CONTEXT.open(encoding="utf-8") as handle:
        document = json.load(handle)
    if "@context" not in document:
        raise ValueError("ontology/context.jsonld must contain @context")
    print("parsed ontology/context.jsonld: JSON context present")

    valid_graph = parse_rdf(VALID_EXAMPLE)
    valid_conforms, _, valid_report = run_shacl(valid_graph, shapes_graph, ontology_graph)
    print(valid_report)
    if not valid_conforms:
        print("Expected valid fixture to conform, but it failed", file=sys.stderr)
        return 1
    print("positive SHACL fixture passed")

    invalid_graph = parse_rdf(INVALID_EXAMPLE)
    invalid_conforms, _, invalid_report = run_shacl(invalid_graph, shapes_graph, ontology_graph)
    print(invalid_report)
    if invalid_conforms:
        print("Expected invalid fixture to fail, but it conformed", file=sys.stderr)
        return 1
    print("negative SHACL fixture failed as expected")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
