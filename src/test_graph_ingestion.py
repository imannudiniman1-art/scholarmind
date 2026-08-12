"""
Tests for ScholarMind Knowledge Graph Ingestion.
"""

from data_loader import load_research_data
from graph import KnowledgeGraph
from graph_ingestion import ingest_paper


def test_ingest_real_research_paper():
    papers = load_research_data(
        "../data/research_papers.json"
    )

    paper = papers[0]

    graph = KnowledgeGraph()

    ingest_paper(
        graph,
        paper,
        "zenodo_18707122"
    )

    nodes = graph.get_nodes()

    assert "zenodo_18707122" in nodes

    assert (
        "zenodo_18707122_methodology"
        in nodes
    )

    assert (
        "zenodo_18707122_dataset"
        in nodes
    )

    assert (
        "zenodo_18707122_finding"
        in nodes
    )

    assert (
        "zenodo_18707122_source"
        in nodes
    )


def test_ingest_keywords():
    papers = load_research_data(
        "../data/research_papers.json"
    )

    paper = papers[0]

    graph = KnowledgeGraph()

    ingest_paper(
        graph,
        paper,
        "zenodo_18707122"
    )

    nodes = graph.get_nodes()

    keyword_nodes = [
        node
        for node in nodes.values()
        if node["type"] == "keyword"
    ]

    assert len(keyword_nodes) == len(
        paper.keywords
    )


def test_ingest_relationships():
    papers = load_research_data(
        "../data/research_papers.json"
    )

    paper = papers[0]

    graph = KnowledgeGraph()

    ingest_paper(
        graph,
        paper,
        "zenodo_18707122"
    )

    relationships = graph.get_relationships()

    assert len(relationships) >= 6

    relations = [
        item["relation"]
        for item in relationships
    ]

    assert "uses" in relations
    assert "reports" in relations
    assert "has_keyword" in relations
    assert "has_source" in relations