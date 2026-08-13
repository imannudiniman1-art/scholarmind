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
# HEADER
# =========================================================

st.title("🔎 Ask ScholarMind")

st.markdown(
    "Ask questions about the research papers in the ScholarMind "
    "knowledge base."
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

                st.markdown("## 💡 ScholarMind Answer")

                # =================================================
                # RESULT TYPE
                # =================================================

                result_type = result.get(
                    "type",
                    "unknown"
                ) if isinstance(result, dict) else "text"

                answer = (
                    result.get("answer", result)
                    if isinstance(result, dict)
                    else result
                )



                # -------------------------------------------------
                # Extract answer
                # -------------------------------------------------

                answer = result.get(
                    "answer",
                    result
                )


                # =================================================
                # QUESTION TYPE
                # =================================================

                question_lower = question.lower()

                if (
                    "artificial intelligence" in question_lower
                    or "machine learning" in question_lower
                    or "deep learning" in question_lower
                    or " ai " in f" {question_lower} "
                ):

                    display_field = "ai_methods"
                    display_label = "AI Methods"

                elif (
                    "author" in question_lower
                    or "authors" in question_lower
                ):

                    display_field = "authors"
                    display_label = "Authors"

                elif (
                    "methodology" in question_lower
                    or "method" in question_lower
                    or "technique" in question_lower
                ):

                    display_field = "methodology"
                    display_label = "Methodology"

                elif (
                    "dataset" in question_lower
                    or "data" in question_lower
                ):

                    display_field = "dataset"
                    display_label = "Dataset"

                elif (
                    "finding" in question_lower
                    or "findings" in question_lower
                    or "result" in question_lower
                    or "results" in question_lower
                    or "conclusion" in question_lower
                ):

                    display_field = "findings"
                    display_label = "Findings"

                elif "doi" in question_lower:

                    display_field = "doi"
                    display_label = "DOI"

                elif (
                    "year" in question_lower
                    or "when" in question_lower
                    or "published" in question_lower
                ):

                    display_field = "year"
                    display_label = "Year"

                elif (
                    "abstract" in question_lower
                    or "summary" in question_lower
                ):

                    display_field = "abstract"
                    display_label = "Abstract"

                elif (
                    "source" in question_lower
                    or "repository" in question_lower
                ):

                    display_field = "source"
                    display_label = "Source"

                else:

                    display_field = None
                    display_label = None


# =================================================
# GET DISPLAY VALUE
# =================================================
if display_field == "ai_methods":

    ai_methods = paper.get("ai_methods")

    if ai_methods:
        if isinstance(ai_methods, list):
            display_value = ", ".join(
                str(method) for method in ai_methods
            )
        else:
            display_value = str(ai_methods)

    else:
        # Fallback: ambil AI method dari methodology
        methodology = paper.get("methodology", "")

        if "random forest" in methodology.lower():
            display_value = "Random Forest"
        elif "neural network" in methodology.lower():
            display_value = "Artificial Neural Network (ANN)"
        elif "ann" in methodology.lower():
            display_value = "Artificial Neural Network (ANN)"
        elif "machine learning" in methodology.lower():
            display_value = "Machine Learning"
        else:
            display_value = "N/A"

else:

    display_value = paper.get(
        display_field,
        "N/A"
    )


                # =================================================
                # ERROR RESULT
                # =================================================

                if result_type == "error":

                    st.error(answer)


                # =================================================
                # LIST OF PAPERS
                # =================================================

                elif isinstance(answer, list):

                    st.write(
                        f"**{len(answer)} relevant research "
                        f"paper(s) found.**"
                    )

                    for i, paper in enumerate(
                        answer,
                        start=1
                    ):

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
                                f"**DOI:** "
                                f"{paper.get('doi')}"
                            )


                        # Requested field

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
                                f"**{display_label}:** "
                                f"{value}"
                            )


                        # General question

                        else:

                            if paper.get("authors"):

                                authors = paper.get(
                                    "authors"
                                )

                                if isinstance(
                                    authors,
                                    list
                                ):

                                    authors = ", ".join(
                                        str(author)
                                        for author in authors
                                    )

                                st.write(
                                    f"**Authors:** "
                                    f"{authors}"
                                )


                            if paper.get("year"):

                                st.write(
                                    f"**Year:** "
                                    f"{paper.get('year')}"
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


                # =================================================
                # SINGLE PAPER
                # =================================================

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
                            f"**DOI:** "
                            f"{answer.get('doi')}"
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
                            f"**{display_label}:** "
                            f"{value}"
                        )

                    else:

                        if answer.get("authors"):

                            authors = answer.get(
                                "authors"
                            )

                            if isinstance(
                                authors,
                                list
                            ):

                                authors = ", ".join(
                                    str(author)
                                    for author in authors
                                )

                            st.write(
                                f"**Authors:** "
                                f"{authors}"
                            )


                        if answer.get("year"):

                            st.write(
                                f"**Year:** "
                                f"{answer.get('year')}"
                            )


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


                # =================================================
                # TEXT ANSWER
                # =================================================

                else:

                    st.write(answer)


            except Exception as e:

                st.error(
                    f"ScholarMind encountered an error: {e}"
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

        if isinstance(
            authors,
            list
        ):

            authors = ", ".join(
                str(author)
                for author in authors
            )

        st.write(
            f"**Authors:** {authors}"
        )


        if paper.get("year"):

            st.write(
                f"**Year:** "
                f"{paper.get('year')}"
            )


        if paper.get("doi"):

            st.write(
                f"**DOI:** "
                f"{paper.get('doi')}"
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


       