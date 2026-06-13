import streamlit as st
import pandas as pd

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="KimIA — Analisis Kation & Anion", layout="wide")

# --- CSS CUSTOM UNTUK MENYAMAKAN TAMPILAN ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .main {
        background-color: #0d1117;
        color: #f1f5f9;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #161b22;
        border-radius: 10px 10px 0px 0px;
        color: #94a3b8;
        padding: 10px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #7c3aed !important;
        color: white !important;
    }

    .gol-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: 600;
        margin-bottom: 10px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .rxn-eq {
        font-family: 'Courier New', monospace;
        padding: 10px;
        background: rgba(6, 182, 212, 0.1);
        border-left: 5px solid #06b6d4;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("⚗️ KimIA — Analisis Kation & Anion")
st.write("Panduan lengkap analisis kualitatif ion dalam larutan [1, 2]")

# --- NAVIGASI TAB ---
tab_titles = ["🏠 Panduan", "📚 Materi", "🧪 Pengujian", "⚗️ Reaksi", "🎯 Kuis"]
tabs = st.tabs(tab_titles)

# --- TAB 1: PANDUAN ---
with tabs:
    st.header("Selamat Datang di KimIA")
    st.info("Platform interaktif untuk mempelajari analisis kualitatif Kation (Golongan I–V) dan Anion secara lengkap. [3]")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Cara Menggunakan Aplikasi")
        st.markdown("""
        1. **Pelajari Materi**: Buka tab Materi untuk teori lengkap.
        2. **Ikuti Pengujian**: Lihat prosedur sistematis di tab Pengujian.
        3. **Lihat Reaksi**: Visualisasikan persamaan reaksi di tab Reaksi.
        4. **Uji Pemahaman**: Kerjakan kuis untuk mengevaluasi diri. [4-6]
        """)
    with col2:
        st.subheader("Cakupan Materi")
        st.markdown("""
        - **Kation Gol I - V**: Dari Ag⁺ hingga NH₄⁺.
        - **Anion**: Cl⁻, SO₄²⁻, CO₃²⁻, NO₃⁻, PO₄³⁻, I⁻, S²⁻. [7, 8]
        """)

# --- TAB 2: MATERI ---
with tabs[1]:
    st.header("Materi Kation & Anion")
    materi_choice = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan II", "Golongan III", "Golongan IV", "Golongan V", "Anion"])
    
    if materi_choice == "Golongan I":
        st.markdown("<div class='gol-badge' style='background:#7c3aed'>Golongan I — Klorida Tidak Larut</div>", unsafe_allow_html=True)
        st.write("**Prinsip:** Diendapkan dengan HCl encer (2M). [9, 10]")
        st.markdown("- **Ag⁺**: Endapan putih AgCl, larut dalam NH₄OH berlebih. [10]")
        st.markdown("- **Hg₂²⁺**: Endapan putih Hg₂Cl₂, berubah hitam dengan amonia. [11]")
        st.markdown("- **Pb²⁺**: Endapan putih PbCl₂, larut dalam air panas. [12]")
        
    elif materi_choice == "Golongan II":
        st.markdown("<div class='gol-badge' style='background:#06b6d4'>Golongan II — Sulfida dalam Suasana Asam</div>", unsafe_allow_html=True)
        st.write("**Prinsip:** Diendapkan sebagai sulfida dengan H₂S dalam HCl 0.3M. [13]")
        st.write("**Ion:** Cu²⁺ (hitam), Bi³⁺ (hitam), Cd²⁺ (kuning), Sn²⁺ (coklat). [14-16]")

    elif materi_choice == "Golongan III":
        st.markdown("<div class='gol-badge' style='background:#f59e0b'>Golongan III — Sulfida/Hidroksida Basa</div>", unsafe_allow_html=True)
        st.write("**Prinsip:** Menggunakan (NH₄)₂S dalam buffer NH₄OH/NH₄Cl. [17]")
        st.write("**Ion:** Fe³⁺ (coklat merah), Al³⁺ (putih gelatin), Cr³⁺ (hijau abu), Ni²⁺ (merah w/ DMG). [18-20]")

    elif materi_choice == "Golongan IV":
        st.markdown("<div class='gol-badge' style='background:#10b981'>Golongan IV — Karbonat Basa</div>", unsafe_allow_html=True)
        st.write("**Prinsip:** Diendapkan dengan (NH₄)₂CO₃. [21]")
        st.write("**Ion:** Ba²⁺, Sr²⁺, Ca²⁺ (semua endapan karbonat putih). [22, 23]")

    elif materi_choice == "Golongan V":
        st.markdown("<div class='gol-badge' style='background:#ef4444'>Golongan V — Tidak Terendapkan</div>", unsafe_allow_html=True)
        st.write("**Prinsip:** Identifikasi melalui uji spesifik (misal: Uji Nyala). [24]")
        st.write("**Ion:** Mg²⁺, K⁺ (nyala violet), Na⁺ (nyala kuning), NH₄⁺ (bau amonia). [25-27]")

    elif materi_choice == "Anion":
        st.markdown("<div class='gol-badge' style='background:#ec4899'>Anion — Ion Bermuatan Negatif</div>", unsafe_allow_html=True)
        st.write("**Uji Spesifik:** [28-31]")
        st.markdown("- **Cl⁻**: +AgNO₃ → Putih.")
        st.markdown("- **SO₄²⁻**: +BaCl₂ → Putih (tahan asam).")
        st.markdown("- **NO₃⁻**: Uji Cincin Coklat.")

# --- TAB 3: PENGUJIAN ---
with tabs[32]:
    st.header("Tabel Prosedur Pengujian")
    gol_test = st.radio("Pilih Golongan Kation untuk Detail Prosedur:", ["Gol I", "Gol II", "Gol III", "Gol IV", "Gol V"], horizontal=True)
    
    if gol_test == "Gol I":
        data = {
            "Uji": ["Golongan", "Pemisahan Pb²⁺", "Uji Ag⁺ spesifik"],
            "Reagen": ["HCl 2M", "Air Panas", "HNO₃ + K₂CrO₄"],
            "Hasil": ["Endapan Putih", "Pb²⁺ Larut", "AgCrO₄ Merah Bata"],
            "Kesimpulan": ["Ada Gol I", "Identifikasi Pb", "Confirm Ag⁺"]
        }
        st.table(pd.DataFrame(data)) # Berdasarkan data di [33-35]

# --- TAB 4: REAKSI ---
with tabs[36]:
    st.header("Persamaan Reaksi Kimia")
    st.write("Berikut adalah beberapa reaksi konfirmasi penting:")
    
    reaksi_data = [
        {"judul": "Konfirmasi Ag⁺", "eq": "Ag⁺ + Cl⁻ → AgCl↓ (putih) [37]"},
        {"judul": "Konfirmasi Pb²⁺", "eq": "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ (kuning) [38]"},
        {"judul": "Konfirmasi Fe³⁺", "eq": "Fe³⁺ + 3SCN⁻ → [Fe(SCN)₃] (merah darah) [39]"},
        {"judul": "Konfirmasi Ni²⁺", "eq": "Ni²⁺ + 2DMG → Ni(HDMG)₂↓ (merah) [40]"},
        {"judul": "Konfirmasi NH₄⁺", "eq": "NH₄⁺ + OH⁻ → NH₃↑ + H₂O (gas bau tajam) [41]"}
    ]
    
    for rx in reaksi_data:
        with st.expander(rx["judul"]):
            st.markdown(f"<div class='rxn-eq'>{rx['eq']}</div>", unsafe_allow_html=True)

# --- TAB 5: KUIS ---
with tabs[42]:
    st.header("Kuis Kation & Anion")
    
    # Inisialisasi state kuis
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = False

    # Contoh Soal (diambil dari sumber [43-45])
    st.subheader("Pertanyaan:")
    q1 = st.radio("1. Reagen apa yang digunakan untuk mengendapkan kation Golongan I?", 
                  ["H₂SO₄ encer", "HCl encer", "NaOH", "(NH₄)₂S"], index=None)
    
    if q1:
        if q1 == "HCl encer":
            st.success("Benar! Kation Golongan I diendapkan sebagai klorida tidak larut. [43]")
        else:
            st.error("Salah. Jawaban yang benar adalah HCl encer. [43]")

    q2 = st.radio("2. Warna larutan Cu²⁺ dalam NH₄OH berlebih adalah?", 
                  ["Merah", "Hijau", "Kuning", "Biru tua"], index=None)
    
    if q2:
        if q2 == "Biru tua":
            st.success("Benar! Terbentuk kompleks tetraaminatembaga(II) biru tua. [45]")
        else:
            st.error("Salah. Tembaga membentuk larutan biru tua dengan amonia berlebih. [45]")

    if st.button("Reset Kuis"):
        st.rerun()

# --- FOOTER ---
st.divider()
st.caption("Aplikasi ini bersifat edukatif. Selalu ikuti prosedur keselamatan laboratorium. [46]")
