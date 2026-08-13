"""
ScholarMind Demo Application
"""

import json
import sys
from pathlib import Path

import streamlit as st


# =========================================================
# PATH CONFIGURATION
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"

sys.path.insert(0, str(SRC_DIR))


# =========================================================
# IMPORT SCHOLARMIND
# =========================================================

from unified_assistant import unified_assistant


# =========================================================
# LOAD RESEARCH DATA
# =========================================================

DATA_FILE = ROOT_DIR / "data" / "research_papers.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

if isinstance(data, dict):
    papers = data.get("papers", [])
else:
    papers = data


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def normalize_value(value):
    """Convert lists and other values into displayable text."""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    if value is None or value == "":
        return "N/A"
    return str(value)


def get_ai_methods(paper):
    """Return AI methods, with a methodology fallback."""
    ai_methods = paper.get("ai_methods")

    if ai_methods:
        return normalize_value(ai_methods)

    methodology = str(paper.get("methodology", ""))

    if "random forest" in methodology.lower():
        return "Random Forest"

    if "neural network" in methodology.lower():
        return "Artificial Neural Network (ANN)"

    if "ann" in methodology.lower():
        return "Artificial Neural Network (ANN)"

    if "machine learning" in methodology.lower():
        return "Machine Learning"

    return "N/A"


def get_question_field(question):
    """Detect which research field the user is asking about."""
    question_lower = question.lower()

    if (
        "artificial intelligence" in question_lower
        or "machine learning" in question_lower
        or "deep learning" in question_lower
        or " ai " in f" {question_lower} "
    ):
        return "ai_methods", "AI Methods"

    if (
        "author" in question_lower
        or "authors" in question_lower
    ):
        return "authors", "Authors"

    if (
        "methodology" in question_lower
        or "method" in question_lower
        or "technique" in question_lower
    ):
        return "methodology", "Methodology"

    if (
        "dataset" in question_lower
        or "data" in question_lower
    ):
        return "dataset", "Dataset"

    if (
        "finding" in question_lower
        or "findings" in question_lower
        or "result" in question_lower
        or "results" in question_lower
        or "conclusion" in question_lower
    ):
        return "findings", "Findings"

    if "doi" in question_lower:
        return "doi", "DOI"

    if (
        "year" in question_lower
        or "when" in question_lower
        or "published" in question_lower
    ):
        return "year", "Year"

    if (
        "abstract" in question_lower
        or "summary" in question_lower
    ):
        return "abstract", "Abstract"

    if (
        "source" in question_lower
        or "repository" in question_lower
    ):
        return "source", "Source"

    return None, None


def get_display_value(paper, display_field):
    """Get the requested field from a paper."""
    if display_field == "ai_methods":
        return get_ai_methods(paper)

    return normalize_value(
        paper.get(display_field, "N/A")
    )


def display_general_paper_info(paper):
    """Display common research metadata."""
    if paper.get("authors"):
        st.write(
            f"**Authors:** "
            f"{normalize_value(paper.get('authors'))}"
        )

    if paper.get("year"):
        st.write(
            f"**Year:** {paper.get('year')}"
        )

    if paper.get("methodology"):
        st.write(
            f"**Methodology:** "
            f"{paper.get('methodology')}"
        )

    if paper.get("dataset"):
        st.write(
            f"**Dataset:** "
            f"{paper.get('dataset')}"
        )

    if paper.get("findings"):
        st.write(
            f"**Findings:** "
            f"{paper.get('findings')}"
        )


def display_paper(paper, index=None, display_field=None, display_label=None):
    """Display one research paper."""
    if not isinstance(paper, dict):
        st.write(paper)
        return

    title = paper.get(
        "title",
        "Untitled Research"
    )

    if index is not None:
        st.markdown(
            f"### 📄 {index}. {title}"
        )
    else:
        st.markdown(
            f"### 📄 {title}"
        )

    if paper.get("doi"):
        st.write(
            f"**DOI:** {paper.get('doi')}"
        )

    if display_field:
        value = get_display_value(
            paper,
            display_field
        )

        st.write(
            f"**{display_label}:** {value}"
        )
    else:
        display_general_paper_info(paper)


# =========================================================
# HEADER
# =========================================================

st.title("🔎 Ask ScholarMind")

st.markdown(
    "Ask questions about the research papers "
    "in the ScholarMind knowledge base."
)


# =========================================================
# ASK SCHOLARMIND
# =========================================================

st.markdown("### Ask a research question")

question = st.text_area(
    "",
    placeholder=(
        "Example: What are the main methodologies "
        "used in these research papers?"
    ),
    height=120
)


# =========================================================
# ASK BUTTON
# =========================================================

if st.button(
    "Ask ScholarMind",
    type="primary"
):

    if not question.strip():

        st.warning(
            "Please enter a research question."
        )

    else:

        # Detect requested metadata field
        display_field, display_label = (
            get_question_field(question)
        )

        # Run ScholarMind
        with st.spinner(
            "ScholarMind is analyzing "
            "the research knowledge..."
        ):

            try:

                result = unified_assistant(
                    papers,
                    question
                )

            except Exception as e:

                st.error(
                    f"ScholarMind error: {e}"
                )

                result = {
                    "type": "error",
                    "answer": str(e)
                }

        st.markdown(
            "## 💡 ScholarMind Answer"
        )

        # =================================================
        # RESULT TYPE
        # =================================================

        if isinstance(result, dict):
            result_type = result.get(
                "type",
                "unknown"
            )
        else:
            result_type = "text"

        # =================================================
        # EXTRACT ANSWER
        # =================================================

        if isinstance(result, dict):
            answer = result.get(
                "answer",
                result
            )
        else:
            answer = result

        # =================================================
        # ERROR RESULT
        # =================================================

        if result_type == "error":

            st.error(
                normalize_value(answer)
            )

        # =================================================
        # LIST OF PAPERS
        # =================================================

        elif isinstance(answer, list):

            st.write(
                f"**{len(answer)} relevant "
                f"research paper(s) found.**"
            )

            for i, paper in enumerate(
                answer,
                start=1
            ):

                display_paper(
                    paper,
                    index=i,
                    display_field=display_field,
                    display_label=display_label
                )

                st.divider()

        # =================================================
        # SINGLE PAPER / DICTIONARY
        # =================================================

        elif isinstance(answer, dict):

            display_paper(
                answer,
                display_field=display_field,
                display_label=display_label
            )

        # =================================================
        # TEXT ANSWER
        # =================================================

        else:

            st.write(
                normalize_value(answer)
            )


# =========================================================
# RESEARCH KNOWLEDGE BASE
# =========================================================

st.divider()

with st.expander(
    "📖 View Research Knowledge Base"
):

    for i, paper in enumerate(
        papers,
        start=1
    ):

        if not isinstance(paper, dict):
            continue

        st.markdown(
            f"### {i}. "
            f"{paper.get('title', 'Untitled Research')}"
        )

        authors = paper.get(
            "authors",
            []
        )

        st.write(
            f"**Authors:** "
            f"{normalize_value(authors)}"
        )

        if paper.get("year"):
            st.write(
                f"**Year:** {paper.get('year')}"
            )

        if paper.get("doi"):
            st.write(
                f"**DOI:** {paper.get('doi')}"
            )

        if paper.get("methodology"):
            st.write(
                f"**Methodology:** "
                f"{paper.get('methodology')}"
            )

        if paper.get("dataset"):
            st.write(
                f"**Dataset:** "
                f"{paper.get('dataset')}"
            )

        if paper.get("findings"):
            st.write(
                f"**Findings:** "
                f"{paper.get('findings')}"
            )

        if paper.get("abstract"):
            st.write(
                f"**Abstract:** "
                f"{paper.get('abstract')}"
            )

        st.divider()
