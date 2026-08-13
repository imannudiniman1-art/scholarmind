"""
Tests Cross-Paper Retrieval using real ScholarMind data.
"""

import json

from cross_paper import search_across_papers


def load_papers():
    with open(
        "../data/research_papers.json",
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    return data["papers"]


def test_real_papers_ai():
    papers = load_papers()

    results = search_across_papers(
        papers,
        "artificial intelligence"
    )

    assert len(results) == 2


def test_real_papers_environmental_risk():
    papers = load_papers()

    results = search_across_papers(
        papers,
        "environmental risk assessment"
    )

    assert len(results) == 2


def test_real_papers_satellite():
    papers = load_papers()

    results = search_across_papers(
        papers,
        "satellite"
    )

    assert len(results) == 1
    assert results[0]["id"] == "zenodo_18276886"


def test_real_papers_random_forest():
    papers = load_papers()

    results = search_across_papers(
        papers,
        "random forest"
    )

    assert len(results) == 1
    assert results[0]["id"] == "zenodo_18707122"


def test_real_papers_ann():
    papers = load_papers()

    results = search_across_papers(
        papers,
        "artificial neural network"
    )

    assert len(results) == 1
    assert results[0]["id"] == "zenodo_18276886"