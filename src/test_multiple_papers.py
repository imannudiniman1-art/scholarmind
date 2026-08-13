"""
Tests for multiple research papers.
"""

from scholarmind import ScholarMind


def test_multiple_papers_are_loaded():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    assert len(scholar.research_data) == 2


def test_first_paper_is_loaded():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    paper_ids = [
        paper["id"]
        for paper in scholar.research_data
    ]

    assert "zenodo_18707122" in paper_ids


def test_second_paper_is_loaded():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    paper_ids = [
        paper["id"]
        for paper in scholar.research_data
    ]

    assert "zenodo_18276886" in paper_ids