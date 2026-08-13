"""
ScholarMind Cross-Paper Retrieval

Searches research knowledge across multiple papers.
"""


def search_across_papers(papers, keyword):
    """
    Find papers containing a keyword across
    relevant research fields.
    """

    keyword = keyword.lower().strip()

    if not keyword:
        return []

    matches = []

    searchable_fields = [
        "title",
        "abstract",
        "methodology",
        "dataset",
        "findings",
        "source",
    ]

    for paper in papers:
        text_parts = []

        for field in searchable_fields:
            value = paper.get(field, "")

            if isinstance(value, list):
                text_parts.extend(
                    str(item).lower()
                    for item in value
                )
            else:
                text_parts.append(
                    str(value).lower()
                )

        text = " ".join(text_parts)

        if keyword in text:
            matches.append(paper)

    return matches