import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="KimIA — Analisis Kation & Anion", layout="wide")

# Header
st.title("⚗️ KimIA — Analisis Kation & Anion")
st.write("Panduan lengkap analisis kualitatif **Kation (Golongan I–V)** dan **Anion** secara lengkap, visual, dan menyenangkan.")
st.info("✨ Dibuat untuk mahasiswa kimia & analis laboratorium")

# Tabs utama
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["🏠 Panduan", "📚 Materi", "🧪 Pengujian", "⚗️ Reaksi Kation", "🔬 Reaksi Anion", "🎯 Kuis"]
)

with tab1:
    st.header("Cara Menggunakan Aplikasi")
    steps = [
        "📚 Pelajari Materi",
        "🧪 Ikuti Prosedur Pengujian",
        "⚗️ Lihat Animasi Reaksi Kation",
        "🔬 Lihat Animasi Reaksi Anion",
        "🎯 Uji Pemahaman",
        "🔄 Ulang & Kuasai"
    ]
    for i, step in enumerate(steps, 1):
        st.markdown(f"**{i}. {step}**")

    st.subheader("Tentang Aplikasi")
    st.write("""
    🎯 Tujuan: Membantu mahasiswa kimia memahami analisis kualitatif kation dan anion melalui visualisasi interaktif, animasi reaksi, dan latihan soal.
    📋 Cakupan Materi:
    - Kation Golongan I: Ag⁺, Hg₂²⁺, Pb²⁺
    - Kation Golongan II: Cu²⁺, Bi³⁺, Cd²⁺, Sn²⁺, As³⁺
    - Kation Golongan III: Fe³⁺, Al³⁺, Cr³⁺, Mn²⁺, Ni²⁺, Co²⁺, Zn²⁺
    - Kation Golongan IV: Ca²⁺, Sr²⁺, Ba²⁺
    - Kation Golongan V: Mg²⁺, K⁺, Na⁺, NH₄⁺
    - Anion: Cl⁻, SO₄²⁻, CO₃²⁻, NO₃⁻, PO₄³⁻, I⁻, S²⁻
    """)

with tab2:
    st.header("Materi Kation & Anion")
    subtab1, subtab2, subtab3, subtab4, subtab5, subtab6 = st.tabs(
        ["Gol. I", "Gol. II", "Gol. III", "Gol. IV", "Gol. V", "Anion"]
    )

    with subtab1:
        st.subheader("Golongan I — Klorida Tidak Larut")
        st.write("Reagen pengendap: HCl encer (2M)")
        st.markdown("- Ag⁺ → AgCl putih, larut dalam NH₄OH berlebih")
        st.markdown("- Hg₂²⁺ → Hg₂Cl₂ putih, berubah hitam dengan NH₄OH")
        st.markdown("- Pb²⁺ → PbCl₂ putih, larut dalam air panas")

    with subtab2:
        st.subheader("Golongan II — Sulfida dalam Suasana Asam")
        st.write("Reagen pengendap: H₂S dalam HCl encer")
        st.markdown("- Cu²⁺ → CuS hitam")
        st.markdown("- Bi³⁺ → Bi₂S₃ hitam")
        st.markdown("- Cd²⁺ → CdS kuning")

    # dst untuk Golongan III, IV, V, dan Anion

with tab3:
    st.header("Pengujian")
    st.write("Tabel prosedur uji sistematis bisa ditambahkan di sini dengan `st.dataframe` atau `st.table`.")

with tab4:
    st.header("Reaksi Kation")
    st.write("Animasi tabung reaksi bisa diganti dengan diagram atau teks reaksi.")

with tab5:
    st.header("Reaksi Anion")
    st.write("Animasi tabung reaksi untuk anion.")

with tab6:
    st.header("Kuis")
    st.write("Kuis interaktif bisa dibuat dengan `st.radio` atau `st.selectbox` untuk pilihan jawaban.")
