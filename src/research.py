"""
ScholarMind Research Module
Initial representation of a research paper.
"""


class ResearchPaper:
    def __init__(
        self,
        title,
        authors=None,
        year=None,
        method=None,
        dataset=None,
        findings=None
    ):
        self.title = title
        self.authors = authors or []
        self.year = year
        self.method = method
        self.dataset = dataset
        self.findings = findings

    def summary(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "method": self.method,
            "dataset": self.dataset,
            "findings": self.findings
        }


def create_research_paper(
    title,
    authors=None,
    year=None,
    method=None,
    dataset=None,
    findings=None
):
    return ResearchPaper(
        title=title,
        authors=authors,
        year=year,
        method=method,
        dataset=dataset,
        findings=findings
    )