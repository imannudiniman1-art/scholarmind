"""
Tests for ScholarMind Research Assistant
"""

from research_assistant import ask_about_paper
from graph import KnowledgeGraph


def build_test_graph():
    graph = KnowledgeGraph()

    graph.add_node(
        "paper_1",
        "paper",
        "AI for Environmental Risk Assessment"
    )

    graph.add_node(
        "methodology_1",
        "methodology",
        "Comparative machine learning analysis"
    )

    graph.add_node(
        "dataset_1",
        "dataset",
        "Environmental Sensor Data"
    )

    graph.add_node(
        "finding_1",
        "finding",
        "AI can support environmental risk assessment."
    )

    graph.add_relationship(
        "paper_1",
        "uses",
        "methodology_1"
    )

    graph.add_relationship(
        "paper_1",
        "uses",
        "dataset_1"
    )

    graph.add_relationship(
        "paper_1",
        "reports",
        "finding_1"
    )

    return graph


def test_ask_about_methodology():
    graph = build_test_graph()

    results = ask_about_paper(
        graph,
        "paper_1",
        "methodology"
    )

    assert len(results) == 1
    assert results[0]["type"] == "methodology"
    assert results[0]["label"] == (
        "Comparative machine learning analysis"
    )


def test_ask_about_dataset():
    graph = build_test_graph()

    results = ask_about_paper(
        graph,
        "paper_1",
        "dataset"
    )

    assert len(results) == 1
    assert results[0]["type"] == "dataset"
    assert results[0]["label"] == (
        "Environmental Sensor Data"
    )


def test_ask_about_finding():
    graph = build_test_graph()

    results = ask_about_paper(
        graph,
        "paper_1",
        "finding"
    )

    assert len(results) == 1
    assert results[0]["type"] == "finding"


def test_unknown_topic():
    graph = build_test_graph()

    results = ask_about_paper(
        graph,
        "paper_1",
        "unknown"
    )

    assert results == []