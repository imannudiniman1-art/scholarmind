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


def test_add_relationship():
    graph = KnowledgeGraph()

    graph.add_node(
        "paper_001",
        "paper",
        "AI Environmental Risk Assessment"
    )

    graph.add_node(
        "method_001",
        "method",
        "Random Forest"
    )

    graph.add_relationship(
        "paper_001",
        "uses",
        "method_001"
    )

    assert graph.count_nodes() == 2
    assert graph.count_relationships() == 1

    relationship = graph.get_relationships()[0]

    assert relationship["source"] == "paper_001"
    assert relationship["relation"] == "uses"
    assert relationship["target"] == "method_001"