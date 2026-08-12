"""
Tests for ScholarMind Natural Language Research Assistant.
"""

from scholarmind import ScholarMind


def test_natural_language_methodology():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    results = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "What methodology was used in this research?"
    )

    assert len(results) == 1
    assert results[0]["type"] == "methodology"

    assert "Random Forest" in (
        results[0]["label"]
    )


def test_natural_language_dataset():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    results = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "What dataset was used in this study?"
    )

    assert len(results) == 1
    assert results[0]["type"] == "dataset"

    assert "500 simulated" in (
        results[0]["label"]
    )


def test_natural_language_findings():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    results = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "What were the main findings?"
    )

    assert len(results) == 1
    assert results[0]["type"] == "finding"

    assert "76%" in (
        results[0]["label"]
    )


def test_unknown_question():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    results = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "Tell me something interesting about this paper."
    )

    assert results == []