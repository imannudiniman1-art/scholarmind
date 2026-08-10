"""
Integration test for the ScholarMind prototype.

Tests the flow:
Research Paper
    -> Knowledge Item
    -> Research Memory
    -> Knowledge Graph
"""

from research import create_research_paper
from knowledge import create_knowledge_item
from memory import create_memory
from graph import KnowledgeGraph


def test_scholarmind_research_flow():

    # 1. Create a research paper
    paper = create_research_paper(
        title="AI for Environmental Risk Assessment",
        authors=["ScholarMind Research"],
        year=2026,
        method="Random Forest",
        dataset="Environmental Sensor Data",
        findings="AI can support environmental risk assessment."
    )

    # 2. Convert research paper into a knowledge item
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

    # 5. Create relationships
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

    # 6. Verify the complete system
    assert paper.title == "AI for Environmental Risk Assessment"

    assert memory.count() == 1

    assert graph.count_nodes() == 3

    assert graph.count_relationships() == 2