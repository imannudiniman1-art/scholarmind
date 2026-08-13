"""
Tests for ScholarMind Cross-Paper Retrieval.
"""

from cross_paper import search_across_papers


def test_search_across_papers_ai():
    papers = [
        {
            "id": "paper_1",
            "title": "AI and Geophysical Sensing",
            "abstract": "Artificial intelligence for environmental risk.",
            "methodology": "Random Forest classification.",
            "dataset": "Simulated geophysical signals.",
            "findings": "Environmental risk classification.",
            "source": "Zenodo"
        },
        {
            "id": "paper_2",
            "title": "AI and Satellite Infrastructure",
            "abstract": "Artificial intelligence for environmental sustainability.",
            "methodology": "Artificial neural network.",
            "dataset": "Simulated environmental data.",
            "findings": "Environmental risk prediction.",
            "source": "Zenodo"
        }
    ]

    results = search_across_papers(
        papers,
        "artificial intelligence"
    )

    assert len(results) == 2


def test_search_across_papers_satellite():
    papers = [
        {
            "id": "paper_1",
            "title": "AI and Geophysical Sensing",
            "abstract": "Artificial intelligence for environmental risk.",
            "methodology": "Random Forest classification.",
            "dataset": "Simulated geophysical signals.",
            "findings": "Environmental risk classification.",
            "source": "Zenodo"
        },
        {
            "id": "paper_2",
            "title": "AI and Satellite Infrastructure",
            "abstract": "Artificial intelligence and satellite infrastructure.",
            "methodology": "Artificial neural network.",
            "dataset": "Simulated environmental data.",
            "findings": "Environmental risk prediction.",
            "source": "Zenodo"
        }
    ]

    results = search_across_papers(
        papers,
        "satellite"
    )

    assert len(results) == 1
    assert results[0]["id"] == "paper_2"


def test_search_across_papers_no_match():
    papers = [
        {
            "id": "paper_1",
            "title": "AI Research",
            "abstract": "Environmental research.",
            "methodology": "Random Forest.",
            "dataset": "Simulated data.",
            "findings": "Risk classification.",
            "source": "Zenodo"
        }
    ]

    results = search_across_papers(
        papers,
        "quantum computing"
    )

    assert results == []


def test_empty_keyword():
    papers = [
        {
            "id": "paper_1",
            "title": "AI Research"
        }
    ]

    results = search_across_papers(
        papers,
        ""
    )

    assert results == []