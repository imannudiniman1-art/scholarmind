"""
Tests for ScholarMind Research Module
"""

from research import create_research_paper


def test_create_research_paper():
    paper = create_research_paper(
        title="AI for Environmental Risk Assessment",
        authors=["Researcher"],
        year=2026,
        method="Random Forest",
        dataset="Environmental Sensor Data",
        findings="AI can support environmental risk assessment."
    )

    assert paper.title == "AI for Environmental Risk Assessment"
    assert paper.authors == ["Researcher"]
    assert paper.year == 2026
    assert paper.method == "Random Forest"
    assert paper.dataset == "Environmental Sensor Data"
    assert paper.findings == (
        "AI can support environmental risk assessment."
    )


def test_research_paper_summary():
    paper = create_research_paper(
        title="Knowledge Graph for Research",
        authors=["ScholarMind"],
        year=2026,
        method="Knowledge Graph",
        dataset="Research Data",
        findings="Research knowledge can be connected."
    )

    summary = paper.summary()

    assert summary["title"] == "Knowledge Graph for Research"
    assert summary["method"] == "Knowledge Graph"
    assert summary["dataset"] == "Research Data"