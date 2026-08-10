"""
Tests for ScholarMind Data Loader
"""

from data_loader import load_research_data


def test_load_research_data():
    papers = load_research_data(
        "../data/sample_research.json"
    )

    assert len(papers) == 1

    paper = papers[0]

    assert paper.title == "AI for Environmental Risk Assessment"
    assert paper.authors == ["ScholarMind Research"]
    assert paper.year == 2026

    assert paper.doi == "10.1234/example.doi"

    assert paper.abstract == (
        "An example research paper for the ScholarMind prototype."
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