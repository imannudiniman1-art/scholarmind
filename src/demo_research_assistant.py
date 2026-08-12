"""
ScholarMind Research Assistant Demo
"""

from scholarmind import ScholarMind


def main():
    scholar = ScholarMind(
        "../data/research_papers.json"
    )

    scholar.load_data()

    paper_id = "10.5281/zenodo.18707122"

    questions = [
        "methodology",
        "dataset",
        "finding"
    ]

    print("ScholarMind Research Assistant")
    print("=" * 40)

    for question in questions:
        results = scholar.ask_about_paper(
            paper_id,
            question
        )

        print()
        print("Question:", question)

        for item in results:
            print(
                item["type"],
                "→",
                item["label"]
            )


if __name__ == "__main__":
    main()