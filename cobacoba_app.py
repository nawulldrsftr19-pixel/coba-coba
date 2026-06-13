import streamlit as st
from data.kation_data import GOLONGAN_DATA
from data.anion_data import ANION_DATA
from data.quiz_data import QUIZ_DATA
from tabs import panduan, materi, pengujian, reaksi_kation, reaksi_anion, kuis

# ─── PAGE CONFIG ───────────────────────────────────────────
st.set_page_config(
    page_title="KimIA — Analisis Kation & Anion",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CUSTOM CSS ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* Hide default streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0d1117 0%, #0d1117 100%);
}

/* App header banner */
.app-header {
    background: linear-gradient(135deg, #1a0533 0%, #0d1117 50%, #001a2e 100%);
    border: 1px solid #2d3748;
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.app-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(124,58,237,.3) 0%, transparent 70%);
    pointer-events: none;
}
.app-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, #c4b5fd 50%, #67e8f9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0.5rem 0;
}
.app-subtitle {
    color: #94a3b8;
    font-size: 1rem;
    margin-top: 0.5rem;
}
.app-badge {
    display: inline-block;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 0.8rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    font-weight: 600;
}

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
    background: #161b22;
    border-radius: 14px;
    padding: 0.5rem;
    border: 1px solid #2d3748;
}
.stTabs [data-baseweb="tab"] {
    height: auto;
    padding: 0.6rem 1.2rem;
    background: transparent;
    border-radius: 10px;
    color: #94a3b8;
    font-weight: 500;
    font-size: 0.88rem;
    border: none;
    transition: all 0.2s;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #06b6d4) !important;
    color: white !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding-top: 1.5rem;
}

/* Cards */
.info-card {
    background: #161b22;
    border: 1px solid #2d3748;
    border-radius: 16px;
    padding: 1.4rem;
    margin-bottom: 1rem;
    transition: transform 0.2s, border-color 0.2s;
}
.info-card:hover {
    transform: translateY(-2px);
    border-color: #7c3aed;
}
.gradient-card {
    background: linear-gradient(135deg, #161b22 0%, rgba(124,58,237,0.08) 100%);
    border: 1px solid rgba(124,58,237,0.3);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.highlight-card {
    background: linear-gradient(135deg, rgba(124,58,237,0.1), rgba(6,182,212,0.08));
    border: 1px solid rgba(124,58,237,0.25);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 1rem;
}

/* Badges */
.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    font-family: monospace;
    margin-bottom: 0.75rem;
}
.badge-gol1 { background: rgba(124,58,237,.2); color: #c4b5fd; border: 1px solid rgba(124,58,237,.4); }
.badge-gol2 { background: rgba(6,182,212,.2); color: #67e8f9; border: 1px solid rgba(6,182,212,.4); }
.badge-gol3 { background: rgba(245,158,11,.2); color: #fcd34d; border: 1px solid rgba(245,158,11,.4); }
.badge-gol4 { background: rgba(16,185,129,.2); color: #6ee7b7; border: 1px solid rgba(16,185,129,.4); }
.badge-gol5 { background: rgba(239,68,68,.2); color: #fca5a5; border: 1px solid rgba(239,68,68,.4); }
.badge-anion { background: rgba(236,72,153,.2); color: #f9a8d4; border: 1px solid rgba(236,72,153,.4); }

/* Reaction equation box */
.rxn-box {
    background: rgba(6,182,212,0.08);
    border: 1px solid rgba(6,182,212,0.25);
    border-radius: 10px;
    padding: 0.7rem 1rem;
    font-family: monospace;
    font-size: 0.85rem;
    color: #67e8f9;
    margin-top: 0.5rem;
    word-break: break-all;
}

/* Tube animation container */
.tube-rack {
    background: rgba(0,0,0,0.3);
    border-radius: 0 0 14px 14px;
    padding: 1.5rem 1rem;
    display: flex;
    justify-content: center;
    gap: 2rem;
    align-items: flex-end;
    min-height: 160px;
}

/* Step cards for panduan */
.step-card {
    background: #161b22;
    border: 1px solid #2d3748;
    border-radius: 14px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}
.step-num {
    font-family: monospace;
    font-size: 2rem;
    font-weight: 700;
    color: rgba(124,58,237,0.3);
    line-height: 1;
    margin-bottom: 0.5rem;
}

/* Quiz styling */
.quiz-option {
    background: #161b22;
    border: 1.5px solid #2d3748;
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    margin: 0.5rem 0;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 0.95rem;
    color: #f1f5f9;
}
.quiz-correct {
    border-color: #10b981 !important;
    background: rgba(16,185,129,0.12) !important;
    color: #6ee7b7 !important;
}
.quiz-wrong {
    border-color: #ef4444 !important;
    background: rgba(239,68,68,0.12) !important;
    color: #fca5a5 !important;
}
.explanation-box {
    background: rgba(6,182,212,0.08);
    border: 1px solid rgba(6,182,212,0.2);
    border-radius: 10px;
    padding: 1rem;
    color: #67e8f9;
    font-size: 0.88rem;
    line-height: 1.6;
    margin-top: 1rem;
}

/* Metric overrides */
[data-testid="metric-container"] {
    background: #161b22;
    border: 1px solid #2d3748;
    border-radius: 12px;
    padding: 1rem;
}

/* Dataframe / table */
.stDataFrame {
    border: 1px solid #2d3748;
    border-radius: 12px;
    overflow: hidden;
}

/* Button overrides */
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    color: white;
    border: none;
    border-radius: 10px;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    padding: 0.6rem 1.5rem;
    transition: all 0.2s;
}
.stButton > button:hover {
    opacity: 0.85;
    transform: translateY(-1px);
}

/* Selectbox */
.stSelectbox > div > div {
    background: #161b22;
    border-color: #2d3748;
    color: #f1f5f9;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #161b22;
    border-right: 1px solid #2d3748;
}

/* Section headers */
.section-h2 {
    font-size: 1.8rem;
    font-weight: 700;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

/* Ion chip */
.ion-chip {
    display: inline-block;
    background: #1f2937;
    border: 1px solid #2d3748;
    border-radius: 8px;
    padding: 0.25rem 0.75rem;
    font-family: monospace;
    font-size: 0.82rem;
    color: #f1f5f9;
    margin: 0.2rem;
}

/* Divider */
.custom-divider {
    border: none;
    border-top: 1px solid #2d3748;
    margin: 1.5rem 0;
}

/* Color swatch inline */
.swatch {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Progress bar custom */
.prog-wrap {
    background: #1f2937;
    border-radius: 999px;
    height: 8px;
    margin-bottom: 1.5rem;
    overflow: hidden;
}
.prog-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    transition: width 0.4s ease;
}

/* Score ring */
.score-container {
    text-align: center;
    padding: 2rem;
    background: #161b22;
    border: 1px solid #2d3748;
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

# ─── APP HEADER ────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div class="app-badge">⚗️ Aplikasi Kimia Analitik</div>
    <div class="app-title">Kation &amp; Anion</div>
    <div class="app-subtitle">Panduan lengkap analisis kualitatif ion dalam larutan</div>
</div>
""", unsafe_allow_html=True)

# ─── MAIN TABS ─────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠  Panduan",
    "📚  Materi",
    "🧪  Pengujian",
    "⚗️  Reaksi Kation",
    "🔬  Reaksi Anion",
    "🎯  Kuis",
])

with tab1:
    panduan.render()

with tab2:
    materi.render(GOLONGAN_DATA, ANION_DATA)

with tab3:
    pengujian.render()

with tab4:
    reaksi_kation.render(GOLONGAN_DATA)

with tab5:
    reaksi_anion.render(ANION_DATA)

with tab6:
    kuis.render(QUIZ_DATA)
