"""
Tests for ScholarMind
"""

from knowledge import create_knowledge_item
from memory import create_memory


def test_create_knowledge_item():
    item = create_knowledge_item(
        title="AI Research",
        knowledge_type="Research Topic",
        description="Testing ScholarMind knowledge representation."
    )

    assert item.title == "AI Research"
    assert item.knowledge_type == "Research Topic"
    assert item.description == "Testing ScholarMind knowledge representation."


def test_research_memory():
    memory = create_memory()

    item = create_knowledge_item(
        title="Knowledge Graph",
        knowledge_type="Concept",
        description="Testing research memory."
    )

    memory.add(item)

    assert memory.count() == 1
    assert memory.get_all()[0].title == "Knowledge Graph"
