"""
ScholarMind End-to-End Test

Tests the complete research workflow from
data loading to research knowledge retrieval.
"""

from scholarmind import ScholarMind


def test_scholarmind_end_to_end():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    # 1. Load research data
    papers = scholar.load_data()

    assert len(papers) == 1

    # 2. Verify research paper
    paper = papers[0]

    assert paper.title == (
        "Integration of AI and Geophysical Sensing "
        "for Environmental Risk Assessment"
    )

    assert paper.doi == (
        "10.5281/zenodo.18707122"
    )

    # 3. Verify Knowledge Graph
    status = scholar.status()

    assert status["papers"] == 1
    assert status["graph_nodes"] > 1
    assert status["graph_relationships"] > 1

    # 4. Search research
    results = scholar.search(
        "machine learning"
    )

    assert len(results) >= 1

    # 5. Research Assistant
    methodology = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "methodology"
    )

    assert len(methodology) == 1
    assert methodology[0]["type"] == "methodology"

    # 6. Dataset retrieval
    dataset = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "dataset"
    )

    assert len(dataset) == 1
    assert dataset[0]["type"] == "dataset"

    # 7. Finding retrieval
    finding = scholar.ask_about_paper(
        "10.5281/zenodo.18707122",
        "finding"
    )

    assert len(finding) == 1
    assert finding[0]["type"] == "finding"