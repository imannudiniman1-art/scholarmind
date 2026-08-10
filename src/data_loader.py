"""
ScholarMind Data Loader

Loads research metadata from JSON files.
"""

import json
from research import create_research_paper


def load_research_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    papers = []

    for item in data.get("papers", []):
        paper = create_research_paper(
            title=item.get("title"),
            authors=item.get("authors"),
            year=item.get("year"),
            method=item.get("method"),
            dataset=item.get("dataset"),
            findings=item.get("findings")
        )

        papers.append(paper)

    return papers