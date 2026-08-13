"""
Tests for ScholarMind Unified Research Assistant.
"""

from unified_assistant import unified_assistant


def create_papers():
    return [
        {
            "id": "paper_1",
            "title": "AI and Geophysical Sensing",
            "methodology": "Random Forest classification",
            "dataset": "Simulated geophysical signals",
            "findings": "76% accuracy",
            "keywords": [
                "Artificial Intelligence",
                "Random Forest"
            ]
        },
        {
            "id": "paper_2",
            "title": "AI and Satellite Infrastructure",
            "methodology": "Artificial Neural Network",
            "dataset": "Simulated environmental data",
            "findings": "Low prediction error",
            "keywords": [
                "Artificial Intelligence",
                "Satellite"
            ]
        }
    ]


def test_single_paper_routing():
    papers = create_papers()

    result = unified_assistant(
        papers,
        "What methodology was used?",
        paper_id="paper_1"
    )

    assert result["type"] == "single_paper"
    assert result["answer"]["id"] == "paper_1"


def test_cross_paper_routing():
    papers = create_papers()

    result = unified_assistant(
        papers,
        "Which papers use artificial intelligence?"
    )

    assert result["type"] == "cross_paper"
    assert len(result["answer"]) == 2


def test_comparison_routing():
    papers = create_papers()

    result = unified_assistant(
        papers,
        "Compare these papers.",
        comparison_ids=[
            "paper_1",
            "paper_2"
        ]
    )

    assert result["type"] == "comparison"

    assert (
        result["answer"]["methodology"]["paper_a"]
        == "Random Forest classification"
    )

    assert (
        result["answer"]["methodology"]["paper_b"]
        == "Artificial Neural Network"
    )


def test_missing_paper():
    papers = create_papers()

    result = unified_assistant(
        papers,
        "What methodology was used?",
        paper_id="unknown"
    )

    assert result["type"] == "error"


def test_invalid_comparison():
    papers = create_papers()

    result = unified_assistant(
        papers,
        "Compare these papers.",
        comparison_ids=["paper_1"]
    )

    assert result["type"] == "error"


def test_empty_question():
    papers = create_papers()

    result = unified_assistant(
        papers,
        ""
    )

    assert result["type"] == "error"