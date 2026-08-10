"""
ScholarMind Knowledge Graph Module
Knowledge relationships for research information.
"""


class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        self.relationships = []

    def add_node(self, node_id, node_type, label):
        self.nodes[node_id] = {
            "type": node_type,
            "label": label
        }

    def add_relationship(self, source, relation, target):
        self.relationships.append({
            "source": source,
            "relation": relation,
            "target": target
        })

    def get_nodes(self):
        return self.nodes

    def get_relationships(self):
        return self.relationships

    def count_nodes(self):
        return len(self.nodes)

    def count_relationships(self):
        return len(self.relationships)