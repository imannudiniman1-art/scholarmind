"""
Tests Unified Assistant using real ScholarMind data.
"""

import json

from unified_assistant import unified_assistant


def load_papers():
    with open(
        "../data/research_papers.json",
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    return data["papers"]


def test_real_single_paper():
    papers = load_papers()

    result = unified_assistant(
        papers,
        "What methodology was used?",
        paper_id="zenodo_18707122"
    )

    assert result["type"] == "single_paper"

    assert (
        result["answer"]["id"]
        == "zenodo_18707122"
    )


def test_real_cross_paper():
    papers = load_papers()

    result = unified_assistant(
        papers,
        "Which papers use artificial intelligence?"
    )

    assert result["type"] == "cross_paper"
    assert len(result["answer"]) == 2


def test_real_comparison():
    papers = load_papers()

    result = unified_assistant(
        papers,
        "Compare these two papers.",
        comparison_ids=[
            "zenodo_18707122",
            "zenodo_18276886"
        ]
    )

    assert result["type"] == "comparison"

    assert (
        "Random Forest"
        in result["answer"]["methodology"]["paper_a"]
    )

    assert (
        "neural network"
        in result["answer"]["methodology"]["paper_b"].lower()
    )


def test_real_satellite_question():
    papers = load_papers()

    result = unified_assistant(
        papers,
        "Which paper uses satellite?"
    )

    assert result["type"] == "cross_paper"

    assert len(result["answer"]) == 1

    assert (
        result["answer"][0]["id"]
        == "zenodo_18276886"
    )