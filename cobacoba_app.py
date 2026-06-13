import streamlit as st

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Glow ion — Analisis Kation & Anion",
    page_icon="⚗️",
    layout="wide",
)

import streamlit as st

# CSS hijau + transisi halus
st.markdown("""
<style>
:root {
  --bg-light: #e8f5e9;   /* hijau muda (mode terang) */
  --bg-dark:  #004d40;   /* hijau tua (mode gelap) */
  --text-light: #1b1b1b; /* teks gelap */
  --text-dark:  #f1f5f9; /* teks terang */
}

/* default: terang */
html, body, [data-testid="stApp"] {
  background-color: var(--bg-light) !important;
  color: var(--text-light) !important;
  font-family: 'Space Grotesk', sans-serif;
  transition: background-color 0.6s ease, color 0.6s ease; /* transisi halus */
}

/* kotak langkah */
.step-box {
  background: #2e7d32;   /* hijau solid */
  color: #f1f5f9;
  border-radius: 12px;
  padding: 1rem 1.25rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.25);
  transition: background 0.6s ease, color 0.6s ease;
}
.step-box strong {
  color: #ffeb3b; /* aksen kuning */
}
</style>
""", unsafe_allow_html=True)

# Toggle mode gelap/terang
mode = st.radio("Pilih tema:", ["Terang", "Gelap"], horizontal=True)

if mode == "Gelap":
    st.markdown("""
    <style>
    html, body, [data-testid="stApp"] {
      background-color: var(--bg-dark) !important;
      color: var(--text-dark) !important;
    }
    .step-box {
      background: #1b5e20; /* hijau gelap untuk kotak */
      color: #f1f5f9;
    }
    </style>
    """, unsafe_allow_html=True)

# ─── CUSTOM CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
  --bg:      #0d1117;
  --surface: #161b22;
  --surface2:#1f2937;
  --border:  #2d3748;
  --accent1: #7c3aed;
  --accent2: #06b6d4;
  --accent3: #f59e0b;
  --accent4: #10b981;
  --accent5: #ef4444;
  --accent6: #ec4899;
  --text:    #f1f5f9;
  --muted:   #94a3b8;
}

[data-testid="stSidebar"] { display: none; }
[data-testid="stHeader"]  { display: none; }
#MainMenu, footer         { display: none; }

.block-container {
  padding-top: 0 !important;
  padding-bottom: 2rem !important;
  max-width: 1200px !important;
}

/* ── HEADER ── */
.app-header {
  background: linear-gradient(135deg, #0d1117 0%, #1a0533 50%, #0d1117 100%);
  border-bottom: 1px solid #2d3748;
  padding: 2.5rem 2rem 2rem;
  text-align: center;
  margin: -1rem -1rem 2rem -1rem;
  position: relative;
}
.app-header::before {
  content:'';
  position:absolute;
  inset:0;
  background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(124,58,237,.35) 0%, transparent 70%);
  pointer-events:none;
}
.header-badge {
  display: inline-block;
  background: linear-gradient(90deg, #7c3aed, #06b6d4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-family: 'JetBrains Mono', monospace;
  font-size: .75rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  margin-bottom: .75rem;
}
.app-header h1 {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(2rem,5vw,3.5rem);
  background: linear-gradient(135deg, #fff 0%, #c4b5fd 50%, #67e8f9 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.1;
  margin: 0;
}
.app-header p { color: #94a3b8; margin-top: .5rem; font-size: .95rem; }

/* ── CARDS ── */
.card {
  background: #161b22;
  border: 1px solid #2d3748;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.25rem;
}
.card-gradient {
  background: linear-gradient(135deg, #001f3f 0%, rgba(124,58,237,.08) 100%);
  border-color: rgba(124,58,237,.3);
  box-shadow: 0 0 0 1px rgba(124,58,237,.2), 0 8px 32px rgba(124,58,237,.15);
}
.highlight-box {
  background: linear-gradient(135deg,rgba(124,58,237,.1),rgba(6,182,212,.08));
  border: 1px solid rgba(124,58,237,.25);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  margin-bottom: 1rem;
}

/* ── BADGES ── */
.gol-badge {
  display:inline-block; padding:.25rem .75rem; border-radius:999px;
  font-size:.78rem; font-weight:600;
  font-family:'JetBrains Mono',monospace; margin-bottom:.75rem;
}
.gol1 { background:rgba(124,58,237,.2);color:#c4b5fd;border:1px solid rgba(124,58,237,.4); }
.gol2 { background:rgba(6,182,212,.2);color:#67e8f9;border:1px solid rgba(6,182,212,.4); }
.gol3 { background:rgba(245,158,11,.2);color:#fcd34d;border:1px solid rgba(245,158,11,.4); }
.gol4 { background:rgba(16,185,129,.2);color:#6ee7b7;border:1px solid rgba(16,185,129,.4); }
.gol5 { background:rgba(239,68,68,.2);color:#fca5a5;border:1px solid rgba(239,68,68,.4); }
.anion-badge { background:rgba(236,72,153,.2);color:#f9a8d4;border:1px solid rgba(236,72,153,.4); }

/* ── ION CHIPS ── */
.ion-chips { display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.75rem; }
.ion-chip {
  padding:.3rem .8rem; border-radius:8px;
  font-family:'JetBrains Mono',monospace; font-size:.82rem;
  background:#1f2937; border:1px solid #2d3748; color:#f1f5f9;
  display:inline-block;
}

/* ── REACTION EQ ── */
.rxn-eq {
  font-family:'JetBrains Mono',monospace; font-size:.78rem;
  color:#67e8f9; background:rgba(6,182,212,.08);
  border:1px solid rgba(6,182,212,.2); border-radius:8px;
  padding:.6rem .8rem; margin-top:.5rem;
  word-break:break-all; line-height:1.6;
}

/* ── STEP CARDS ── */
.step-card {
  background:#161b22; border:1px solid #2d3748;
  border-radius:14px; padding:1.25rem;
  position:relative; overflow:hidden;
}
.step-card::before {
  content:''; position:absolute;
  top:0;left:0;right:0; height:3px;
}
.step-card-1::before{background:linear-gradient(90deg,#7c3aed,#06b6d4);}
.step-card-2::before{background:linear-gradient(90deg,#06b6d4,#10b981);}
.step-card-3::before{background:linear-gradient(90deg,#10b981,#f59e0b);}
.step-card-4::before{background:linear-gradient(90deg,#f59e0b,#ef4444);}
.step-card-5::before{background:linear-gradient(90deg,#ef4444,#ec4899);}
.step-card-6::before{background:linear-gradient(90deg,#ec4899,#7c3aed);}
.step-num {
  font-family:'JetBrains Mono',monospace; font-size:2rem;
  font-weight:700; color:rgba(124,58,237,.3); line-height:1; margin-bottom:.5rem;
}
.step-card h3 { color:#f1f5f9; font-size:1rem; margin:.4rem 0 .3rem; }
.step-card p  { color:#94a3b8; font-size:.88rem; line-height:1.6; margin:0; }

/* ── INFO PILL ── */
.info-pill {
  display:inline-block; background:rgba(124,58,237,.15);
  border:1px solid rgba(124,58,237,.3); color:#c4b5fd;
  border-radius:999px; padding:.4rem 1.2rem; font-size:.85rem;
}

/* ── GRADIENT HEADINGS ── */
.grad-h2 {
  font-family:'DM Serif Display',serif; font-size:1.6rem; margin-bottom:1rem;
  background:linear-gradient(90deg,#7c3aed,#06b6d4);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.muted-p { color:#94a3b8; line-height:1.7; font-size:.95rem; }

/* ── TABLE ── */
.styled-table { width:100%; border-collapse:collapse; font-size:.88rem; }
.styled-table thead { background:linear-gradient(90deg,rgba(124,58,237,.25),rgba(6,182,212,.15)); }
.styled-table th {
  padding:.85rem 1rem; text-align:left; font-weight:600; font-size:.8rem;
  letter-spacing:.05em; text-transform:uppercase; color:#67e8f9;
}
.styled-table td {
  padding:.75rem 1rem; border-top:1px solid rgba(255,255,255,.05);
  color:#94a3b8; vertical-align:top; line-height:1.5;
}
.table-wrap {
  overflow-x:auto; border-radius:12px;
  border:1px solid #2d3748; background:#161b22;
}

/* ── TUBE ANIMATION ── */
.tube-rack {
  display:flex; justify-content:center; gap:2rem; flex-wrap:wrap;
  padding:1.5rem 1rem; background:linear-gradient(180deg,rgba(0,0,0,.3),rgba(0,0,0,.1));
  border-radius:14px; min-height:170px; align-items:flex-end; margin-bottom:1rem;
}
.tube-unit { display:flex; flex-direction:column; align-items:center; gap:.4rem; }
.tube-cap {
  width:44px; height:8px; background:rgba(255,255,255,.15);
  border-radius:4px 4px 0 0; border:1px solid rgba(255,255,255,.2);
}
.tube-body {
  width:40px; border:2px solid rgba(255,255,255,.2);
  border-top:none; border-radius:0 0 20px 20px;
  position:relative; overflow:hidden;
  background:rgba(255,255,255,.03);
}
.tube-name {
  font-size:.7rem; font-family:'JetBrains Mono',monospace;
  color:#94a3b8; text-align:center; max-width:70px;
  word-break:break-word; line-height:1.3;
}

/* ── REACTION CARD ── */
.rxn-card {
  background:#161b22; border:1px solid #2d3748;
  border-radius:16px; overflow:hidden; margin-bottom:.75rem;
}
.rxn-header {
  padding:.9rem 1.2rem; display:flex;
  justify-content:space-between; align-items:center;
}
.rxn-title { font-weight:600; font-size:1rem; color:#f1f5f9; }
.rxn-reagent { font-size:.75rem; color:#94a3b8; font-family:'JetBrains Mono',monospace; }
.obs-badge {
  display:inline-flex; align-items:center; gap:.4rem;
  padding:.3rem .7rem; border-radius:999px; font-size:.75rem; margin-top:.5rem; border:1px solid;
}

/* ── QUIZ ── */
.quiz-question {
  font-size:1.1rem; font-weight:600; color:#f1f5f9;
  line-height:1.5; margin-bottom:1rem;
}
.quiz-progress {
  background:#1f2937; border-radius:999px; height:6px; overflow:hidden; margin-bottom:1rem;
}
.quiz-progress-fill {
  height:100%; border-radius:999px;
  background:linear-gradient(90deg,#7c3aed,#06b6d4);
}
.explanation-box {
  background:rgba(6,182,212,.08); border:1px solid rgba(6,182,212,.25);
  border-radius:12px; padding:1rem 1.25rem; margin-top:.75rem; color:#94a3b8; font-size:.9rem;
}
.score-circle {
  width:140px; height:140px; border-radius:50%;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  font-family:'JetBrains Mono',monospace; margin:0 auto 1rem;
}
.score-num { font-size:2.5rem; font-weight:700; color:#f1f5f9; line-height:1; }
.score-label { font-size:.85rem; color:#94a3b8; }

/* ── STBUTTON OVERRIDE ── */
div[data-testid="stButton"] > button {
  font-family:'Space Grotesk',sans-serif; border-radius:10px;
  transition:all .2s; font-weight:500;
}
</style>
""", unsafe_allow_html=True)

# ─── SESSION STATE ─────────────────────────────────────────────────────────────
if "tab"          not in st.session_state: st.session_state.tab          = "🏠 Panduan"
if "materi_sub"   not in st.session_state: st.session_state.materi_sub   = "Gol. I"
if "test_sub"     not in st.session_state: st.session_state.test_sub     = "Golongan I"
if "rxk_sub"      not in st.session_state: st.session_state.rxk_sub      = "Gol. I"
if "quiz_idx"     not in st.session_state: st.session_state.quiz_idx     = 0
if "quiz_score"   not in st.session_state: st.session_state.quiz_score   = 0
if "quiz_done"    not in st.session_state: st.session_state.quiz_done    = False
if "quiz_answered"not in st.session_state: st.session_state.quiz_answered= False
if "selected_opt" not in st.session_state: st.session_state.selected_opt = None
if "anim_states"  not in st.session_state: st.session_state.anim_states  = {}

# ─── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
  <div class="header-badge">⚗️ Aplikasi Kimia Analitik</div>
  <h1>Kation &amp; Anion</h1>
  <p>Panduan lengkap analisis kualitatif ion dalam larutan</p>
</div>
""", unsafe_allow_html=True)

# ─── TAB NAVIGATION ───────────────────────────────────────────────────────────
TABS = ["🏠 Panduan", "📚 Materi", "🧪 Pengujian", "⚗️ Reaksi Kation", "🔬 Reaksi Anion", "🎯 Kuis"]
cols = st.columns(len(TABS))
for i, (col, label) in enumerate(zip(cols, TABS)):
    with col:
        if st.button(label, key=f"nav_{i}", use_container_width=True,
                     type="primary" if st.session_state.tab == label else "secondary"):
            st.session_state.tab = label
            st.rerun()

st.markdown("<hr style='border-color:#2d3748;margin:0 0 1.5rem'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HELPER
# ══════════════════════════════════════════════════════════════════════════════
def card(content, extra_class=""):
    st.markdown(f'<div class="card {extra_class}">{content}</div>', unsafe_allow_html=True)

def tube_svg(liquid_color, sediment_color=None, pct=60):
    """Return SVG of an animated test-tube."""
    h = 100
    liq_h = int(h * pct / 100)
    sed_h = 18 if sediment_color else 0
    sed_col = sediment_color or "transparent"
    return f"""
    <svg width="44" height="120" viewBox="0 0 44 120" xmlns="http://www.w3.org/2000/svg">
      <!-- tube outline -->
      <rect x="2" y="0" width="40" height="100" rx="0" ry="0" fill="rgba(255,255,255,.03)" stroke="rgba(255,255,255,.22)" stroke-width="2"/>
      <ellipse cx="22" cy="100" rx="20" ry="10" fill="rgba(255,255,255,.03)" stroke="rgba(255,255,255,.22)" stroke-width="2"/>
      <!-- liquid -->
      <clipPath id="clip{abs(hash(liquid_color))}">
        <rect x="2" y="{100-liq_h}" width="40" height="{liq_h}"/>
        <ellipse cx="22" cy="100" rx="20" ry="10"/>
      </clipPath>
      <g clip-path="url(#clip{abs(hash(liquid_color))})">
        <rect x="2" y="{100-liq_h}" width="40" height="{liq_h}" fill="{liquid_color}"/>
        <ellipse cx="22" cy="100" rx="20" ry="10" fill="{liquid_color}"/>
      </g>
      <!-- sediment -->
      <clipPath id="clips{abs(hash(sed_col))}">
        <rect x="2" y="{100-sed_h}" width="40" height="{sed_h}"/>
        <ellipse cx="22" cy="100" rx="20" ry="10"/>
      </clipPath>
      <g clip-path="url(#clips{abs(hash(sed_col))})">
        <rect x="2" y="{100-sed_h}" width="40" height="{sed_h}" fill="{sed_col}"/>
        <ellipse cx="22" cy="100" rx="20" ry="10" fill="{sed_col}"/>
      </g>
      <!-- shine -->
      <rect x="8" y="5" width="5" height="90" rx="2" fill="rgba(255,255,255,.09)"/>
    </svg>"""

def render_tube_pair(key, before, after, ion, reagent, equation, obs, header_color):
    """Render a reaction card with before/after tubes."""
    animated = st.session_state.anim_states.get(key, False)
    liq_b   = before["liquid"]
    sed_b   = before.get("sediment")
    liq_a   = after["liquid"]
    sed_a   = after.get("sediment")

    before_svg = tube_svg(liq_b, sed_b)
    after_svg  = tube_svg(liq_a, sed_a) if animated else tube_svg(liq_b, None, 30)

    st.markdown(f"""
    <div class="rxn-card">
      <div class="rxn-header" style="background:linear-gradient(135deg,{header_color}22,{header_color}11);border-bottom:1px solid {header_color}33;">
        <div>
          <div class="rxn-title">{ion}</div>
          <div class="rxn-reagent">+ {reagent}</div>
        </div>
        <div style="font-size:1.4rem;">⚗️</div>
      </div>
      <div class="tube-rack">
        <div class="tube-unit">{before_svg}<div class="tube-name">Sebelum</div></div>
        <div style="color:#94a3b8;font-size:1.4rem;align-self:center;">→</div>
        <div class="tube-unit">{after_svg}<div class="tube-name">Sesudah</div></div>
      </div>
    """, unsafe_allow_html=True)

    if animated:
        st.markdown(f"""
        <div style="padding:.5rem 1.2rem 1rem;">
          <div class="rxn-eq">{equation}</div>
          <span class="obs-badge" style="background:{header_color}22;border-color:{header_color}44;color:{header_color};">
            👁 {obs}
          </span>
        </div>""", unsafe_allow_html=True)
    else:
        btn_col, _ = st.columns([1, 3])
        with btn_col:
            if st.button("▶ Animasi", key=f"btn_{key}"):
                st.session_state.anim_states[key] = True
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════════════════════
RX_KATION = {
    "Gol. I": [
        {"ion":"Ag⁺","reagent":"HCl 2M","equation":"Ag⁺ + Cl⁻ → AgCl↓","obs":"Endapan putih","header":"#7c3aed",
         "before":{"liquid":"#e8f4fd","sediment":None},"after":{"liquid":"#c8dff0","sediment":"#e2e8f0"}},
        {"ion":"Ag⁺","reagent":"NH₄OH berlebih","equation":"AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻","obs":"AgCl larut","header":"#7c3aed",
         "before":{"liquid":"#c8dff0","sediment":"#e2e8f0"},"after":{"liquid":"#d4f1d4","sediment":None}},
        {"ion":"Ag⁺","reagent":"K₂CrO₄","equation":"2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄↓","obs":"Endapan merah bata","header":"#7c3aed",
         "before":{"liquid":"#e8f4fd","sediment":None},"after":{"liquid":"#fde8d8","sediment":"#c2410c"}},
        {"ion":"Hg₂²⁺","reagent":"HCl 2M","equation":"Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓","obs":"Endapan putih","header":"#06b6d4",
         "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#e0f2fe","sediment":"#f1f5f9"}},
        {"ion":"Hg₂²⁺","reagent":"NH₄OH","equation":"Hg₂Cl₂ + 2NH₃ → Hg↓ + HgNH₂Cl↓ + NH₄⁺ + Cl⁻","obs":"Endapan hitam","header":"#06b6d4",
         "before":{"liquid":"#e0f2fe","sediment":"#f1f5f9"},"after":{"liquid":"#94a3b8","sediment":"#1e293b"}},
        {"ion":"Pb²⁺","reagent":"HCl 2M","equation":"Pb²⁺ + 2Cl⁻ → PbCl₂↓","obs":"Endapan putih","header":"#f59e0b",
         "before":{"liquid":"#fffbeb","sediment":None},"after":{"liquid":"#fef3c7","sediment":"#e2e8f0"}},
        {"ion":"Pb²⁺","reagent":"Air panas","equation":"PbCl₂(s) → Pb²⁺(aq) + 2Cl⁻(aq)","obs":"Endapan larut","header":"#f59e0b",
         "before":{"liquid":"#fef3c7","sediment":"#e2e8f0"},"after":{"liquid":"#fef3c7","sediment":None}},
        {"ion":"Pb²⁺","reagent":"K₂CrO₄","equation":"Pb²⁺ + CrO₄²⁻ → PbCrO₄↓","obs":"Endapan kuning","header":"#f59e0b",
         "before":{"liquid":"#fef3c7","sediment":None},"after":{"liquid":"#fef08a","sediment":"#ca8a04"}},
    ],
    "Gol. II": [
        {"ion":"Cu²⁺","reagent":"H₂S/HCl","equation":"Cu²⁺ + S²⁻ → CuS↓","obs":"Endapan hitam","header":"#0891b2",
         "before":{"liquid":"#bfdbfe","sediment":None},"after":{"liquid":"#7dd3fc","sediment":"#1e293b"}},
        {"ion":"Cu²⁺","reagent":"NH₄OH berlebih","equation":"Cu²⁺ + 4NH₃ → [Cu(NH₃)₄]²⁺","obs":"Larutan biru tua","header":"#0891b2",
         "before":{"liquid":"#bae6fd","sediment":None},"after":{"liquid":"#1d4ed8","sediment":None}},
        {"ion":"Bi³⁺","reagent":"H₂S/HCl","equation":"2Bi³⁺ + 3S²⁻ → Bi₂S₃↓","obs":"Endapan hitam","header":"#7c3aed",
         "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#d1fae5","sediment":"#1e293b"}},
        {"ion":"Bi³⁺","reagent":"SnCl₂ basa","equation":"2Bi³⁺ + 3Sn²⁺ → 2Bi↓ + 3Sn⁴⁺","obs":"Endapan hitam (Bi)","header":"#7c3aed",
         "before":{"liquid":"#e0f2fe","sediment":None},"after":{"liquid":"#94a3b8","sediment":"#0f172a"}},
        {"ion":"Cd²⁺","reagent":"H₂S","equation":"Cd²⁺ + S²⁻ → CdS↓","obs":"Endapan kuning","header":"#ca8a04",
         "before":{"liquid":"#fffbeb","sediment":None},"after":{"liquid":"#fef3c7","sediment":"#eab308"}},
        {"ion":"Sn²⁺","reagent":"HgCl₂","equation":"Sn²⁺ + 2HgCl₂ → SnCl₄ + Hg₂Cl₂↓","obs":"Putih → abu → hitam","header":"#4b5563",
         "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#94a3b8","sediment":"#475569"}},
    ],
    "Gol. III": [
        {"ion":"Fe³⁺","reagent":"KSCN","equation":"Fe³⁺ + 3SCN⁻ → [Fe(SCN)₃]","obs":"Larutan merah darah","header":"#dc2626",
         "before":{"liquid":"#fde68a","sediment":None},"after":{"liquid":"#b91c1c","sediment":None}},
        {"ion":"Fe³⁺","reagent":"NaOH","equation":"Fe³⁺ + 3OH⁻ → Fe(OH)₃↓","obs":"Endapan coklat merah","header":"#dc2626",
         "before":{"liquid":"#fde68a","sediment":None},"after":{"liquid":"#fed7aa","sediment":"#b45309"}},
        {"ion":"Al³⁺","reagent":"NaOH","equation":"Al³⁺ + 3OH⁻ → Al(OH)₃↓","obs":"Endapan putih gelatin","header":"#9ca3af",
         "before":{"liquid":"#f8fafc","sediment":None},"after":{"liquid":"#e2e8f0","sediment":"#f1f5f9"}},
        {"ion":"Cr³⁺","reagent":"NaOH+H₂O₂","equation":"2Cr³⁺ + 3H₂O₂ + 10OH⁻ → 2CrO₄²⁻ + 8H₂O","obs":"Larutan kuning","header":"#065f46",
         "before":{"liquid":"#6ee7b7","sediment":None},"after":{"liquid":"#ca8a04","sediment":None}},
        {"ion":"Mn²⁺","reagent":"NaBiO₃/HNO₃","equation":"2Mn²⁺ + 5BiO₃⁻ + 14H⁺ → 2MnO₄⁻ + 5Bi³⁺ + 7H₂O","obs":"Larutan ungu (MnO₄⁻)","header":"#7e22ce",
         "before":{"liquid":"#fce7f3","sediment":None},"after":{"liquid":"#7c3aed","sediment":None}},
        {"ion":"Ni²⁺","reagent":"Dimetilglioksim","equation":"Ni²⁺ + 2HDMG → Ni(HDMG)₂↓ + 2H⁺","obs":"Endapan merah","header":"#be185d",
         "before":{"liquid":"#d1fae5","sediment":None},"after":{"liquid":"#fce7f3","sediment":"#e11d48"}},
        {"ion":"Co²⁺","reagent":"KSCN + aseton","equation":"Co²⁺ + 4SCN⁻ → [Co(SCN)₄]²⁻","obs":"Larutan biru","header":"#1d4ed8",
         "before":{"liquid":"#fce7f3","sediment":None},"after":{"liquid":"#3b82f6","sediment":None}},
        {"ion":"Zn²⁺","reagent":"K₄[Fe(CN)₆]","equation":"2Zn²⁺ + [Fe(CN)₆]⁴⁻ → Zn₂[Fe(CN)₆]↓","obs":"Endapan putih","header":"#475569",
         "before":{"liquid":"#f0fdf4","sediment":None},"after":{"liquid":"#dcfce7","sediment":"#f1f5f9"}},
    ],
    "Gol. IV": [
        {"ion":"Ba²⁺","reagent":"K₂CrO₄","equation":"Ba²⁺ + CrO₄²⁻ → BaCrO₄↓","obs":"Endapan kuning","header":"#d97706",
         "before":{"liquid":"#fffbeb","sediment":None},"after":{"liquid":"#fef9c3","sediment":"#ca8a04"}},
        {"ion":"Sr²⁺","reagent":"H₂SO₄","equation":"Sr²⁺ + SO₄²⁻ → SrSO₄↓","obs":"Endapan putih halus","header":"#059669",
         "before":{"liquid":"#ecfdf5","sediment":None},"after":{"liquid":"#d1fae5","sediment":"#f1f5f9"}},
        {"ion":"Ca²⁺","reagent":"(NH₄)₂C₂O₄","equation":"Ca²⁺ + C₂O₄²⁻ → CaC₂O₄↓","obs":"Endapan putih","header":"#dc2626",
         "before":{"liquid":"#fef2f2","sediment":None},"after":{"liquid":"#fee2e2","sediment":"#e2e8f0"}},
        {"ion":"Ba²⁺","reagent":"(NH₄)₂CO₃","equation":"Ba²⁺ + CO₃²⁻ → BaCO₃↓","obs":"Endapan putih","header":"#d97706",
         "before":{"liquid":"#fffbeb","sediment":None},"after":{"liquid":"#fef3c7","sediment":"#e2e8f0"}},
    ],
    "Gol. V": [
        {"ion":"NH₄⁺","reagent":"NaOH panas","equation":"NH₄⁺ + OH⁻ → NH₃↑ + H₂O","obs":"Gas NH₃ (bau tajam)","header":"#7c3aed",
         "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#ddd6fe","sediment":None}},
        {"ion":"K⁺","reagent":"Na₃[Co(NO₂)₆]","equation":"2K⁺ + Na⁺ + [Co(NO₂)₆]³⁻ → K₂Na[Co(NO₂)₆]↓","obs":"Endapan kuning","header":"#ca8a04",
         "before":{"liquid":"#fffbeb","sediment":None},"after":{"liquid":"#fef3c7","sediment":"#eab308"}},
        {"ion":"Na⁺","reagent":"Uji nyala","equation":"Na → D-line 589 nm","obs":"Nyala kuning intens","header":"#f59e0b",
         "before":{"liquid":"#fffbeb","sediment":None},"after":{"liquid":"#fde047","sediment":None}},
        {"ion":"Mg²⁺","reagent":"Na₂HPO₄+NH₃","equation":"Mg²⁺ + NH₄⁺ + PO₄³⁻ → MgNH₄PO₄↓","obs":"Endapan putih kristalin","header":"#0891b2",
         "before":{"liquid":"#f0fdf4","sediment":None},"after":{"liquid":"#d1fae5","sediment":"#f1f5f9"}},
    ],
}

RX_ANION = [
    {"ion":"Cl⁻","reagent":"AgNO₃","equation":"Ag⁺ + Cl⁻ → AgCl↓","obs":"Endapan putih, larut NH₄OH","header":"#7c3aed",
     "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#e0f2fe","sediment":"#f1f5f9"}},
    {"ion":"SO₄²⁻","reagent":"BaCl₂/HCl","equation":"Ba²⁺ + SO₄²⁻ → BaSO₄↓","obs":"Endapan putih, tidak larut HCl","header":"#06b6d4",
     "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#e0f2fe","sediment":"#f8fafc"}},
    {"ion":"CO₃²⁻","reagent":"HCl encer","equation":"CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O","obs":"Gelembung gas CO₂","header":"#10b981",
     "before":{"liquid":"#ecfdf5","sediment":None},"after":{"liquid":"#bbf7d0","sediment":None}},
    {"ion":"NO₃⁻","reagent":"FeSO₄+H₂SO₄ pekat","equation":"Fe²⁺ + NO → [Fe(NO)]²⁺","obs":"Cincin coklat di antarmuka","header":"#f59e0b",
     "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#92400e","sediment":None}},
    {"ion":"PO₄³⁻","reagent":"AgNO₃","equation":"3Ag⁺ + PO₄³⁻ → Ag₃PO₄↓","obs":"Endapan kuning","header":"#ec4899",
     "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#fef9c3","sediment":"#ca8a04"}},
    {"ion":"I⁻","reagent":"AgNO₃","equation":"Ag⁺ + I⁻ → AgI↓","obs":"Endapan kuning muda","header":"#eab308",
     "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#fefce8","sediment":"#eab308"}},
    {"ion":"I⁻","reagent":"Cl₂ + kanji","equation":"Cl₂ + 2I⁻ → 2Cl⁻ + I₂; I₂+kanji→biru","obs":"Larutan biru tua","header":"#3b82f6",
     "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#1e3a8a","sediment":None}},
    {"ion":"S²⁻","reagent":"Pb(CH₃COO)₂","equation":"Pb²⁺ + S²⁻ → PbS↓","obs":"Endapan hitam","header":"#94a3b8",
     "before":{"liquid":"#f0f9ff","sediment":None},"after":{"liquid":"#94a3b8","sediment":"#0f172a"}},
    {"ion":"CH₃COO⁻","reagent":"FeCl₃","equation":"3CH₃COO⁻ + Fe³⁺ → Fe(CH₃COO)₃","obs":"Larutan merah coklat","header":"#b45309",
     "before":{"liquid":"#fffbeb","sediment":None},"after":{"liquid":"#92400e","sediment":None}},
]

QUIZ_DATA = [
    {"q":"Reagen apa yang digunakan untuk mengendapkan kation Golongan I?",
     "opts":["H₂SO₄ encer","HCl encer","NaOH","(NH₄)₂S"],"ans":1,
     "exp":"Kation Golongan I (Ag⁺, Hg₂²⁺, Pb²⁺) diendapkan sebagai klorida tidak larut menggunakan HCl encer (2M)."},
    {"q":"Pengendap apa yang terbentuk saat Ag⁺ bereaksi dengan HCl?",
     "opts":["AgNO₃","Ag₂SO₄","AgCl","Ag₂O"],"ans":2,
     "exp":"AgCl (perak klorida) terbentuk sebagai endapan putih yang tidak larut dalam air."},
    {"q":"Apa yang terjadi ketika Hg₂Cl₂ ditambah NH₄OH?",
     "opts":["Larut membentuk larutan bening","Terbentuk endapan putih larut","Terbentuk endapan hitam (Hg)","Tidak terjadi reaksi"],"ans":2,
     "exp":"Hg₂Cl₂ + 2NH₃ → Hg↓ (hitam) + HgNH₂Cl (putih). Campuran ini tampak hitam karena Hg logam."},
    {"q":"Kation Golongan II diendapkan menggunakan?",
     "opts":["HCl dalam suasana asam","H₂S dalam suasana asam","(NH₄)₂CO₃ basa","NaOH berlebih"],"ans":1,
     "exp":"H₂S dialirkan ke dalam larutan yang mengandung HCl 0.3M (asam) untuk mengendapkan kation Golongan II sebagai sulfida."},
    {"q":"Warna larutan Cu²⁺ dalam NH₄OH berlebih adalah?",
     "opts":["Merah","Hijau","Kuning","Biru tua"],"ans":3,
     "exp":"Cu²⁺ + 4NH₃ → [Cu(NH₃)₄]²⁺, kompleks tetraaminatembaga(II) berwarna biru tua (biru intensif)."},
    {"q":"Uji spesifik untuk Fe³⁺ menggunakan?",
     "opts":["KSCN","K₂CrO₄","DMG","Na₂HPO₄"],"ans":0,
     "exp":"KSCN (kalium tiosianat) menghasilkan warna merah darah [Fe(SCN)]²⁺ yang sangat sensitif untuk deteksi Fe³⁺."},
    {"q":"Endapan apa yang terbentuk dari reaksi Pb²⁺ + K₂CrO₄?",
     "opts":["PbSO₄ putih","PbCrO₄ kuning","PbCO₃ putih","PbCl₂ putih"],"ans":1,
     "exp":"Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ berwarna kuning, digunakan sebagai uji konfirmasi Pb²⁺."},
    {"q":"Kation golongan III mana yang bereaksi dengan dimetilglioksim menghasilkan endapan merah?",
     "opts":["Co²⁺","Fe³⁺","Ni²⁺","Zn²⁺"],"ans":2,
     "exp":"Ni²⁺ + 2HDMG → Ni(HDMG)₂↓ merah. Reaksi dengan dimetilglioksim sangat spesifik untuk Ni²⁺."},
    {"q":"Reagen golongan IV untuk mengendapkan Ca²⁺, Sr²⁺, dan Ba²⁺ adalah?",
     "opts":["(NH₄)₂S","HCl","(NH₄)₂CO₃","H₂SO₄"],"ans":2,
     "exp":"(NH₄)₂CO₃ dalam NH₄OH mengendapkan kation Golongan IV sebagai karbonat."},
    {"q":"Uji apa yang digunakan untuk identifikasi NH₄⁺?",
     "opts":["Uji nyala ungu","NaOH panas → bau NH₃","K₂CrO₄","Reagen Mayer"],"ans":1,
     "exp":"NH₄⁺ + OH⁻ → NH₃↑ + H₂O. Gas NH₃ berbau tajam dan membirukan kertas lakmus merah."},
    {"q":"Warna nyala Na⁺ pada uji nyala adalah?",
     "opts":["Violet","Merah","Kuning","Hijau"],"ans":2,
     "exp":"Na⁺ menghasilkan nyala kuning intens pada panjang gelombang 589 nm (garis D natrium)."},
    {"q":"Warna endapan CdS adalah?",
     "opts":["Putih","Hitam","Kuning","Merah"],"ans":2,
     "exp":"CdS (kadmium sulfida) berwarna kuning dan terbentuk saat Cd²⁺ direaksikan dengan H₂S dalam suasana asam."},
    {"q":"Anion apa yang menghasilkan endapan putih dengan AgNO₃ yang larut dalam NH₄OH?",
     "opts":["I⁻","SO₄²⁻","Cl⁻","PO₄³⁻"],"ans":2,
     "exp":"AgCl (putih) larut dalam NH₄OH membentuk [Ag(NH₃)₂]⁺. AgI dan Ag₃PO₄ tidak larut dalam NH₄OH."},
    {"q":"Uji cincin coklat digunakan untuk mengidentifikasi anion?",
     "opts":["SO₄²⁻","Cl⁻","NO₃⁻","CO₃²⁻"],"ans":2,
     "exp":"NO₃⁻ diidentifikasi dengan uji cincin coklat: Fe²⁺ + NO → [Fe(NO)]²⁺ coklat di antarmuka H₂SO₄ pekat."},
    {"q":"Endapan BaSO₄ memiliki sifat?",
     "opts":["Larut dalam HCl encer","Larut dalam HNO₃ encer","Tidak larut dalam asam apapun","Larut dalam air panas"],"ans":2,
     "exp":"BaSO₄ sangat sukar larut dan tidak larut dalam HCl, HNO₃, atau air. Ini yang membedakannya dari BaCO₃."},
    {"q":"Warna larutan yang terbentuk saat Mn²⁺ dioksidasi dengan NaBiO₃/HNO₃?",
     "opts":["Kuning","Ungu","Biru","Merah"],"ans":1,
     "exp":"Mn²⁺ teroksidasi menjadi MnO₄⁻ (permanganat) yang berwarna ungu/violet. Reaksi ini sensitif untuk Mn²⁺."},
    {"q":"Ion apa yang menghasilkan nyala merah karmin pada uji nyala?",
     "opts":["K⁺","Na⁺","Ba²⁺","Sr²⁺"],"ans":3,
     "exp":"Sr²⁺ menghasilkan nyala merah karmin (merah terang). Ba²⁺ hijau, K⁺ violet, Na⁺ kuning."},
    {"q":"Reagen Nessler digunakan untuk mendeteksi?",
     "opts":["K⁺","Na⁺","NH₄⁺","Mg²⁺"],"ans":2,
     "exp":"Reagen Nessler (K₂[HgI₄] dalam KOH) bereaksi dengan NH₄⁺ menghasilkan warna coklat jingga."},
    {"q":"Bagaimana cara membedakan Ag⁺ dan Pb²⁺ dalam endapan klorida?",
     "opts":["Tambah HNO₃","Panaskan dengan air → Pb²⁺ larut","Tambah NaOH","Uji nyala"],"ans":1,
     "exp":"PbCl₂ larut dalam air panas sedangkan AgCl tidak. Filtrat panas + K₂CrO₄ → PbCrO₄ kuning untuk konfirmasi Pb²⁺."},
    {"q":"Apa warna endapan Bi₂S₃?",
     "opts":["Kuning","Putih","Merah","Hitam"],"ans":3,
     "exp":"Bi₂S₃ (bismut(III) sulfida) berwarna hitam, terbentuk dalam suasana asam dengan H₂S."},
]

# ══════════════════════════════════════════════════════════════════════════════
# TAB: PANDUAN
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.tab == "🏠 Panduan":
    st.markdown("""
    <div class="card card-gradient" style="text-align:center;padding:2rem;">
      <div style="font-size:3rem;margin-bottom:1rem;">⚗️</div>
      <div class="grad-h2" style="font-size:2rem;">Selamat Datang di Glow ion</div>
      <p class="muted-p" style="max-width:560px;margin:0 auto 1rem;">
        Platform interaktif untuk mempelajari analisis kualitatif
        <strong style="color:#67e8f9">Kation</strong> (Golongan I–V) dan
        <strong style="color:#f9a8d4">Anion</strong> secara lengkap, visual, dan menyenangkan.
      </p>
      <span class="info-pill">✨ Dibuat untuk mahasiswa kimia &amp; analis laboratorium</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="grad-h2">Cara Menggunakan Aplikasi</div>', unsafe_allow_html=True)

    steps = [
        ("01","📚 Pelajari Materi","Buka Tab <strong>Materi</strong> untuk membaca teori lengkap kation golongan I–V dan anion beserta ciri-ciri, reagen, dan karakteristiknya."),
        ("02","🧪 Ikuti Prosedur Pengujian","Di Tab <strong>Pengujian</strong>, pilih golongan kation dan ikuti tabel prosedur uji sistematis mulai dari uji pendahuluan hingga uji spesifik."),
        ("03","⚗️ Lihat Animasi Reaksi Kation","Tab <strong>Reaksi Kation</strong> menampilkan animasi tabung reaksi berwarna dan persamaan reaksi kimia untuk setiap kation."),
        ("04","🔬 Lihat Animasi Reaksi Anion","Tab <strong>Reaksi Anion</strong> menampilkan animasi tabung reaksi dan reaksi kimia untuk identifikasi anion penting."),
        ("05","🎯 Uji Pemahaman","Kerjakan <strong>Kuis</strong> untuk menguji pemahamanmu. Ada feedback langsung dan penjelasan jawaban."),
        ("06","🔄 Ulang &amp; Kuasai","Navigasi bebas antar tab kapan saja. Kuis bisa diulang untuk meningkatkan skor. Selamat belajar!"),
    ]
    c1, c2 = st.columns(2)
    for i, (num, title, desc) in enumerate(steps):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""
            <div class="step-card step-card-{i+1}">
              <div class="step-num">{num}</div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-top:1.5rem;">
      <div class="grad-h2">Tentang Aplikasi</div>
    """, unsafe_allow_html=True)

    a1, a2 = st.columns(2)
    with a1:
        st.markdown("""
        <h3 style="color:#f1f5f9;font-size:1rem;margin-bottom:.5rem;">🎯 Tujuan</h3>
        <p class="muted-p">Membantu mahasiswa kimia memahami analisis kualitatif kation dan anion melalui visualisasi interaktif, animasi reaksi, dan latihan soal yang komprehensif.</p>
        <h3 style="color:#f1f5f9;font-size:1rem;margin:.75rem 0 .5rem;">📋 Cakupan Materi</h3>
        <ul style="color:#94a3b8;line-height:2;font-size:.9rem;">
          <li>Kation Golongan I: Ag⁺, Hg₂²⁺, Pb²⁺</li>
          <li>Kation Golongan II: Cu²⁺, Bi³⁺, Cd²⁺, Sn²⁺, As³⁺</li>
          <li>Kation Golongan III: Fe³⁺, Al³⁺, Cr³⁺, Mn²⁺, Ni²⁺, Co²⁺, Zn²⁺</li>
          <li>Kation Golongan IV: Ca²⁺, Sr²⁺, Ba²⁺</li>
          <li>Kation Golongan V: Mg²⁺, K⁺, Na⁺, NH₄⁺</li>
          <li>Anion: Cl⁻, SO₄²⁻, CO₃²⁻, NO₃⁻, PO₄³⁻, I⁻, S²⁻</li>
        </ul>
        """, unsafe_allow_html=True)
    with a2:
        st.markdown("""
        <h3 style="color:#f1f5f9;font-size:1rem;margin-bottom:.5rem;">🛠️ Fitur Utama</h3>
        <ul style="color:#94a3b8;line-height:2;font-size:.9rem;">
          <li>Animasi tabung reaksi berwarna real-time</li>
          <li>Tabel prosedur pengujian sistematis</li>
          <li>Persamaan reaksi kimia lengkap</li>
          <li>Kuis interaktif dengan feedback instan</li>
          <li>Navigasi mudah antar golongan</li>
          <li>Tampilan responsif</li>
        </ul>
        <div class="highlight-box" style="margin-top:1rem;">
          <strong style="color:#f59e0b;">⚠️ Catatan:</strong>
          <p class="muted-p" style="margin:0;font-size:.88rem;">Aplikasi ini bersifat edukatif. Selalu ikuti prosedur keselamatan laboratorium saat melakukan percobaan nyata.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB: MATERI
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.tab == "📚 Materi":
    st.markdown('<div class="grad-h2">Materi Kation &amp; Anion</div>', unsafe_allow_html=True)

    sub_opts = ["Gol. I","Gol. II","Gol. III","Gol. IV","Gol. V","Anion"]
    sub_cols = st.columns(len(sub_opts))
    for i, (col, label) in enumerate(zip(sub_cols, sub_opts)):
        with col:
            if st.button(label, key=f"msub_{i}", use_container_width=True,
                         type="primary" if st.session_state.materi_sub==label else "secondary"):
                st.session_state.materi_sub = label
                st.rerun()

    sub = st.session_state.materi_sub

    if sub == "Gol. I":
        st.markdown('<span class="gol-badge gol1">Golongan I — Klorida Tidak Larut</span>', unsafe_allow_html=True)
        st.markdown("""<div class="card">
          <h3 style="color:#f1f5f9;font-size:1rem;">Prinsip Pemisahan</h3>
          <p class="muted-p">Kation Golongan I diendapkan sebagai <strong style="color:#67e8f9">klorida tidak larut</strong> dengan penambahan HCl encer ke larutan sampel.</p>
          <p class="muted-p"><strong>Reagen pengendap:</strong> HCl encer (2M)</p>
          <div class="ion-chips">
            <span class="ion-chip">Ag⁺ (Perak)</span>
            <span class="ion-chip">Hg₂²⁺ (Merkuri I)</span>
            <span class="ion-chip">Pb²⁺ (Timbal)</span>
          </div></div>""", unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        with c1:
            st.markdown("""<div class="card"><span class="gol-badge gol1">Ag⁺</span>
              <h3 style="color:#f1f5f9;font-size:1rem;">Ion Perak</h3>
              <p class="muted-p"><strong>Endapan:</strong> AgCl — putih</p>
              <p class="muted-p"><strong>Uji spesifik:</strong> Larut dalam NH₄OH berlebih</p>
              <p class="muted-p"><strong>Pengamatan:</strong> Dengan K₂CrO₄ → AgCrO₄ merah bata</p>
              <div class="rxn-eq">Ag⁺ + Cl⁻ → AgCl↓ (putih)</div></div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class="card"><span class="gol-badge gol1">Hg₂²⁺</span>
              <h3 style="color:#f1f5f9;font-size:1rem;">Ion Merkuri(I)</h3>
              <p class="muted-p"><strong>Endapan:</strong> Hg₂Cl₂ — putih</p>
              <p class="muted-p"><strong>Uji spesifik:</strong> + NH₄OH → hitam</p>
              <p class="muted-p"><strong>Pengamatan:</strong> Berubah hitam saat ditambah amonia</p>
              <div class="rxn-eq">Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓ (putih)</div></div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class="card"><span class="gol-badge gol1">Pb²⁺</span>
              <h3 style="color:#f1f5f9;font-size:1rem;">Ion Timbal</h3>
              <p class="muted-p"><strong>Endapan:</strong> PbCl₂ — putih</p>
              <p class="muted-p"><strong>Uji spesifik:</strong> Larut dalam air panas</p>
              <p class="muted-p"><strong>Pengamatan:</strong> Endapan larut saat dipanaskan</p>
              <div class="rxn-eq">Pb²⁺ + 2Cl⁻ → PbCl₂↓ (putih)</div></div>""", unsafe_allow_html=True)

    elif sub == "Gol. II":
        st.markdown('<span class="gol-badge gol2">Golongan II — Sulfida dalam Suasana Asam</span>', unsafe_allow_html=True)
        st.markdown("""<div class="card">
          <h3 style="color:#f1f5f9;font-size:1rem;">Prinsip Pemisahan</h3>
          <p class="muted-p">Kation Golongan II diendapkan sebagai <strong style="color:#67e8f9">sulfida</strong> dengan mengalirkan gas H₂S dalam suasana asam (HCl 0.3M).</p>
          <p class="muted-p"><strong>Reagen pengendap:</strong> H₂S gas / (NH₄)₂S dalam HCl encer</p>
          <div class="ion-chips">
            <span class="ion-chip">Cu²⁺</span><span class="ion-chip">Bi³⁺</span>
            <span class="ion-chip">Cd²⁺</span><span class="ion-chip">Hg²⁺</span>
            <span class="ion-chip">Sn²⁺/Sn⁴⁺</span><span class="ion-chip">As³⁺/As⁵⁺</span>
            <span class="ion-chip">Sb³⁺</span>
          </div></div>""", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        ions_g2 = [
            ("gol2","Cu²⁺ — Tembaga","CuS — hitam","Larut dalam HNO₃ panas → biru dalam NH₄OH berlebih","Cu²⁺ + S²⁻ → CuS↓ (hitam)"),
            ("gol2","Bi³⁺ — Bismut","Bi₂S₃ — hitam","Dengan SnCl₂ → Bi hitam (reduksi)","2Bi³⁺ + 3S²⁻ → Bi₂S₃↓ (hitam)"),
            ("gol2","Cd²⁺ — Kadmium","CdS — kuning","Larut dalam HCl panas, tidak larut dalam (NH₄)₂S","Cd²⁺ + S²⁻ → CdS↓ (kuning)"),
            ("gol2","Sn²⁺ — Timah","SnS — coklat","Larut dalam (NH₄)₂Sx → SnS₃²⁻","Sn²⁺ + S²⁻ → SnS↓ (coklat)"),
        ]
        for i,(badge,title,endapan,uji,rxn) in enumerate(ions_g2):
            col = c1 if i%2==0 else c2
            with col:
                st.markdown(f"""<div class="card"><span class="gol-badge {badge}">{title}</span>
                  <p class="muted-p"><strong>Endapan:</strong> {endapan}</p>
                  <p class="muted-p"><strong>Uji spesifik:</strong> {uji}</p>
                  <div class="rxn-eq">{rxn}</div></div>""", unsafe_allow_html=True)

    elif sub == "Gol. III":
        st.markdown('<span class="gol-badge gol3">Golongan III — Sulfida/Hidroksida dalam Suasana Basa</span>', unsafe_allow_html=True)
        st.markdown("""<div class="card">
          <h3 style="color:#f1f5f9;font-size:1rem;">Prinsip Pemisahan</h3>
          <p class="muted-p">Golongan III dibagi dua sub-golongan: <strong style="color:#fcd34d">IIIa</strong> mengendap sebagai sulfida dan <strong style="color:#fcd34d">IIIb</strong> sebagai hidroksida.</p>
          <p class="muted-p"><strong>Reagen pengendap:</strong> (NH₄)₂S dalam NH₄OH/NH₄Cl</p>
          <div class="ion-chips">
            <span class="ion-chip">Fe³⁺</span><span class="ion-chip">Al³⁺</span>
            <span class="ion-chip">Cr³⁺</span><span class="ion-chip">Mn²⁺</span>
            <span class="ion-chip">Ni²⁺</span><span class="ion-chip">Co²⁺</span>
            <span class="ion-chip">Zn²⁺</span>
          </div></div>""", unsafe_allow_html=True)
        g3_ions = [
            ("Fe³⁺ — Besi","Fe(OH)₃ — coklat merah","+ KSCN → merah darah","Fe³⁺ + 3OH⁻ → Fe(OH)₃↓"),
            ("Al³⁺ — Aluminium","Al(OH)₃ — putih gelatin","Larut dalam NaOH berlebih (amfoter)","Al³⁺ + 3OH⁻ → Al(OH)₃↓"),
            ("Cr³⁺ — Kromium","Cr(OH)₃ — hijau abu","Oksidasi → CrO₄²⁻ kuning","Cr³⁺ + 3OH⁻ → Cr(OH)₃↓"),
            ("Mn²⁺ — Mangan","MnS — merah muda","Oksidasi → MnO₄⁻ ungu","Mn²⁺ + S²⁻ → MnS↓ (merah muda)"),
            ("Ni²⁺ — Nikel","NiS — hitam","+ Dimetilglioksim → merah","Ni²⁺ + S²⁻ → NiS↓ (hitam)"),
            ("Zn²⁺ — Seng","ZnS — putih","Larut dalam HCl, + K₄[Fe(CN)₆] → putih","Zn²⁺ + S²⁻ → ZnS↓ (putih)"),
        ]
        c1,c2,c3 = st.columns(3)
        cols3 = [c1,c2,c3,c1,c2,c3]
        for i,(title,endapan,uji,rxn) in enumerate(g3_ions):
            with cols3[i]:
                st.markdown(f"""<div class="card"><span class="gol-badge gol3">{title}</span>
                  <p class="muted-p"><strong>Endapan:</strong> {endapan}</p>
                  <p class="muted-p"><strong>Uji spesifik:</strong> {uji}</p>
                  <div class="rxn-eq">{rxn}</div></div>""", unsafe_allow_html=True)

    elif sub == "Gol. IV":
        st.markdown('<span class="gol-badge gol4">Golongan IV — Karbonat dalam Suasana Basa</span>', unsafe_allow_html=True)
        st.markdown("""<div class="card">
          <h3 style="color:#f1f5f9;font-size:1rem;">Prinsip Pemisahan</h3>
          <p class="muted-p">Kation Golongan IV diendapkan sebagai <strong style="color:#6ee7b7">karbonat</strong> menggunakan (NH₄)₂CO₃ dalam suasana basa (NH₄OH).</p>
          <p class="muted-p"><strong>Reagen pengendap:</strong> (NH₄)₂CO₃ dalam NH₄OH</p>
          <div class="ion-chips">
            <span class="ion-chip">Ca²⁺ (Kalsium)</span>
            <span class="ion-chip">Sr²⁺ (Stronsium)</span>
            <span class="ion-chip">Ba²⁺ (Barium)</span>
          </div></div>""", unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        with c1:
            st.markdown("""<div class="card"><span class="gol-badge gol4">Ca²⁺ — Kalsium</span>
              <p class="muted-p"><strong>Endapan:</strong> CaCO₃ — putih</p>
              <p class="muted-p"><strong>Uji spesifik:</strong> + (NH₄)₂C₂O₄ → CaC₂O₄ putih; nyala: merah jingga</p>
              <div class="rxn-eq">Ca²⁺ + CO₃²⁻ → CaCO₃↓ (putih)</div></div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class="card"><span class="gol-badge gol4">Sr²⁺ — Stronsium</span>
              <p class="muted-p"><strong>Endapan:</strong> SrCO₃ — putih</p>
              <p class="muted-p"><strong>Uji spesifik:</strong> + H₂SO₄ → SrSO₄ putih; nyala: merah karmin</p>
              <div class="rxn-eq">Sr²⁺ + CO₃²⁻ → SrCO₃↓ (putih)</div></div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class="card"><span class="gol-badge gol4">Ba²⁺ — Barium</span>
              <p class="muted-p"><strong>Endapan:</strong> BaCO₃ — putih</p>
              <p class="muted-p"><strong>Uji spesifik:</strong> + K₂CrO₄ → BaCrO₄ kuning; nyala: hijau kekuningan</p>
              <div class="rxn-eq">Ba²⁺ + CO₃²⁻ → BaCO₃↓ (putih)</div></div>""", unsafe_allow_html=True)

    elif sub == "Gol. V":
        st.markdown('<span class="gol-badge gol5">Golongan V — Tidak Terendapkan</span>', unsafe_allow_html=True)
        st.markdown("""<div class="card">
          <h3 style="color:#f1f5f9;font-size:1rem;">Prinsip Identifikasi</h3>
          <p class="muted-p">Kation Golongan V adalah kation yang <strong style="color:#fca5a5">tidak dapat diendapkan</strong> oleh reagen golongan I–IV. Identifikasi dilakukan melalui uji spesifik masing-masing ion.</p>
          <div class="ion-chips">
            <span class="ion-chip">Mg²⁺ (Magnesium)</span>
            <span class="ion-chip">K⁺ (Kalium)</span>
            <span class="ion-chip">Na⁺ (Natrium)</span>
            <span class="ion-chip">NH₄⁺ (Amonium)</span>
          </div></div>""", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        g5_ions = [
            ("Mg²⁺ — Magnesium","+ Na₂HPO₄ + NH₄OH → MgNH₄PO₄ putih kristalin","+ Titan Yellow → merah dalam basa","Mg²⁺ + NH₄⁺ + PO₄³⁻ → MgNH₄PO₄↓ (putih)"),
            ("K⁺ — Kalium","+ Na₃[Co(NO₂)₆] → K₂Na[Co(NO₂)₆] kuning","Uji nyala: Violet/ungu melalui kaca kobalt","2K⁺ + Na⁺ + [Co(NO₂)₆]³⁻ → K₂Na[Co(NO₂)₆]↓"),
            ("Na⁺ — Natrium","+ Zn(UO₂)₃(CH₃COO)₈ → kuning kristalin","Uji nyala: Kuning intensif (D-line)","Na⁺ → nyala kuning (589 nm)"),
            ("NH₄⁺ — Amonium","+ NaOH panas → gas NH₃ (bau tajam, kertas lakmus merah → biru)","Uji Nessler: + reagen Nessler → coklat jingga","NH₄⁺ + OH⁻ → NH₃↑ + H₂O"),
        ]
        cols5 = [c1,c2,c1,c2]
        for i,(title,uji1,uji2,rxn) in enumerate(g5_ions):
            with cols5[i]:
                st.markdown(f"""<div class="card"><span class="gol-badge gol5">{title}</span>
                  <p class="muted-p"><strong>Uji spesifik:</strong> {uji1}</p>
                  <p class="muted-p"><strong>Uji lain:</strong> {uji2}</p>
                  <div class="rxn-eq">{rxn}</div></div>""", unsafe_allow_html=True)

    elif sub == "Anion":
        st.markdown('<span class="gol-badge anion-badge">Anion — Ion Bermuatan Negatif</span>', unsafe_allow_html=True)
        st.markdown("""<div class="card">
          <h3 style="color:#f1f5f9;font-size:1rem;">Pengantar Analisis Anion</h3>
          <p class="muted-p">Analisis anion melibatkan identifikasi ion negatif dalam larutan. Identifikasi dilakukan melalui <strong style="color:#f9a8d4">uji pendahuluan</strong> dan <strong style="color:#f9a8d4">uji spesifik</strong>.</p>
          </div>""", unsafe_allow_html=True)
        anion_list = [
            ("Cl⁻ — Klorida","+ AgNO₃ → AgCl putih, larut dalam NH₄OH","Ag⁺ + Cl⁻ → AgCl↓ (putih)"),
            ("SO₄²⁻ — Sulfat","+ BaCl₂ → BaSO₄ putih, tidak larut HCl/HNO₃","Ba²⁺ + SO₄²⁻ → BaSO₄↓ (putih)"),
            ("CO₃²⁻ — Karbonat","+ HCl → gas CO₂ (mengeruhkan Ca(OH)₂)","CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O"),
            ("NO₃⁻ — Nitrat","+ FeSO₄ + H₂SO₄ pekat → cincin coklat Fe[NO]SO₄","Fe²⁺ + NO → [Fe(NO)]²⁺ (coklat)"),
            ("PO₄³⁻ — Fosfat","+ AgNO₃ → Ag₃PO₄ kuning; + molibdat → kuning kristalin","3Ag⁺ + PO₄³⁻ → Ag₃PO₄↓ (kuning)"),
            ("I⁻ — Iodida","+ AgNO₃ → AgI kuning; + Cl₂/kanji → biru (I₂)","Ag⁺ + I⁻ → AgI↓ (kuning)"),
            ("S²⁻ — Sulfida","+ Pb(CH₃COO)₂ → PbS hitam; bau telur busuk","Pb²⁺ + S²⁻ → PbS↓ (hitam)"),
            ("CH₃COO⁻ — Asetat","+ FeCl₃ → merah coklat; bau cuka saat dipanaskan","3CH₃COO⁻ + Fe³⁺ → Fe(CH₃COO)₃ (merah coklat)"),
        ]
        c1,c2 = st.columns(2)
        for i,(title,uji,rxn) in enumerate(anion_list):
            col = c1 if i%2==0 else c2
            with col:
                st.markdown(f"""<div class="card"><span class="gol-badge anion-badge">{title}</span>
                  <p class="muted-p"><strong>Uji spesifik:</strong> {uji}</p>
                  <div class="rxn-eq">{rxn}</div></div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB: PENGUJIAN
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.tab == "🧪 Pengujian":
    st.markdown('<div class="grad-h2">Tabel Prosedur Pengujian Kation</div>', unsafe_allow_html=True)
    st.markdown('<p class="muted-p" style="margin-bottom:1.5rem;">Pilih golongan kation untuk melihat prosedur pengujian sistematis.</p>', unsafe_allow_html=True)

    t_opts = ["Golongan I","Golongan II","Golongan III","Golongan IV","Golongan V"]
    tcols = st.columns(5)
    for i,(col,label) in enumerate(zip(tcols, t_opts)):
        with col:
            if st.button(label, key=f"tsub_{i}", use_container_width=True,
                         type="primary" if st.session_state.test_sub==label else "secondary"):
                st.session_state.test_sub = label
                st.rerun()

    TEST_TABLES = {
        "Golongan I": {
            "info": '<strong style="color:#c4b5fd">Golongan I</strong> — Reagen Pengendap: <span class="formula" style="font-family:monospace;color:#f59e0b;">HCl 2M</span> → Endapan: Klorida tidak larut',
            "rows": [
                ["Uji Golongan","Ag⁺, Hg₂²⁺, Pb²⁺","Tambahkan HCl 2M ke larutan sampel","HCl 2M","⬜ Endapan putih terbentuk","Ada kation Gol. I"],
                ["Pemisahan Pb²⁺","Pb²⁺","Cuci endapan dengan air panas 80°C","Air panas","🟢 Pb²⁺ larut, Ag⁺ dan Hg₂²⁺ tetap","Identifikasi Pb²⁺"],
                ["Uji Pb²⁺","Pb²⁺","Filtrat panas + K₂CrO₄","K₂CrO₄ 0.1M","🟡 Endapan PbCrO₄ kuning","+Pb²⁺ confirmed"],
                ["Uji Ag⁺ vs Hg₂²⁺","Ag⁺, Hg₂²⁺","Sisa endapan + NH₄OH berlebih","NH₄OH 6M","AgCl larut jernih; Hg₂Cl₂ → ⬛ hitam","Hg₂²⁺ jika hitam"],
                ["Uji Ag⁺ spesifik","Ag⁺","Filtrat + HNO₃ encer → + K₂CrO₄","HNO₃ + K₂CrO₄","🔴 AgCrO₄ merah bata","+Ag⁺ confirmed"],
                ["Uji Hg₂²⁺ spesifik","Hg₂²⁺","Endapan hitam + HNO₃ panas","HNO₃ pekat","Endapan larut → merkuri(II) nitrat","+Hg₂²⁺ confirmed"],
            ]
        },
        "Golongan II": {
            "info": '<strong style="color:#67e8f9">Golongan II</strong> — Reagen Pengendap: <span style="font-family:monospace;color:#f59e0b;">H₂S dalam HCl 0.3M</span>',
            "rows": [
                ["Uji Golongan","Cu²⁺,Bi³⁺,Cd²⁺,Hg²⁺,Sn,As,Sb","Alirkan H₂S ke larutan dalam HCl 0.3M","H₂S gas","Endapan berwarna (hitam/kuning)","Ada kation Gol. II"],
                ["Pemisahan Cu²⁺","Cu²⁺","Endapan + NH₄OH berlebih","NH₄OH","🔵 Larutan biru tua [Cu(NH₃)₄]²⁺","+Cu²⁺"],
                ["Uji Cu²⁺ spesifik","Cu²⁺","Larutan biru + K₄[Fe(CN)₆]","K₄[Fe(CN)₆]","🔴 Cu₂[Fe(CN)₆] merah coklat","+Cu²⁺ confirmed"],
                ["Uji Bi³⁺","Bi³⁺","Endapan Bi₂S₃ + SnCl₂ basa","SnCl₂ alkali","⬛ Bi hitam (reduksi)","+Bi³⁺"],
                ["Uji Cd²⁺","Cd²⁺","Larutan asam + H₂S","H₂S","🟡 CdS kuning","+Cd²⁺"],
                ["Uji Sn²⁺","Sn²⁺","Larutan + HgCl₂","HgCl₂","Endapan putih → abu → hitam","+Sn²⁺"],
            ]
        },
        "Golongan III": {
            "info": '<strong style="color:#fcd34d">Golongan III</strong> — Reagen Pengendap: <span style="font-family:monospace;color:#f59e0b;">(NH₄)₂S dalam NH₄OH/NH₄Cl</span>',
            "rows": [
                ["Uji Golongan","Fe³⁺,Al³⁺,Cr³⁺,Mn²⁺,Ni²⁺,Co²⁺,Zn²⁺","Tambahkan (NH₄)₂S dalam buffer NH₄OH/NH₄Cl","(NH₄)₂S","Campuran endapan warna-warni","Ada kation Gol. III"],
                ["Uji Fe³⁺","Fe³⁺","Larutan + KSCN","KSCN 0.1M","🔴 Merah darah [Fe(SCN)]²⁺","+Fe³⁺"],
                ["Uji Al³⁺","Al³⁺","Endapan + NaOH berlebih + aluminon","NaOH + aluminon","Endapan merah (lake aluminon)","+Al³⁺"],
                ["Uji Cr³⁺","Cr³⁺","Larutan + NaOH + H₂O₂; asamkan + BaCl₂","NaOH, H₂O₂, BaCl₂","🟡 BaCrO₄ kuning","+Cr³⁺"],
                ["Uji Mn²⁺","Mn²⁺","+ NaBiO₃ dalam HNO₃","NaBiO₃/HNO₃","🟣 Larutan ungu (MnO₄⁻)","+Mn²⁺"],
                ["Uji Ni²⁺","Ni²⁺","+ Dimetilglioksim dalam NH₄OH","DMG","🔴 Endapan merah Ni-DMG","+Ni²⁺"],
                ["Uji Co²⁺","Co²⁺","+ KSCN + aseton","KSCN+aseton","🔵 Larutan biru [Co(SCN)₄]²⁻","+Co²⁺"],
                ["Uji Zn²⁺","Zn²⁺","+ K₄[Fe(CN)₆] asam","K₄[Fe(CN)₆]","Endapan putih Zn₂[Fe(CN)₆]","+Zn²⁺"],
            ]
        },
        "Golongan IV": {
            "info": '<strong style="color:#6ee7b7">Golongan IV</strong> — Reagen Pengendap: <span style="font-family:monospace;color:#f59e0b;">(NH₄)₂CO₃ dalam NH₄OH</span>',
            "rows": [
                ["Uji Golongan","Ca²⁺, Sr²⁺, Ba²⁺","Tambahkan (NH₄)₂CO₃ dalam NH₄OH","(NH₄)₂CO₃","Endapan karbonat putih","Ada kation Gol. IV"],
                ["Uji Ba²⁺","Ba²⁺","Larutan asam asetat + K₂CrO₄","K₂CrO₄","🟡 BaCrO₄ kuning","+Ba²⁺"],
                ["Uji Sr²⁺","Sr²⁺","Larutan + (NH₄)₂SO₄","(NH₄)₂SO₄","SrSO₄ putih halus","+Sr²⁺"],
                ["Uji Ca²⁺","Ca²⁺","Filtrat + (NH₄)₂C₂O₄","(NH₄)₂C₂O₄","⬜ CaC₂O₄ putih kristalin","+Ca²⁺"],
                ["Uji nyala Ba²⁺","Ba²⁺","Uji nyala kawat platinum","—","Nyala hijau kekuningan","+Ba²⁺ nyala"],
                ["Uji nyala Ca²⁺","Ca²⁺","Uji nyala kawat platinum","—","Nyala merah jingga (bata)","+Ca²⁺ nyala"],
            ]
        },
        "Golongan V": {
            "info": '<strong style="color:#fca5a5">Golongan V</strong> — Tidak ada reagen golongan; identifikasi dengan uji spesifik',
            "rows": [
                ["Uji NH₄⁺","NH₄⁺","Sampel + NaOH → panaskan, kertas lakmus merah di atas","NaOH 6M","Gas NH₃ bau tajam; lakmus merah → biru","+NH₄⁺"],
                ["Uji NH₄⁺ Nessler","NH₄⁺","Larutan + reagen Nessler","K₂[HgI₄]/KOH","🟠 Coklat jingga","+NH₄⁺ sensitif"],
                ["Uji K⁺","K⁺","Larutan netral + Na₃[Co(NO₂)₆]","Na₃[Co(NO₂)₆]","🟡 Endapan K₂Na[Co(NO₂)₆] kuning","+K⁺"],
                ["Uji nyala K⁺","K⁺","Nyala melalui kaca kobalt biru","Kaca kobalt","Violet/ungu","+K⁺"],
                ["Uji Na⁺","Na⁺","Uji nyala langsung","—","Kuning intens (D-line 589nm)","+Na⁺"],
                ["Uji Na⁺ spesifik","Na⁺","+ Zink uranil asetat","Zn(UO₂)₃(OAc)₈","Endapan kristal kuning","+Na⁺"],
                ["Uji Mg²⁺","Mg²⁺","+ Na₂HPO₄ dalam NH₄OH/NH₄Cl","Na₂HPO₄","MgNH₄PO₄ putih kristalin","+Mg²⁺"],
            ]
        },
    }

    tdata = TEST_TABLES[st.session_state.test_sub]
    st.markdown(f'<div class="highlight-box">{tdata["info"]}</div>', unsafe_allow_html=True)

    header = ["Uji","Ion","Prosedur","Reagen","Pengamatan / Hasil","Kesimpulan"]
    rows_html = "".join(
        "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
        for row in tdata["rows"]
    )
    thead = "".join(f"<th>{h}</th>" for h in header)
    st.markdown(f"""
    <div class="table-wrap">
      <table class="styled-table">
        <thead><tr>{thead}</tr></thead>
        <tbody>{rows_html}</tbody>
      </table>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB: REAKSI KATION
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.tab == "⚗️ Reaksi Kation":
    st.markdown('<div class="grad-h2">Animasi Reaksi Kation</div>', unsafe_allow_html=True)
    st.markdown('<p class="muted-p" style="margin-bottom:1.5rem;">Klik tombol ▶ Animasi untuk melihat perubahan tabung reaksi, persamaan kimia, dan pengamatan.</p>', unsafe_allow_html=True)

    rxk_opts = list(RX_KATION.keys())
    rxk_cols = st.columns(len(rxk_opts))
    for i,(col,label) in enumerate(zip(rxk_cols, rxk_opts)):
        with col:
            if st.button(label, key=f"rxksub_{i}", use_container_width=True,
                         type="primary" if st.session_state.rxk_sub==label else "secondary"):
                st.session_state.rxk_sub = label
                st.rerun()

    rxk_data = RX_KATION[st.session_state.rxk_sub]
    ncols = 2
    grid_cols = st.columns(ncols)
    for i, rxn in enumerate(rxk_data):
        with grid_cols[i % ncols]:
            key = f"rxk_{st.session_state.rxk_sub}_{i}"
            render_tube_pair(key, rxn["before"], rxn["after"], rxn["ion"], rxn["reagent"], rxn["equation"], rxn["obs"], rxn["header"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB: REAKSI ANION
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.tab == "🔬 Reaksi Anion":
    st.markdown('<div class="grad-h2">Animasi Reaksi Anion</div>', unsafe_allow_html=True)
    st.markdown('<p class="muted-p" style="margin-bottom:1.5rem;">Klik tombol ▶ Animasi untuk melihat animasi tabung reaksi identifikasi anion.</p>', unsafe_allow_html=True)

    ncols = 2
    grid_cols = st.columns(ncols)
    for i, rxn in enumerate(RX_ANION):
        with grid_cols[i % ncols]:
            key = f"rxa_{i}"
            render_tube_pair(key, rxn["before"], rxn["after"], rxn["ion"], rxn["reagent"], rxn["equation"], rxn["obs"], rxn["header"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB: KUIS
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.tab == "🎯 Kuis":
    st.markdown("""
    <div style="text-align:center;margin-bottom:2rem;">
      <div class="grad-h2" style="font-size:2rem;">Kuis Kation &amp; Anion</div>
      <p class="muted-p">Uji pemahamanmu tentang analisis kualitatif ion!</p>
    </div>""", unsafe_allow_html=True)

    # Quiz done / score screen
    if st.session_state.quiz_done:
        pct = round(st.session_state.quiz_score / len(QUIZ_DATA) * 100)
        if pct >= 90:   emoji, msg = "🏆", "Luar biasa! Kamu menguasai materi dengan sangat baik!"
        elif pct >= 70: emoji, msg = "🎉", "Bagus! Pelajari kembali bagian yang masih kurang."
        elif pct >= 50: emoji, msg = "📚", "Lumayan! Masih ada yang perlu diperbaiki."
        else:           emoji, msg = "💪", "Jangan menyerah! Ulangi materi dan coba lagi."

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown(f"""
            <div class="card" style="text-align:center;padding:2.5rem;">
              <div style="font-size:3.5rem;margin-bottom:1rem;">{emoji}</div>
              <div class="score-circle" style="background:conic-gradient(#7c3aed 0% {pct}%, #2d3748 {pct}% 100%);">
                <div style="background:#0d1117;width:110px;height:110px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;">
                  <span class="score-num">{st.session_state.quiz_score}</span>
                  <span class="score-label">dari {len(QUIZ_DATA)}</span>
                </div>
              </div>
              <h3 style="color:#f1f5f9;font-size:1.4rem;margin:1rem 0 .5rem;">{pct}%</h3>
              <p class="muted-p">{msg}</p>
            </div>""", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔄 Ulangi Kuis", use_container_width=True, type="primary"):
                    st.session_state.quiz_idx = 0
                    st.session_state.quiz_score = 0
                    st.session_state.quiz_done = False
                    st.session_state.quiz_answered = False
                    st.session_state.selected_opt = None
                    st.rerun()
            with c2:
                if st.button("🏠 Ke Panduan", use_container_width=True):
                    st.session_state.tab = "🏠 Panduan"
                    st.rerun()

    else:
        idx   = st.session_state.quiz_idx
        total = len(QUIZ_DATA)
        q     = QUIZ_DATA[idx]
        pct   = int(idx / total * 100)

        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown(f"""
            <div class="quiz-progress"><div class="quiz-progress-fill" style="width:{pct}%;"></div></div>
            <div style="color:#94a3b8;font-size:.85rem;margin-bottom:.5rem;">Soal {idx+1} dari {total}</div>
            <div class="quiz-question">{q["q"]}</div>
            """, unsafe_allow_html=True)

            answered = st.session_state.quiz_answered
            opts = q["opts"]
            letters = ["A","B","C","D"]

            for i, opt in enumerate(opts):
                if answered:
                    correct = (i == q["ans"])
                    chosen  = (i == st.session_state.selected_opt)
                    if correct:
                        btn_style = "background:#052e16;border:2px solid #16a34a;color:#4ade80;"
                        prefix = "✅ "
                    elif chosen:
                        btn_style = "background:#2d0a0a;border:2px solid #dc2626;color:#f87171;"
                        prefix = "❌ "
                    else:
                        btn_style = "background:#161b22;border:1px solid #2d3748;color:#94a3b8;"
                        prefix = ""
                    st.markdown(f"""
                    <div style="padding:.75rem 1.2rem;border-radius:12px;margin-bottom:.5rem;{btn_style}">
                      {prefix}{letters[i]}. {opt}
                    </div>""", unsafe_allow_html=True)
                else:
                    if st.button(f"{letters[i]}. {opt}", key=f"opt_{idx}_{i}", use_container_width=True):
                        st.session_state.quiz_answered = True
                        st.session_state.selected_opt  = i
                        if i == q["ans"]:
                            st.session_state.quiz_score += 1
                        st.rerun()

            if answered:
                st.markdown(f"""
                <div class="explanation-box">
                  💡 {q["exp"]}
                </div>""", unsafe_allow_html=True)

                score_now = st.session_state.quiz_score
                st.markdown(f'<div style="color:#f59e0b;font-size:.9rem;margin:.75rem 0;">⭐ Skor: {score_now}/{idx+1}</div>', unsafe_allow_html=True)

                if st.button("Lanjut →", key="next_q", type="primary"):
                    st.session_state.quiz_idx += 1
                    st.session_state.quiz_answered = False
                    st.session_state.selected_opt  = None
                    if st.session_state.quiz_idx >= total:
                        st.session_state.quiz_done = True
                    st.rerun()
