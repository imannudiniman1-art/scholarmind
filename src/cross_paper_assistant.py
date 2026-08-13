"""
ScholarMind Cross-Paper Assistant

Answers research questions across multiple papers.
"""

from cross_paper import search_across_papers


def ask_across_papers(papers, question):
    """
    Search across multiple research papers
    using a natural-language research question.
    """

    question = question.lower().strip()

    if not question:
        return []

    keywords = [
        "artificial intelligence",
        "environmental risk assessment",
        "satellite",
        "random forest",
        "artificial neural network",
        "machine learning",
        "renewable energy",
    ]

    for keyword in keywords:
        if keyword in question:
            return search_across_papers(
                papers,
                keyword
            )

    return []