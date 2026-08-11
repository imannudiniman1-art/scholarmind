"""
Tests for ScholarMind Research Query Module
"""

from query import search_papers, find_related_knowledge
from graph import KnowledgeGraph
from research import create_research_paper


def test_search_papers():
    paper = create_research_paper(
        title="AI for Environmental Risk Assessment",
        abstract="AI supports environmental risk assessment.",
        keywords=[
            "artificial intelligence",
            "machine learning"
        ],
        methodology="Comparative machine learning analysis",
        findings="AI can support risk assessment."
    )

    results = search_papers(
        [paper],
        "machine learning"
    )

    assert len(results) == 1
    assert results[0].title == (
        "AI for Environmental Risk Assessment"
    )


def test_find_related_knowledge():
    graph = KnowledgeGraph()

    graph.add_node(
        "paper_001",
        "paper",
        "AI for Environmental Risk Assessment"
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

    results = find_related_knowledge(
        graph,
        "paper_001"
    )

    assert len(results) == 3

    labels = [
        item["label"]
        for item in results
    ]

    assert "Comparative machine learning analysis" in labels
    assert "Environmental Sensor Data" in labels
    assert (
        "AI can support environmental risk assessment."
        in labels
    )


def test_find_related_knowledge_by_relation():
    graph = KnowledgeGraph()

    graph.add_node(
        "paper_001",
        "paper",
        "AI Research"
    )

    graph.add_node(
        "methodology_001",
        "methodology",
        "Machine Learning"
    )

    graph.add_node(
        "dataset_001",
        "dataset",
        "Sensor Data"
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

    results = find_related_knowledge(
        graph,
        "paper_001",
        relation="uses"
    )

    assert len(results) == 2

    types = [
        item["type"]
        for item in results
    ]

    assert "methodology" in types
    assert "dataset" in types