"""
ScholarMind Demo Application
"""

import json
import sys
from pathlib import Path

import streamlit as st


# Make src available
ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

from unified_assistant import unified_assistant


# Load research papers
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

st.title("🧠 ScholarMind")
st.subheader("AI Research and Knowledge Management Assistant")

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
        len(data)
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

        st.warning("Please enter a research question.")

    else:

        with st.spinner("ScholarMind is analyzing the research knowledge..."):

            try:

                answer = unified_assistant(
                    question,
                    data
                )

                st.markdown("### 💡 ScholarMind Answer")

                st.write(answer)

            except Exception as e:

                st.error(
                    f"ScholarMind encountered an error: {e}"
                )


st.divider()


# ---------------------------------------------------------
# Research Papers
# ---------------------------------------------------------

with st.expander("📖 View Research Knowledge Base"):

    for i, paper in enumerate(data, start=1):

        st.markdown(f"#### {i}. {paper.get('title', 'Untitled Research')}")

        authors = paper.get("authors", [])

        if isinstance(authors, list):
            authors = ", ".join(authors)

        st.write(f"**Authors:** {authors}")

        if paper.get("year"):
            st.write(f"**Year:** {paper.get('year')}")

        if paper.get("doi"):
            st.write(f"**DOI:** {paper.get('doi')}")

        if paper.get("abstract"):
            st.write(f"**Abstract:** {paper.get('abstract')}")

        st.divider()


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.caption(
    "ScholarMind — AI Research and Knowledge Management Project"
)

# Page configuration
st.set_page_config(
    page_title="ScholarMind",
    page_icon="🧠",
    layout="centered"
)


# Header
st.title("🧠 ScholarMind")
st.subheader("AI Research & Knowledge Assistant")

st.write(
    "Ask questions about research papers, "
    "search across papers, or compare research methodologies."
)


# Question input
question = st.text_area(
    "Research Question",
    placeholder=(
        "Example: Which papers use artificial intelligence?"
    )
)


# Paper selection
paper_options = {
    paper["title"]: paper["id"]
    for paper in papers
}

selected_paper = st.selectbox(
    "Optional: Select a paper",
    ["None"] + list(paper_options.keys())
)


# Comparison option
compare = st.checkbox(
    "Compare the two available papers"
)


# Ask button
if st.button("🔎 Ask ScholarMind"):

    if not question.strip() and not compare:
        st.warning("Please enter a research question.")

    elif compare:

        comparison_ids = [
            paper["id"]
            for paper in papers[:2]
        ]

        result = unified_assistant(
            papers,
            "Compare these two papers.",
            comparison_ids=comparison_ids
        )

        st.subheader("📊 Research Comparison")

        if result["type"] == "comparison":

            comparison = result["answer"]

            st.markdown("### Methodology")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Paper 1**")
                st.write(
                    comparison["methodology"]["paper_a"]
                )

            with col2:
                st.write("**Paper 2**")
                st.write(
                    comparison["methodology"]["paper_b"]
                )

            st.markdown("### Dataset")

            st.write(
                "**Paper 1:**",
                comparison["dataset"]["paper_a"]
            )

            st.write(
                "**Paper 2:**",
                comparison["dataset"]["paper_b"]
            )

    else:

        paper_id = None

        if selected_paper != "None":
            paper_id = paper_options[selected_paper]

        result = unified_assistant(
            papers,
            question,
            paper_id=paper_id
        )

        st.subheader("💡 ScholarMind Result")

        result_type = result["type"]

        st.caption(
            f"Research mode: {result_type}"
        )

        answer = result["answer"]

        if isinstance(answer, list):

            st.write(
                f"**{len(answer)} relevant paper(s) found.**"
            )

            for paper in answer:

                st.markdown(
                    f"### 📄 {paper.get('title', 'Untitled')}"
                )

                st.write(
                    f"**DOI:** {paper.get('doi', 'N/A')}"
                )

                st.write(
                    f"**Methodology:** "
                    f"{paper.get('methodology', 'N/A')}"
                )

        elif isinstance(answer, dict):

            st.markdown(
                f"### 📄 {answer.get('title', 'Research Paper')}"
            )

            st.write(
                f"**DOI:** {answer.get('doi', 'N/A')}"
            )

            st.write(
                f"**Methodology:** "
                f"{answer.get('methodology', 'N/A')}"
            )

            st.write(
                f"**Dataset:** "
                f"{answer.get('dataset', 'N/A')}"
            )

            st.write(
                f"**Findings:** "
                f"{answer.get('findings', 'N/A')}"
            )

        else:
            st.write(answer)