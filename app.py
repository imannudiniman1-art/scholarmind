"""ScholarMind Demo Application - AI Research Assistant"""

import json
import sys
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ScholarMind | AI Research Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.stApp{background:radial-gradient(circle at top left,#eef4ff 0%,transparent 35%),radial-gradient(circle at top right,#f5f0ff 0%,transparent 35%),#fff}
.block-container{max-width:1100px;padding-top:2rem;padding-bottom:4rem}
.hero{padding:1.8rem 2rem;border-radius:24px;background:linear-gradient(135deg,#eef4ff 0%,#fff 55%,#f5f0ff 100%);border:1px solid #dce6f5;box-shadow:0 8px 30px rgba(40,60,100,.08);margin-bottom:1.5rem}
.hero-title{font-size:2.6rem;font-weight:800;color:#172033}.hero-subtitle{font-size:1.05rem;color:#5d6678}
.metric{padding:1rem;border-radius:16px;background:#fff;border:1px solid #e5e9f0;text-align:center;box-shadow:0 4px 14px rgba(30,40,70,.05)}
.paper-title{font-size:1.35rem;font-weight:750;color:#1d2940}.answer{padding:1.2rem 1.4rem;border-radius:18px;background:#f8fbff;border-left:5px solid #4f7cff}
div.stButton>button{border-radius:12px;font-weight:700}.small{color:#6b7280;font-size:.9rem}
</style>
""", unsafe_allow_html=True)

ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from unified_assistant import unified_assistant

DATA_FILE = ROOT_DIR / "data" / "research_papers.json"

try:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    papers = data.get("papers", []) if isinstance(data, dict) else data
except FileNotFoundError:
    papers = []
    st.error("Research data file was not found: data/research_papers.json")
except json.JSONDecodeError as e:
    papers = []
    st.error(f"Invalid JSON research data: {e}")


def normalize_value(value):
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    if value is None or value == "":
        return "N/A"
    return str(value)


def get_ai_methods(paper):
    ai_methods = paper.get("ai_methods")
    if ai_methods:
        return normalize_value(ai_methods)
    methodology = str(paper.get("methodology", "")).lower()
    if "random forest" in methodology:
        return "Random Forest"
    if "neural network" in methodology or "ann" in methodology:
        return "Artificial Neural Network (ANN)"
    if "machine learning" in methodology:
        return "Machine Learning"
    return "N/A"


def get_question_field(question):
    q = question.lower()
    if ("artificial intelligence" in q or "machine learning" in q or
            "deep learning" in q or " ai " in f" {q} "):
        return "ai_methods", "AI Methods"
    if "author" in q or "authors" in q:
        return "authors", "Authors"
    if "methodology" in q or "method" in q or "technique" in q:
        return "methodology", "Methodology"
    if "dataset" in q or "data" in q:
        return "dataset", "Dataset"
    if ("finding" in q or "findings" in q or "result" in q or
            "results" in q or "conclusion" in q):
        return "findings", "Findings"
    if "doi" in q:
        return "doi", "DOI"
    if "year" in q or "when" in q or "published" in q:
        return "year", "Year"
    if "abstract" in q or "summary" in q:
        return "abstract", "Abstract"
    if "source" in q or "repository" in q:
        return "source", "Source"
    return None, None


def get_display_value(paper, field):
    return get_ai_methods(paper) if field == "ai_methods" else normalize_value(paper.get(field, "N/A"))


def display_general_paper_info(paper):
    fields = [("Authors", "authors"), ("Year", "year"),
              ("Methodology", "methodology"), ("Dataset", "dataset"),
              ("Findings", "findings")]
    for label, key in fields:
        if paper.get(key):
            st.write(f"**{label}:** {normalize_value(paper.get(key))}")


def display_paper(paper, index=None, display_field=None, display_label=None):
    if not isinstance(paper, dict):
        st.write(paper)
        return
    title = paper.get("title", "Untitled Research")
    prefix = f"{index}. " if index is not None else ""
    st.markdown(f'<div class="paper-title">📄 {prefix}{title}</div>', unsafe_allow_html=True)
    if paper.get("doi"):
        st.write(f"**DOI:** {paper.get('doi')}")
    if display_field:
        st.write(f"**{display_label}:** {get_display_value(paper, display_field)}")
    else:
        display_general_paper_info(paper)


st.markdown("""
<div class="hero">
<div class="hero-title">🧠 ScholarMind</div>
<p class="hero-subtitle">AI Research Assistant for exploring, connecting, and understanding scientific knowledge.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="metric"><b>📚 Research Papers</b><br><span style="font-size:1.7rem;font-weight:800">{len(papers)}</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric"><b>🔎 Research Search</b><br>AI-assisted</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric"><b>🧠 Knowledge Base</b><br>ScholarMind Core</div>', unsafe_allow_html=True)

st.write("")
st.markdown("### 🔎 Ask ScholarMind")
st.markdown('<p class="small">Ask questions about the research papers in the ScholarMind knowledge base.</p>', unsafe_allow_html=True)

question = st.text_area(
    "Research question",
    placeholder="Example: What are the main methodologies used in these research papers?",
    height=130,
    label_visibility="collapsed",
)

st.markdown("**Quick questions**")
q1, q2, q3, q4 = st.columns(4)
with q1:
    if st.button("👤 Authors", use_container_width=True):
        st.session_state.quick_question = "Who are the authors?"
with q2:
    if st.button("🤖 AI Methods", use_container_width=True):
        st.session_state.quick_question = "What AI methods are used?"
with q3:
    if st.button("🧪 Methodology", use_container_width=True):
        st.session_state.quick_question = "What methodologies are used?"
with q4:
    if st.button("📊 Findings", use_container_width=True):
        st.session_state.quick_question = "What are the findings?"

if "quick_question" in st.session_state and not question:
    question = st.session_state.quick_question

if st.button("🚀 Ask ScholarMind", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a research question.")
    else:
        display_field, display_label = get_question_field(question)
        with st.spinner("ScholarMind is analyzing the research knowledge..."):
            try:
                result = unified_assistant(papers, question)
            except Exception as e:
                result = {"type": "error", "answer": str(e)}

        st.markdown("## 💡 ScholarMind Answer")
        result_type = result.get("type", "unknown") if isinstance(result, dict) else "text"
        answer = result.get("answer", result) if isinstance(result, dict) else result

        if result_type == "error":
            st.error(normalize_value(answer))
        elif isinstance(answer, list):
            st.write(f"**{len(answer)} relevant research paper(s) found.**")
            for i, paper in enumerate(answer, start=1):
                with st.container(border=True):
                    display_paper(paper, i, display_field, display_label)
        elif isinstance(answer, dict):
            with st.container(border=True):
                display_paper(answer, display_field=display_field, display_label=display_label)
        else:
            st.markdown('<div class="answer">', unsafe_allow_html=True)
            st.write(normalize_value(answer))
            st.markdown('</div>', unsafe_allow_html=True)

st.divider()
with st.expander("📖 View Research Knowledge Base"):
    if not papers:
        st.info("No research papers are currently available.")
    for i, paper in enumerate(papers, start=1):
        if not isinstance(paper, dict):
            continue
        with st.container(border=True):
            st.markdown(f"### 📄 {i}. {paper.get('title', 'Untitled Research')}")
            for label, key in [("Authors", "authors"), ("Year", "year"), ("DOI", "doi"),
                               ("Methodology", "methodology"), ("Dataset", "dataset"),
                               ("Findings", "findings"), ("Abstract", "abstract")]:
                if paper.get(key):
                    st.write(f"**{label}:** {normalize_value(paper.get(key))}")

st.divider()
st.markdown('<div style="text-align:center;color:#6b7280;padding:1rem">🧠 <b>ScholarMind</b><br>AI Research & Knowledge Management<br><span class="small">Research Assistant Demo</span></div>', unsafe_allow_html=True)
