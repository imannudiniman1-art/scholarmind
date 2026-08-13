"""
ScholarMind Research Comparison

Provides structured comparison between research papers.
"""


def compare_papers(paper_a, paper_b):
    """
    Compare two research papers using their
    structured research metadata.
    """

    return {
        "titles": {
            "paper_a": paper_a.get("title", ""),
            "paper_b": paper_b.get("title", "")
        },
        "methodology": {
            "paper_a": paper_a.get("methodology", ""),
            "paper_b": paper_b.get("methodology", "")
        },
        "dataset": {
            "paper_a": paper_a.get("dataset", ""),
            "paper_b": paper_b.get("dataset", "")
        },
        "findings": {
            "paper_a": paper_a.get("findings", ""),
            "paper_b": paper_b.get("findings", "")
        },
        "keywords": {
            "paper_a": paper_a.get("keywords", []),
            "paper_b": paper_b.get("keywords", [])
        }
    }