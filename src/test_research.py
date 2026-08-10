"""
Tests for ScholarMind Research Module
"""

from research import create_research_paper


def test_create_research_paper():
    paper = create_research_paper(
        title="AI for Environmental Risk Assessment",
        authors=["ScholarMind Research"],
        year=2026,
        doi="10.1234/example.doi",
        abstract="An example abstract for testing ScholarMind.",
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

    assert paper.title == "AI for Environmental Risk Assessment"
    assert paper.authors == ["ScholarMind Research"]
    assert paper.year == 2026
    assert paper.doi == "10.1234/example.doi"

    assert paper.abstract == (
        "An example abstract for testing ScholarMind."
    )

    assert paper.keywords == [
        "artificial intelligence",
        "environmental risk",
        "machine learning"
    ]

    assert paper.methodology == (
        "Comparative machine learning analysis"
    )

    assert paper.dataset == "Environmental Sensor Data"

    assert paper.findings == (
        "AI can support environmental risk assessment."
    )

    assert paper.source == "ScholarMind Research Dataset"


def test_research_paper_summary():
    paper = create_research_paper(
        title="Knowledge Graph for Research",
        authors=["ScholarMind"],
        year=2026,
        doi="10.1234/knowledge.graph",
        abstract="Research knowledge can be connected.",
        keywords=["knowledge graph", "research"],
        methodology="Knowledge graph modeling",
        dataset="Research Data",
        findings="Research knowledge can be connected.",
        source="ScholarMind"
    )

    summary = paper.summary()

    assert summary["title"] == "Knowledge Graph for Research"
    assert summary["doi"] == "10.1234/knowledge.graph"
    assert summary["methodology"] == "Knowledge graph modeling"
    assert summary["source"] == "ScholarMind"