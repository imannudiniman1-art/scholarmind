"""
ScholarMind Unified Research Assistant

Provides a single interface for:
- Single-paper questions
- Cross-paper questions
- Research comparison
- Methodology, dataset, findings and metadata queries
"""

from research_comparison import compare_papers


def _get_paper_by_id(papers, paper_id):
    for paper in papers:
        if paper.get("id") == paper_id:
            return paper

    return None


def _paper_text(paper):
    """
    Combine searchable research fields into one text.
    """
    fields = [
        paper.get("title", ""),
        paper.get("abstract", ""),
        paper.get("keywords", ""),
        paper.get("methodology", ""),
        paper.get("dataset", ""),
        paper.get("findings", ""),
        paper.get("authors", ""),
        paper.get("doi", ""),
    ]

    text_parts = []

    for value in fields:
        if isinstance(value, list):
            text_parts.append(" ".join(str(x) for x in value))
        else:
            text_parts.append(str(value))

    return " ".join(text_parts).lower()


def _answer_cross_paper_question(papers, question):
    """
    Answer common research questions directly from the
    structured research knowledge base.
    """

    q = question.lower()

    # -----------------------------------------------------
    # Methodology
    # -----------------------------------------------------

    if any(
        term in q
        for term in [
            "methodology",
            "methodologies",
            "method",
            "methods",
            "approach",
            "approaches",
        ]
    ):

        results = []

        for paper in papers:

            methodology = paper.get(
                "methodology",
                "Not specified"
            )

            results.append(
                {
                    "title": paper.get(
                        "title",
                        "Untitled Research"
                    ),
                    "doi": paper.get(
                        "doi",
                        "N/A"
                    ),
                    "methodology": methodology,
                }
            )

        return {
            "type": "methodology",
            "answer": results,
        }

    # -----------------------------------------------------
    # Dataset
    # -----------------------------------------------------

    if any(
        term in q
        for term in [
            "dataset",
            "data used",
            "data set",
            "data source",
        ]
    ):

        results = []

        for paper in papers:

            results.append(
                {
                    "title": paper.get(
                        "title",
                        "Untitled Research"
                    ),
                    "doi": paper.get(
                        "doi",
                        "N/A"
                    ),
                    "dataset": paper.get(
                        "dataset",
                        "Not specified"
                    ),
                }
            )

        return {
            "type": "dataset",
            "answer": results,
        }

    # -----------------------------------------------------
    # Findings / Results
    # -----------------------------------------------------

    if any(
        term in q
        for term in [
            "finding",
            "findings",
            "result",
            "results",
            "conclusion",
            "conclusions",
        ]
    ):

        results = []

        for paper in papers:

            results.append(
                {
                    "title": paper.get(
                        "title",
                        "Untitled Research"
                    ),
                    "doi": paper.get(
                        "doi",
                        "N/A"
                    ),
                    "findings": paper.get(
                        "findings",
                        "Not specified"
                    ),
                }
            )

        return {
            "type": "findings",
            "answer": results,
        }

    # -----------------------------------------------------
    # Authors
    # -----------------------------------------------------

    if any(
        term in q
        for term in [
            "author",
            "authors",
            "who wrote",
            "researcher",
            "researchers",
        ]
    ):

        results = []

        for paper in papers:

            results.append(
                {
                    "title": paper.get(
                        "title",
                        "Untitled Research"
                    ),
                    "authors": paper.get(
                        "authors",
                        "Not specified"
                    ),
                }
            )

        return {
            "type": "authors",
            "answer": results,
        }

    # -----------------------------------------------------
    # General search
    # -----------------------------------------------------

    query_words = [
        word
        for word in q.split()
        if len(word) > 2
    ]

    matched = []

    for paper in papers:

        searchable = _paper_text(paper)

        score = sum(
            1
            for word in query_words
            if word in searchable
        )

        if score > 0:
            matched.append(
                (
                    score,
                    paper
                )
            )

    matched.sort(
        key=lambda item: item[0],
        reverse=True
    )

    if matched:

        return {
            "type": "search",
            "answer": [
                paper
                for score, paper in matched
            ],
        }

    # -----------------------------------------------------
    # If no keyword match, show the knowledge base
    # instead of returning an empty result.
    # -----------------------------------------------------

    return {
        "type": "cross_paper",
        "answer": papers,
    }


def unified_assistant(
    papers,
    question,
    paper_id=None,
    comparison_ids=None
):
    """
    Route a research question to the appropriate
    ScholarMind capability.
    """

    question = (question or "").strip()

    if not question:

        return {
            "type": "error",
            "answer": "Question cannot be empty."
        }

    # -----------------------------------------------------
    # Explicit comparison request
    # -----------------------------------------------------

    if comparison_ids:

        if len(comparison_ids) != 2:

            return {
                "type": "error",
                "answer": "Please select exactly two papers."
            }

        paper_a = _get_paper_by_id(
            papers,
            comparison_ids[0]
        )

        paper_b = _get_paper_by_id(
            papers,
            comparison_ids[1]
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
            ),
        }

    # -----------------------------------------------------
    # Single paper request
    # -----------------------------------------------------

    if paper_id:

        paper = _get_paper_by_id(
            papers,
            paper_id
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

    # -----------------------------------------------------
    # Cross-paper research question
    # -----------------------------------------------------

    return _answer_cross_paper_question(
        papers,
        question
    )