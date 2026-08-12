"""
End-to-end test for ScholarMind answer generation.
"""

from scholarmind import ScholarMind


def test_scholarmind_generates_methodology_answer():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    answer = scholar.answer_question(
        "10.5281/zenodo.18707122",
        "What methodology was used in this research?"
    )

    assert isinstance(answer, str)
    assert "methodology" in answer.lower()
    assert "Random Forest" in answer


def test_scholarmind_generates_dataset_answer():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    answer = scholar.answer_question(
        "10.5281/zenodo.18707122",
        "What dataset was used in this study?"
    )

    assert isinstance(answer, str)
    assert "dataset" in answer.lower()
    assert "500 simulated" in answer


def test_scholarmind_generates_finding_answer():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    answer = scholar.answer_question(
        "10.5281/zenodo.18707122",
        "What were the main findings?"
    )

    assert isinstance(answer, str)
    assert "findings" in answer.lower()
    assert "76%" in answer