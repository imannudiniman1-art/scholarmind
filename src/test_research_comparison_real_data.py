"""
Tests Research Comparison using real ScholarMind papers.
"""

import json

from research_comparison import compare_papers


def load_papers():
    with open(
        "../data/research_papers.json",
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    return data["papers"]


def test_compare_real_papers():
    papers = load_papers()

    paper_1 = papers[0]
    paper_2 = papers[1]

    result = compare_papers(
        paper_1,
        paper_2
    )

    assert (
        result["titles"]["paper_a"]
        == paper_1["title"]
    )

    assert (
        result["titles"]["paper_b"]
        == paper_2["title"]
    )


def test_compare_real_methodologies():
    papers = load_papers()

    result = compare_papers(
        papers[0],
        papers[1]
    )

    assert "Random Forest" in (
        result["methodology"]["paper_a"]
    )

    assert "neural network" in (
        result["methodology"]["paper_b"].lower()
    )


def test_compare_real_datasets():
    papers = load_papers()

    result = compare_papers(
        papers[0],
        papers[1]
    )

    assert "500 simulated" in (
        result["dataset"]["paper_a"].lower()
    )

    assert "simulated environmental" in (
        result["dataset"]["paper_b"].lower()
    )


def test_compare_real_findings():
    papers = load_papers()

    result = compare_papers(
        papers[0],
        papers[1]
    )

    assert "76%" in (
        result["findings"]["paper_a"]
    )

    assert "prediction error" in (
        result["findings"]["paper_b"].lower()
    )