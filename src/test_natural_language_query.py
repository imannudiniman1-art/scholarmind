"""
Tests for ScholarMind Natural Language Query.
"""

from query import interpret_research_question


def test_methodology_question():
    question = "What methodology was used in this research?"

    assert (
        interpret_research_question(question)
        == "methodology"
    )


def test_dataset_question():
    question = "What dataset was used in this study?"

    assert (
        interpret_research_question(question)
        == "dataset"
    )


def test_finding_question():
    question = "What were the main findings?"

    assert (
        interpret_research_question(question)
        == "finding"
    )


def test_keyword_question():
    question = "What are the main keywords?"

    assert (
        interpret_research_question(question)
        == "keyword"
    )


def test_source_question():
    question = "What is the source of this research?"

    assert (
        interpret_research_question(question)
        == "source"
    )


def test_unknown_question():
    question = "Tell me something about this paper."

    assert (
        interpret_research_question(question)
        is None
    )