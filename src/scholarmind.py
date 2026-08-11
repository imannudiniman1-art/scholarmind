"""
ScholarMind Core

Main interface for the ScholarMind research
and knowledge management system.
"""

from data_loader import load_research_data
from memory import create_memory
from graph import KnowledgeGraph
from query import search_papers
from answer import answer_question
from research_assistant import ask_about_paper


class ScholarMind:
    def __init__(self, data_path):
        self.data_path = data_path

        self.papers = []
        self.memory = create_memory()
        self.graph = KnowledgeGraph()

    def load_data(self):
        self.papers = load_research_data(
            self.data_path
        )

        return self.papers

    def search(self, query):
        return search_papers(
            self.papers,
            query
        )

    def answer(self, question):
        return answer_question(
            self.papers,
            self.graph,
            question
        )

    def ask_about_paper(
        self,
        paper_id,
        topic
    ):
        return ask_about_paper(
            self.graph,
            paper_id,
            topic
        )

    def status(self):
        return {
            "papers": len(self.papers),
            "memory_items": self.memory.count(),
            "graph_nodes": self.graph.count_nodes(),
            "graph_relationships": (
                self.graph.count_relationships()
            )
        }
