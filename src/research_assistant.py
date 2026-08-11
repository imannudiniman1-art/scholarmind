"""
ScholarMind Research Assistant

Provides simple research-oriented questions
using the Knowledge Graph.
"""

from query import find_related_knowledge


def ask_about_paper(graph, paper_id, topic):
    """
    Retrieve knowledge about a specific topic
    from a research paper.
    """

    related = find_related_knowledge(
        graph,
        paper_id
    )

    topic = topic.lower().strip()

    matches = []

    for item in related:
        searchable = " ".join([
            item["type"],
            item["label"]
        ]).lower()

        if topic in searchable:
            matches.append(item)

    return matches