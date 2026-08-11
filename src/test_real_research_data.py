"""
Test for real research metadata ingestion.
"""

from data_loader import load_research_data


def test_load_real_research_paper():
    papers = load_research_data(
        "../data/research_papers.json"
    )

    assert len(papers) == 1

    paper = papers[0]

    assert paper.title == (
        "Integration of AI and Geophysical Sensing "
        "for Environmental Risk Assessment"
    )

    assert paper.doi == (
        "10.5281/zenodo.18707122"
    )

    assert paper.source == "Zenodo"