def interpret_research_question(question):
    """
    Interpret a natural-language research question
    into a ScholarMind knowledge topic.
    """

    question = question.lower().strip()

    if (
        "methodology" in question
        or "method" in question
        or "approach" in question
        or "technique" in question
    ):
        return "methodology"

    if (
        "dataset" in question
        or "data" in question
        or "samples" in question
    ):
        return "dataset"

    if (
        "finding" in question
        or "result" in question
        or "results" in question
    ):
        return "finding"

    if (
        "keyword" in question
        or "keywords" in question
        or "topic" in question
    ):
        return "keyword"

    if "source" in question:
        return "source"

    return None