"""
ScholarMind
AI Research and Knowledge Management Project
"""

from knowledge import create_knowledge_item
from memory import create_memory

PROJECT_NAME = "ScholarMind"
VERSION = "0.1.0"


def main():
    print(f"{PROJECT_NAME} v{VERSION}")
    print("AI Research and Knowledge Management Project")

    memory = create_memory()

    item = create_knowledge_item(
        title="AI Research and Knowledge Management",
        knowledge_type="Research Concept",
        description="Initial ScholarMind research knowledge."
    )

    memory.add(item)

    print(f"Research memory contains {memory.count()} item(s).")
    print(item.summary())


if __name__ == "__main__":
    main()