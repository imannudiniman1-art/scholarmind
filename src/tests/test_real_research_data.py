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

    assert paper.authors == [
        "Iman Imannudin, S.Si., M.Kom"
    ]

    assert paper.year == 2026

    assert paper.doi == (
        "10.5281/zenodo.18707122"
    )

    assert "Artificial Intelligence" in paper.keywords

    assert "Random Forest" in paper.keywords

    assert "supervised machine learning" in (
        paper.methodology.lower()
    )

    assert "500 simulated" in (
        paper.dataset.lower()
    )

    assert "76%" in paper.findings

    assert paper.source == "Zenodo"