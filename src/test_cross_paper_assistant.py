"""
Tests for ScholarMind Cross-Paper Assistant.
"""

from cross_paper_assistant import ask_across_papers


def test_ai_question():
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
            "abstract": "Artificial intelligence for sustainability.",
            "methodology": "Artificial neural network.",
            "dataset": "Simulated environmental data.",
            "findings": "Environmental risk prediction.",
            "source": "Zenodo"
        }
    ]

    results = ask_across_papers(
        papers,
        "Which papers use artificial intelligence?"
    )

    assert len(results) == 2


def test_random_forest_question():
    papers = [
        {
            "id": "paper_1",
            "title": "AI and Geophysical Sensing",
            "abstract": "Environmental risk assessment.",
            "methodology": "Random Forest classification.",
            "dataset": "Simulated geophysical signals.",
            "findings": "Risk classification.",
            "source": "Zenodo"
        },
        {
            "id": "paper_2",
            "title": "AI and Satellite Infrastructure",
            "abstract": "Environmental sustainability.",
            "methodology": "Artificial neural network.",
            "dataset": "Simulated environmental data.",
            "findings": "Risk prediction.",
            "source": "Zenodo"
        }
    ]

    results = ask_across_papers(
        papers,
        "Which paper uses Random Forest?"
    )

    assert len(results) == 1
    assert results[0]["id"] == "paper_1"


def test_satellite_question():
    papers = [
        {
            "id": "paper_1",
            "title": "AI and Geophysical Sensing",
            "abstract": "Environmental risk assessment.",
            "methodology": "Random Forest classification.",
            "dataset": "Simulated geophysical signals.",
            "findings": "Risk classification.",
            "source": "Zenodo"
        },
        {
            "id": "paper_2",
            "title": "AI and Satellite Infrastructure",
            "abstract": "Satellite infrastructure for sustainability.",
            "methodology": "Artificial neural network.",
            "dataset": "Simulated environmental data.",
            "findings": "Risk prediction.",
            "source": "Zenodo"
        }
    ]

    results = ask_across_papers(
        papers,
        "Which paper uses satellite?"
    )

    assert len(results) == 1
    assert results[0]["id"] == "paper_2"


def test_unknown_question():
    papers = [
        {
            "id": "paper_1",
            "title": "AI Research"
        }
    ]

    results = ask_across_papers(
        papers,
        "What is the history of quantum computing?"
    )

    assert results == []