"""
Tests for ScholarMind Research Comparison.
"""

from research_comparison import compare_papers


def test_compare_methodologies():
    paper_a = {
        "title": "Paper A",
        "methodology": "Random Forest classification",
        "dataset": "Simulated geophysical signals",
        "findings": "76% accuracy",
        "keywords": [
            "Artificial Intelligence",
            "Random Forest"
        ]
    }

    paper_b = {
        "title": "Paper B",
        "methodology": "Artificial Neural Network",
        "dataset": "Simulated environmental data",
        "findings": "Low prediction error",
        "keywords": [
            "Artificial Intelligence",
            "ANN"
        ]
    }

    result = compare_papers(
        paper_a,
        paper_b
    )

    assert (
        result["methodology"]["paper_a"]
        == "Random Forest classification"
    )

    assert (
        result["methodology"]["paper_b"]
        == "Artificial Neural Network"
    )


def test_compare_datasets():
    paper_a = {
        "dataset": "Simulated geophysical signals"
    }

    paper_b = {
        "dataset": "Simulated environmental data"
    }

    result = compare_papers(
        paper_a,
        paper_b
    )

    assert (
        result["dataset"]["paper_a"]
        == "Simulated geophysical signals"
    )

    assert (
        result["dataset"]["paper_b"]
        == "Simulated environmental data"
    )


def test_compare_findings():
    paper_a = {
        "findings": "76% accuracy"
    }

    paper_b = {
        "findings": "Low prediction error"
    }

    result = compare_papers(
        paper_a,
        paper_b
    )

    assert (
        result["findings"]["paper_a"]
        == "76% accuracy"
    )

    assert (
        result["findings"]["paper_b"]
        == "Low prediction error"
    )


def test_compare_keywords():
    paper_a = {
        "keywords": [
            "Artificial Intelligence",
            "Random Forest"
        ]
    }

    paper_b = {
        "keywords": [
            "Artificial Intelligence",
            "ANN"
        ]
    }

    result = compare_papers(
        paper_a,
        paper_b
    )

    assert "Artificial Intelligence" in (
        result["keywords"]["paper_a"]
    )

    assert "Artificial Intelligence" in (
        result["keywords"]["paper_b"]
    )