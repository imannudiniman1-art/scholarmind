"""
ScholarMind Research Assistant
Provides simple research-oriented questions
using the Knowledge Graph.
"""

from query import (
    find_related_knowledge,
    interpret_research_question
)

from query import find_related_knowledge


def ask_about_paper(graph, paper_id, question):

    """
    Answer a natural-language research question
    about a specific paper.
    """

    topic = interpret_research_question(
        question
    )

    if topic is None:
        return []

    related = find_related_knowledge(
        graph,
        paper_id
    )

    matches = []

    for item in related:
        if item["type"] == topic:
            matches.append(item)

    return matches