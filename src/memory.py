"""
ScholarMind Research Memory Module
Initial implementation of research memory.
"""

class ResearchMemory:
    def __init__(self):
        self.items = []

    def add(self, knowledge_item):
        self.items.append(knowledge_item)

    def get_all(self):
        return self.items

    def count(self):
        return len(self.items)


def create_memory():
    return ResearchMemory()