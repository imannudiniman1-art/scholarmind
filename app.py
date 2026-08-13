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


# Support both:
# 1. JSON list
# 2. JSON object containing "papers"

if isinstance(data, dict):
    papers = data.get("papers", [])
else:
    papers = data


# =========================================================
# STREAMLIT CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ScholarMind",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("🧠 ScholarMind")
st.subheader("AI Research and Knowledge Management Assistant")

st.markdown(
    """
    ScholarMind helps researchers explore scientific knowledge,
    connect research information, and retrieve relevant insights.
    """
)

st.divider()


# =========================================================
# RESEARCH KNOWLEDGE BASE
# =========================================================

st.markdown("### 📚 Research Knowledge Base")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Research Papers",
        len(papers)
    )

with col2:
    st.metric(
        "Knowledge Status",
        "Ready"
    )

with col3:
    st.metric(
        "Assistant",
        "Online"
    )

st.divider()


# =========================================================
# ASK SCHOLARMIND
# =========================================================

st.markdown("### 🔎 Ask ScholarMind")

question = st.text_area(
    "Ask a research question",
    placeholder=(
        "Example: What are the main methodologies "
        "used in these research papers?"
    ),
    height=120
)


# =========================================================
# ASK BUTTON
# =========================================================

if st.button("Ask ScholarMind", type="primary"):

    if not question.strip():

        st.warning("Please enter a research question.")

    else:

        with st.spinner(
            "ScholarMind is analyzing the research knowledge..."
        ):

            try:

                result = unified_assistant(
                    papers,
                    question
                )

                st.markdown("### 💡 ScholarMind Answer")

                # -------------------------------------------------
                # Determine question type
                # -------------------------------------------------

                question_lower = question.lower()

                if "dataset" in question_lower or "data" in question_lower:

                    display_field = "dataset"
                    display_label = "Dataset"

                elif (
                    "methodology" in question_lower
                    or "method" in question_lower
                    or "technique" in question_lower
                ):

                    display_field = "methodology"
                    display_label = "Methodology"

                elif (
                    "finding" in question_lower
                    or "result" in question_lower
                    or "conclusion" in question_lower
                ):

                    display_field = "findings"
                    display_label = "Findings"

                elif "doi" in question_lower:

                    display_field = "doi"
                    display_label = "DOI"

                elif (
                    "author" in question_lower
                    or "authors" in question_lower
                ):

                    display_field = "authors"
                    display_label = "Authors"

                else:

                    display_field = None
                    display_label = None


                # -------------------------------------------------
                # Extract answer
                # -------------------------------------------------

                answer = result.get("answer", result)


                # -------------------------------------------------
                # LIST OF PAPERS
                # -------------------------------------------------

                if isinstance(answer, list):

                    st.write(
                        f"**{len(answer)} relevant research paper(s) found.**"
                    )

                    for i, paper in enumerate(answer, start=1):

                        if not isinstance(paper, dict):
                            st.write(paper)
                            continue

                        title = paper.get(
                            "title",
                            "Untitled Research"
                        )

                        st.markdown(
                            f"### 📄 {i}. {title}"
                        )

                        # DOI

                        if paper.get("doi"):

                            st.write(
                                f"**DOI:** {paper.get('doi')}"
                            )


                        # Selected information

                        if display_field:

                            value = paper.get(
                                display_field,
                                "N/A"
                            )

                            if isinstance(value, list):

                                value = ", ".join(
                                    str(item)
                                    for item in value
                                )

                            st.write(
                                f"**{display_label}:** {value}"
                            )

                        else:

                            # General question:
                            # show useful research information

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

                        st.divider()


                # -------------------------------------------------
                # SINGLE PAPER
                # -------------------------------------------------

                elif isinstance(answer, dict):

                    title = answer.get(
                        "title",
                        "Research Paper"
                    )

                    st.markdown(
                        f"### 📄 {title}"
                    )

                    if answer.get("doi"):

                        st.write(
                            f"**DOI:** {answer.get('doi')}"
                        )


                    if display_field:

                        value = answer.get(
                            display_field,
                            "N/A"
                        )

                        if isinstance(value, list):

                            value = ", ".join(
                                str(item)
                                for item in value
                            )

                        st.write(
                            f"**{display_label}:** {value}"
                        )

                    else:

                        if answer.get("methodology"):
                            st.write(
                                f"**Methodology:** "
                                f"{answer.get('methodology')}"
                            )

                        if answer.get("dataset"):
                            st.write(
                                f"**Dataset:** "
                                f"{answer.get('dataset')}"
                            )

                        if answer.get("findings"):
                            st.write(
                                f"**Findings:** "
                                f"{answer.get('findings')}"
                            )


                # -------------------------------------------------
                # TEXT ANSWER
                # -------------------------------------------------

                else:

                    st.write(answer)


            except Exception as e:

                st.error(
                    f"ScholarMind encountered an error: {e}"
                )


st.divider()


# =========================================================
# RESEARCH KNOWLEDGE BASE
# =========================================================

with st.expander("📖 View Research Knowledge Base"):

    for i, paper in enumerate(papers, start=1):

        if not isinstance(paper, dict):
            continue

        st.markdown(
            f"#### {i}. "
            f"{paper.get('title', 'Untitled Research')}"
        )

        authors = paper.get("authors", [])

        if isinstance(authors, list):
            authors = ", ".join(
                str(author) for author in authors
            )

        st.write(
            f"**Authors:** {authors}"
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


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "ScholarMind — AI Research and Knowledge Management Project"
)