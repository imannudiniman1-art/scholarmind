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

def find_related_knowledge(graph, paper_id,     relation=None):
    """
    Find knowledge connected to a research paper.

    If relation is provided, only relationships
    with that relation are returned.
    """

    results = []

    for relationship in graph.get_relationships():

        if relationship["source"] != paper_id:
            continue

        if relation is not None:
            if relationship["relation"] != relation:
                continue

        target_id = relationship["target"]

        node = graph.get_nodes().get(target_id)

        if node is not None:
            results.append({
                "relation": relationship["relation"],
                "id": target_id,
                "type": node["type"],
                "label": node["label"]
            })

    return results