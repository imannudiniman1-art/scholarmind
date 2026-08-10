 

    """
ScholarMind
AI Research and Knowledge Management Project
"""

from data_loader import load_research_data
from knowledge import create_knowledge_item
from memory import create_memory
from graph import KnowledgeGraph


PROJECT_NAME = "ScholarMind"
VERSION = "0.1.0"


def main():
    print(f"{PROJECT_NAME} v{VERSION}")
    print("AI Research and Knowledge Management Project")

    # Load research data
    papers = load_research_data(
        "../data/sample_research.json"
    )

    # Create research memory
    memory = create_memory()

    # Create knowledge graph
    graph = KnowledgeGraph()

    for index, paper in enumerate(papers, start=1):

        # Convert research paper into knowledge
        knowledge = create_knowledge_item(
            title=paper.title,
            knowledge_type="Research Paper",
            description=paper.findings
        )

        # Store in research memory
        memory.add(knowledge)

        # Create graph nodes
        paper_id = f"paper_{index}"
        method_id = f"method_{index}"
        dataset_id = f"dataset_{index}"

        graph.add_node(
            paper_id,
            "paper",
            paper.title
        )

        graph.add_node(
            method_id,
            "method",
            paper.method
        )

        graph.add_node(
            dataset_id,
            "dataset",
            paper.dataset
        )

        # Create relationships
        graph.add_relationship(
            paper_id,
            "uses",
            method_id
        )

        graph.add_relationship(
            paper_id,
            "uses",
            dataset_id
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
    