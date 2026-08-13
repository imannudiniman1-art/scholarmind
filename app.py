"""
ScholarMind Demo Application
"""

import json
import sys
from pathlib import Path

import streamlit as st


# ---------------------------------------------------------
# Project Paths
# ---------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"

sys.path.insert(0, str(SRC_DIR))


# ---------------------------------------------------------
# ScholarMind Assistant
# ---------------------------------------------------------

from unified_assistant import unified_assistant


# ---------------------------------------------------------
# Load Research Papers
# ---------------------------------------------------------

DATA_FILE = ROOT_DIR / "data" / "research_papers.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

papers = data["papers"]


# ---------------------------------------------------------
# Streamlit Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="ScholarMind",
    page_icon="🧠",
    layout="wide"
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🧠 ScholarMind")

st.subheader(
    "AI Research and Knowledge Management Assistant"
)

st.markdown(
    """
    ScholarMind helps researchers explore scientific knowledge,
    connect research information, and retrieve relevant insights.
    """
)

st.divider()


# ---------------------------------------------------------
# Research Statistics
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# Research Assistant
# ---------------------------------------------------------

st.markdown("### 🔎 Ask ScholarMind")

question = st.text_area(
    "Ask a research question",
    placeholder=(
        "Example: What are the main methodologies "
        "used in these research papers?"
    ),
    height=120
)


if st.button("Ask ScholarMind", type="primary"):

    if not question.strip():

        st.warning(
            "Please enter a research question."
        )

    else:

        with st.spinner(
            "ScholarMind is analyzing the research knowledge..."
        ):

            try:

                result = unified_assistant(
                    papers,
                    question
                )

                st.markdown(
                    "### 💡 ScholarMind Answer"
                )

                if isinstance(result, dict):

                    if "answer" in result:

                        answer = result["answer"]

                    else:

                        answer = result

                else:

                    answer = result

                st.write(answer)

            except Exception as e:

                st.error(
                    f"ScholarMind encountered an error: {e}"
                )


st.divider()


# ---------------------------------------------------------
# Research Knowledge Base
# ---------------------------------------------------------

with st.expander(
    "📖 View Research Knowledge Base"
):

    for i, paper in enumerate(
        papers,
        start=1
    ):

        st.markdown(
            f"#### {i}. "
            f"{paper.get('title', 'Untitled Research')}"
        )

        authors = paper.get(
            "authors",
            []
        )

        if isinstance(authors, list):

            authors = ", ".join(authors)

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


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.caption(
    "ScholarMind — AI Research and Knowledge Management Project"
)