"""
ScholarMind Answer Module

Combines research search and knowledge graph retrieval
to build a structured research answer.
"""

from query import search_papers, find_related_knowledge


def answer_question(papers, graph, question):
    """
    Answer a research question using text search
    and knowledge graph retrieval.
    """

    results = search_papers(
        papers,
        question
    )

    answer = {
        "question": question,
        "papers": [],
        "related_knowledge": []
    }

    for paper in results:
        answer["papers"].append({
            "title": paper.title,
            "authors": paper.authors,
            "year": paper.year,
            "doi": paper.doi
        })

    for paper_id in graph.get_nodes():

        node = graph.get_nodes()[paper_id]

        if node["type"] != "paper":
            continue

        related = find_related_knowledge(
            graph,
            paper_id
        )

        for item in related:
            answer["related_knowledge"].append(item)

    return answer