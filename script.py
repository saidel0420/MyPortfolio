import streamlit as st

# HTML + CSS كامل مدموج
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portfolio | Said El Alaoui</title>

  <!-- Google Font -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

  <style>
    /* ================== CSS كامل ================== */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }

    body {
      background: #0f172a;
      color: #e5e7eb;
    }

    /* NAVBAR */
    .header {
      position: fixed;
      width: 100%;
      top: 0;
      background: rgba(15,23,42,0.95);
      z-index: 1000;
    }

    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 60px;
      background: rgba(15,23,42,0.95);
      box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }

    .logo {
      font-size: 24px;
      font-weight: 700;
    }

    .logo span {
      color: #38bdf8;
    }

    .nav-links {
      list-style: none;
      display: flex;
      gap: 30px;
    }

    .nav-links li a {
      color: #e5e7eb;
      text-decoration: none;
      font-weight: 500;
      position: relative;
      padding: 5px 0;
      transition: 0.3s ease;
    }

    .nav-links li a::after {
      content: '';
      position: absolute;
      width: 0%;
      height: 2px;
      bottom: 0;
      left: 0;
      background-color: #38bdf8;
      transition: width 0.3s ease;
    }

    .nav-links li a:hover::after {
      width: 100%;
    }

    .nav-links li a:hover {
      color: #38bdf8;
    }

    .nav-links li a.active {
      color: #38bdf8;
    }

    .nav-links li a.active::after {
      width: 100%;
    }

    @media screen and (max-width: 768px) {
      .nav-links {
        flex-direction: column;
        background: rgba(15,23,42,0.95);
        position: fixed;
        top: 70px;
        right: -100%;
        width: 200px;
        padding: 20px;
        gap: 20px;
        transition: right 0.3s ease;
        border-radius: 10px 0 0 10px;
      }

      .nav-links.show {
        right: 0;
      }
    }

    /* HERO */
    .hero {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #0f172a, #1e293b);
      color: #e5e7eb;
      text-align: center;
      padding: 0 20px;
      position: relative;
    }

    .hero-title {
      font-size: 2.5rem;
      margin-bottom: 20px;
      opacity: 0;
      transform: translateY(-20px);
      animation: fadeSlideIn 1s forwards;
    }

    .hero-title .highlight {
      color: #38bdf8;
      animation: highlightPulse 2s infinite;
    }

    .hero-subtitle {
      font-size: 1.1rem;
      color: #94a3b8;
      margin-bottom: 30px;
      opacity: 0;
      transform: translateY(20px);
      animation: fadeSlideIn 1s forwards 0.5s;
    }

    .hero-buttons {
      display: flex;
      gap: 20px;
      justify-content: center;
      opacity: 0;
      animation: fadeSlideIn 1s forwards 1s;
    }

    .hero-btn {
      background: #38bdf8;
      color: #0f172a;
      padding: 12px 28px;
      border-radius: 30px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s ease;
    }

    .hero-btn:hover { background: #2563eb; transform: scale(1.05); }

    .hero-btn-outline {
      border: 2px solid #38bdf8;
      color: #38bdf8;
      padding: 10px 26px;
      border-radius: 30px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s ease;
    }

    .hero-btn-outline:hover { background: #38bdf8; color: #0f172a; transform: scale(1.05); }

    .hero-icons {
      margin-top: 40px;
      display: flex;
      gap: 25px;
      justify-content: center;
      font-size: 1.5rem;
      opacity: 0;
      animation: fadeSlideIn 1s forwards 1.5s;
    }

    .hero-icons a {
      color: #e5e7eb;
      transition: transform 0.3s, color 0.3s;
    }

    .hero-icons a:hover { color: #38bdf8; transform: translateY(-5px) scale(1.2); }

    @keyframes fadeSlideIn { to { opacity: 1; transform: translateY(0); } }
    @keyframes highlightPulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }

    @media screen and (max-width: 768px) {
      .hero-title { font-size: 2rem; }
      .hero-subtitle { font-size: 1rem; }
    }

    /* EDUCATION */
    #education {
      padding: 50px 20px;
      text-align: center;
    }

    #education h2 { font-size: 2em; margin-bottom: 30px; }
    .education-container {
      display: flex;
      flex-direction: column;
      gap: 20px;
      align-items: center;
    }
    .education-item {
      background-color: #fff;
      padding: 20px;
      width: 80%;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: transform 0.3s;
    }
    .education-item:hover { transform: translateY(-5px); }
    .education-item h3 { color: #0077cc; margin-bottom: 5px; }
    .education-item p { margin: 5px 0; color: #555; }
  </style>
</head>

<body>

<header class="header">
  <nav class="navbar">
    <div class="logo">SAID<span>EL ALAOUI</span></div>
    <ul class="nav-links">
       <li><a href="#home" >Home</a></li>
       <li><a href="#education" >Education</a></li>
       <li><a href="#skills">Skills</a></li>
       <li><a href="#projects">Projets</a></li>
       <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>
</header>

<section class="hero" id="home">
  <div class="hero-content">
    <h1 class="hero-title">
      Bonjour, je suis <span class="highlight">Said El Alaoui</span>
    </h1>
    <p class="hero-subtitle">
      Diplômé en Informatique Décisionnelle et Statistiques, passionné par l’analyse de données, le développement et les solutions intelligentes.
    </p>
    <div class="hero-buttons">
      <a href="#contact" class="btn hero-btn">Me contacter</a>
      <a href="#projects" class="btn hero-btn">Voir mes projets</a>
    </div>
    <div class="hero-icons">
      <a href="https://github.com/saidel0420" target="_blank"><i class="fab fa-github"></i></a>
      <a href="https://www.linkedin.com/in/said-el-alaoui-11a1a535b" target="_blank"><i class="fab fa-linkedin"></i></a>
      <a href="mailto:saidelalaoui0420@gmail.com"><i class="fas fa-envelope"></i></a>
    </div>
  </div>
</section>

<section id="education">
  <h2>Éducation</h2>
  <div class="education-container">
    <div class="education-item">
      <h3>DUT Informatique Décisionnelle et Statistiques</h3>
      <p>École supérieure de technologie, Fquih Ben Salah</p>
      <p>2024 - 2025</p>
    </div>
    <div class="education-item">
      <h3>Baccalauréat scientifique (Science Physique)</h3>
      <p>Lycée El Khawarizmi</p>
      <p>2021 - 2022</p>
    </div>
  </div>
</section>

</body>
</html>
"""

# عرض HTML كامل فـ Streamlit
st.components.v1.html(html_content, height=1000, scrolling=True)
