"""
Test ScholarMind query on the real research paper.
"""

from scholarmind import ScholarMind


def test_real_paper_methodology_query():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    results = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "methodology"
    )

    assert len(results) == 1

    assert results[0]["type"] == "methodology"

    assert "Random Forest" in (
        results[0]["label"]
    )


def test_real_paper_dataset_query():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    results = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "dataset"
    )

    assert len(results) == 1

    assert results[0]["type"] == "dataset"

    assert "500 simulated" in (
        results[0]["label"]
    )


def test_real_paper_finding_query():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    results = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "finding"
    )

    assert len(results) == 1

    assert results[0]["type"] == "finding"

    assert "76%" in (
        results[0]["label"]
    )