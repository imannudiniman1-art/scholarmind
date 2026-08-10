
"""
ScholarMind
AI Research and Knowledge Management Project
"""

from data_loader import load_research_data
from knowledge import create_knowledge_item
from memory import create_memory
from graph import KnowledgeGraph
from query import search_papers


PROJECT_NAME = "ScholarMind"
VERSION = "0.2.0"


def main():
    print(f"{PROJECT_NAME} v{VERSION}")
    print("AI Research and Knowledge Management Project")

    papers = load_research_data(
        "../data/sample_research.json"
    )
        # Research Query
    results = search_papers(
        papers,
        "machine learning"
    )

    print()
    print("Search Results:", len(results))

    for paper in results:
        print("-", paper.title)

    memory = create_memory()
    graph = KnowledgeGraph()

    for index, paper in enumerate(papers, start=1):

        # Research Paper → Knowledge
        knowledge = create_knowledge_item(
            title=paper.title,
            knowledge_type="Research Paper",
            description=paper.findings
        )

        memory.add(knowledge)

        paper_id = f"paper_{index}"

        # Paper node
        graph.add_node(
            paper_id,
            "paper",
            paper.title
        )

        # Methodology
        methodology_id = f"methodology_{index}"

        graph.add_node(
            methodology_id,
            "methodology",
            paper.methodology
        )

        graph.add_relationship(
            paper_id,
            "uses",
            methodology_id
        )

        # Dataset
        dataset_id = f"dataset_{index}"

        graph.add_node(
            dataset_id,
            "dataset",
            paper.dataset
        )

        graph.add_relationship(
            paper_id,
            "uses",
            dataset_id
        )

        # Finding
        finding_id = f"finding_{index}"

        graph.add_node(
            finding_id,
            "finding",
            paper.findings
        )

        graph.add_relationship(
            paper_id,
            "reports",
            finding_id
        )

        # Source
        source_id = f"source_{index}"

        graph.add_node(
            source_id,
            "source",
            paper.source
        )

        graph.add_relationship(
            paper_id,
            "has_source",
            source_id
        )

        # Keywords
        for keyword_index, keyword in enumerate(
            paper.keywords,
            start=1
        ):
            keyword_id = (
                f"keyword_{index}_{keyword_index}"
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

    print()
    print("Research Papers:", len(papers))
    print("Research Memory:", memory.count(), "item(s)")
    print("Knowledge Graph Nodes:", graph.count_nodes())
    print(
        "Knowledge Graph Relationships:",
        graph.count_relationships()
    )


if __name__ == "__main__":
    main()