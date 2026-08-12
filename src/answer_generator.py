"""
ScholarMind Answer Generator

Converts structured research knowledge into
natural-language research answers.
"""


def generate_answer(question, results):
    """
    Generate a structured natural-language answer
    from retrieved research knowledge.
    """

    if not results:
        return (
            "No relevant research knowledge "
            "was found for this question."
        )

    topic = results[0]["type"]

    labels = [
        item["label"]
        for item in results
    ]

    if topic == "methodology":
        return (
            "The methodology used in this research was: "
            + "; ".join(labels)
            + "."
        )

    if topic == "dataset":
        return (
            "The dataset used in this research was: "
            + "; ".join(labels)
            + "."
        )

    if topic == "finding":
        return (
            "The findings reported in this research were: "
            + "; ".join(labels)
            + "."
        )

    if topic == "keyword":
        return (
            "The research keywords include: "
            + ", ".join(labels)
            + "."
        )

    if topic == "source":
        return (
            "The research source is: "
            + ", ".join(labels)
            + "."
        )

    return (
        "Relevant research knowledge: "
        + "; ".join(labels)
        + "."
    )