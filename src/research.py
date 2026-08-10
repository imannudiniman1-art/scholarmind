"""
ScholarMind Research Module
Research paper representation.
"""


class ResearchPaper:
    def __init__(
        self,
        title,
        authors=None,
        year=None,
        doi=None,
        abstract=None,
        keywords=None,
        methodology=None,
        dataset=None,
        findings=None,
        source=None
    ):
        self.title = title
        self.authors = authors or []
        self.year = year
        self.doi = doi
        self.abstract = abstract
        self.keywords = keywords or []
        self.methodology = methodology
        self.dataset = dataset
        self.findings = findings
        self.source = source

    def summary(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "doi": self.doi,
            "abstract": self.abstract,
            "keywords": self.keywords,
            "methodology": self.methodology,
            "dataset": self.dataset,
            "findings": self.findings,
            "source": self.source
        }


def create_research_paper(
    title,
    authors=None,
    year=None,
    doi=None,
    abstract=None,
    keywords=None,
    methodology=None,
    dataset=None,
    findings=None,
    source=None
):
    return ResearchPaper(
        title=title,
        authors=authors,
        year=year,
        doi=doi,
        abstract=abstract,
        keywords=keywords,
        methodology=methodology,
        dataset=dataset,
        findings=findings,
        source=source
    )