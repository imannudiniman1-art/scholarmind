"""
Tests Cross-Paper Assistant using real ScholarMind data.
"""

import json

from cross_paper_assistant import ask_across_papers


def load_papers():
    with open(
        "../data/research_papers.json",
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    return data["papers"]


def test_real_ai_question():
    papers = load_papers()

    results = ask_across_papers(
        papers,
        "Which papers use artificial intelligence?"
    )

    assert len(results) == 2


def test_real_random_forest_question():
    papers = load_papers()

    results = ask_across_papers(
        papers,
        "Which paper uses Random Forest?"
    )

    assert len(results) == 1
    assert results[0]["id"] == "zenodo_18707122"


def test_real_satellite_question():
    papers = load_papers()

    results = ask_across_papers(
        papers,
        "Which paper uses satellite?"
    )

    assert len(results) == 1
    assert results[0]["id"] == "zenodo_18276886"


def test_real_ann_question():
    papers = load_papers()

    results = ask_across_papers(
        papers,
        "Which paper uses artificial neural network?"
    )

    assert len(results) == 1
    assert results[0]["id"] == "zenodo_18276886"