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
    assert paper.year == 2026
    assert paper.method == "Random Forest"
    assert paper.dataset == "Environmental Sensor Data"