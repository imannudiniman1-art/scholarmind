"""
ScholarMind Knowledge Graph Ingestion

Converts research paper metadata into
Knowledge Graph nodes and relationships.
"""


def ingest_paper(graph, paper, paper_id):
    """
    Add a research paper and its metadata
    to the Knowledge Graph.
    """

    graph.add_node(
        paper_id,
        "paper",
        paper.title
    )

    graph.add_node(
        f"{paper_id}_methodology",
        "methodology",
        paper.methodology
    )

    graph.add_relationship(
        paper_id,
        "uses",
        f"{paper_id}_methodology"
    )

    graph.add_node(
        f"{paper_id}_dataset",
        "dataset",
        paper.dataset
    )

    graph.add_relationship(
        paper_id,
        "uses",
        f"{paper_id}_dataset"
    )

    graph.add_node(
        f"{paper_id}_finding",
        "finding",
        paper.findings
    )

    graph.add_relationship(
        paper_id,
        "reports",
        f"{paper_id}_finding"
    )

    for index, keyword in enumerate(
        paper.keywords
    ):
        keyword_id = (
            f"{paper_id}_keyword_{index}"
        )

        graph.add_node(
            keyword_id,
            "keyword",
            keyword
        )

        graph.add_relationship(
            paper_id,
            "has_keyword",
            keyword_id
        )

    graph.add_node(
        f"{paper_id}_source",
        "source",
        paper.source
    )

    graph.add_relationship(
        paper_id,
        "has_source",
        f"{paper_id}_source"
    )

    return graph