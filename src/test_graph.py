"""
Tests for ScholarMind Knowledge Graph
"""

from graph import KnowledgeGraph


def test_add_node():
    graph = KnowledgeGraph()

    graph.add_node(
        "paper_001",
        "paper",
        "AI Environmental Risk Assessment"
    )

    assert graph.count_nodes() == 1
    assert graph.get_nodes()["paper_001"]["type"] == "paper"


def test_research_relationships():
    graph = KnowledgeGraph()

    graph.add_node(
        "paper_001",
        "paper",
        "AI Environmental Risk Assessment"
    )

    graph.add_node(
        "methodology_001",
        "methodology",
        "Comparative machine learning analysis"
    )

    graph.add_node(
        "dataset_001",
        "dataset",
        "Environmental Sensor Data"
    )

    graph.add_node(
        "finding_001",
        "finding",
        "AI can support environmental risk assessment."
    )

    graph.add_node(
        "source_001",
        "source",
        "ScholarMind Research Dataset"
    )

    graph.add_node(
        "keyword_001",
        "keyword",
        "artificial intelligence"
    )

    graph.add_relationship(
        "paper_001",
        "uses",
        "methodology_001"
    )

    graph.add_relationship(
        "paper_001",
        "uses",
        "dataset_001"
    )

    graph.add_relationship(
        "paper_001",
        "reports",
        "finding_001"
    )

    graph.add_relationship(
        "paper_001",
        "has_source",
        "source_001"
    )

    graph.add_relationship(
        "paper_001",
        "has_keyword",
        "keyword_001"
    )

    assert graph.count_nodes() == 6
    assert graph.count_relationships() == 5


def test_relationship_content():
    graph = KnowledgeGraph()

    graph.add_relationship(
        "paper_001",
        "has_keyword",
        "keyword_001"
    )

    relationship = graph.get_relationships()[0]

    assert relationship["source"] == "paper_001"
    assert relationship["relation"] == "has_keyword"
    assert relationship["target"] == "keyword_001"