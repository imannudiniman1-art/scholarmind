 """
ScholarMind Demo Application
AI Research and Knowledge Management Assistant
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
# IMPORT SCHOLARMIND ASSISTANT
# =========================================================

from unified_assistant import unified_assistant


# =========================================================
# LOAD RESEARCH DATA
# =========================================================

DATA_FILE = ROOT_DIR / "data" / "research_papers.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)


# Make sure we always work with the papers list
if isinstance(data, dict):
    papers = data.get("papers", [])
elif isinstance(data, list):
    papers = data
else:
    papers = []


# =========================================================
# STREAMLIT CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ScholarMind",
    page_icon="🧠",
    layout="centered"
)


# =========================================================
# HEADER
# =========================================================

st.title("🧠 ScholarMind")

st.subheader(
    "AI Research & Knowledge Management Assistant"
)

st.markdown(
    """
    ScholarMind helps researchers explore scientific knowledge,
    connect research information, and retrieve relevant insights.
    """
)

st.divider()


# =========================================================
# RESEARCH STATISTICS
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
# PAPER SELECTION
# =========================================================

paper_options = {
    paper.get("title", "Untitled Research"): paper.get("id")
    for paper in papers
}

selected_paper = st.selectbox(
    "Optional: Select a paper",
    ["None"] + list(paper_options.keys())
)


# =========================================================
# COMPARISON
# =========================================================

compare = st.checkbox(
    "Compare the two available papers"
)


# =========================================================
# ASK BUTTON
# =========================================================

if st.button(
    "Ask ScholarMind",
    type="primary"
):

    # -----------------------------------------------------
    # Empty question
    # -----------------------------------------------------

    if not question.strip() and not compare:

        st.warning(
            "Please enter a research question."
        )


    # -----------------------------------------------------
    # Comparison mode
    # -----------------------------------------------------

    elif compare:

        if len(papers) < 2:

            st.warning(
                "At least two research papers are required "
                "for comparison."
            )

        else:

            comparison_ids = [
                paper.get("id")
                for paper in papers[:2]
            ]

            with st.spinner(
                "ScholarMind is comparing the research papers..."
            ):

                try:

                    result = unified_assistant(
                        papers,
                        "Compare these two papers.",
                        comparison_ids=comparison_ids
                    )

                    st.markdown(
                        "### 📊 Research Comparison"
                    )

                    if isinstance(result, dict):

                        result_type = result.get(
                            "type",
                            "comparison"
                        )

                        st.caption(
                            f"Research mode: {result_type}"
                        )

                        answer = result.get(
                            "answer",
                            result
                        )

                        if isinstance(answer, dict):

                            comparison = answer

                            methodology = comparison.get(
                                "methodology",
                                {}
                            )

                            dataset = comparison.get(
                                "dataset",
                                {}
                            )

                            st.markdown(
                                "#### Methodology"
                            )

                            col1, col2 = st.columns(2)

                            with col1:

                                st.write(
                                    "**Paper 1**"
                                )

                                st.write(
                                    methodology.get(
                                        "paper_a",
                                        "N/A"
                                    )
                                )

                            with col2:

                                st.write(
                                    "**Paper 2**"
                                )

                                st.write(
                                    methodology.get(
                                        "paper_b",
                                        "N/A"
                                    )
                                )

                            st.markdown(
                                "#### Dataset"
                            )

                            st.write(
                                "**Paper 1:**",
                                dataset.get(
                                    "paper_a",
                                    "N/A"
                                )
                            )

                            st.write(
                                "**Paper 2:**",
                                dataset.get(
                                    "paper_b",
                                    "N/A"
                                )
                            )

                        else:

                            st.write(answer)

                    else:

                        st.write(result)

                except Exception as e:

                    st.error(
                        f"ScholarMind encountered an error: {e}"
                    )


    # -----------------------------------------------------
    # Normal question mode
    # -----------------------------------------------------

    else:

        paper_id = None

        if selected_paper != "None":

            paper_id = paper_options[
                selected_paper
            ]

        with st.spinner(
            "ScholarMind is analyzing the research knowledge..."
        ):

            try:

                result = unified_assistant(
                    papers,
                    question,
                    paper_id=paper_id
                )

                st.markdown(
                    "### 💡 ScholarMind Answer"
                )

                # -----------------------------------------
                # Result dictionary
                # -----------------------------------------

                if isinstance(result, dict):

                    result_type = result.get(
                        "type",
                        "research"
                    )

                    st.caption(
                        f"Research mode: {result_type}"
                    )

                    answer = result.get(
                        "answer",
                        result
                    )

                else:

                    answer = result


                # -----------------------------------------
                # List of papers
                # -----------------------------------------

                if isinstance(answer, list):

                    if not answer:

                        st.info(
                            "No relevant research papers "
                            "were found."
                        )

                    else:

                        st.write(
                            f"**{len(answer)} relevant "
                            f"paper(s) found.**"
                        )

                        for paper in answer:

                            st.markdown(
                                f"#### 📄 "
                                f"{paper.get('title', 'Untitled')}"
                            )

                            st.write(
                                f"**DOI:** "
                                f"{paper.get('doi', 'N/A')}"
                            )

                            st.write(
                                f"**Methodology:** "
                                f"{paper.get('methodology', 'N/A')}"
                            )

                            st.write(
                                f"**Dataset:** "
                                f"{paper.get('dataset', 'N/A')}"
                            )

                            st.write(
                                f"**Findings:** "
                                f"{paper.get('findings', 'N/A')}"
                            )

                            st.divider()


                # -----------------------------------------
                # Single paper / dictionary
                # -----------------------------------------

                elif isinstance(answer, dict):

                    st.markdown(
                        f"#### 📄 "
                        f"{answer.get('title', 'Research Paper')}"
                    )

                    st.write(
                        f"**DOI:** "
                        f"{answer.get('doi', 'N/A')}"
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


                # -----------------------------------------
                # Text answer
                # -----------------------------------------

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

with st.expander(
    "📖 View Research Knowledge Base"
):

    if not papers:

        st.warning(
            "No research papers found."
        )

    else:

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

            st.write(
                f"**Year:** "
                f"{paper.get('year', 'N/A')}"
            )

            st.write(
                f"**DOI:** "
                f"{paper.get('doi', 'N/A')}"
            )

            if paper.get("abstract"):

                st.write(
                    f"**Abstract:** "
                    f"{paper.get('abstract')}"
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

            st.divider()


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "ScholarMind — AI Research and Knowledge Management Project"
)