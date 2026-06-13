import streamlit as st

<div>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>KimIA — Analisis Kation &amp; Anion</title>
        <style dangerouslySetInnerHTML={{__html: "\n  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;600&display=swap');\n\n  :root {\n    --bg:        #0d1117;\n    --surface:   #161b22;\n    --surface2:  #1f2937;\n    --border:    #2d3748;\n    --accent1:   #7c3aed;\n    --accent2:   #06b6d4;\n    --accent3:   #f59e0b;\n    --accent4:   #10b981;\n    --accent5:   #ef4444;\n    --accent6:   #ec4899;\n    --text:      #f1f5f9;\n    --muted:     #94a3b8;\n    --glow1: rgba(124,58,237,0.25);\n    --glow2: rgba(6,182,212,0.25);\n  }\n\n  * { margin:0; padding:0; box-sizing:border-box; }\n\n  body {\n    font-family: 'Space Grotesk', sans-serif;\n    background: var(--bg);\n    color: var(--text);\n    min-height: 100vh;\n    overflow-x: hidden;\n  }\n\n  /* ── HEADER ── */\n  header {\n    position: relative;\n    padding: 2rem 2rem 1.5rem;\n    text-align: center;\n    background: linear-gradient(135deg, #0d1117 0%, #1a0533 50%, #0d1117 100%);\n    border-bottom: 1px solid var(--border);\n    overflow: hidden;\n  }\n  header::before {\n    content:'';\n    position:absolute;\n    inset:0;\n    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(124,58,237,.35) 0%, transparent 70%);\n    pointer-events:none;\n  }\n  .header-badge {\n    display: inline-block;\n    background: linear-gradient(90deg, var(--accent1), var(--accent2));\n    -webkit-background-clip: text;\n    -webkit-text-fill-color: transparent;\n    font-family: 'JetBrains Mono', monospace;\n    font-size: .75rem;\n    letter-spacing: .2em;\n    text-transform: uppercase;\n    margin-bottom: .75rem;\n  }\n  header h1 {\n    font-family: 'DM Serif Display', serif;\n    font-size: clamp(2rem, 5vw, 3.5rem);\n    background: linear-gradient(135deg, #fff 0%, #c4b5fd 50%, #67e8f9 100%);\n    -webkit-background-clip: text;\n    -webkit-text-fill-color: transparent;\n    line-height: 1.1;\n  }\n  header p {\n    color: var(--muted);\n    margin-top: .5rem;\n    font-size: .95rem;\n  }\n\n  /* floating atoms bg */\n  .atom { position:absolute; border-radius:50%; opacity:.12; animation: drift linear infinite; }\n\n  /* ── TABS ── */\n  .tab-nav {\n    display: flex;\n    overflow-x: auto;\n    background: var(--surface);\n    border-bottom: 2px solid var(--border);\n    gap: 0;\n    scrollbar-width: none;\n  }\n  .tab-nav::-webkit-scrollbar { display:none; }\n  .tab-btn {\n    flex: 0 0 auto;\n    padding: .9rem 1.4rem;\n    background: none;\n    border: none;\n    color: var(--muted);\n    font-family: 'Space Grotesk', sans-serif;\n    font-size: .85rem;\n    font-weight: 500;\n    cursor: pointer;\n    border-bottom: 3px solid transparent;\n    margin-bottom: -2px;\n    transition: all .25s;\n    white-space: nowrap;\n    display: flex;\n    align-items: center;\n    gap: .45rem;\n  }\n  .tab-btn:hover { color: var(--text); background: rgba(255,255,255,.04); }\n  .tab-btn.active { color: var(--text); border-color: var(--accent1); background: rgba(124,58,237,.08); }\n  .tab-btn .tab-icon { font-size: 1.1rem; }\n\n  /* ── CONTENT ── */\n  .tab-content { display:none; padding: 2rem; max-width: 1200px; margin: 0 auto; }\n  .tab-content.active { display:block; }\n\n  /* ── CARDS ── */\n  .card {\n    background: var(--surface);\n    border: 1px solid var(--border);\n    border-radius: 16px;\n    padding: 1.5rem;\n    margin-bottom: 1.5rem;\n  }\n  .card-gradient {\n    background: linear-gradient(135deg, var(--surface) 0%, rgba(124,58,237,.08) 100%);\n    border-color: rgba(124,58,237,.3);\n  }\n\n  h2 {\n    font-family: 'DM Serif Display', serif;\n    font-size: 1.6rem;\n    margin-bottom: 1rem;\n    background: linear-gradient(90deg, var(--accent1), var(--accent2));\n    -webkit-background-clip: text;\n    -webkit-text-fill-color: transparent;\n  }\n  h3 { font-size: 1.1rem; font-weight: 600; margin-bottom: .6rem; color: var(--text); }\n  p { color: var(--muted); line-height: 1.7; margin-bottom: .75rem; font-size: .95rem; }\n  ul, ol { color: var(--muted); padding-left: 1.4rem; line-height: 1.9; font-size: .95rem; }\n\n  /* ── GRID ── */\n  .grid-2 { display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; }\n  .grid-3 { display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }\n\n  /* ── STEP CARDS (Tab 1) ── */\n  .step-card {\n    background: var(--surface);\n    border: 1px solid var(--border);\n    border-radius: 14px;\n    padding: 1.25rem;\n    position: relative;\n    overflow: hidden;\n    transition: transform .2s, border-color .2s;\n  }\n  .step-card:hover { transform: translateY(-3px); }\n  .step-card::before {\n    content: '';\n    position: absolute;\n    top: 0; left: 0; right: 0;\n    height: 3px;\n  }\n  .step-card:nth-child(1)::before { background: linear-gradient(90deg, var(--accent1), var(--accent2)); }\n  .step-card:nth-child(2)::before { background: linear-gradient(90deg, var(--accent2), var(--accent4)); }\n  .step-card:nth-child(3)::before { background: linear-gradient(90deg, var(--accent4), var(--accent3)); }\n  .step-card:nth-child(4)::before { background: linear-gradient(90deg, var(--accent3), var(--accent5)); }\n  .step-card:nth-child(5)::before { background: linear-gradient(90deg, var(--accent5), var(--accent6)); }\n  .step-card:nth-child(6)::before { background: linear-gradient(90deg, var(--accent6), var(--accent1)); }\n  .step-num {\n    font-family: 'JetBrains Mono', monospace;\n    font-size: 2rem;\n    font-weight: 700;\n    color: rgba(124,58,237,.3);\n    line-height: 1;\n    margin-bottom: .5rem;\n  }\n\n  /* ── MATERI TABS (Tab 2) ── */\n  .subtab-nav {\n    display: flex;\n    gap: .5rem;\n    margin-bottom: 1.5rem;\n    flex-wrap: wrap;\n  }\n  .subtab-btn {\n    padding: .5rem 1.1rem;\n    border-radius: 999px;\n    border: 1px solid var(--border);\n    background: none;\n    color: var(--muted);\n    font-family: 'Space Grotesk', sans-serif;\n    font-size: .82rem;\n    cursor: pointer;\n    transition: all .2s;\n  }\n  .subtab-btn:hover { border-color: var(--accent1); color: var(--text); }\n  .subtab-btn.active { background: var(--accent1); border-color: var(--accent1); color: #fff; }\n  .subtab-panel { display:none; }\n  .subtab-panel.active { display:block; }\n\n  /* ── GOLONGAN BADGE ── */\n  .gol-badge {\n    display: inline-block;\n    padding: .25rem .75rem;\n    border-radius: 999px;\n    font-size: .78rem;\n    font-weight: 600;\n    font-family: 'JetBrains Mono', monospace;\n    margin-bottom: .75rem;\n  }\n  .gol1 { background: rgba(124,58,237,.2); color: #c4b5fd; border: 1px solid rgba(124,58,237,.4); }\n  .gol2 { background: rgba(6,182,212,.2); color: #67e8f9; border: 1px solid rgba(6,182,212,.4); }\n  .gol3 { background: rgba(245,158,11,.2); color: #fcd34d; border: 1px solid rgba(245,158,11,.4); }\n  .gol4 { background: rgba(16,185,129,.2); color: #6ee7b7; border: 1px solid rgba(16,185,129,.4); }\n  .gol5 { background: rgba(239,68,68,.2); color: #fca5a5; border: 1px solid rgba(239,68,68,.4); }\n  .anion { background: rgba(236,72,153,.2); color: #f9a8d4; border: 1px solid rgba(236,72,153,.4); }\n\n  /* ion chips */\n  .ion-chips { display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.75rem; }\n  .ion-chip {\n    padding: .3rem .8rem;\n    border-radius: 8px;\n    font-family: 'JetBrains Mono', monospace;\n    font-size: .82rem;\n    background: var(--surface2);\n    border: 1px solid var(--border);\n    color: var(--text);\n  }\n\n  /* ── PENGUJIAN TABLE (Tab 3) ── */\n  .test-nav {\n    display: flex;\n    gap: .5rem;\n    flex-wrap: wrap;\n    margin-bottom: 1.5rem;\n  }\n  .test-btn {\n    padding: .5rem 1.1rem;\n    border-radius: 10px;\n    border: 1px solid var(--border);\n    background: var(--surface);\n    color: var(--muted);\n    font-size: .85rem;\n    cursor: pointer;\n    font-family: 'Space Grotesk', sans-serif;\n    transition: all .2s;\n  }\n  .test-btn:hover { border-color: var(--accent2); color: var(--text); }\n  .test-btn.active { background: linear-gradient(135deg, var(--accent1), var(--accent2)); border-color: transparent; color: #fff; }\n\n  .table-wrap { overflow-x: auto; border-radius: 12px; border: 1px solid var(--border); }\n  table { width:100%; border-collapse: collapse; font-size: .88rem; }\n  thead { background: linear-gradient(90deg, rgba(124,58,237,.25), rgba(6,182,212,.15)); }\n  th { padding: .85rem 1rem; text-align:left; font-weight:600; font-size:.8rem; letter-spacing:.05em; text-transform:uppercase; color: var(--accent2); }\n  td { padding: .8rem 1rem; border-top: 1px solid rgba(255,255,255,.05); color: var(--muted); vertical-align:top; line-height:1.5; }\n  tr:hover td { background: rgba(124,58,237,.06); color: var(--text); }\n\n  /* result dots */\n  .dot { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; flex-shrink:0; }\n  .endapan-putih { background:#e2e8f0; }\n  .endapan-kuning { background:#fde047; }\n  .endapan-hitam  { background:#1e293b; border:1px solid #475569; }\n  .endapan-merah  { background:#ef4444; }\n  .endapan-jingga { background:#f97316; }\n  .endapan-biru   { background:#3b82f6; }\n  .larut          { background:linear-gradient(135deg,#22c55e,#16a34a); }\n  .td-flex { display:flex; align-items:center; }\n\n  /* ── REAKSI + ANIMASI (Tab 4 & 5) ── */\n  .reaction-grid { display:grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.25rem; }\n  .reaction-card {\n    background: var(--surface);\n    border: 1px solid var(--border);\n    border-radius: 16px;\n    overflow: hidden;\n    transition: transform .25s, box-shadow .25s;\n    cursor: pointer;\n  }\n  .reaction-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,0,0,.4); }\n  .reaction-header {\n    padding: .9rem 1.2rem;\n    display:flex;\n    justify-content:space-between;\n    align-items:center;\n  }\n  .reaction-title { font-weight: 600; font-size: 1rem; }\n  .reaction-reagent { font-size: .75rem; color: var(--muted); font-family:'JetBrains Mono',monospace; }\n\n  /* Test tube animation */\n  .tube-wrap {\n    display:flex;\n    justify-content:center;\n    align-items:flex-end;\n    gap: 1rem;\n    padding: 1rem 1rem .5rem;\n    background: rgba(0,0,0,.2);\n    min-height: 140px;\n    flex-wrap: wrap;\n  }\n  .tube-container { display:flex; flex-direction:column; align-items:center; gap:.3rem; }\n  .tube-label { font-size:.68rem; color:var(--muted); font-family:'JetBrains Mono',monospace; text-align:center; max-width:64px; word-break:break-word; }\n  .tube {\n    width: 36px;\n    height: 90px;\n    border: 2px solid rgba(255,255,255,.25);\n    border-radius: 0 0 18px 18px;\n    border-top: none;\n    position: relative;\n    overflow: hidden;\n    background: rgba(255,255,255,.04);\n  }\n  .tube::before {\n    content:'';\n    position:absolute;\n    top:0; left:0; right:0;\n    height:100%;\n    background:linear-gradient(90deg, rgba(255,255,255,.12) 0%, transparent 40%, rgba(255,255,255,.06) 100%);\n    z-index:2;\n    pointer-events:none;\n  }\n  .liquid {\n    position: absolute;\n    bottom: 0;\n    left: 0; right: 0;\n    transition: height 1.2s cubic-bezier(.4,0,.2,1), background-color 1.4s ease;\n    border-radius: 0 0 16px 16px;\n  }\n  .sediment {\n    position:absolute;\n    bottom:0;\n    left:0; right:0;\n    height:0;\n    border-radius:0 0 16px 16px;\n    transition: height 1.5s ease 0.4s;\n  }\n  .reaction-info { padding: .9rem 1.2rem; }\n  .rxn-eq {\n    font-family:'JetBrains Mono',monospace;\n    font-size:.75rem;\n    color: var(--accent2);\n    background: rgba(6,182,212,.08);\n    border: 1px solid rgba(6,182,212,.2);\n    border-radius:8px;\n    padding:.6rem .8rem;\n    margin-top:.5rem;\n    word-break:break-all;\n    line-height:1.6;\n  }\n  .obs-badge {\n    display:inline-flex;\n    align-items:center;\n    gap:.4rem;\n    padding:.3rem .7rem;\n    border-radius:999px;\n    font-size:.75rem;\n    margin-top:.5rem;\n    border: 1px solid;\n  }\n\n  /* ── QUIZ (Tab 6) ── */\n  .quiz-box {\n    max-width: 680px;\n    margin: 0 auto;\n  }\n  .quiz-header {\n    text-align:center;\n    margin-bottom:2rem;\n  }\n  .progress-bar-wrap {\n    background: var(--surface2);\n    border-radius:999px;\n    height:6px;\n    margin-bottom:1.5rem;\n    overflow:hidden;\n  }\n  .progress-bar {\n    height:100%;\n    border-radius:999px;\n    background: linear-gradient(90deg, var(--accent1), var(--accent2));\n    transition: width .4s ease;\n  }\n  .question-num { color:var(--muted); font-size:.85rem; margin-bottom:.5rem; }\n  .question-text {\n    font-size:1.15rem;\n    font-weight:600;\n    line-height:1.5;\n    margin-bottom:1.5rem;\n    color: var(--text);\n  }\n  .option-list { list-style:none; padding:0; display:flex; flex-direction:column; gap:.75rem; }\n  .option-btn {\n    width:100%;\n    text-align:left;\n    padding: .9rem 1.2rem;\n    border-radius:12px;\n    border: 1.5px solid var(--border);\n    background: var(--surface);\n    color: var(--text);\n    font-family:'Space Grotesk',sans-serif;\n    font-size:.95rem;\n    cursor:pointer;\n    transition: all .2s;\n    position:relative;\n  }\n  .option-btn:hover:not(:disabled) { border-color: var(--accent1); background: rgba(124,58,237,.08); }\n  .option-btn.correct { border-color: var(--accent4) !important; background: rgba(16,185,129,.12) !important; color: #6ee7b7 !important; }\n  .option-btn.wrong   { border-color: var(--accent5) !important; background: rgba(239,68,68,.12) !important; color: #fca5a5 !important; }\n  .option-btn:disabled { cursor: default; }\n  .explanation {\n    margin-top:1rem;\n    padding:1rem;\n    border-radius:10px;\n    background: rgba(6,182,212,.08);\n    border:1px solid rgba(6,182,212,.2);\n    color: var(--accent2);\n    font-size:.88rem;\n    line-height:1.6;\n  }\n  .quiz-controls { display:flex; justify-content:space-between; align-items:center; margin-top:1.5rem; }\n  .btn {\n    padding: .7rem 1.6rem;\n    border-radius:10px;\n    border:none;\n    font-family:'Space Grotesk',sans-serif;\n    font-weight:600;\n    font-size:.9rem;\n    cursor:pointer;\n    transition: all .2s;\n  }\n  .btn-primary {\n    background: linear-gradient(135deg, var(--accent1), var(--accent2));\n    color:#fff;\n  }\n  .btn-primary:hover { opacity:.85; transform:translateY(-1px); }\n  .btn-secondary { background:var(--surface2); color:var(--text); border:1px solid var(--border); }\n  .btn-secondary:hover { border-color:var(--accent1); }\n\n  .score-screen {\n    text-align:center;\n    padding: 3rem 2rem;\n  }\n  .score-ring {\n    width:140px; height:140px;\n    border-radius:50%;\n    margin:0 auto 1.5rem;\n    display:flex; align-items:center; justify-content:center;\n    font-size:2.5rem;\n    font-weight:700;\n    background: conic-gradient(var(--accent1) 0%, var(--accent2) 50%, var(--border) 50%);\n    position:relative;\n  }\n  .score-ring::after {\n    content:'';\n    position:absolute;\n    inset:12px;\n    background: var(--bg);\n    border-radius:50%;\n  }\n  .score-num {\n    position:relative;\n    z-index:1;\n    font-family:'DM Serif Display',serif;\n  }\n  .score-label { color:var(--muted); margin-top:.25rem; }\n\n  /* ── SCROLLBAR ── */\n  ::-webkit-scrollbar { width:6px; height:6px; }\n  ::-webkit-scrollbar-track { background:transparent; }\n  ::-webkit-scrollbar-thumb { background:var(--border); border-radius:3px; }\n\n  /* ── INFO PILL ── */\n  .info-pill {\n    display:inline-flex; align-items:center; gap:.4rem;\n    padding:.3rem .9rem;\n    border-radius:999px;\n    font-size:.78rem;\n    background:rgba(245,158,11,.12);\n    border:1px solid rgba(245,158,11,.3);\n    color:#fcd34d;\n    margin-bottom:1.5rem;\n  }\n\n  /* glow card */\n  .glow-card {\n    box-shadow: 0 0 0 1px rgba(124,58,237,.2), 0 8px 32px rgba(124,58,237,.15);\n  }\n\n  /* divider */\n  .divider { border:none; border-top:1px solid var(--border); margin:1.5rem 0; }\n\n  /* chemical formula styling */\n  .formula { font-family:'JetBrains Mono',monospace; color:var(--accent3); font-size:.9rem; }\n\n  @keyframes drift {\n    0% { transform: translateY(0) rotate(0deg); }\n    100% { transform: translateY(-200px) rotate(360deg); }\n  }\n  @keyframes pop { 0%{transform:scale(.95);opacity:0} 100%{transform:scale(1);opacity:1} }\n  .pop { animation: pop .3s ease; }\n\n  .highlight-box {\n    background: linear-gradient(135deg, rgba(124,58,237,.1), rgba(6,182,212,.08));\n    border: 1px solid rgba(124,58,237,.25);\n    border-radius: 12px;\n    padding: 1rem 1.25rem;\n    margin-bottom: 1rem;\n  }\n\n  /* Tube rack */\n  .tube-rack {\n    display:flex;\n    justify-content:center;\n    gap:1.5rem;\n    flex-wrap:wrap;\n    padding: 1.5rem 1rem;\n    background: linear-gradient(180deg, rgba(0,0,0,.3), rgba(0,0,0,.1));\n    border-radius:0 0 14px 14px;\n    min-height:160px;\n    align-items:flex-end;\n  }\n  .tube-unit { display:flex; flex-direction:column; align-items:center; gap:.4rem; }\n  .tube-cap {\n    width:42px; height:8px;\n    background: rgba(255,255,255,.15);\n    border-radius:4px 4px 0 0;\n    border: 1px solid rgba(255,255,255,.2);\n  }\n  .tube-body {\n    width:38px; height:100px;\n    border: 2px solid rgba(255,255,255,.2);\n    border-top:none;\n    border-radius: 0 0 19px 19px;\n    position:relative;\n    overflow:hidden;\n    background: rgba(255,255,255,.03);\n  }\n  .tube-body::before {\n    content:'';\n    position:absolute;\n    left:5px; top:0; bottom:0; width:4px;\n    background: rgba(255,255,255,.1);\n    border-radius:2px;\n  }\n  .tube-liquid {\n    position:absolute;\n    bottom:0; left:0; right:0;\n    transition: height 1.2s cubic-bezier(.4,0,.2,1);\n    border-radius: 0 0 17px 17px;\n  }\n  .tube-sediment {\n    position:absolute;\n    bottom:0; left:0; right:0;\n    border-radius: 0 0 17px 17px;\n    transition: height 1.5s ease .5s;\n  }\n  .tube-name {\n    font-size:.7rem;\n    font-family:'JetBrains Mono',monospace;\n    color:var(--muted);\n    text-align:center;\n    max-width:60px;\n    word-break:break-word;\n    line-height:1.3;\n  }\n" }} />
        {/* decorative atoms */}
        <header>
          <div className="header-badge">⚗️ Aplikasi Kimia Analitik</div>
          <h1>Kation &amp; Anion</h1>
          <p>Panduan lengkap analisis kualitatif ion dalam larutan</p>
        </header>
        <nav className="tab-nav">
          <button className="tab-btn active" onclick="showTab(0)"><span className="tab-icon">🏠</span> Panduan</button>
          <button className="tab-btn" onclick="showTab(1)"><span className="tab-icon">📚</span> Materi</button>
          <button className="tab-btn" onclick="showTab(2)"><span className="tab-icon">🧪</span> Pengujian</button>
          <button className="tab-btn" onclick="showTab(3)"><span className="tab-icon">⚗️</span> Reaksi Kation</button>
          <button className="tab-btn" onclick="showTab(4)"><span className="tab-icon">🔬</span> Reaksi Anion</button>
          <button className="tab-btn" onclick="showTab(5)"><span className="tab-icon">🎯</span> Kuis</button>
        </nav>
        {/* ═══════════ TAB 1: PANDUAN ═══════════ */}
        <div className="tab-content active" id="tab0">
          <div className="card card-gradient glow-card" style={{textAlign: 'center', padding: '2rem'}}>
            <div style={{fontSize: '3rem', marginBottom: '1rem'}}>⚗️</div>
            <h2 style={{fontSize: '2rem'}}>Selamat Datang di KimIA</h2>
            <p style={{maxWidth: '560px', margin: '0 auto 1rem'}}>Platform interaktif untuk mempelajari analisis kualitatif <strong style={{color: 'var(--accent2)'}}>Kation</strong> (Golongan I–V) dan <strong style={{color: 'var(--accent6)'}}>Anion</strong> secara lengkap, visual, dan menyenangkan.</p>
            <div className="info-pill">✨ Dibuat untuk mahasiswa kimia &amp; analis laboratorium</div>
          </div>
          <h2>Cara Menggunakan Aplikasi</h2>
          <div className="grid-2">
            <div className="step-card">
              <div className="step-num">01</div>
              <h3>📚 Pelajari Materi</h3>
              <p>Buka Tab <strong>Materi</strong> untuk membaca teori lengkap kation golongan I–V dan anion beserta ciri-ciri, reagen, dan karakteristiknya.</p>
            </div>
            <div className="step-card">
              <div className="step-num">02</div>
              <h3>🧪 Ikuti Prosedur Pengujian</h3>
              <p>Di Tab <strong>Pengujian</strong>, pilih golongan kation dan ikuti tabel prosedur uji sistematis mulai dari uji pendahuluan hingga uji spesifik.</p>
            </div>
            <div className="step-card">
              <div className="step-num">03</div>
              <h3>⚗️ Lihat Animasi Reaksi Kation</h3>
              <p>Tab <strong>Reaksi Kation</strong> menampilkan animasi tabung reaksi berwarna dan persamaan reaksi kimia untuk setiap kation.</p>
            </div>
            <div className="step-card">
              <div className="step-num">04</div>
              <h3>🔬 Lihat Animasi Reaksi Anion</h3>
              <p>Tab <strong>Reaksi Anion</strong> menampilkan animasi tabung reaksi dan reaksi kimia untuk identifikasi anion penting.</p>
            </div>
            <div className="step-card">
              <div className="step-num">05</div>
              <h3>🎯 Uji Pemahaman</h3>
              <p>Kerjakan <strong>Kuis</strong> di Tab 6 untuk menguji pemahamanmu. Ada feedback langsung dan penjelasan jawaban.</p>
            </div>
            <div className="step-card">
              <div className="step-num">06</div>
              <h3>🔄 Ulang &amp; Kuasai</h3>
              <p>Navigasi bebas antar tab kapan saja. Kuis bisa diulang untuk meningkatkan skor. Selamat belajar!</p>
            </div>
          </div>
          <div className="card" style={{marginTop: '1.5rem'}}>
            <h2>Tentang Aplikasi</h2>
            <div className="grid-2">
              <div>
                <h3>🎯 Tujuan</h3>
                <p>Membantu mahasiswa kimia memahami analisis kualitatif kation dan anion melalui visualisasi interaktif, animasi reaksi, dan latihan soal yang komprehensif.</p>
                <h3 style={{marginTop: '1rem'}}>📋 Cakupan Materi</h3>
                <ul>
                  <li>Kation Golongan I: Ag⁺, Hg₂²⁺, Pb²⁺</li>
                  <li>Kation Golongan II: Cu²⁺, Bi³⁺, Cd²⁺, Sn²⁺, As³⁺</li>
                  <li>Kation Golongan III: Fe³⁺, Al³⁺, Cr³⁺, Mn²⁺, Ni²⁺, Co²⁺, Zn²⁺</li>
                  <li>Kation Golongan IV: Ca²⁺, Sr²⁺, Ba²⁺</li>
                  <li>Kation Golongan V: Mg²⁺, K⁺, Na⁺, NH₄⁺</li>
                  <li>Anion: Cl⁻, SO₄²⁻, CO₃²⁻, NO₃⁻, PO₄³⁻, I⁻, S²⁻</li>
                </ul>
              </div>
              <div>
                <h3>🛠️ Fitur Utama</h3>
                <ul>
                  <li>Animasi tabung reaksi berwarna real-time</li>
                  <li>Tabel prosedur pengujian sistematis</li>
                  <li>Persamaan reaksi kimia lengkap</li>
                  <li>Kuis interaktif dengan feedback instan</li>
                  <li>Navigasi mudah antar golongan</li>
                  <li>Tampilan responsif mobile &amp; desktop</li>
                </ul>
                <div className="highlight-box" style={{marginTop: '1rem'}}>
                  <strong style={{color: 'var(--accent3)'}}>⚠️ Catatan:</strong>
                  <p style={{margin: 0, fontSize: '.88rem'}}>Aplikasi ini bersifat edukatif. Selalu ikuti prosedur keselamatan laboratorium saat melakukan percobaan nyata.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* ═══════════ TAB 2: MATERI ═══════════ */}
        <div className="tab-content" id="tab1">
          <h2>Materi Kation &amp; Anion</h2>
          <div className="subtab-nav">
            <button className="subtab-btn active" onclick="showSubtab('materi','gol1')">Gol. I</button>
            <button className="subtab-btn" onclick="showSubtab('materi','gol2')">Gol. II</button>
            <button className="subtab-btn" onclick="showSubtab('materi','gol3')">Gol. III</button>
            <button className="subtab-btn" onclick="showSubtab('materi','gol4')">Gol. IV</button>
            <button className="subtab-btn" onclick="showSubtab('materi','gol5')">Gol. V</button>
            <button className="subtab-btn" onclick="showSubtab('materi','anion')">Anion</button>
          </div>
          {/* GOL I */}
          <div className="subtab-panel active" id="materi-gol1">
            <div className="gol-badge gol1">Golongan I — Klorida Tidak Larut</div>
            <div className="card">
              <h3>Prinsip Pemisahan</h3>
              <p>Kation Golongan I diendapkan sebagai <strong style={{color: 'var(--accent2)'}}>klorida tidak larut</strong> dengan penambahan HCl encer ke larutan sampel. Ini merupakan golongan pertama yang dipisahkan dalam analisis sistematik.</p>
              <p><strong>Reagen pengendap:</strong> HCl encer (2M)</p>
              <div className="ion-chips">
                <span className="ion-chip">Ag⁺ (Perak)</span>
                <span className="ion-chip">Hg₂²⁺ (Merkuri I)</span>
                <span className="ion-chip">Pb²⁺ (Timbal)</span>
              </div>
            </div>
            <div className="grid-3">
              <div className="card">
                <div className="gol-badge gol1">Ag⁺</div>
                <h3>Ion Perak</h3>
                <p><strong>Endapan:</strong> AgCl — putih</p>
                <p><strong>Uji spesifik:</strong> Larut dalam NH₄OH berlebih, tidak larut HNO₃</p>
                <p><strong>Pengamatan:</strong> Dengan K₂CrO₄ → AgCrO₄ merah bata</p>
                <div className="rxn-eq">Ag⁺ + Cl⁻ → AgCl↓ (putih)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol1">Hg₂²⁺</div>
                <h3>Ion Merkuri(I)</h3>
                <p><strong>Endapan:</strong> Hg₂Cl₂ — putih</p>
                <p><strong>Uji spesifik:</strong> + NH₄OH → hitam (campuran Hg + HgNH₂Cl)</p>
                <p><strong>Pengamatan:</strong> Berubah hitam saat ditambah amonia</p>
                <div className="rxn-eq">Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓ (putih)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol1">Pb²⁺</div>
                <h3>Ion Timbal</h3>
                <p><strong>Endapan:</strong> PbCl₂ — putih</p>
                <p><strong>Uji spesifik:</strong> Larut dalam air panas, + K₂CrO₄ → PbCrO₄ kuning</p>
                <p><strong>Pengamatan:</strong> Endapan larut saat dipanaskan</p>
                <div className="rxn-eq">Pb²⁺ + 2Cl⁻ → PbCl₂↓ (putih)</div>
              </div>
            </div>
          </div>
          {/* GOL II */}
          <div className="subtab-panel" id="materi-gol2">
            <div className="gol-badge gol2">Golongan II — Sulfida dalam Suasana Asam</div>
            <div className="card">
              <h3>Prinsip Pemisahan</h3>
              <p>Kation Golongan II diendapkan sebagai <strong style={{color: 'var(--accent2)'}}>sulfida</strong> dengan mengalirkan gas H₂S dalam suasana asam (HCl 0.3M). Kation golongan ini memiliki Ksp sulfida yang sangat kecil.</p>
              <p><strong>Reagen pengendap:</strong> H₂S gas / (NH₄)₂S dalam HCl encer</p>
              <div className="ion-chips">
                <span className="ion-chip">Cu²⁺</span><span className="ion-chip">Bi³⁺</span>
                <span className="ion-chip">Cd²⁺</span><span className="ion-chip">Hg²⁺</span>
                <span className="ion-chip">Sn²⁺/Sn⁴⁺</span><span className="ion-chip">As³⁺/As⁵⁺</span>
                <span className="ion-chip">Sb³⁺</span>
              </div>
            </div>
            <div className="grid-2">
              <div className="card">
                <div className="gol-badge gol2">Cu²⁺ — Tembaga</div>
                <p><strong>Endapan:</strong> CuS — hitam</p>
                <p><strong>Uji spesifik:</strong> Larut dalam HNO₃ panas → biru dalam NH₄OH berlebih</p>
                <div className="rxn-eq">Cu²⁺ + S²⁻ → CuS↓ (hitam)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol2">Bi³⁺ — Bismut</div>
                <p><strong>Endapan:</strong> Bi₂S₃ — hitam</p>
                <p><strong>Uji spesifik:</strong> Dengan SnCl₂ → Bi hitam (reduksi)</p>
                <div className="rxn-eq">2Bi³⁺ + 3S²⁻ → Bi₂S₃↓ (hitam)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol2">Cd²⁺ — Kadmium</div>
                <p><strong>Endapan:</strong> CdS — kuning</p>
                <p><strong>Uji spesifik:</strong> Larut dalam HCl panas, tidak larut dalam (NH₄)₂S</p>
                <div className="rxn-eq">Cd²⁺ + S²⁻ → CdS↓ (kuning)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol2">Sn²⁺ — Timah</div>
                <p><strong>Endapan:</strong> SnS — coklat</p>
                <p><strong>Uji spesifik:</strong> Larut dalam (NH₄)₂Sx → SnS₃²⁻</p>
                <div className="rxn-eq">Sn²⁺ + S²⁻ → SnS↓ (coklat)</div>
              </div>
            </div>
          </div>
          {/* GOL III */}
          <div className="subtab-panel" id="materi-gol3">
            <div className="gol-badge gol3">Golongan III — Sulfida/Hidroksida dalam Suasana Basa</div>
            <div className="card">
              <h3>Prinsip Pemisahan</h3>
              <p>Kation Golongan III dibagi dua sub-golongan: <strong style={{color: '#fcd34d'}}>IIIa</strong> yang mengendap sebagai <strong>sulfida</strong> (CoS, NiS, MnS, ZnS) dan <strong style={{color: '#fcd34d'}}>IIIb</strong> yang mengendap sebagai <strong>hidroksida</strong> (Fe(OH)₃, Al(OH)₃, Cr(OH)₃).</p>
              <p><strong>Reagen pengendap:</strong> (NH₄)₂S dalam NH₄OH/NH₄Cl</p>
              <div className="ion-chips">
                <span className="ion-chip">Fe³⁺</span><span className="ion-chip">Al³⁺</span>
                <span className="ion-chip">Cr³⁺</span><span className="ion-chip">Mn²⁺</span>
                <span className="ion-chip">Ni²⁺</span><span className="ion-chip">Co²⁺</span>
                <span className="ion-chip">Zn²⁺</span>
              </div>
            </div>
            <div className="grid-3">
              <div className="card">
                <div className="gol-badge gol3">Fe³⁺ — Besi</div>
                <p><strong>Endapan:</strong> Fe(OH)₃ — coklat merah</p>
                <p><strong>Uji spesifik:</strong> + KSCN → merah darah</p>
                <div className="rxn-eq">Fe³⁺ + 3OH⁻ → Fe(OH)₃↓</div>
              </div>
              <div className="card">
                <div className="gol-badge gol3">Al³⁺ — Aluminium</div>
                <p><strong>Endapan:</strong> Al(OH)₃ — putih gelatin</p>
                <p><strong>Uji spesifik:</strong> Larut dalam NaOH berlebih (amfoter)</p>
                <div className="rxn-eq">Al³⁺ + 3OH⁻ → Al(OH)₃↓</div>
              </div>
              <div className="card">
                <div className="gol-badge gol3">Cr³⁺ — Kromium</div>
                <p><strong>Endapan:</strong> Cr(OH)₃ — hijau abu</p>
                <p><strong>Uji spesifik:</strong> Oksidasi → CrO₄²⁻ kuning</p>
                <div className="rxn-eq">Cr³⁺ + 3OH⁻ → Cr(OH)₃↓</div>
              </div>
              <div className="card">
                <div className="gol-badge gol3">Mn²⁺ — Mangan</div>
                <p><strong>Endapan:</strong> MnS — merah muda</p>
                <p><strong>Uji spesifik:</strong> Oksidasi → MnO₄⁻ ungu</p>
                <div className="rxn-eq">Mn²⁺ + S²⁻ → MnS↓ (merah muda)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol3">Ni²⁺ — Nikel</div>
                <p><strong>Endapan:</strong> NiS — hitam</p>
                <p><strong>Uji spesifik:</strong> + Dimetilglioksim → merah</p>
                <div className="rxn-eq">Ni²⁺ + S²⁻ → NiS↓ (hitam)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol3">Zn²⁺ — Seng</div>
                <p><strong>Endapan:</strong> ZnS — putih</p>
                <p><strong>Uji spesifik:</strong> Larut dalam HCl, + K₄[Fe(CN)₆] → putih</p>
                <div className="rxn-eq">Zn²⁺ + S²⁻ → ZnS↓ (putih)</div>
              </div>
            </div>
          </div>
          {/* GOL IV */}
          <div className="subtab-panel" id="materi-gol4">
            <div className="gol-badge gol4">Golongan IV — Karbonat dalam Suasana Basa</div>
            <div className="card">
              <h3>Prinsip Pemisahan</h3>
              <p>Kation Golongan IV diendapkan sebagai <strong style={{color: '#6ee7b7'}}>karbonat</strong> menggunakan (NH₄)₂CO₃ dalam suasana basa (NH₄OH). Golongan ini mencakup logam alkali tanah yang tidak mengendap pada golongan sebelumnya.</p>
              <p><strong>Reagen pengendap:</strong> (NH₄)₂CO₃ dalam NH₄OH</p>
              <div className="ion-chips">
                <span className="ion-chip">Ca²⁺ (Kalsium)</span>
                <span className="ion-chip">Sr²⁺ (Stronsium)</span>
                <span className="ion-chip">Ba²⁺ (Barium)</span>
              </div>
            </div>
            <div className="grid-3">
              <div className="card">
                <div className="gol-badge gol4">Ca²⁺ — Kalsium</div>
                <p><strong>Endapan:</strong> CaCO₃ — putih</p>
                <p><strong>Uji spesifik:</strong> + (NH₄)₂C₂O₄ → CaC₂O₄ putih; nyala: merah jingga</p>
                <div className="rxn-eq">Ca²⁺ + CO₃²⁻ → CaCO₃↓ (putih)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol4">Sr²⁺ — Stronsium</div>
                <p><strong>Endapan:</strong> SrCO₃ — putih</p>
                <p><strong>Uji spesifik:</strong> + H₂SO₄ → SrSO₄ putih tidak larut; nyala: merah karmin</p>
                <div className="rxn-eq">Sr²⁺ + CO₃²⁻ → SrCO₃↓ (putih)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol4">Ba²⁺ — Barium</div>
                <p><strong>Endapan:</strong> BaCO₃ — putih</p>
                <p><strong>Uji spesifik:</strong> + K₂CrO₄ → BaCrO₄ kuning; nyala: hijau kekuningan</p>
                <div className="rxn-eq">Ba²⁺ + CO₃²⁻ → BaCO₃↓ (putih)</div>
              </div>
            </div>
          </div>
          {/* GOL V */}
          <div className="subtab-panel" id="materi-gol5">
            <div className="gol-badge gol5">Golongan V — Tidak Terendapkan</div>
            <div className="card">
              <h3>Prinsip Identifikasi</h3>
              <p>Kation Golongan V adalah kation yang <strong style={{color: '#fca5a5'}}>tidak dapat diendapkan</strong> oleh reagen golongan I–IV. Identifikasi dilakukan melalui uji spesifik masing-masing ion menggunakan reagen karakteristik.</p>
              <div className="ion-chips">
                <span className="ion-chip">Mg²⁺ (Magnesium)</span>
                <span className="ion-chip">K⁺ (Kalium)</span>
                <span className="ion-chip">Na⁺ (Natrium)</span>
                <span className="ion-chip">NH₄⁺ (Amonium)</span>
              </div>
            </div>
            <div className="grid-2">
              <div className="card">
                <div className="gol-badge gol5">Mg²⁺ — Magnesium</div>
                <p><strong>Uji spesifik:</strong> + Na₂HPO₄ + NH₄OH → MgNH₄PO₄ putih kristalin</p>
                <p><strong>Uji lain:</strong> + Titan Yellow → merah dalam basa</p>
                <div className="rxn-eq">Mg²⁺ + NH₄⁺ + PO₄³⁻ → MgNH₄PO₄↓ (putih)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol5">K⁺ — Kalium</div>
                <p><strong>Uji spesifik:</strong> + Na₃[Co(NO₂)₆] → K₂Na[Co(NO₂)₆] kuning</p>
                <p><strong>Uji nyala:</strong> Violet/ungu melalui kaca kobalt</p>
                <div className="rxn-eq">2K⁺ + Na⁺ + [Co(NO₂)₆]³⁻ → K₂Na[Co(NO₂)₆]↓</div>
              </div>
              <div className="card">
                <div className="gol-badge gol5">Na⁺ — Natrium</div>
                <p><strong>Uji spesifik:</strong> + Zn(UO₂)₃(CH₃COO)₈ → kuning kristalin</p>
                <p><strong>Uji nyala:</strong> Kuning intensif (D-line)</p>
                <div className="rxn-eq">Na⁺ → nyala kuning (589 nm)</div>
              </div>
              <div className="card">
                <div className="gol-badge gol5">NH₄⁺ — Amonium</div>
                <p><strong>Uji spesifik:</strong> + NaOH panas → gas NH₃ (bau tajam, kertas lakmus merah → biru)</p>
                <p><strong>Uji Nessler:</strong> + reagen Nessler → coklat jingga</p>
                <div className="rxn-eq">NH₄⁺ + OH⁻ → NH₃↑ + H₂O</div>
              </div>
            </div>
          </div>
          {/* ANION */}
          <div className="subtab-panel" id="materi-anion">
            <div className="gol-badge anion">Anion — Ion Bermuatan Negatif</div>
            <div className="card">
              <h3>Pengantar Analisis Anion</h3>
              <p>Analisis anion melibatkan identifikasi ion negatif dalam larutan. Berbeda dengan kation, anion tidak memiliki skema pemisahan golongan yang seragam. Identifikasi dilakukan melalui <strong style={{color: 'var(--accent6)'}}>uji pendahuluan</strong> (warna, bau, uji nyala) dan <strong style={{color: 'var(--accent6)'}}>uji spesifik</strong>.</p>
            </div>
            <div className="grid-2">
              <div className="card">
                <div className="gol-badge anion">Cl⁻ — Klorida</div>
                <p><strong>Uji spesifik:</strong> + AgNO₃ → AgCl putih, larut dalam NH₄OH</p>
                <div className="rxn-eq">Ag⁺ + Cl⁻ → AgCl↓ (putih)</div>
              </div>
              <div className="card">
                <div className="gol-badge anion">SO₄²⁻ — Sulfat</div>
                <p><strong>Uji spesifik:</strong> + BaCl₂ → BaSO₄ putih, tidak larut HCl/HNO₃</p>
                <div className="rxn-eq">Ba²⁺ + SO₄²⁻ → BaSO₄↓ (putih)</div>
              </div>
              <div className="card">
                <div className="gol-badge anion">CO₃²⁻ — Karbonat</div>
                <p><strong>Uji spesifik:</strong> + HCl → gas CO₂ (mengeruhkan Ca(OH)₂)</p>
                <div className="rxn-eq">CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O</div>
              </div>
              <div className="card">
                <div className="gol-badge anion">NO₃⁻ — Nitrat</div>
                <p><strong>Uji cincin coklat:</strong> + FeSO₄ + H₂SO₄ pekat → cincin coklat Fe[NO]SO₄</p>
                <div className="rxn-eq">Fe²⁺ + NO → [Fe(NO)]²⁺ (coklat)</div>
              </div>
              <div className="card">
                <div className="gol-badge anion">PO₄³⁻ — Fosfat</div>
                <p><strong>Uji spesifik:</strong> + AgNO₃ → Ag₃PO₄ kuning; + molibdat → kuning kristalin</p>
                <div className="rxn-eq">3Ag⁺ + PO₄³⁻ → Ag₃PO₄↓ (kuning)</div>
              </div>
              <div className="card">
                <div className="gol-badge anion">I⁻ — Iodida</div>
                <p><strong>Uji spesifik:</strong> + AgNO₃ → AgI kuning; + Cl₂/kanji → biru (I₂)</p>
                <div className="rxn-eq">Ag⁺ + I⁻ → AgI↓ (kuning)</div>
              </div>
              <div className="card">
                <div className="gol-badge anion">S²⁻ — Sulfida</div>
                <p><strong>Uji spesifik:</strong> + Pb(CH₃COO)₂ → PbS hitam; bau telur busuk</p>
                <div className="rxn-eq">Pb²⁺ + S²⁻ → PbS↓ (hitam)</div>
              </div>
              <div className="card">
                <div className="gol-badge anion">CH₃COO⁻ — Asetat</div>
                <p><strong>Uji spesifik:</strong> + FeCl₃ → merah coklat (besi asetat); bau cuka saat dipanaskan</p>
                <div className="rxn-eq">3CH₃COO⁻ + Fe³⁺ → Fe(CH₃COO)₃ (merah coklat)</div>
              </div>
            </div>
          </div>
        </div>
        {/* ═══════════ TAB 3: PENGUJIAN ═══════════ */}
        <div className="tab-content" id="tab2">
          <h2>Tabel Prosedur Pengujian Kation</h2>
          <p style={{marginBottom: '1.5rem'}}>Pilih golongan kation untuk melihat prosedur pengujian sistematis dari uji pendahuluan hingga uji spesifik.</p>
          <div className="test-nav">
            <button className="test-btn active" onclick="showTest('t1')">Golongan I</button>
            <button className="test-btn" onclick="showTest('t2')">Golongan II</button>
            <button className="test-btn" onclick="showTest('t3')">Golongan III</button>
            <button className="test-btn" onclick="showTest('t4')">Golongan IV</button>
            <button className="test-btn" onclick="showTest('t5')">Golongan V</button>
          </div>
          <div id="test-t1">
            <div className="card highlight-box" style={{padding: '.8rem 1.2rem', marginBottom: '1rem'}}>
              <strong style={{color: 'var(--accent1)'}}>Golongan I</strong> — Reagen Pengendap: <span className="formula">HCl 2M</span> → Endapan: Klorida tidak larut
            </div>
            <div className="table-wrap">
              <table>
                <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
                <tbody>
                  <tr><td><strong>Uji Golongan</strong></td><td>Ag⁺, Hg₂²⁺, Pb²⁺</td><td>Tambahkan HCl 2M ke larutan sampel</td><td>HCl 2M</td><td><span className="td-flex"><span className="dot endapan-putih" />Endapan putih terbentuk</span></td><td>Ada kation Gol. I</td></tr>
                  <tr><td><strong>Pemisahan Pb²⁺</strong></td><td>Pb²⁺</td><td>Cuci endapan dengan air panas 80°C</td><td>Air panas</td><td><span className="td-flex"><span className="dot larut" />Pb²⁺ larut, Ag⁺ dan Hg₂²⁺ tetap</span></td><td>Identifikasi Pb²⁺</td></tr>
                  <tr><td><strong>Uji Pb²⁺</strong></td><td>Pb²⁺</td><td>Filtrat panas + K₂CrO₄</td><td>K₂CrO₄ 0.1M</td><td><span className="td-flex"><span className="dot endapan-kuning" />Endapan PbCrO₄ kuning</span></td><td>+Pb²⁺ confirmed</td></tr>
                  <tr><td><strong>Uji Ag⁺ vs Hg₂²⁺</strong></td><td>Ag⁺, Hg₂²⁺</td><td>Sisa endapan + NH₄OH berlebih</td><td>NH₄OH 6M</td><td>AgCl larut → larutan jernih; Hg₂Cl₂ → <span className="td-flex"><span className="dot endapan-hitam" />hitam</span></td><td>Hg₂²⁺ jika hitam</td></tr>
                  <tr><td><strong>Uji Ag⁺ spesifik</strong></td><td>Ag⁺</td><td>Filtrat + HNO₃ encer → endapan kembali + K₂CrO₄</td><td>HNO₃ + K₂CrO₄</td><td><span className="td-flex"><span className="dot endapan-merah" />AgCrO₄ merah bata</span></td><td>+Ag⁺ confirmed</td></tr>
                  <tr><td><strong>Uji Hg₂²⁺ spesifik</strong></td><td>Hg₂²⁺</td><td>Endapan hitam + HNO₃ panas</td><td>HNO₃ pekat</td><td>Endapan larut → merkuri(II) nitrat</td><td>+Hg₂²⁺ confirmed</td></tr>
                </tbody>
              </table>
            </div>
          </div>
          <div id="test-t2" style={{display: 'none'}}>
            <div className="card highlight-box" style={{padding: '.8rem 1.2rem', marginBottom: '1rem'}}>
              <strong style={{color: 'var(--accent2)'}}>Golongan II</strong> — Reagen Pengendap: <span className="formula">H₂S dalam HCl 0.3M</span> → Endapan: Sulfida asam
            </div>
            <div className="table-wrap">
              <table>
                <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
                <tbody>
                  <tr><td><strong>Uji Golongan</strong></td><td>Cu²⁺,Bi³⁺,Cd²⁺,Hg²⁺,Sn,As,Sb</td><td>Alirkan H₂S ke larutan dalam HCl 0.3M</td><td>H₂S gas</td><td>Endapan berwarna (hitam/kuning)</td><td>Ada kation Gol. II</td></tr>
                  <tr><td><strong>Pemisahan Cu²⁺</strong></td><td>Cu²⁺</td><td>Endapan + NH₄OH berlebih</td><td>NH₄OH</td><td><span className="td-flex"><span className="dot endapan-biru" />Larutan biru tua [Cu(NH₃)₄]²⁺</span></td><td>+Cu²⁺</td></tr>
                  <tr><td><strong>Uji Cu²⁺ spesifik</strong></td><td>Cu²⁺</td><td>Larutan biru + K₄[Fe(CN)₆]</td><td>K₄[Fe(CN)₆]</td><td><span className="td-flex"><span className="dot endapan-merah" />Cu₂[Fe(CN)₆] merah coklat</span></td><td>+Cu²⁺ confirmed</td></tr>
                  <tr><td><strong>Uji Bi³⁺</strong></td><td>Bi³⁺</td><td>Endapan Bi₂S₃ + SnCl₂ basa</td><td>SnCl₂ alkali</td><td><span className="td-flex"><span className="dot endapan-hitam" />Bi hitam (reduksi)</span></td><td>+Bi³⁺</td></tr>
                  <tr><td><strong>Uji Cd²⁺</strong></td><td>Cd²⁺</td><td>Larutan asam + H₂S</td><td>H₂S</td><td><span className="td-flex"><span className="dot endapan-kuning" />CdS kuning</span></td><td>+Cd²⁺</td></tr>
                  <tr><td><strong>Uji Sn²⁺</strong></td><td>Sn²⁺</td><td>Larutan + HgCl₂</td><td>HgCl₂</td><td>Endapan putih → abu → hitam</td><td>+Sn²⁺</td></tr>
                </tbody>
              </table>
            </div>
          </div>
          <div id="test-t3" style={{display: 'none'}}>
            <div className="card highlight-box" style={{padding: '.8rem 1.2rem', marginBottom: '1rem'}}>
              <strong style={{color: 'var(--accent3)'}}>Golongan III</strong> — Reagen Pengendap: <span className="formula">(NH₄)₂S dalam NH₄OH/NH₄Cl</span>
            </div>
            <div className="table-wrap">
              <table>
                <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
                <tbody>
                  <tr><td><strong>Uji Golongan</strong></td><td>Fe³⁺,Al³⁺,Cr³⁺,Mn²⁺,Ni²⁺,Co²⁺,Zn²⁺</td><td>Tambahkan (NH₄)₂S dalam buffer NH₄OH/NH₄Cl</td><td>(NH₄)₂S</td><td>Campuran endapan warna-warni</td><td>Ada kation Gol. III</td></tr>
                  <tr><td><strong>Uji Fe³⁺</strong></td><td>Fe³⁺</td><td>Larutan + KSCN</td><td>KSCN 0.1M</td><td><span className="td-flex"><span className="dot endapan-merah" />Merah darah [Fe(SCN)]²⁺</span></td><td>+Fe³⁺</td></tr>
                  <tr><td><strong>Uji Al³⁺</strong></td><td>Al³⁺</td><td>Endapan + NaOH berlebih → larut; + aluminon</td><td>NaOH + aluminon</td><td>Endapan merah (lake aluminon)</td><td>+Al³⁺</td></tr>
                  <tr><td><strong>Uji Cr³⁺</strong></td><td>Cr³⁺</td><td>Larutan + NaOH + H₂O₂ → kuning; asamkan + BaCl₂</td><td>NaOH, H₂O₂, BaCl₂</td><td><span className="td-flex"><span className="dot endapan-kuning" />BaCrO₄ kuning</span></td><td>+Cr³⁺</td></tr>
                  <tr><td><strong>Uji Mn²⁺</strong></td><td>Mn²⁺</td><td>+ NaBiO₃ dalam HNO₃</td><td>NaBiO₃/HNO₃</td><td>Larutan ungu (MnO₄⁻)</td><td>+Mn²⁺</td></tr>
                  <tr><td><strong>Uji Ni²⁺</strong></td><td>Ni²⁺</td><td>+ Dimetilglioksim dalam NH₄OH</td><td>DMG</td><td><span className="td-flex"><span className="dot endapan-merah" />Endapan merah Ni-DMG</span></td><td>+Ni²⁺</td></tr>
                  <tr><td><strong>Uji Co²⁺</strong></td><td>Co²⁺</td><td>+ KSCN + aseton</td><td>KSCN+aseton</td><td>Larutan biru [Co(SCN)₄]²⁻</td><td>+Co²⁺</td></tr>
                  <tr><td><strong>Uji Zn²⁺</strong></td><td>Zn²⁺</td><td>+ K₄[Fe(CN)₆] asam</td><td>K₄[Fe(CN)₆]</td><td>Endapan putih Zn₂[Fe(CN)₆]</td><td>+Zn²⁺</td></tr>
                </tbody>
              </table>
            </div>
          </div>
          <div id="test-t4" style={{display: 'none'}}>
            <div className="card highlight-box" style={{padding: '.8rem 1.2rem', marginBottom: '1rem'}}>
              <strong style={{color: 'var(--accent4)'}}>Golongan IV</strong> — Reagen Pengendap: <span className="formula">(NH₄)₂CO₃ dalam NH₄OH</span>
            </div>
            <div className="table-wrap">
              <table>
                <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
                <tbody>
                  <tr><td><strong>Uji Golongan</strong></td><td>Ca²⁺, Sr²⁺, Ba²⁺</td><td>Tambahkan (NH₄)₂CO₃ dalam NH₄OH</td><td>(NH₄)₂CO₃</td><td>Endapan karbonat putih</td><td>Ada kation Gol. IV</td></tr>
                  <tr><td><strong>Uji Ba²⁺</strong></td><td>Ba²⁺</td><td>Larutan asam asetat + K₂CrO₄</td><td>K₂CrO₄</td><td><span className="td-flex"><span className="dot endapan-kuning" />BaCrO₄ kuning</span></td><td>+Ba²⁺</td></tr>
                  <tr><td><strong>Uji Sr²⁺</strong></td><td>Sr²⁺</td><td>Larutan + (NH₄)₂SO₄</td><td>(NH₄)₂SO₄</td><td>SrSO₄ putih halus (sesudah Ba²⁺ diendapkan)</td><td>+Sr²⁺</td></tr>
                  <tr><td><strong>Uji Ca²⁺</strong></td><td>Ca²⁺</td><td>Filtrat + (NH₄)₂C₂O₄</td><td>(NH₄)₂C₂O₄</td><td><span className="td-flex"><span className="dot endapan-putih" />CaC₂O₄ putih kristalin</span></td><td>+Ca²⁺</td></tr>
                  <tr><td><strong>Uji nyala Ba²⁺</strong></td><td>Ba²⁺</td><td>Uji nyala kawat platinum</td><td>—</td><td>Nyala hijau kekuningan</td><td>+Ba²⁺ nyala</td></tr>
                  <tr><td><strong>Uji nyala Ca²⁺</strong></td><td>Ca²⁺</td><td>Uji nyala kawat platinum</td><td>—</td><td>Nyala merah jingga (bata)</td><td>+Ca²⁺ nyala</td></tr>
                </tbody>
              </table>
            </div>
          </div>
          <div id="test-t5" style={{display: 'none'}}>
            <div className="card highlight-box" style={{padding: '.8rem 1.2rem', marginBottom: '1rem'}}>
              <strong style={{color: 'var(--accent5)'}}>Golongan V</strong> — Tidak ada reagen golongan; identifikasi dengan uji spesifik
            </div>
            <div className="table-wrap">
              <table>
                <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
                <tbody>
                  <tr><td><strong>Uji NH₄⁺</strong></td><td>NH₄⁺</td><td>Sampel + NaOH → panaskan, kertas lakmus merah di atas</td><td>NaOH 6M</td><td>Gas NH₃ bau tajam; lakmus merah → biru</td><td>+NH₄⁺</td></tr>
                  <tr><td><strong>Uji NH₄⁺ Nessler</strong></td><td>NH₄⁺</td><td>Larutan + reagen Nessler</td><td>K₂[HgI₄]/KOH</td><td><span className="td-flex"><span className="dot endapan-jingga" />Coklat jingga</span></td><td>+NH₄⁺ sensitif</td></tr>
                  <tr><td><strong>Uji K⁺</strong></td><td>K⁺</td><td>Larutan netral + Na₃[Co(NO₂)₆]</td><td>Na₃[Co(NO₂)₆]</td><td><span className="td-flex"><span className="dot endapan-kuning" />Endapan K₂Na[Co(NO₂)₆] kuning</span></td><td>+K⁺</td></tr>
                  <tr><td><strong>Uji nyala K⁺</strong></td><td>K⁺</td><td>Nyala melalui kaca kobalt biru</td><td>Kaca kobalt</td><td>Violet/ungu</td><td>+K⁺</td></tr>
                  <tr><td><strong>Uji Na⁺</strong></td><td>Na⁺</td><td>Uji nyala langsung</td><td>—</td><td>Kuning intens (D-line 589nm)</td><td>+Na⁺</td></tr>
                  <tr><td><strong>Uji Na⁺ spesifik</strong></td><td>Na⁺</td><td>+ Zink uranil asetat</td><td>Zn(UO₂)₃(OAc)₈</td><td>Endapan kristal kuning</td><td>+Na⁺</td></tr>
                  <tr><td><strong>Uji Mg²⁺</strong></td><td>Mg²⁺</td><td>+ Na₂HPO₄ dalam NH₄OH/NH₄Cl</td><td>Na₂HPO₄</td><td>MgNH₄PO₄ putih kristalin (microscopically cross)</td><td>+Mg²⁺</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        {/* ═══════════ TAB 4: REAKSI KATION ═══════════ */}
        <div className="tab-content" id="tab3">
          <h2>Animasi Reaksi Kation</h2>
          <p style={{marginBottom: '1.5rem'}}>Klik kartu untuk melihat animasi tabung reaksi. Perhatikan perubahan warna larutan dan pembentukan endapan.</p>
          <div className="subtab-nav">
            <button className="subtab-btn active" onclick="showSubtab('rxk','rxk1')">Gol. I</button>
            <button className="subtab-btn" onclick="showSubtab('rxk','rxk2')">Gol. II</button>
            <button className="subtab-btn" onclick="showSubtab('rxk','rxk3')">Gol. III</button>
            <button className="subtab-btn" onclick="showSubtab('rxk','rxk4')">Gol. IV</button>
            <button className="subtab-btn" onclick="showSubtab('rxk','rxk5')">Gol. V</button>
          </div>
          <div className="subtab-panel active" id="rxk-rxk1">
            <div className="reaction-grid" id="rxk1-grid" />
          </div>
          <div className="subtab-panel" id="rxk-rxk2">
            <div className="reaction-grid" id="rxk2-grid" />
          </div>
          <div className="subtab-panel" id="rxk-rxk3">
            <div className="reaction-grid" id="rxk3-grid" />
          </div>
          <div className="subtab-panel" id="rxk-rxk4">
            <div className="reaction-grid" id="rxk4-grid" />
          </div>
          <div className="subtab-panel" id="rxk-rxk5">
            <div className="reaction-grid" id="rxk5-grid" />
          </div>
        </div>
        {/* ═══════════ TAB 5: REAKSI ANION ═══════════ */}
        <div className="tab-content" id="tab4">
          <h2>Animasi Reaksi Anion</h2>
          <p style={{marginBottom: '1.5rem'}}>Klik kartu untuk melihat animasi tabung reaksi identifikasi anion.</p>
          <div className="reaction-grid" id="anion-grid" />
        </div>
        {/* ═══════════ TAB 6: KUIS ═══════════ */}
        <div className="tab-content" id="tab5">
          <div className="quiz-box">
            <div className="quiz-header">
              <h2>Kuis Kation &amp; Anion</h2>
              <p>Uji pemahamanmu tentang analisis kualitatif ion!</p>
            </div>
            <div id="quiz-main" />
          </div>
        </div>
      </div>
    );
  }
});
