 
 
import json
import sys
from pathlib import Path

import streamlit as st


# Path
ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"

sys.path.insert(0, str(SRC_DIR))


# Import ScholarMind
from unified_assistant import unified_assistant


# Load data
DATA_FILE = ROOT_DIR / "data" / "research_papers.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)


# Get papers
if isinstance(data, dict):
    papers = data.get("papers", [])
else:
    papers = data


# Page
st.set_page_config(
    page_title="ScholarMind",
    page_icon="🧠",
    layout="centered"
)


# Header
st.title("🧠 ScholarMind")
st.subheader("AI Research & Knowledge Assistant")

st.write(
    "Ask questions about research papers "
    "and explore scientific knowledge."
)


st.divider()


# Statistics
st.markdown("### 📚 Research Knowledge Base")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Research Papers", len(papers))

with col2:
    st.metric("Knowledge Status", "Ready")

with col3:
    st.metric("Assistant", "Online")


st.divider()


# Ask ScholarMind
st.markdown("### 🔎 Ask ScholarMind")

question = st.text_area(
    "Ask a research question",
    placeholder="Example: What are the main methodologies used in these research papers?",
    height=120
)


if st.button("Ask ScholarMind", type="primary"):

    if not question.strip():

        st.warning("Please enter a research question.")

    else:

        with st.spinner("ScholarMind is analyzing the research..."):

            try:

                result = unified_assistant(
                    papers,
                    question
                )

                st.markdown("### 💡 ScholarMind Answer")

                if isinstance(result, dict):

                    answer = result.get(
                        "answer",
                        result
                    )

                    if isinstance(answer, list):

                        if len(answer) == 0:

                            st.info(
                                "No relevant research papers were found."
                            )

                        else:

                            for paper in answer:

                                st.markdown(
                                    f"#### 📄 {paper.get('title', 'Untitled')}"
                                )

                                st.write(
                                    f"**DOI:** {paper.get('doi', 'N/A')}"
                                )

                                st.write(
                                    f"**Methodology:** {paper.get('methodology', 'N/A')}"
                                )

                    elif isinstance(answer, dict):

                        st.write(
                            f"**Title:** {answer.get('title', 'N/A')}"
                        )

                        st.write(
                            f"**DOI:** {answer.get('doi', 'N/A')}"
                        )

                        st.write(
                            f"**Methodology:** {answer.get('methodology', 'N/A')}"
                        )

                        st.write(
                            f"**Dataset:** {answer.get('dataset', 'N/A')}"
                        )

                        st.write(
                            f"**Findings:** {answer.get('findings', 'N/A')}"
                        )

                    else:

                        st.write(answer)

                else:

                    st.write(result)

            except Exception as e:

                st.error(
                    f"ScholarMind encountered an error: {e}"
                )


st.divider()


# Research Knowledge Base
with st.expander("📖 View Research Knowledge Base"):

    for i, paper in enumerate(papers, start=1):

        st.markdown(
            f"### {i}. {paper.get('title', 'Untitled Research')}"
        )

        authors = paper.get("authors", [])

        if isinstance(authors, list):
            authors = ", ".join(authors)

        st.write(f"**Authors:** {authors}")

        st.write(
            f"**Year:** {paper.get('year', 'N/A')}"
        )

        st.write(
            f"**DOI:** {paper.get('doi', 'N/A')}"
        )

        st.write(
            f"**Abstract:** {paper.get('abstract', 'N/A')}"
        )

        st.write(
            f"**Methodology:** {paper.get('methodology', 'N/A')}"
        )

        st.write(
            f"**Dataset:** {paper.get('dataset', 'N/A')}"
        )

        st.write(
            f"**Findings:** {paper.get('findings', 'N/A')}"
        )

        st.divider()


st.caption(
    "ScholarMind — AI Research and Knowledge Management Project"
)