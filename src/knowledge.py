"""
ScholarMind Knowledge Module
Initial representation of research knowledge.
"""

class KnowledgeItem:
    def __init__(self, title, knowledge_type, description=""):
        self.title = title
        self.knowledge_type = knowledge_type
        self.description = description

    def summary(self):
        return {
            "title": self.title,
            "type": self.knowledge_type,
            "description": self.description
        }


def create_knowledge_item(title, knowledge_type, description=""):
    return KnowledgeItem(title, knowledge_type, description)