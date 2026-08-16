#!/usr/bin/env python3
"""Parse ontology artefacts and validate example data against SHACL."""
from pathlib import Path
import json
import sys

from rdflib import Graph
from pyshacl import validate

ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / "ontology" / "strategic-advocacy.ttl"
SHAPES = ROOT / "ontology" / "shapes.ttl"
CONTEXT = ROOT / "ontology" / "context.jsonld"
EXAMPLE = ROOT / "ontology" / "examples" / "minimal-valid.ttl"


def parse_rdf(path: Path, fmt: str = "turtle") -> Graph:
    graph = Graph()
    graph.parse(path, format=fmt)
    print(f"parsed {path.relative_to(ROOT)}: {len(graph)} triples")
    return graph


def main() -> int:
    ontology_graph = parse_rdf(ONTOLOGY)
    shapes_graph = parse_rdf(SHAPES)
    data_graph = parse_rdf(EXAMPLE)

    with CONTEXT.open(encoding="utf-8") as handle:
        document = json.load(handle)
    if "@context" not in document:
        raise ValueError("ontology/context.jsonld must contain @context")
    print("parsed ontology/context.jsonld: JSON context present")

    conforms, _, report = validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        ont_graph=ontology_graph,
        inference="rdfs",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
    )
    print(report)
    if not conforms:
        print("SHACL validation failed", file=sys.stderr)
        return 1
    print("SHACL validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
