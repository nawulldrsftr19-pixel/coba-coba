<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KimIA — Analisis Kation & Anion</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;600&display=swap');

  :root {
    --bg:        #0d1117;
    --surface:   #161b22;
    --surface2:  #1f2937;
    --border:    #2d3748;
    --accent1:   #7c3aed;
    --accent2:   #06b6d4;
    --accent3:   #f59e0b;
    --accent4:   #10b981;
    --accent5:   #ef4444;
    --accent6:   #ec4899;
    --text:      #f1f5f9;
    --muted:     #94a3b8;
    --glow1: rgba(124,58,237,0.25);
    --glow2: rgba(6,182,212,0.25);
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  body {
    font-family: 'Space Grotesk', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ── HEADER ── */
  header {
    position: relative;
    padding: 2rem 2rem 1.5rem;
    text-align: center;
    background: linear-gradient(135deg, #0d1117 0%, #1a0533 50%, #0d1117 100%);
    border-bottom: 1px solid var(--border);
    overflow: hidden;
  }
  header::before {
    content:'';
    position:absolute;
    inset:0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(124,58,237,.35) 0%, transparent 70%);
    pointer-events:none;
  }
  .header-badge {
    display: inline-block;
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'JetBrains Mono', monospace;
    font-size: .75rem;
    letter-spacing: .2em;
    text-transform: uppercase;
    margin-bottom: .75rem;
  }
  header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2rem, 5vw, 3.5rem);
    background: linear-gradient(135deg, #fff 0%, #c4b5fd 50%, #67e8f9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
  }
  header p {
    color: var(--muted);
    margin-top: .5rem;
    font-size: .95rem;
  }

  /* floating atoms bg */
  .atom { position:absolute; border-radius:50%; opacity:.12; animation: drift linear infinite; }

  /* ── TABS ── */
  .tab-nav {
    display: flex;
    overflow-x: auto;
    background: var(--surface);
    border-bottom: 2px solid var(--border);
    gap: 0;
    scrollbar-width: none;
  }
  .tab-nav::-webkit-scrollbar { display:none; }
  .tab-btn {
    flex: 0 0 auto;
    padding: .9rem 1.4rem;
    background: none;
    border: none;
    color: var(--muted);
    font-family: 'Space Grotesk', sans-serif;
    font-size: .85rem;
    font-weight: 500;
    cursor: pointer;
    border-bottom: 3px solid transparent;
    margin-bottom: -2px;
    transition: all .25s;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: .45rem;
  }
  .tab-btn:hover { color: var(--text); background: rgba(255,255,255,.04); }
  .tab-btn.active { color: var(--text); border-color: var(--accent1); background: rgba(124,58,237,.08); }
  .tab-btn .tab-icon { font-size: 1.1rem; }

  /* ── CONTENT ── */
  .tab-content { display:none; padding: 2rem; max-width: 1200px; margin: 0 auto; }
  .tab-content.active { display:block; }

  /* ── CARDS ── */
  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .card-gradient {
    background: linear-gradient(135deg, var(--surface) 0%, rgba(124,58,237,.08) 100%);
    border-color: rgba(124,58,237,.3);
  }

  h2 {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    margin-bottom: 1rem;
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  h3 { font-size: 1.1rem; font-weight: 600; margin-bottom: .6rem; color: var(--text); }
  p { color: var(--muted); line-height: 1.7; margin-bottom: .75rem; font-size: .95rem; }
  ul, ol { color: var(--muted); padding-left: 1.4rem; line-height: 1.9; font-size: .95rem; }

  /* ── GRID ── */
  .grid-2 { display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; }
  .grid-3 { display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }

  /* ── STEP CARDS (Tab 1) ── */
  .step-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.25rem;
    position: relative;
    overflow: hidden;
    transition: transform .2s, border-color .2s;
  }
  .step-card:hover { transform: translateY(-3px); }
  .step-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
  }
  .step-card:nth-child(1)::before { background: linear-gradient(90deg, var(--accent1), var(--accent2)); }
  .step-card:nth-child(2)::before { background: linear-gradient(90deg, var(--accent2), var(--accent4)); }
  .step-card:nth-child(3)::before { background: linear-gradient(90deg, var(--accent4), var(--accent3)); }
  .step-card:nth-child(4)::before { background: linear-gradient(90deg, var(--accent3), var(--accent5)); }
  .step-card:nth-child(5)::before { background: linear-gradient(90deg, var(--accent5), var(--accent6)); }
  .step-card:nth-child(6)::before { background: linear-gradient(90deg, var(--accent6), var(--accent1)); }
  .step-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: rgba(124,58,237,.3);
    line-height: 1;
    margin-bottom: .5rem;
  }

  /* ── MATERI TABS (Tab 2) ── */
  .subtab-nav {
    display: flex;
    gap: .5rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
  }
  .subtab-btn {
    padding: .5rem 1.1rem;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: none;
    color: var(--muted);
    font-family: 'Space Grotesk', sans-serif;
    font-size: .82rem;
    cursor: pointer;
    transition: all .2s;
  }
  .subtab-btn:hover { border-color: var(--accent1); color: var(--text); }
  .subtab-btn.active { background: var(--accent1); border-color: var(--accent1); color: #fff; }
  .subtab-panel { display:none; }
  .subtab-panel.active { display:block; }

  /* ── GOLONGAN BADGE ── */
  .gol-badge {
    display: inline-block;
    padding: .25rem .75rem;
    border-radius: 999px;
    font-size: .78rem;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: .75rem;
  }
  .gol1 { background: rgba(124,58,237,.2); color: #c4b5fd; border: 1px solid rgba(124,58,237,.4); }
  .gol2 { background: rgba(6,182,212,.2); color: #67e8f9; border: 1px solid rgba(6,182,212,.4); }
  .gol3 { background: rgba(245,158,11,.2); color: #fcd34d; border: 1px solid rgba(245,158,11,.4); }
  .gol4 { background: rgba(16,185,129,.2); color: #6ee7b7; border: 1px solid rgba(16,185,129,.4); }
  .gol5 { background: rgba(239,68,68,.2); color: #fca5a5; border: 1px solid rgba(239,68,68,.4); }
  .anion { background: rgba(236,72,153,.2); color: #f9a8d4; border: 1px solid rgba(236,72,153,.4); }

  /* ion chips */
  .ion-chips { display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.75rem; }
  .ion-chip {
    padding: .3rem .8rem;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: .82rem;
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
  }

  /* ── PENGUJIAN TABLE (Tab 3) ── */
  .test-nav {
    display: flex;
    gap: .5rem;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
  }
  .test-btn {
    padding: .5rem 1.1rem;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--muted);
    font-size: .85rem;
    cursor: pointer;
    font-family: 'Space Grotesk', sans-serif;
    transition: all .2s;
  }
  .test-btn:hover { border-color: var(--accent2); color: var(--text); }
  .test-btn.active { background: linear-gradient(135deg, var(--accent1), var(--accent2)); border-color: transparent; color: #fff; }

  .table-wrap { overflow-x: auto; border-radius: 12px; border: 1px solid var(--border); }
  table { width:100%; border-collapse: collapse; font-size: .88rem; }
  thead { background: linear-gradient(90deg, rgba(124,58,237,.25), rgba(6,182,212,.15)); }
  th { padding: .85rem 1rem; text-align:left; font-weight:600; font-size:.8rem; letter-spacing:.05em; text-transform:uppercase; color: var(--accent2); }
  td { padding: .8rem 1rem; border-top: 1px solid rgba(255,255,255,.05); color: var(--muted); vertical-align:top; line-height:1.5; }
  tr:hover td { background: rgba(124,58,237,.06); color: var(--text); }

  /* result dots */
  .dot { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; flex-shrink:0; }
  .endapan-putih { background:#e2e8f0; }
  .endapan-kuning { background:#fde047; }
  .endapan-hitam  { background:#1e293b; border:1px solid #475569; }
  .endapan-merah  { background:#ef4444; }
  .endapan-jingga { background:#f97316; }
  .endapan-biru   { background:#3b82f6; }
  .larut          { background:linear-gradient(135deg,#22c55e,#16a34a); }
  .td-flex { display:flex; align-items:center; }

  /* ── REAKSI + ANIMASI (Tab 4 & 5) ── */
  .reaction-grid { display:grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.25rem; }
  .reaction-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    transition: transform .25s, box-shadow .25s;
    cursor: pointer;
  }
  .reaction-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,0,0,.4); }
  .reaction-header {
    padding: .9rem 1.2rem;
    display:flex;
    justify-content:space-between;
    align-items:center;
  }
  .reaction-title { font-weight: 600; font-size: 1rem; }
  .reaction-reagent { font-size: .75rem; color: var(--muted); font-family:'JetBrains Mono',monospace; }

  /* Test tube animation */
  .tube-wrap {
    display:flex;
    justify-content:center;
    align-items:flex-end;
    gap: 1rem;
    padding: 1rem 1rem .5rem;
    background: rgba(0,0,0,.2);
    min-height: 140px;
    flex-wrap: wrap;
  }
  .tube-container { display:flex; flex-direction:column; align-items:center; gap:.3rem; }
  .tube-label { font-size:.68rem; color:var(--muted); font-family:'JetBrains Mono',monospace; text-align:center; max-width:64px; word-break:break-word; }
  .tube {
    width: 36px;
    height: 90px;
    border: 2px solid rgba(255,255,255,.25);
    border-radius: 0 0 18px 18px;
    border-top: none;
    position: relative;
    overflow: hidden;
    background: rgba(255,255,255,.04);
  }
  .tube::before {
    content:'';
    position:absolute;
    top:0; left:0; right:0;
    height:100%;
    background:linear-gradient(90deg, rgba(255,255,255,.12) 0%, transparent 40%, rgba(255,255,255,.06) 100%);
    z-index:2;
    pointer-events:none;
  }
  .liquid {
    position: absolute;
    bottom: 0;
    left: 0; right: 0;
    transition: height 1.2s cubic-bezier(.4,0,.2,1), background-color 1.4s ease;
    border-radius: 0 0 16px 16px;
  }
  .sediment {
    position:absolute;
    bottom:0;
    left:0; right:0;
    height:0;
    border-radius:0 0 16px 16px;
    transition: height 1.5s ease 0.4s;
  }
  .reaction-info { padding: .9rem 1.2rem; }
  .rxn-eq {
    font-family:'JetBrains Mono',monospace;
    font-size:.75rem;
    color: var(--accent2);
    background: rgba(6,182,212,.08);
    border: 1px solid rgba(6,182,212,.2);
    border-radius:8px;
    padding:.6rem .8rem;
    margin-top:.5rem;
    word-break:break-all;
    line-height:1.6;
  }
  .obs-badge {
    display:inline-flex;
    align-items:center;
    gap:.4rem;
    padding:.3rem .7rem;
    border-radius:999px;
    font-size:.75rem;
    margin-top:.5rem;
    border: 1px solid;
  }

  /* ── QUIZ (Tab 6) ── */
  .quiz-box {
    max-width: 680px;
    margin: 0 auto;
  }
  .quiz-header {
    text-align:center;
    margin-bottom:2rem;
  }
  .progress-bar-wrap {
    background: var(--surface2);
    border-radius:999px;
    height:6px;
    margin-bottom:1.5rem;
    overflow:hidden;
  }
  .progress-bar {
    height:100%;
    border-radius:999px;
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    transition: width .4s ease;
  }
  .question-num { color:var(--muted); font-size:.85rem; margin-bottom:.5rem; }
  .question-text {
    font-size:1.15rem;
    font-weight:600;
    line-height:1.5;
    margin-bottom:1.5rem;
    color: var(--text);
  }
  .option-list { list-style:none; padding:0; display:flex; flex-direction:column; gap:.75rem; }
  .option-btn {
    width:100%;
    text-align:left;
    padding: .9rem 1.2rem;
    border-radius:12px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-family:'Space Grotesk',sans-serif;
    font-size:.95rem;
    cursor:pointer;
    transition: all .2s;
    position:relative;
  }
  .option-btn:hover:not(:disabled) { border-color: var(--accent1); background: rgba(124,58,237,.08); }
  .option-btn.correct { border-color: var(--accent4) !important; background: rgba(16,185,129,.12) !important; color: #6ee7b7 !important; }
  .option-btn.wrong   { border-color: var(--accent5) !important; background: rgba(239,68,68,.12) !important; color: #fca5a5 !important; }
  .option-btn:disabled { cursor: default; }
  .explanation {
    margin-top:1rem;
    padding:1rem;
    border-radius:10px;
    background: rgba(6,182,212,.08);
    border:1px solid rgba(6,182,212,.2);
    color: var(--accent2);
    font-size:.88rem;
    line-height:1.6;
  }
  .quiz-controls { display:flex; justify-content:space-between; align-items:center; margin-top:1.5rem; }
  .btn {
    padding: .7rem 1.6rem;
    border-radius:10px;
    border:none;
    font-family:'Space Grotesk',sans-serif;
    font-weight:600;
    font-size:.9rem;
    cursor:pointer;
    transition: all .2s;
  }
  .btn-primary {
    background: linear-gradient(135deg, var(--accent1), var(--accent2));
    color:#fff;
  }
  .btn-primary:hover { opacity:.85; transform:translateY(-1px); }
  .btn-secondary { background:var(--surface2); color:var(--text); border:1px solid var(--border); }
  .btn-secondary:hover { border-color:var(--accent1); }

  .score-screen {
    text-align:center;
    padding: 3rem 2rem;
  }
  .score-ring {
    width:140px; height:140px;
    border-radius:50%;
    margin:0 auto 1.5rem;
    display:flex; align-items:center; justify-content:center;
    font-size:2.5rem;
    font-weight:700;
    background: conic-gradient(var(--accent1) 0%, var(--accent2) 50%, var(--border) 50%);
    position:relative;
  }
  .score-ring::after {
    content:'';
    position:absolute;
    inset:12px;
    background: var(--bg);
    border-radius:50%;
  }
  .score-num {
    position:relative;
    z-index:1;
    font-family:'DM Serif Display',serif;
  }
  .score-label { color:var(--muted); margin-top:.25rem; }

  /* ── SCROLLBAR ── */
  ::-webkit-scrollbar { width:6px; height:6px; }
  ::-webkit-scrollbar-track { background:transparent; }
  ::-webkit-scrollbar-thumb { background:var(--border); border-radius:3px; }

  /* ── INFO PILL ── */
  .info-pill {
    display:inline-flex; align-items:center; gap:.4rem;
    padding:.3rem .9rem;
    border-radius:999px;
    font-size:.78rem;
    background:rgba(245,158,11,.12);
    border:1px solid rgba(245,158,11,.3);
    color:#fcd34d;
    margin-bottom:1.5rem;
  }

  /* glow card */
  .glow-card {
    box-shadow: 0 0 0 1px rgba(124,58,237,.2), 0 8px 32px rgba(124,58,237,.15);
  }

  /* divider */
  .divider { border:none; border-top:1px solid var(--border); margin:1.5rem 0; }

  /* chemical formula styling */
  .formula { font-family:'JetBrains Mono',monospace; color:var(--accent3); font-size:.9rem; }

  @keyframes drift {
    0% { transform: translateY(0) rotate(0deg); }
    100% { transform: translateY(-200px) rotate(360deg); }
  }
  @keyframes pop { 0%{transform:scale(.95);opacity:0} 100%{transform:scale(1);opacity:1} }
  .pop { animation: pop .3s ease; }

  .highlight-box {
    background: linear-gradient(135deg, rgba(124,58,237,.1), rgba(6,182,212,.08));
    border: 1px solid rgba(124,58,237,.25);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 1rem;
  }

  /* Tube rack */
  .tube-rack {
    display:flex;
    justify-content:center;
    gap:1.5rem;
    flex-wrap:wrap;
    padding: 1.5rem 1rem;
    background: linear-gradient(180deg, rgba(0,0,0,.3), rgba(0,0,0,.1));
    border-radius:0 0 14px 14px;
    min-height:160px;
    align-items:flex-end;
  }
  .tube-unit { display:flex; flex-direction:column; align-items:center; gap:.4rem; }
  .tube-cap {
    width:42px; height:8px;
    background: rgba(255,255,255,.15);
    border-radius:4px 4px 0 0;
    border: 1px solid rgba(255,255,255,.2);
  }
  .tube-body {
    width:38px; height:100px;
    border: 2px solid rgba(255,255,255,.2);
    border-top:none;
    border-radius: 0 0 19px 19px;
    position:relative;
    overflow:hidden;
    background: rgba(255,255,255,.03);
  }
  .tube-body::before {
    content:'';
    position:absolute;
    left:5px; top:0; bottom:0; width:4px;
    background: rgba(255,255,255,.1);
    border-radius:2px;
  }
  .tube-liquid {
    position:absolute;
    bottom:0; left:0; right:0;
    transition: height 1.2s cubic-bezier(.4,0,.2,1);
    border-radius: 0 0 17px 17px;
  }
  .tube-sediment {
    position:absolute;
    bottom:0; left:0; right:0;
    border-radius: 0 0 17px 17px;
    transition: height 1.5s ease .5s;
  }
  .tube-name {
    font-size:.7rem;
    font-family:'JetBrains Mono',monospace;
    color:var(--muted);
    text-align:center;
    max-width:60px;
    word-break:break-word;
    line-height:1.3;
  }
</style>
</head>
<body>

<!-- decorative atoms -->
<script>
document.addEventListener('DOMContentLoaded',()=>{
  const h = document.querySelector('header');
  for(let i=0;i<8;i++){
    const a=document.createElement('div');
    a.className='atom';
    const s=Math.random()*60+20;
    a.style.cssText=`width:${s}px;height:${s}px;left:${Math.random()*100}%;top:${Math.random()*100}%;background:${['#7c3aed','#06b6d4','#f59e0b','#10b981'][Math.floor(Math.random()*4)]};animation-duration:${Math.random()*15+10}s;animation-delay:-${Math.random()*10}s`;
    h.appendChild(a);
  }
});
</script>

<header>
  <div class="header-badge">⚗️ Aplikasi Kimia Analitik</div>
  <h1>Kation &amp; Anion</h1>
  <p>Panduan lengkap analisis kualitatif ion dalam larutan</p>
</header>

<nav class="tab-nav">
  <button class="tab-btn active" onclick="showTab(0)"><span class="tab-icon">🏠</span> Panduan</button>
  <button class="tab-btn" onclick="showTab(1)"><span class="tab-icon">📚</span> Materi</button>
  <button class="tab-btn" onclick="showTab(2)"><span class="tab-icon">🧪</span> Pengujian</button>
  <button class="tab-btn" onclick="showTab(3)"><span class="tab-icon">⚗️</span> Reaksi Kation</button>
  <button class="tab-btn" onclick="showTab(4)"><span class="tab-icon">🔬</span> Reaksi Anion</button>
  <button class="tab-btn" onclick="showTab(5)"><span class="tab-icon">🎯</span> Kuis</button>
</nav>

<!-- ═══════════ TAB 1: PANDUAN ═══════════ -->
<div class="tab-content active" id="tab0">
  <div class="card card-gradient glow-card" style="text-align:center; padding:2rem;">
    <div style="font-size:3rem; margin-bottom:1rem;">⚗️</div>
    <h2 style="font-size:2rem;">Selamat Datang di KimIA</h2>
    <p style="max-width:560px; margin:0 auto 1rem;">Platform interaktif untuk mempelajari analisis kualitatif <strong style="color:var(--accent2)">Kation</strong> (Golongan I–V) dan <strong style="color:var(--accent6)">Anion</strong> secara lengkap, visual, dan menyenangkan.</p>
    <div class="info-pill">✨ Dibuat untuk mahasiswa kimia &amp; analis laboratorium</div>
  </div>

  <h2>Cara Menggunakan Aplikasi</h2>
  <div class="grid-2">
    <div class="step-card">
      <div class="step-num">01</div>
      <h3>📚 Pelajari Materi</h3>
      <p>Buka Tab <strong>Materi</strong> untuk membaca teori lengkap kation golongan I–V dan anion beserta ciri-ciri, reagen, dan karakteristiknya.</p>
    </div>
    <div class="step-card">
      <div class="step-num">02</div>
      <h3>🧪 Ikuti Prosedur Pengujian</h3>
      <p>Di Tab <strong>Pengujian</strong>, pilih golongan kation dan ikuti tabel prosedur uji sistematis mulai dari uji pendahuluan hingga uji spesifik.</p>
    </div>
    <div class="step-card">
      <div class="step-num">03</div>
      <h3>⚗️ Lihat Animasi Reaksi Kation</h3>
      <p>Tab <strong>Reaksi Kation</strong> menampilkan animasi tabung reaksi berwarna dan persamaan reaksi kimia untuk setiap kation.</p>
    </div>
    <div class="step-card">
      <div class="step-num">04</div>
      <h3>🔬 Lihat Animasi Reaksi Anion</h3>
      <p>Tab <strong>Reaksi Anion</strong> menampilkan animasi tabung reaksi dan reaksi kimia untuk identifikasi anion penting.</p>
    </div>
    <div class="step-card">
      <div class="step-num">05</div>
      <h3>🎯 Uji Pemahaman</h3>
      <p>Kerjakan <strong>Kuis</strong> di Tab 6 untuk menguji pemahamanmu. Ada feedback langsung dan penjelasan jawaban.</p>
    </div>
    <div class="step-card">
      <div class="step-num">06</div>
      <h3>🔄 Ulang &amp; Kuasai</h3>
      <p>Navigasi bebas antar tab kapan saja. Kuis bisa diulang untuk meningkatkan skor. Selamat belajar!</p>
    </div>
  </div>

  <div class="card" style="margin-top:1.5rem;">
    <h2>Tentang Aplikasi</h2>
    <div class="grid-2">
      <div>
        <h3>🎯 Tujuan</h3>
        <p>Membantu mahasiswa kimia memahami analisis kualitatif kation dan anion melalui visualisasi interaktif, animasi reaksi, dan latihan soal yang komprehensif.</p>
        <h3 style="margin-top:1rem;">📋 Cakupan Materi</h3>
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
        <div class="highlight-box" style="margin-top:1rem;">
          <strong style="color:var(--accent3)">⚠️ Catatan:</strong>
          <p style="margin:0; font-size:.88rem;">Aplikasi ini bersifat edukatif. Selalu ikuti prosedur keselamatan laboratorium saat melakukan percobaan nyata.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════ TAB 2: MATERI ═══════════ -->
<div class="tab-content" id="tab1">
  <h2>Materi Kation &amp; Anion</h2>

  <div class="subtab-nav">
    <button class="subtab-btn active" onclick="showSubtab('materi','gol1')">Gol. I</button>
    <button class="subtab-btn" onclick="showSubtab('materi','gol2')">Gol. II</button>
    <button class="subtab-btn" onclick="showSubtab('materi','gol3')">Gol. III</button>
    <button class="subtab-btn" onclick="showSubtab('materi','gol4')">Gol. IV</button>
    <button class="subtab-btn" onclick="showSubtab('materi','gol5')">Gol. V</button>
    <button class="subtab-btn" onclick="showSubtab('materi','anion')">Anion</button>
  </div>

  <!-- GOL I -->
  <div class="subtab-panel active" id="materi-gol1">
    <div class="gol-badge gol1">Golongan I — Klorida Tidak Larut</div>
    <div class="card">
      <h3>Prinsip Pemisahan</h3>
      <p>Kation Golongan I diendapkan sebagai <strong style="color:var(--accent2)">klorida tidak larut</strong> dengan penambahan HCl encer ke larutan sampel. Ini merupakan golongan pertama yang dipisahkan dalam analisis sistematik.</p>
      <p><strong>Reagen pengendap:</strong> HCl encer (2M)</p>
      <div class="ion-chips">
        <span class="ion-chip">Ag⁺ (Perak)</span>
        <span class="ion-chip">Hg₂²⁺ (Merkuri I)</span>
        <span class="ion-chip">Pb²⁺ (Timbal)</span>
      </div>
    </div>
    <div class="grid-3">
      <div class="card">
        <div class="gol-badge gol1">Ag⁺</div>
        <h3>Ion Perak</h3>
        <p><strong>Endapan:</strong> AgCl — putih</p>
        <p><strong>Uji spesifik:</strong> Larut dalam NH₄OH berlebih, tidak larut HNO₃</p>
        <p><strong>Pengamatan:</strong> Dengan K₂CrO₄ → AgCrO₄ merah bata</p>
        <div class="rxn-eq">Ag⁺ + Cl⁻ → AgCl↓ (putih)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol1">Hg₂²⁺</div>
        <h3>Ion Merkuri(I)</h3>
        <p><strong>Endapan:</strong> Hg₂Cl₂ — putih</p>
        <p><strong>Uji spesifik:</strong> + NH₄OH → hitam (campuran Hg + HgNH₂Cl)</p>
        <p><strong>Pengamatan:</strong> Berubah hitam saat ditambah amonia</p>
        <div class="rxn-eq">Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓ (putih)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol1">Pb²⁺</div>
        <h3>Ion Timbal</h3>
        <p><strong>Endapan:</strong> PbCl₂ — putih</p>
        <p><strong>Uji spesifik:</strong> Larut dalam air panas, + K₂CrO₄ → PbCrO₄ kuning</p>
        <p><strong>Pengamatan:</strong> Endapan larut saat dipanaskan</p>
        <div class="rxn-eq">Pb²⁺ + 2Cl⁻ → PbCl₂↓ (putih)</div>
      </div>
    </div>
  </div>

  <!-- GOL II -->
  <div class="subtab-panel" id="materi-gol2">
    <div class="gol-badge gol2">Golongan II — Sulfida dalam Suasana Asam</div>
    <div class="card">
      <h3>Prinsip Pemisahan</h3>
      <p>Kation Golongan II diendapkan sebagai <strong style="color:var(--accent2)">sulfida</strong> dengan mengalirkan gas H₂S dalam suasana asam (HCl 0.3M). Kation golongan ini memiliki Ksp sulfida yang sangat kecil.</p>
      <p><strong>Reagen pengendap:</strong> H₂S gas / (NH₄)₂S dalam HCl encer</p>
      <div class="ion-chips">
        <span class="ion-chip">Cu²⁺</span><span class="ion-chip">Bi³⁺</span>
        <span class="ion-chip">Cd²⁺</span><span class="ion-chip">Hg²⁺</span>
        <span class="ion-chip">Sn²⁺/Sn⁴⁺</span><span class="ion-chip">As³⁺/As⁵⁺</span>
        <span class="ion-chip">Sb³⁺</span>
      </div>
    </div>
    <div class="grid-2">
      <div class="card">
        <div class="gol-badge gol2">Cu²⁺ — Tembaga</div>
        <p><strong>Endapan:</strong> CuS — hitam</p>
        <p><strong>Uji spesifik:</strong> Larut dalam HNO₃ panas → biru dalam NH₄OH berlebih</p>
        <div class="rxn-eq">Cu²⁺ + S²⁻ → CuS↓ (hitam)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol2">Bi³⁺ — Bismut</div>
        <p><strong>Endapan:</strong> Bi₂S₃ — hitam</p>
        <p><strong>Uji spesifik:</strong> Dengan SnCl₂ → Bi hitam (reduksi)</p>
        <div class="rxn-eq">2Bi³⁺ + 3S²⁻ → Bi₂S₃↓ (hitam)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol2">Cd²⁺ — Kadmium</div>
        <p><strong>Endapan:</strong> CdS — kuning</p>
        <p><strong>Uji spesifik:</strong> Larut dalam HCl panas, tidak larut dalam (NH₄)₂S</p>
        <div class="rxn-eq">Cd²⁺ + S²⁻ → CdS↓ (kuning)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol2">Sn²⁺ — Timah</div>
        <p><strong>Endapan:</strong> SnS — coklat</p>
        <p><strong>Uji spesifik:</strong> Larut dalam (NH₄)₂Sx → SnS₃²⁻</p>
        <div class="rxn-eq">Sn²⁺ + S²⁻ → SnS↓ (coklat)</div>
      </div>
    </div>
  </div>

  <!-- GOL III -->
  <div class="subtab-panel" id="materi-gol3">
    <div class="gol-badge gol3">Golongan III — Sulfida/Hidroksida dalam Suasana Basa</div>
    <div class="card">
      <h3>Prinsip Pemisahan</h3>
      <p>Kation Golongan III dibagi dua sub-golongan: <strong style="color:#fcd34d">IIIa</strong> yang mengendap sebagai <strong>sulfida</strong> (CoS, NiS, MnS, ZnS) dan <strong style="color:#fcd34d">IIIb</strong> yang mengendap sebagai <strong>hidroksida</strong> (Fe(OH)₃, Al(OH)₃, Cr(OH)₃).</p>
      <p><strong>Reagen pengendap:</strong> (NH₄)₂S dalam NH₄OH/NH₄Cl</p>
      <div class="ion-chips">
        <span class="ion-chip">Fe³⁺</span><span class="ion-chip">Al³⁺</span>
        <span class="ion-chip">Cr³⁺</span><span class="ion-chip">Mn²⁺</span>
        <span class="ion-chip">Ni²⁺</span><span class="ion-chip">Co²⁺</span>
        <span class="ion-chip">Zn²⁺</span>
      </div>
    </div>
    <div class="grid-3">
      <div class="card">
        <div class="gol-badge gol3">Fe³⁺ — Besi</div>
        <p><strong>Endapan:</strong> Fe(OH)₃ — coklat merah</p>
        <p><strong>Uji spesifik:</strong> + KSCN → merah darah</p>
        <div class="rxn-eq">Fe³⁺ + 3OH⁻ → Fe(OH)₃↓</div>
      </div>
      <div class="card">
        <div class="gol-badge gol3">Al³⁺ — Aluminium</div>
        <p><strong>Endapan:</strong> Al(OH)₃ — putih gelatin</p>
        <p><strong>Uji spesifik:</strong> Larut dalam NaOH berlebih (amfoter)</p>
        <div class="rxn-eq">Al³⁺ + 3OH⁻ → Al(OH)₃↓</div>
      </div>
      <div class="card">
        <div class="gol-badge gol3">Cr³⁺ — Kromium</div>
        <p><strong>Endapan:</strong> Cr(OH)₃ — hijau abu</p>
        <p><strong>Uji spesifik:</strong> Oksidasi → CrO₄²⁻ kuning</p>
        <div class="rxn-eq">Cr³⁺ + 3OH⁻ → Cr(OH)₃↓</div>
      </div>
      <div class="card">
        <div class="gol-badge gol3">Mn²⁺ — Mangan</div>
        <p><strong>Endapan:</strong> MnS — merah muda</p>
        <p><strong>Uji spesifik:</strong> Oksidasi → MnO₄⁻ ungu</p>
        <div class="rxn-eq">Mn²⁺ + S²⁻ → MnS↓ (merah muda)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol3">Ni²⁺ — Nikel</div>
        <p><strong>Endapan:</strong> NiS — hitam</p>
        <p><strong>Uji spesifik:</strong> + Dimetilglioksim → merah</p>
        <div class="rxn-eq">Ni²⁺ + S²⁻ → NiS↓ (hitam)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol3">Zn²⁺ — Seng</div>
        <p><strong>Endapan:</strong> ZnS — putih</p>
        <p><strong>Uji spesifik:</strong> Larut dalam HCl, + K₄[Fe(CN)₆] → putih</p>
        <div class="rxn-eq">Zn²⁺ + S²⁻ → ZnS↓ (putih)</div>
      </div>
    </div>
  </div>

  <!-- GOL IV -->
  <div class="subtab-panel" id="materi-gol4">
    <div class="gol-badge gol4">Golongan IV — Karbonat dalam Suasana Basa</div>
    <div class="card">
      <h3>Prinsip Pemisahan</h3>
      <p>Kation Golongan IV diendapkan sebagai <strong style="color:#6ee7b7">karbonat</strong> menggunakan (NH₄)₂CO₃ dalam suasana basa (NH₄OH). Golongan ini mencakup logam alkali tanah yang tidak mengendap pada golongan sebelumnya.</p>
      <p><strong>Reagen pengendap:</strong> (NH₄)₂CO₃ dalam NH₄OH</p>
      <div class="ion-chips">
        <span class="ion-chip">Ca²⁺ (Kalsium)</span>
        <span class="ion-chip">Sr²⁺ (Stronsium)</span>
        <span class="ion-chip">Ba²⁺ (Barium)</span>
      </div>
    </div>
    <div class="grid-3">
      <div class="card">
        <div class="gol-badge gol4">Ca²⁺ — Kalsium</div>
        <p><strong>Endapan:</strong> CaCO₃ — putih</p>
        <p><strong>Uji spesifik:</strong> + (NH₄)₂C₂O₄ → CaC₂O₄ putih; nyala: merah jingga</p>
        <div class="rxn-eq">Ca²⁺ + CO₃²⁻ → CaCO₃↓ (putih)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol4">Sr²⁺ — Stronsium</div>
        <p><strong>Endapan:</strong> SrCO₃ — putih</p>
        <p><strong>Uji spesifik:</strong> + H₂SO₄ → SrSO₄ putih tidak larut; nyala: merah karmin</p>
        <div class="rxn-eq">Sr²⁺ + CO₃²⁻ → SrCO₃↓ (putih)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol4">Ba²⁺ — Barium</div>
        <p><strong>Endapan:</strong> BaCO₃ — putih</p>
        <p><strong>Uji spesifik:</strong> + K₂CrO₄ → BaCrO₄ kuning; nyala: hijau kekuningan</p>
        <div class="rxn-eq">Ba²⁺ + CO₃²⁻ → BaCO₃↓ (putih)</div>
      </div>
    </div>
  </div>

  <!-- GOL V -->
  <div class="subtab-panel" id="materi-gol5">
    <div class="gol-badge gol5">Golongan V — Tidak Terendapkan</div>
    <div class="card">
      <h3>Prinsip Identifikasi</h3>
      <p>Kation Golongan V adalah kation yang <strong style="color:#fca5a5">tidak dapat diendapkan</strong> oleh reagen golongan I–IV. Identifikasi dilakukan melalui uji spesifik masing-masing ion menggunakan reagen karakteristik.</p>
      <div class="ion-chips">
        <span class="ion-chip">Mg²⁺ (Magnesium)</span>
        <span class="ion-chip">K⁺ (Kalium)</span>
        <span class="ion-chip">Na⁺ (Natrium)</span>
        <span class="ion-chip">NH₄⁺ (Amonium)</span>
      </div>
    </div>
    <div class="grid-2">
      <div class="card">
        <div class="gol-badge gol5">Mg²⁺ — Magnesium</div>
        <p><strong>Uji spesifik:</strong> + Na₂HPO₄ + NH₄OH → MgNH₄PO₄ putih kristalin</p>
        <p><strong>Uji lain:</strong> + Titan Yellow → merah dalam basa</p>
        <div class="rxn-eq">Mg²⁺ + NH₄⁺ + PO₄³⁻ → MgNH₄PO₄↓ (putih)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol5">K⁺ — Kalium</div>
        <p><strong>Uji spesifik:</strong> + Na₃[Co(NO₂)₆] → K₂Na[Co(NO₂)₆] kuning</p>
        <p><strong>Uji nyala:</strong> Violet/ungu melalui kaca kobalt</p>
        <div class="rxn-eq">2K⁺ + Na⁺ + [Co(NO₂)₆]³⁻ → K₂Na[Co(NO₂)₆]↓</div>
      </div>
      <div class="card">
        <div class="gol-badge gol5">Na⁺ — Natrium</div>
        <p><strong>Uji spesifik:</strong> + Zn(UO₂)₃(CH₃COO)₈ → kuning kristalin</p>
        <p><strong>Uji nyala:</strong> Kuning intensif (D-line)</p>
        <div class="rxn-eq">Na⁺ → nyala kuning (589 nm)</div>
      </div>
      <div class="card">
        <div class="gol-badge gol5">NH₄⁺ — Amonium</div>
        <p><strong>Uji spesifik:</strong> + NaOH panas → gas NH₃ (bau tajam, kertas lakmus merah → biru)</p>
        <p><strong>Uji Nessler:</strong> + reagen Nessler → coklat jingga</p>
        <div class="rxn-eq">NH₄⁺ + OH⁻ → NH₃↑ + H₂O</div>
      </div>
    </div>
  </div>

  <!-- ANION -->
  <div class="subtab-panel" id="materi-anion">
    <div class="gol-badge anion">Anion — Ion Bermuatan Negatif</div>
    <div class="card">
      <h3>Pengantar Analisis Anion</h3>
      <p>Analisis anion melibatkan identifikasi ion negatif dalam larutan. Berbeda dengan kation, anion tidak memiliki skema pemisahan golongan yang seragam. Identifikasi dilakukan melalui <strong style="color:var(--accent6)">uji pendahuluan</strong> (warna, bau, uji nyala) dan <strong style="color:var(--accent6)">uji spesifik</strong>.</p>
    </div>
    <div class="grid-2">
      <div class="card">
        <div class="gol-badge anion">Cl⁻ — Klorida</div>
        <p><strong>Uji spesifik:</strong> + AgNO₃ → AgCl putih, larut dalam NH₄OH</p>
        <div class="rxn-eq">Ag⁺ + Cl⁻ → AgCl↓ (putih)</div>
      </div>
      <div class="card">
        <div class="gol-badge anion">SO₄²⁻ — Sulfat</div>
        <p><strong>Uji spesifik:</strong> + BaCl₂ → BaSO₄ putih, tidak larut HCl/HNO₃</p>
        <div class="rxn-eq">Ba²⁺ + SO₄²⁻ → BaSO₄↓ (putih)</div>
      </div>
      <div class="card">
        <div class="gol-badge anion">CO₃²⁻ — Karbonat</div>
        <p><strong>Uji spesifik:</strong> + HCl → gas CO₂ (mengeruhkan Ca(OH)₂)</p>
        <div class="rxn-eq">CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O</div>
      </div>
      <div class="card">
        <div class="gol-badge anion">NO₃⁻ — Nitrat</div>
        <p><strong>Uji cincin coklat:</strong> + FeSO₄ + H₂SO₄ pekat → cincin coklat Fe[NO]SO₄</p>
        <div class="rxn-eq">Fe²⁺ + NO → [Fe(NO)]²⁺ (coklat)</div>
      </div>
      <div class="card">
        <div class="gol-badge anion">PO₄³⁻ — Fosfat</div>
        <p><strong>Uji spesifik:</strong> + AgNO₃ → Ag₃PO₄ kuning; + molibdat → kuning kristalin</p>
        <div class="rxn-eq">3Ag⁺ + PO₄³⁻ → Ag₃PO₄↓ (kuning)</div>
      </div>
      <div class="card">
        <div class="gol-badge anion">I⁻ — Iodida</div>
        <p><strong>Uji spesifik:</strong> + AgNO₃ → AgI kuning; + Cl₂/kanji → biru (I₂)</p>
        <div class="rxn-eq">Ag⁺ + I⁻ → AgI↓ (kuning)</div>
      </div>
      <div class="card">
        <div class="gol-badge anion">S²⁻ — Sulfida</div>
        <p><strong>Uji spesifik:</strong> + Pb(CH₃COO)₂ → PbS hitam; bau telur busuk</p>
        <div class="rxn-eq">Pb²⁺ + S²⁻ → PbS↓ (hitam)</div>
      </div>
      <div class="card">
        <div class="gol-badge anion">CH₃COO⁻ — Asetat</div>
        <p><strong>Uji spesifik:</strong> + FeCl₃ → merah coklat (besi asetat); bau cuka saat dipanaskan</p>
        <div class="rxn-eq">3CH₃COO⁻ + Fe³⁺ → Fe(CH₃COO)₃ (merah coklat)</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════ TAB 3: PENGUJIAN ═══════════ -->
<div class="tab-content" id="tab2">
  <h2>Tabel Prosedur Pengujian Kation</h2>
  <p style="margin-bottom:1.5rem;">Pilih golongan kation untuk melihat prosedur pengujian sistematis dari uji pendahuluan hingga uji spesifik.</p>

  <div class="test-nav">
    <button class="test-btn active" onclick="showTest('t1')">Golongan I</button>
    <button class="test-btn" onclick="showTest('t2')">Golongan II</button>
    <button class="test-btn" onclick="showTest('t3')">Golongan III</button>
    <button class="test-btn" onclick="showTest('t4')">Golongan IV</button>
    <button class="test-btn" onclick="showTest('t5')">Golongan V</button>
  </div>

  <div id="test-t1">
    <div class="card highlight-box" style="padding:.8rem 1.2rem; margin-bottom:1rem;">
      <strong style="color:var(--accent1)">Golongan I</strong> — Reagen Pengendap: <span class="formula">HCl 2M</span> → Endapan: Klorida tidak larut
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
        <tbody>
          <tr><td><strong>Uji Golongan</strong></td><td>Ag⁺, Hg₂²⁺, Pb²⁺</td><td>Tambahkan HCl 2M ke larutan sampel</td><td>HCl 2M</td><td><span class="td-flex"><span class="dot endapan-putih"></span>Endapan putih terbentuk</span></td><td>Ada kation Gol. I</td></tr>
          <tr><td><strong>Pemisahan Pb²⁺</strong></td><td>Pb²⁺</td><td>Cuci endapan dengan air panas 80°C</td><td>Air panas</td><td><span class="td-flex"><span class="dot larut"></span>Pb²⁺ larut, Ag⁺ dan Hg₂²⁺ tetap</span></td><td>Identifikasi Pb²⁺</td></tr>
          <tr><td><strong>Uji Pb²⁺</strong></td><td>Pb²⁺</td><td>Filtrat panas + K₂CrO₄</td><td>K₂CrO₄ 0.1M</td><td><span class="td-flex"><span class="dot endapan-kuning"></span>Endapan PbCrO₄ kuning</span></td><td>+Pb²⁺ confirmed</td></tr>
          <tr><td><strong>Uji Ag⁺ vs Hg₂²⁺</strong></td><td>Ag⁺, Hg₂²⁺</td><td>Sisa endapan + NH₄OH berlebih</td><td>NH₄OH 6M</td><td>AgCl larut → larutan jernih; Hg₂Cl₂ → <span class="td-flex"><span class="dot endapan-hitam"></span>hitam</span></td><td>Hg₂²⁺ jika hitam</td></tr>
          <tr><td><strong>Uji Ag⁺ spesifik</strong></td><td>Ag⁺</td><td>Filtrat + HNO₃ encer → endapan kembali + K₂CrO₄</td><td>HNO₃ + K₂CrO₄</td><td><span class="td-flex"><span class="dot endapan-merah"></span>AgCrO₄ merah bata</span></td><td>+Ag⁺ confirmed</td></tr>
          <tr><td><strong>Uji Hg₂²⁺ spesifik</strong></td><td>Hg₂²⁺</td><td>Endapan hitam + HNO₃ panas</td><td>HNO₃ pekat</td><td>Endapan larut → merkuri(II) nitrat</td><td>+Hg₂²⁺ confirmed</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="test-t2" style="display:none">
    <div class="card highlight-box" style="padding:.8rem 1.2rem; margin-bottom:1rem;">
      <strong style="color:var(--accent2)">Golongan II</strong> — Reagen Pengendap: <span class="formula">H₂S dalam HCl 0.3M</span> → Endapan: Sulfida asam
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
        <tbody>
          <tr><td><strong>Uji Golongan</strong></td><td>Cu²⁺,Bi³⁺,Cd²⁺,Hg²⁺,Sn,As,Sb</td><td>Alirkan H₂S ke larutan dalam HCl 0.3M</td><td>H₂S gas</td><td>Endapan berwarna (hitam/kuning)</td><td>Ada kation Gol. II</td></tr>
          <tr><td><strong>Pemisahan Cu²⁺</strong></td><td>Cu²⁺</td><td>Endapan + NH₄OH berlebih</td><td>NH₄OH</td><td><span class="td-flex"><span class="dot endapan-biru"></span>Larutan biru tua [Cu(NH₃)₄]²⁺</span></td><td>+Cu²⁺</td></tr>
          <tr><td><strong>Uji Cu²⁺ spesifik</strong></td><td>Cu²⁺</td><td>Larutan biru + K₄[Fe(CN)₆]</td><td>K₄[Fe(CN)₆]</td><td><span class="td-flex"><span class="dot endapan-merah"></span>Cu₂[Fe(CN)₆] merah coklat</span></td><td>+Cu²⁺ confirmed</td></tr>
          <tr><td><strong>Uji Bi³⁺</strong></td><td>Bi³⁺</td><td>Endapan Bi₂S₃ + SnCl₂ basa</td><td>SnCl₂ alkali</td><td><span class="td-flex"><span class="dot endapan-hitam"></span>Bi hitam (reduksi)</span></td><td>+Bi³⁺</td></tr>
          <tr><td><strong>Uji Cd²⁺</strong></td><td>Cd²⁺</td><td>Larutan asam + H₂S</td><td>H₂S</td><td><span class="td-flex"><span class="dot endapan-kuning"></span>CdS kuning</span></td><td>+Cd²⁺</td></tr>
          <tr><td><strong>Uji Sn²⁺</strong></td><td>Sn²⁺</td><td>Larutan + HgCl₂</td><td>HgCl₂</td><td>Endapan putih → abu → hitam</td><td>+Sn²⁺</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="test-t3" style="display:none">
    <div class="card highlight-box" style="padding:.8rem 1.2rem; margin-bottom:1rem;">
      <strong style="color:var(--accent3)">Golongan III</strong> — Reagen Pengendap: <span class="formula">(NH₄)₂S dalam NH₄OH/NH₄Cl</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
        <tbody>
          <tr><td><strong>Uji Golongan</strong></td><td>Fe³⁺,Al³⁺,Cr³⁺,Mn²⁺,Ni²⁺,Co²⁺,Zn²⁺</td><td>Tambahkan (NH₄)₂S dalam buffer NH₄OH/NH₄Cl</td><td>(NH₄)₂S</td><td>Campuran endapan warna-warni</td><td>Ada kation Gol. III</td></tr>
          <tr><td><strong>Uji Fe³⁺</strong></td><td>Fe³⁺</td><td>Larutan + KSCN</td><td>KSCN 0.1M</td><td><span class="td-flex"><span class="dot endapan-merah"></span>Merah darah [Fe(SCN)]²⁺</span></td><td>+Fe³⁺</td></tr>
          <tr><td><strong>Uji Al³⁺</strong></td><td>Al³⁺</td><td>Endapan + NaOH berlebih → larut; + aluminon</td><td>NaOH + aluminon</td><td>Endapan merah (lake aluminon)</td><td>+Al³⁺</td></tr>
          <tr><td><strong>Uji Cr³⁺</strong></td><td>Cr³⁺</td><td>Larutan + NaOH + H₂O₂ → kuning; asamkan + BaCl₂</td><td>NaOH, H₂O₂, BaCl₂</td><td><span class="td-flex"><span class="dot endapan-kuning"></span>BaCrO₄ kuning</span></td><td>+Cr³⁺</td></tr>
          <tr><td><strong>Uji Mn²⁺</strong></td><td>Mn²⁺</td><td>+ NaBiO₃ dalam HNO₃</td><td>NaBiO₃/HNO₃</td><td>Larutan ungu (MnO₄⁻)</td><td>+Mn²⁺</td></tr>
          <tr><td><strong>Uji Ni²⁺</strong></td><td>Ni²⁺</td><td>+ Dimetilglioksim dalam NH₄OH</td><td>DMG</td><td><span class="td-flex"><span class="dot endapan-merah"></span>Endapan merah Ni-DMG</span></td><td>+Ni²⁺</td></tr>
          <tr><td><strong>Uji Co²⁺</strong></td><td>Co²⁺</td><td>+ KSCN + aseton</td><td>KSCN+aseton</td><td>Larutan biru [Co(SCN)₄]²⁻</td><td>+Co²⁺</td></tr>
          <tr><td><strong>Uji Zn²⁺</strong></td><td>Zn²⁺</td><td>+ K₄[Fe(CN)₆] asam</td><td>K₄[Fe(CN)₆]</td><td>Endapan putih Zn₂[Fe(CN)₆]</td><td>+Zn²⁺</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="test-t4" style="display:none">
    <div class="card highlight-box" style="padding:.8rem 1.2rem; margin-bottom:1rem;">
      <strong style="color:var(--accent4)">Golongan IV</strong> — Reagen Pengendap: <span class="formula">(NH₄)₂CO₃ dalam NH₄OH</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
        <tbody>
          <tr><td><strong>Uji Golongan</strong></td><td>Ca²⁺, Sr²⁺, Ba²⁺</td><td>Tambahkan (NH₄)₂CO₃ dalam NH₄OH</td><td>(NH₄)₂CO₃</td><td>Endapan karbonat putih</td><td>Ada kation Gol. IV</td></tr>
          <tr><td><strong>Uji Ba²⁺</strong></td><td>Ba²⁺</td><td>Larutan asam asetat + K₂CrO₄</td><td>K₂CrO₄</td><td><span class="td-flex"><span class="dot endapan-kuning"></span>BaCrO₄ kuning</span></td><td>+Ba²⁺</td></tr>
          <tr><td><strong>Uji Sr²⁺</strong></td><td>Sr²⁺</td><td>Larutan + (NH₄)₂SO₄</td><td>(NH₄)₂SO₄</td><td>SrSO₄ putih halus (sesudah Ba²⁺ diendapkan)</td><td>+Sr²⁺</td></tr>
          <tr><td><strong>Uji Ca²⁺</strong></td><td>Ca²⁺</td><td>Filtrat + (NH₄)₂C₂O₄</td><td>(NH₄)₂C₂O₄</td><td><span class="td-flex"><span class="dot endapan-putih"></span>CaC₂O₄ putih kristalin</span></td><td>+Ca²⁺</td></tr>
          <tr><td><strong>Uji nyala Ba²⁺</strong></td><td>Ba²⁺</td><td>Uji nyala kawat platinum</td><td>—</td><td>Nyala hijau kekuningan</td><td>+Ba²⁺ nyala</td></tr>
          <tr><td><strong>Uji nyala Ca²⁺</strong></td><td>Ca²⁺</td><td>Uji nyala kawat platinum</td><td>—</td><td>Nyala merah jingga (bata)</td><td>+Ca²⁺ nyala</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="test-t5" style="display:none">
    <div class="card highlight-box" style="padding:.8rem 1.2rem; margin-bottom:1rem;">
      <strong style="color:var(--accent5)">Golongan V</strong> — Tidak ada reagen golongan; identifikasi dengan uji spesifik
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Uji</th><th>Ion</th><th>Prosedur</th><th>Reagen</th><th>Pengamatan / Hasil</th><th>Kesimpulan</th></tr></thead>
        <tbody>
          <tr><td><strong>Uji NH₄⁺</strong></td><td>NH₄⁺</td><td>Sampel + NaOH → panaskan, kertas lakmus merah di atas</td><td>NaOH 6M</td><td>Gas NH₃ bau tajam; lakmus merah → biru</td><td>+NH₄⁺</td></tr>
          <tr><td><strong>Uji NH₄⁺ Nessler</strong></td><td>NH₄⁺</td><td>Larutan + reagen Nessler</td><td>K₂[HgI₄]/KOH</td><td><span class="td-flex"><span class="dot endapan-jingga"></span>Coklat jingga</span></td><td>+NH₄⁺ sensitif</td></tr>
          <tr><td><strong>Uji K⁺</strong></td><td>K⁺</td><td>Larutan netral + Na₃[Co(NO₂)₆]</td><td>Na₃[Co(NO₂)₆]</td><td><span class="td-flex"><span class="dot endapan-kuning"></span>Endapan K₂Na[Co(NO₂)₆] kuning</span></td><td>+K⁺</td></tr>
          <tr><td><strong>Uji nyala K⁺</strong></td><td>K⁺</td><td>Nyala melalui kaca kobalt biru</td><td>Kaca kobalt</td><td>Violet/ungu</td><td>+K⁺</td></tr>
          <tr><td><strong>Uji Na⁺</strong></td><td>Na⁺</td><td>Uji nyala langsung</td><td>—</td><td>Kuning intens (D-line 589nm)</td><td>+Na⁺</td></tr>
          <tr><td><strong>Uji Na⁺ spesifik</strong></td><td>Na⁺</td><td>+ Zink uranil asetat</td><td>Zn(UO₂)₃(OAc)₈</td><td>Endapan kristal kuning</td><td>+Na⁺</td></tr>
          <tr><td><strong>Uji Mg²⁺</strong></td><td>Mg²⁺</td><td>+ Na₂HPO₄ dalam NH₄OH/NH₄Cl</td><td>Na₂HPO₄</td><td>MgNH₄PO₄ putih kristalin (microscopically cross)</td><td>+Mg²⁺</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ═══════════ TAB 4: REAKSI KATION ═══════════ -->
<div class="tab-content" id="tab3">
  <h2>Animasi Reaksi Kation</h2>
  <p style="margin-bottom:1.5rem;">Klik kartu untuk melihat animasi tabung reaksi. Perhatikan perubahan warna larutan dan pembentukan endapan.</p>

  <div class="subtab-nav">
    <button class="subtab-btn active" onclick="showSubtab('rxk','rxk1')">Gol. I</button>
    <button class="subtab-btn" onclick="showSubtab('rxk','rxk2')">Gol. II</button>
    <button class="subtab-btn" onclick="showSubtab('rxk','rxk3')">Gol. III</button>
    <button class="subtab-btn" onclick="showSubtab('rxk','rxk4')">Gol. IV</button>
    <button class="subtab-btn" onclick="showSubtab('rxk','rxk5')">Gol. V</button>
  </div>

  <div class="subtab-panel active" id="rxk-rxk1">
    <div class="reaction-grid" id="rxk1-grid"></div>
  </div>
  <div class="subtab-panel" id="rxk-rxk2">
    <div class="reaction-grid" id="rxk2-grid"></div>
  </div>
  <div class="subtab-panel" id="rxk-rxk3">
    <div class="reaction-grid" id="rxk3-grid"></div>
  </div>
  <div class="subtab-panel" id="rxk-rxk4">
    <div class="reaction-grid" id="rxk4-grid"></div>
  </div>
  <div class="subtab-panel" id="rxk-rxk5">
    <div class="reaction-grid" id="rxk5-grid"></div>
  </div>
</div>

<!-- ═══════════ TAB 5: REAKSI ANION ═══════════ -->
<div class="tab-content" id="tab4">
  <h2>Animasi Reaksi Anion</h2>
  <p style="margin-bottom:1.5rem;">Klik kartu untuk melihat animasi tabung reaksi identifikasi anion.</p>
  <div class="reaction-grid" id="anion-grid"></div>
</div>

<!-- ═══════════ TAB 6: KUIS ═══════════ -->
<div class="tab-content" id="tab5">
  <div class="quiz-box">
    <div class="quiz-header">
      <h2>Kuis Kation &amp; Anion</h2>
      <p>Uji pemahamanmu tentang analisis kualitatif ion!</p>
    </div>
    <div id="quiz-main"></div>
  </div>
</div>

<script>
// ═══════════════════════════════════════
//  TAB NAVIGATION
// ═══════════════════════════════════════
function showTab(i) {
  document.querySelectorAll('.tab-content').forEach((t,idx)=>t.classList.toggle('active',idx===i));
  document.querySelectorAll('.tab-btn').forEach((b,idx)=>b.classList.toggle('active',idx===i));
  if(i===3 && !window.rxkBuilt){ buildRxKation(); window.rxkBuilt=true; }
  if(i===4 && !window.rxaBuilt){ buildRxAnion(); window.rxaBuilt=true; }
  if(i===5 && !window.quizBuilt){ buildQuiz(); window.quizBuilt=true; }
}

function showSubtab(ns,id) {
  const panels=document.querySelectorAll(`[id^="${ns}-"]`);
  panels.forEach(p=>p.classList.toggle('active',p.id===`${ns}-${id}`));
  // buttons
  const btns = [...document.querySelectorAll('.subtab-btn')].filter(b=> {
    const fn = b.getAttribute('onclick')||'';
    return fn.includes(`'${ns}'`);
  });
  btns.forEach(b=>b.classList.toggle('active', (b.getAttribute('onclick')||'').includes(`'${id}'`)));
}

function showTest(id) {
  ['t1','t2','t3','t4','t5'].forEach(t=>{
    const el=document.getElementById('test-'+t);
    if(el) el.style.display=(t===id)?'block':'none';
  });
  document.querySelectorAll('.test-btn').forEach(b=>{
    b.classList.toggle('active',(b.getAttribute('onclick')||'').includes(`'${id}'`));
  });
}

// ═══════════════════════════════════════
//  REACTION DATA
// ═══════════════════════════════════════
const rxKationData = {
  rxk1: [
    { ion:'Ag⁺', reagent:'HCl 2M', equation:'Ag⁺ + Cl⁻ → AgCl↓', obs:'Endapan putih', header:'#7c3aed',
      before:{liquid:'#e8f4fd', sediment:null}, after:{liquid:'#c8dff0', sediment:'#e2e8f0'} },
    { ion:'Ag⁺', reagent:'NH₄OH berlebih', equation:'AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻', obs:'AgCl larut',header:'#7c3aed',
      before:{liquid:'#c8dff0', sediment:'#e2e8f0'}, after:{liquid:'#d4f1d4', sediment:null} },
    { ion:'Ag⁺', reagent:'K₂CrO₄', equation:'2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄↓', obs:'Endapan merah bata', header:'#7c3aed',
      before:{liquid:'#e8f4fd', sediment:null}, after:{liquid:'#fde8d8', sediment:'#c2410c'} },
    { ion:'Hg₂²⁺', reagent:'HCl 2M', equation:'Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓', obs:'Endapan putih', header:'#06b6d4',
      before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#e0f2fe', sediment:'#f1f5f9'} },
    { ion:'Hg₂²⁺', reagent:'NH₄OH', equation:'Hg₂Cl₂ + 2NH₃ → Hg↓ + HgNH₂Cl↓ + NH₄⁺ + Cl⁻', obs:'Endapan hitam', header:'#06b6d4',
      before:{liquid:'#e0f2fe', sediment:'#f1f5f9'}, after:{liquid:'#94a3b8', sediment:'#1e293b'} },
    { ion:'Pb²⁺', reagent:'HCl 2M', equation:'Pb²⁺ + 2Cl⁻ → PbCl₂↓', obs:'Endapan putih', header:'#f59e0b',
      before:{liquid:'#fffbeb', sediment:null}, after:{liquid:'#fef3c7', sediment:'#e2e8f0'} },
    { ion:'Pb²⁺', reagent:'Air panas', equation:'PbCl₂(s) → Pb²⁺(aq) + 2Cl⁻(aq)', obs:'Endapan larut', header:'#f59e0b',
      before:{liquid:'#fef3c7', sediment:'#e2e8f0'}, after:{liquid:'#fef3c7', sediment:null} },
    { ion:'Pb²⁺', reagent:'K₂CrO₄', equation:'Pb²⁺ + CrO₄²⁻ → PbCrO₄↓', obs:'Endapan kuning', header:'#f59e0b',
      before:{liquid:'#fef3c7', sediment:null}, after:{liquid:'#fef08a', sediment:'#ca8a04'} },
  ],
  rxk2: [
    { ion:'Cu²⁺', reagent:'H₂S/HCl', equation:'Cu²⁺ + S²⁻ → CuS↓', obs:'Endapan hitam', header:'#0891b2',
      before:{liquid:'#bfdbfe', sediment:null}, after:{liquid:'#7dd3fc', sediment:'#1e293b'} },
    { ion:'Cu²⁺', reagent:'NH₄OH berlebih', equation:'Cu²⁺ + 4NH₃ → [Cu(NH₃)₄]²⁺', obs:'Larutan biru tua', header:'#0891b2',
      before:{liquid:'#bae6fd', sediment:null}, after:{liquid:'#1d4ed8', sediment:null} },
    { ion:'Bi³⁺', reagent:'H₂S/HCl', equation:'2Bi³⁺ + 3S²⁻ → Bi₂S₃↓', obs:'Endapan hitam', header:'#7c3aed',
      before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#d1fae5', sediment:'#1e293b'} },
    { ion:'Bi³⁺', reagent:'SnCl₂ basa', equation:'2Bi³⁺ + 3Sn²⁺ → 2Bi↓ + 3Sn⁴⁺', obs:'Endapan hitam (Bi)', header:'#7c3aed',
      before:{liquid:'#e0f2fe', sediment:null}, after:{liquid:'#94a3b8', sediment:'#0f172a'} },
    { ion:'Cd²⁺', reagent:'H₂S', equation:'Cd²⁺ + S²⁻ → CdS↓', obs:'Endapan kuning', header:'#ca8a04',
      before:{liquid:'#fffbeb', sediment:null}, after:{liquid:'#fef3c7', sediment:'#eab308'} },
    { ion:'Sn²⁺', reagent:'HgCl₂', equation:'Sn²⁺ + 2HgCl₂ → SnCl₄ + Hg₂Cl₂↓', obs:'Putih → abu → hitam', header:'#4b5563',
      before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#94a3b8', sediment:'#475569'} },
  ],
  rxk3: [
    { ion:'Fe³⁺', reagent:'KSCN', equation:'Fe³⁺ + 3SCN⁻ → [Fe(SCN)₃]', obs:'Larutan merah darah', header:'#dc2626',
      before:{liquid:'#fde68a', sediment:null}, after:{liquid:'#b91c1c', sediment:null} },
    { ion:'Fe³⁺', reagent:'NaOH', equation:'Fe³⁺ + 3OH⁻ → Fe(OH)₃↓', obs:'Endapan coklat merah', header:'#dc2626',
      before:{liquid:'#fde68a', sediment:null}, after:{liquid:'#fed7aa', sediment:'#b45309'} },
    { ion:'Al³⁺', reagent:'NaOH', equation:'Al³⁺ + 3OH⁻ → Al(OH)₃↓', obs:'Endapan putih gelatin', header:'#9ca3af',
      before:{liquid:'#f8fafc', sediment:null}, after:{liquid:'#e2e8f0', sediment:'#f1f5f9'} },
    { ion:'Cr³⁺', reagent:'NaOH+H₂O₂', equation:'2Cr³⁺ + 3H₂O₂ + 10OH⁻ → 2CrO₄²⁻ + 8H₂O', obs:'Larutan kuning', header:'#065f46',
      before:{liquid:'#6ee7b7', sediment:null}, after:{liquid:'#ca8a04', sediment:null} },
    { ion:'Mn²⁺', reagent:'NaBiO₃/HNO₃', equation:'2Mn²⁺ + 5BiO₃⁻ + 14H⁺ → 2MnO₄⁻ + 5Bi³⁺ + 7H₂O', obs:'Larutan ungu (MnO₄⁻)', header:'#7e22ce',
      before:{liquid:'#fce7f3', sediment:null}, after:{liquid:'#7c3aed', sediment:null} },
    { ion:'Ni²⁺', reagent:'Dimetilglioksim', equation:'Ni²⁺ + 2HDMG → Ni(HDMG)₂↓ + 2H⁺', obs:'Endapan merah', header:'#be185d',
      before:{liquid:'#d1fae5', sediment:null}, after:{liquid:'#fce7f3', sediment:'#e11d48'} },
    { ion:'Co²⁺', reagent:'KSCN + aseton', equation:'Co²⁺ + 4SCN⁻ → [Co(SCN)₄]²⁻', obs:'Larutan biru', header:'#1d4ed8',
      before:{liquid:'#fce7f3', sediment:null}, after:{liquid:'#3b82f6', sediment:null} },
    { ion:'Zn²⁺', reagent:'K₄[Fe(CN)₆]', equation:'2Zn²⁺ + [Fe(CN)₆]⁴⁻ → Zn₂[Fe(CN)₆]↓', obs:'Endapan putih', header:'#475569',
      before:{liquid:'#f0fdf4', sediment:null}, after:{liquid:'#dcfce7', sediment:'#f1f5f9'} },
  ],
  rxk4: [
    { ion:'Ba²⁺', reagent:'K₂CrO₄', equation:'Ba²⁺ + CrO₄²⁻ → BaCrO₄↓', obs:'Endapan kuning', header:'#d97706',
      before:{liquid:'#fffbeb', sediment:null}, after:{liquid:'#fef9c3', sediment:'#ca8a04'} },
    { ion:'Sr²⁺', reagent:'H₂SO₄', equation:'Sr²⁺ + SO₄²⁻ → SrSO₄↓', obs:'Endapan putih halus', header:'#059669',
      before:{liquid:'#ecfdf5', sediment:null}, after:{liquid:'#d1fae5', sediment:'#f1f5f9'} },
    { ion:'Ca²⁺', reagent:'(NH₄)₂C₂O₄', equation:'Ca²⁺ + C₂O₄²⁻ → CaC₂O₄↓', obs:'Endapan putih', header:'#dc2626',
      before:{liquid:'#fef2f2', sediment:null}, after:{liquid:'#fee2e2', sediment:'#e2e8f0'} },
    { ion:'Ba²⁺', reagent:'(NH₄)₂CO₃', equation:'Ba²⁺ + CO₃²⁻ → BaCO₃↓', obs:'Endapan putih', header:'#d97706',
      before:{liquid:'#fffbeb', sediment:null}, after:{liquid:'#fef3c7', sediment:'#e2e8f0'} },
  ],
  rxk5: [
    { ion:'NH₄⁺', reagent:'NaOH panas', equation:'NH₄⁺ + OH⁻ → NH₃↑ + H₂O', obs:'Gas NH₃ (bau tajam)', header:'#7c3aed',
      before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#ddd6fe', sediment:null} },
    { ion:'K⁺', reagent:'Na₃[Co(NO₂)₆]', equation:'2K⁺ + Na⁺ + [Co(NO₂)₆]³⁻ → K₂Na[Co(NO₂)₆]↓', obs:'Endapan kuning', header:'#ca8a04',
      before:{liquid:'#fffbeb', sediment:null}, after:{liquid:'#fef3c7', sediment:'#eab308'} },
    { ion:'Na⁺', reagent:'Uji nyala', equation:'Na → D-line 589 nm', obs:'Nyala kuning intens', header:'#f59e0b',
      before:{liquid:'#fffbeb', sediment:null}, after:{liquid:'#fde047', sediment:null} },
    { ion:'Mg²⁺', reagent:'Na₂HPO₄+NH₃', equation:'Mg²⁺ + NH₄⁺ + PO₄³⁻ → MgNH₄PO₄↓', obs:'Endapan putih kristalin', header:'#0891b2',
      before:{liquid:'#f0fdf4', sediment:null}, after:{liquid:'#d1fae5', sediment:'#f1f5f9'} },
  ]
};

const rxAnionData = [
  { ion:'Cl⁻', reagent:'AgNO₃', equation:'Ag⁺ + Cl⁻ → AgCl↓', obs:'Endapan putih, larut NH₄OH',
    before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#e0f2fe', sediment:'#f1f5f9'} },
  { ion:'SO₄²⁻', reagent:'BaCl₂/HCl', equation:'Ba²⁺ + SO₄²⁻ → BaSO₄↓', obs:'Endapan putih, tidak larut HCl',
    before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#e0f2fe', sediment:'#f8fafc'} },
  { ion:'CO₃²⁻', reagent:'HCl encer', equation:'CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O', obs:'Gelembung gas CO₂',
    before:{liquid:'#ecfdf5', sediment:null}, after:{liquid:'#bbf7d0', sediment:null} },
  { ion:'NO₃⁻', reagent:'FeSO₄+H₂SO₄ pekat', equation:'Fe²⁺ + NO → [Fe(NO)]²⁺', obs:'Cincin coklat di antarmuka',
    before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#92400e', sediment:null} },
  { ion:'PO₄³⁻', reagent:'AgNO₃', equation:'3Ag⁺ + PO₄³⁻ → Ag₃PO₄↓', obs:'Endapan kuning',
    before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#fef9c3', sediment:'#ca8a04'} },
  { ion:'I⁻', reagent:'AgNO₃', equation:'Ag⁺ + I⁻ → AgI↓', obs:'Endapan kuning muda',
    before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#fefce8', sediment:'#eab308'} },
  { ion:'I⁻', reagent:'Cl₂ + kanji', equation:'Cl₂ + 2I⁻ → 2Cl⁻ + I₂; I₂+kanji→biru', obs:'Larutan biru tua',
    before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#1e3a8a', sediment:null} },
  { ion:'S²⁻', reagent:'Pb(CH₃COO)₂', equation:'Pb²⁺ + S²⁻ → PbS↓', obs:'Endapan hitam',
    before:{liquid:'#f0f9ff', sediment:null}, after:{liquid:'#94a3b8', sediment:'#0f172a'} },
  { ion:'CH₃COO⁻', reagent:'FeCl₃', equation:'3CH₃COO⁻ + Fe³⁺ → Fe(CH₃COO)₃', obs:'Larutan merah coklat',
    before:{liquid:'#fffbeb', sediment:null}, after:{liquid:'#92400e', sediment:null} },
];

// ═══════════════════════════════════════
//  TUBE ANIMATION ENGINE
// ═══════════════════════════════════════
function makeTube(id, label, liquidColor, sedColor, sedPct=30, liqPct=55) {
  return `
  <div class="tube-unit">
    <div class="tube-cap"></div>
    <div class="tube-body" id="${id}">
      <div class="tube-liquid" id="${id}-liq" style="height:0; background:${liquidColor};"></div>
      <div class="tube-sediment" id="${id}-sed" style="height:0; background:${sedColor||'transparent'};"></div>
    </div>
    <div class="tube-name">${label}</div>
  </div>`;
}

function animateTube(id, liqH, sedH, liqColor, sedColor) {
  setTimeout(()=>{
    const liq=document.getElementById(id+'-liq');
    const sed=document.getElementById(id+'-sed');
    if(liq){ liq.style.height=liqH+'px'; liq.style.background=liqColor; }
    if(sed && sedColor){ sed.style.height=sedH+'px'; sed.style.background=sedColor; }
  }, 100);
}

let activeCard = null;

function buildReactionCard(data, containerId, gClass='') {
  const container = document.getElementById(containerId);
  if(!container) return;

  data.forEach((d,i)=>{
    const cid = containerId + '-' + i;
    const card = document.createElement('div');
    card.className = 'reaction-card';
    card.innerHTML = `
      <div class="reaction-header" style="background:linear-gradient(135deg,${d.header}22,${d.header}11); border-bottom:1px solid ${d.header}33;">
        <div>
          <div class="reaction-title">${d.ion}</div>
          <div class="reaction-reagent">+ ${d.reagent}</div>
        </div>
        <div style="font-size:1.5rem;">⚗️</div>
      </div>
      <div class="tube-rack">
        ${makeTube(cid+'-a','Sebelum',d.before.liquid,d.before.sediment)}
        <div style="color:#94a3b8;font-size:1.4rem;align-self:center;">→</div>
        ${makeTube(cid+'-b','Sesudah',d.before.liquid,null)}
      </div>
      <div class="reaction-info">
        <div style="font-size:.78rem;color:var(--muted);">Klik untuk animasi</div>
        <div class="rxn-eq" style="display:none;" id="${cid}-eq">${d.equation}</div>
        <div id="${cid}-obs" style="display:none;">
          <span class="obs-badge" style="background:${d.header}22;border-color:${d.header}44;color:${d.header};">
            👁 ${d.obs}
          </span>
        </div>
      </div>`;
    card.onclick = () => runAnimation(cid, d);
    container.appendChild(card);
    // init before tube
    setTimeout(()=>animateTube(cid+'-a', 55, d.before.sediment?18:0, d.before.liquid, d.before.sediment), 200+i*50);
  });
}

function runAnimation(cid, d) {
  const eq=document.getElementById(cid+'-eq');
  const obs=document.getElementById(cid+'-obs');
  if(eq) { eq.style.display='block'; eq.classList.add('pop'); }
  if(obs) { obs.style.display='block'; }
  // animate after tube
  const liqH=55, sedH=d.after.sediment?18:0;
  animateTube(cid+'-b', liqH, sedH, d.after.liquid, d.after.sediment);
}

function buildRxKation() {
  buildReactionCard(rxKationData.rxk1, 'rxk1-grid');
  buildReactionCard(rxKationData.rxk2, 'rxk2-grid');
  buildReactionCard(rxKationData.rxk3, 'rxk3-grid');
  buildReactionCard(rxKationData.rxk4, 'rxk4-grid');
  buildReactionCard(rxKationData.rxk5, 'rxk5-grid');
}

function buildRxAnion() {
  buildReactionCard(rxAnionData, 'anion-grid');
}

// ═══════════════════════════════════════
//  QUIZ ENGINE
// ═══════════════════════════════════════
const quizData = [
  { q:'Reagen apa yang digunakan untuk mengendapkan kation Golongan I?', opts:['H₂SO₄ encer','HCl encer','NaOH','(NH₄)₂S'], ans:1, exp:'Kation Golongan I (Ag⁺, Hg₂²⁺, Pb²⁺) diendapkan sebagai klorida tidak larut menggunakan HCl encer (2M).' },
  { q:'Pengendap apa yang terbentuk saat Ag⁺ bereaksi dengan HCl?', opts:['AgNO₃','Ag₂SO₄','AgCl','Ag₂O'], ans:2, exp:'AgCl (perak klorida) terbentuk sebagai endapan putih yang tidak larut dalam air.' },
  { q:'Apa yang terjadi ketika Hg₂Cl₂ ditambah NH₄OH?', opts:['Larut membentuk larutan bening','Terbentuk endapan putih larut','Terbentuk endapan hitam (Hg)','Tidak terjadi reaksi'], ans:2, exp:'Hg₂Cl₂ + 2NH₃ → Hg↓ (hitam) + HgNH₂Cl (putih). Campuran ini tampak hitam karena Hg logam.' },
  { q:'Kation Golongan II diendapkan menggunakan?', opts:['HCl dalam suasana asam','H₂S dalam suasana asam','(NH₄)₂CO₃ basa','NaOH berlebih'], ans:1, exp:'H₂S dialirkan ke dalam larutan yang mengandung HCl 0.3M (asam) untuk mengendapkan kation Golongan II sebagai sulfida.' },
  { q:'Warna larutan Cu²⁺ dalam NH₄OH berlebih adalah?', opts:['Merah','Hijau','Kuning','Biru tua'], ans:3, exp:'Cu²⁺ + 4NH₃ → [Cu(NH₃)₄]²⁺, kompleks tetraaminatembaga(II) berwarna biru tua (biru intensif).' },
  { q:'Uji spesifik untuk Fe³⁺ menggunakan?', opts:['KSCN','K₂CrO₄','DMG','Na₂HPO₄'], ans:0, exp:'KSCN (kalium tiosianat) menghasilkan warna merah darah [Fe(SCN)]²⁺ yang sangat sensitif untuk deteksi Fe³⁺.' },
  { q:'Endapan apa yang terbentuk dari reaksi Pb²⁺ + K₂CrO₄?', opts:['PbSO₄ putih','PbCrO₄ kuning','PbCO₃ putih','PbCl₂ putih'], ans:1, exp:'Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ berwarna kuning, digunakan sebagai uji konfirmasi Pb²⁺.' },
  { q:'Kation golongan III mana yang bereaksi dengan dimetilglioksim menghasilkan endapan merah?', opts:['Co²⁺','Fe³⁺','Ni²⁺','Zn²⁺'], ans:2, exp:'Ni²⁺ + 2HDMG → Ni(HDMG)₂↓ merah. Reaksi dengan dimetilglioksim sangat spesifik untuk Ni²⁺.' },
  { q:'Reagen golongan IV untuk mengendapkan Ca²⁺, Sr²⁺, dan Ba²⁺ adalah?', opts:['(NH₄)₂S','HCl','(NH₄)₂CO₃','H₂SO₄'], ans:2, exp:'(NH₄)₂CO₃ dalam NH₄OH mengendapkan kation Golongan IV sebagai karbonat.' },
  { q:'Uji apa yang digunakan untuk identifikasi NH₄⁺?', opts:['Uji nyala ungu','NaOH panas → bau NH₃','K₂CrO₄','Reagen Mayer'], ans:1, exp:'NH₄⁺ + OH⁻ → NH₃↑ + H₂O. Gas NH₃ berbau tajam dan membirukan kertas lakmus merah.' },
  { q:'Warna nyala Na⁺ pada uji nyala adalah?', opts:['Violet','Merah','Kuning','Hijau'], ans:2, exp:'Na⁺ menghasilkan nyala kuning intens pada panjang gelombang 589 nm (garis D natrium).' },
  { q:'Warna endapan CdS adalah?', opts:['Putih','Hitam','Kuning','Merah'], ans:2, exp:'CdS (kadmium sulfida) berwarna kuning dan terbentuk saat Cd²⁺ direaksikan dengan H₂S dalam suasana asam.' },
  { q:'Anion apa yang menghasilkan endapan putih dengan AgNO₃ yang larut dalam NH₄OH?', opts:['I⁻','SO₄²⁻','Cl⁻','PO₄³⁻'], ans:2, exp:'AgCl (putih) larut dalam NH₄OH membentuk [Ag(NH₃)₂]⁺. AgI dan Ag₃PO₄ tidak larut dalam NH₄OH.' },
  { q:'Uji cincin coklat digunakan untuk mengidentifikasi anion?', opts:['SO₄²⁻','Cl⁻','NO₃⁻','CO₃²⁻'], ans:2, exp:'NO₃⁻ diidentifikasi dengan uji cincin coklat: Fe²⁺ + NO → [Fe(NO)]²⁺ coklat di antarmuka H₂SO₄ pekat.' },
  { q:'Endapan BaSO₄ memiliki sifat?', opts:['Larut dalam HCl encer','Larut dalam HNO₃ encer','Tidak larut dalam asam apapun','Larut dalam air panas'], ans:2, exp:'BaSO₄ sangat sukar larut dan tidak larut dalam HCl, HNO₃, atau air. Ini yang membedakannya dari BaCO₃.' },
  { q:'Warna larutan yang terbentuk saat Mn²⁺ dioksidasi dengan NaBiO₃/HNO₃?', opts:['Kuning','Ungu','Biru','Merah'], ans:1, exp:'Mn²⁺ teroksidasi menjadi MnO₄⁻ (permanganat) yang berwarna ungu/violet. Reaksi ini sensitif untuk Mn²⁺.' },
  { q:'Ion apa yang menghasilkan nyala merah karmin pada uji nyala?', opts:['K⁺','Na⁺','Ba²⁺','Sr²⁺'], ans:3, exp:'Sr²⁺ menghasilkan nyala merah karmin (merah terang). Ba²⁺ hijau, K⁺ violet, Na⁺ kuning.' },
  { q:'Reagen Nessler digunakan untuk mendeteksi?', opts:['K⁺','Na⁺','NH₄⁺','Mg²⁺'], ans:2, exp:'Reagen Nessler (K₂[HgI₄] dalam KOH) bereaksi dengan NH₄⁺ menghasilkan warna coklat jingga.' },
  { q:'Bagaimana cara membedakan Ag⁺ dan Pb²⁺ dalam endapan klorida?', opts:['Tambah HNO₃','Panaskan dengan air → Pb²⁺ larut','Tambah NaOH','Uji nyala'], ans:1, exp:'PbCl₂ larut dalam air panas sedangkan AgCl tidak. Filtrat panas + K₂CrO₄ → PbCrO₄ kuning untuk konfirmasi Pb²⁺.' },
  { q:'Apa warna endapan Bi₂S₃?', opts:['Kuning','Putih','Merah','Hitam'], ans:3, exp:'Bi₂S₃ (bismut(III) sulfida) berwarna hitam, terbentuk dalam suasana asam dengan H₂S.' },
];

let qIdx=0, score=0, answered=false, userAnswers=[];

function buildQuiz() {
  qIdx=0; score=0; answered=false; userAnswers=[];
  renderQuestion();
}

function renderQuestion() {
  const box=document.getElementById('quiz-main');
  if(qIdx>=quizData.length){ renderScore(); return; }
  const q=quizData[qIdx];
  const pct=Math.round((qIdx/quizData.length)*100);
  box.innerHTML=`
    <div class="progress-bar-wrap"><div class="progress-bar" style="width:${pct}%"></div></div>
    <div class="question-num">Soal ${qIdx+1} dari ${quizData.length}</div>
    <div class="question-text">${q.q}</div>
    <ul class="option-list">
      ${q.opts.map((o,i)=>`<li><button class="option-btn" onclick="selectOption(${i})">${String.fromCharCode(65+i)}. ${o}</button></li>`).join('')}
    </ul>
    <div id="quiz-feedback"></div>
    <div class="quiz-controls">
      <div style="color:var(--accent3);font-size:.85rem;">⭐ Skor: ${score}/${qIdx}</div>
      <button class="btn btn-primary" id="next-btn" onclick="nextQ()" style="display:none">Lanjut →</button>
    </div>`;
  answered=false;
}

function selectOption(i) {
  if(answered) return;
  answered=true;
  const q=quizData[qIdx];
  const btns=document.querySelectorAll('.option-btn');
  btns.forEach(b=>b.disabled=true);
  btns[i].classList.add(i===q.ans?'correct':'wrong');
  if(i!==q.ans) btns[q.ans].classList.add('correct');
  if(i===q.ans) score++;
  document.getElementById('quiz-feedback').innerHTML=`<div class="explanation">💡 ${q.exp}</div>`;
  document.getElementById('next-btn').style.display='inline-block';
}

function nextQ() {
  qIdx++;
  renderQuestion();
}

function renderScore() {
  const pct=Math.round((score/quizData.length)*100);
  let msg='', emoji='';
  if(pct>=90){ msg='Luar biasa! Kamu menguasai materi dengan sangat baik!'; emoji='🏆'; }
  else if(pct>=70){ msg='Bagus! Pelajari kembali bagian yang masih kurang.'; emoji='🎉'; }
  else if(pct>=50){ msg='Lumayan! Masih ada yang perlu diperbaiki.'; emoji='📚'; }
  else { msg='Jangan menyerah! Ulangi materi dan coba lagi.'; emoji='💪'; }

  const conic=`conic-gradient(var(--accent1) 0% ${pct}%, var(--border) ${pct}% 100%)`;
  document.getElementById('quiz-main').innerHTML=`
    <div class="score-screen">
      <div style="font-size:3rem;">${emoji}</div>
      <div class="score-ring" style="background:${conic};">
        <span class="score-num">${score}</span>
      </div>
      <div class="score-label">dari ${quizData.length} soal</div>
      <h3 style="margin:1rem 0 .5rem;font-size:1.4rem;">${pct}%</h3>
      <p>${msg}</p>
      <div style="display:flex;gap:1rem;justify-content:center;margin-top:1.5rem;">
        <button class="btn btn-primary" onclick="buildQuiz()">🔄 Ulangi Kuis</button>
        <button class="btn btn-secondary" onclick="showTab(0)">🏠 Kembali ke Panduan</button>
      </div>
    </div>`;
}

// Init on load
window.rxkBuilt=false; window.rxaBuilt=false; window.quizBuilt=false;
</script>
</body>
</html>
