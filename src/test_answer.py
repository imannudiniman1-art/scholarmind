"""
Tests for ScholarMind Answer Module
"""

from answer import answer_question
from graph import KnowledgeGraph
from research import create_research_paper


def build_test_data():
    paper = create_research_paper(
        title="AI for Environmental Risk Assessment",
        authors=["ScholarMind Research"],
        year=2026,
        doi="10.1234/example.doi",
        abstract="AI supports environmental risk assessment.",
        keywords=[
            "artificial intelligence",
            "environmental risk",
            "machine learning"
        ],
        methodology="Comparative machine learning analysis",
        dataset="Environmental Sensor Data",
        findings="AI can support environmental risk assessment.",
        source="ScholarMind Research Dataset"
    )

    graph = KnowledgeGraph()

    graph.add_node(
        "paper_1",
        "paper",
        paper.title
    )

    graph.add_node(
        "methodology_1",
        "methodology",
        paper.methodology
    )

    graph.add_node(
        "dataset_1",
        "dataset",
        paper.dataset
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

    return [paper], graph


def test_answer_question():
    papers, graph = build_test_data()

    answer = answer_question(
        papers,
        graph,
        "machine learning"
    )

    assert answer["question"] == "machine learning"

    assert len(answer["papers"]) == 1

    assert (
        answer["papers"][0]["title"]
        == "AI for Environmental Risk Assessment"
    )

    assert len(answer["related_knowledge"]) == 2


def test_answer_contains_research_metadata():
    papers, graph = build_test_data()

    answer = answer_question(
        papers,
        graph,
        "environmental risk"
    )

    paper = answer["papers"][0]

    assert paper["authors"] == [
        "ScholarMind Research"
    ]

    assert paper["year"] == 2026

    assert paper["doi"] == (
        "10.1234/example.doi"
    )