"""
Tests for ScholarMind Answer Generator.
"""

from answer_generator import generate_answer


def test_methodology_answer():
    results = [
        {
            "type": "methodology",
            "label": "Random Forest"
        }
    ]

    answer = generate_answer(
        "What methodology was used?",
        results
    )

    assert "methodology" in answer.lower()
    assert "Random Forest" in answer


def test_dataset_answer():
    results = [
        {
            "type": "dataset",
            "label": "500 simulated samples"
        }
    ]

    answer = generate_answer(
        "What dataset was used?",
        results
    )

    assert "dataset" in answer.lower()
    assert "500 simulated samples" in answer


def test_finding_answer():
    results = [
        {
            "type": "finding",
            "label": "Testing accuracy was approximately 76%"
        }
    ]

    answer = generate_answer(
        "What were the findings?",
        results
    )

    assert "findings" in answer.lower()
    assert "76%" in answer


def test_empty_results():
    answer = generate_answer(
        "What methodology was used?",
        []
    )

    assert "No relevant research knowledge" in answer