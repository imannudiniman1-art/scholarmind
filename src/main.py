
"""
ScholarMind

Main entry point for the ScholarMind
research and knowledge management system.
"""

from scholarmind import ScholarMind


PROJECT_NAME = "ScholarMind"
VERSION = "0.3.0"


def main():
    print(f"{PROJECT_NAME} v{VERSION}")
    print("AI Research and Knowledge Management Project")

    scholar = ScholarMind(
        "../data/sample_research.json"
    )

    papers = scholar.load_data()

    print()
    print("Research Papers:", len(papers))

    # Search research knowledge
    results = scholar.search(
        "machine learning"
    )

    print()
    print("Search Results:", len(results))

    for paper in results:
        print("-", paper.title)

    # System status
    status = scholar.status()

    print()
    print("ScholarMind Status:")
    print("Papers:", status["papers"])
    print(
        "Memory Items:",
        status["memory_items"]
    )
    print(
        "Graph Nodes:",
        status["graph_nodes"]
    )
    print(
        "Graph Relationships:",
        status["graph_relationships"]
    )


if __name__ == "__main__":
    main()