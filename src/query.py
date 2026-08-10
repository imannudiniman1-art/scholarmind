"""
ScholarMind Research Query Module

Provides simple search capabilities for research papers.
"""


def search_papers(papers, query):
    """
    Search research papers using a keyword.

    The query is matched against:
    - title
    - abstract
    - keywords
    - methodology
    - findings
    """

    query = query.lower().strip()

    results = []

    for paper in papers:

        searchable_text = " ".join([
            paper.title or "",
            paper.abstract or "",
            paper.methodology or "",
            paper.findings or "",
            " ".join(paper.keywords or [])
        ]).lower()

        if query in searchable_text:
            results.append(paper)

    return results