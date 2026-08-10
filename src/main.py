"""
ScholarMind
AI Research and Knowledge Management Project
"""

from knowledge import create_knowledge_item
from memory import create_memory
from graph import KnowledgeGraph
from research import create_research_paper


PROJECT_NAME = "ScholarMind"
VERSION = "0.1.0"


def main():
    print(f"{PROJECT_NAME} v{VERSION}")
    print("AI Research and Knowledge Management Project")

    # 1. Create research paper
    paper = create_research_paper(
        title="AI for Environmental Risk Assessment",
        authors=["ScholarMind Research"],
        year=2026,
        method="Random Forest",
        dataset="Environmental Sensor Data",
        findings="AI can support environmental risk assessment."
    )

    # 2. Create knowledge item
    knowledge = create_knowledge_item(
        title=paper.title,
        knowledge_type="Research Paper",
        description=paper.findings
    )

    # 3. Store knowledge in research memory
    memory = create_memory()
    memory.add(knowledge)

    # 4. Create knowledge graph
    graph = KnowledgeGraph()

    graph.add_node(
        "paper_001",
        "paper",
        paper.title
    )

    graph.add_node(
        "method_001",
        "method",
        paper.method
    )

    graph.add_node(
        "dataset_001",
        "dataset",
        paper.dataset
    )

    graph.add_relationship(
        "paper_001",
        "uses",
        "method_001"
    )

    graph.add_relationship(
        "paper_001",
        "uses",
        "dataset_001"
    )

    print()
    print("Research Memory:", memory.count(), "item(s)")
    print("Knowledge Graph Nodes:", graph.count_nodes())
    print("Knowledge Graph Relationships:", graph.count_relationships())


if __name__ == "__main__":
    main()