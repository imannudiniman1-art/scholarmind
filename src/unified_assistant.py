"""
ScholarMind Unified Research Assistant

Provides a single interface for:
- Single-paper questions
- Cross-paper questions
- Research comparison
"""


from research_comparison import compare_papers
from cross_paper_assistant import ask_across_papers


def unified_assistant(
    papers,
    question,
    paper_id=None,
    comparison_ids=None
):
    """
    Route a research question to the appropriate
    ScholarMind research capability.
    """

    question_lower = question.lower().strip()

    if not question_lower:
        return {
            "type": "error",
            "answer": "Question cannot be empty."
        }

    if comparison_ids:
        if len(comparison_ids) != 2:
            return {
                "type": "error",
                "answer": "Comparison requires exactly two papers."
            }

        paper_a = next(
            (
                paper for paper in papers
                if paper.get("id") == comparison_ids[0]
            ),
            None
        )

        paper_b = next(
            (
                paper for paper in papers
                if paper.get("id") == comparison_ids[1]
            ),
            None
        )

        if not paper_a or not paper_b:
            return {
                "type": "error",
                "answer": "One or more papers were not found."
            }

        return {
            "type": "comparison",
            "answer": compare_papers(
                paper_a,
                paper_b
            )
        }

    cross_paper_terms = [
        "which papers",
        "across papers",
        "among papers",
        "compare papers",
        "multiple papers"
    ]

    if any(
        term in question_lower
        for term in cross_paper_terms
    ):
        return {
            "type": "cross_paper",
            "answer": ask_across_papers(
                papers,
                question
            )
        }

    if paper_id:
        paper = next(
            (
                paper for paper in papers
                if paper.get("id") == paper_id
            ),
            None
        )

        if not paper:
            return {
                "type": "error",
                "answer": "Paper not found."
            }

        return {
            "type": "single_paper",
            "answer": paper
        }

    return {
        "type": "cross_paper",
        "answer": ask_across_papers(
            papers,
            question
        )
    }