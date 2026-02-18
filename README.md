
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Djabou Sonko", page_icon="📍", layout="centered")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stHeader { color: #2c3e50; }
    .skill-tag { 
        background-color: #e1f5fe; 
        border-radius: 15px; 
        padding: 5px 15px; 
        margin: 5px; 
        display: inline-block;
        font-weight: bold;
        color: #01579b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE ---
st.title("DJABOU SONKO")
st.subheader("📍 Géomaticienne")
st.info("Technicienne en géomatique maîtrisant ArcGIS, QGIS et AutoCAD. Spécialisée en cartographie, collecte et analyse de données spatiales.")

# --- CONTACT (Sidebar) ---
with st.sidebar:
    st.header("📫 Contact")
    st.write("📞 +221 77 663 37 68")
    st.write("📧 djabousonko@gmail.com")
    st.write("📍 Dakar, Patte d'Oie")
    st.write("---")
    st.header("🌐 Langues")
    st.write("- Français / Wolof / Diola")
    st.write("- Anglais")
    st.write("---")
    st.header("🎨 Loisirs")
    st.write("📚 Lecture | 🏃‍♀️ Fitness")

# --- CORPS DU CV ---
col1, col2 = st.columns([1, 1.2])

with col1:
    st.header("🎓 Éducation")
    st.markdown("""
    2024 - 2025 | CEDT  
    Licence 1 en Géomatique
    
    2023 - 2024 | Univ. Assane Seck  
    Licence en Géographie
    
    2022 | Les Astuces de Ziguinchor  
    Attestation Hôtellerie & Restauration
    
    2019 : BAC | 2016 : BFEM
    """)

with col2:
    st.header("💼 Expérience")
    st.write("Projets & Missions :")
    st.write("- ✅ Réalisation de cartes thématiques sur QGIS.")
    st.write("- ✅ Collecte de données topographiques par drone.")
    st.write("- ✅ Analyse spatiale pour projets d'aménagement.")

st.write("---")

# --- COMPÉTENCES TECHNIQUES ---
st.header("🛠 Compétences Techniques")
st.write("Logiciels & Outils :")
st.markdown("""
<span class="skill-tag">ArcGIS</span> <span class="skill-tag">QGIS</span> 
<span class="skill-tag">AutoCAD</span> <span class="skill-tag">PostgreSQL</span> 
<span class="skill-tag">WampServer</span> <span class="skill-tag">Mobile Topographer</span>
""", unsafe_allow_html=True)

st.write("Expertises :")
skills = {
    "Cartographie & Plans": 95,
    "Pilotage de Drone": 85,
    "Analyse de données": 90,
    "Bureautique (Office)": 95
}
for skill, level in skills.items():
    st.write(f"{skill}")
    st.progress(level)

# --- BOUTON DE TÉLÉCHARGEMENT ---
st.write("---")
st.download_button(
    label="📂 Télécharger le CV complet (PDF)",
    data="Fichier_CV_Ici", # Remplace par le binaire de ton PDF
    file_name="CV_Djabou_Sonko.pdf",
    mime="application/pdf"
)
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon CV Professionnel</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="cv-container">
        <header>
            <h1>VOTRE PRÉNOM NOM</h1>
            <p class="job-title">Développeur Junior / Votre Métier</p>
        </header>

        <div class="main-content">
            <aside class="sidebar">
                <section>
                    <h3>Contact</h3>
                    <p>📧 email@exemple.com</p>
                    <p>📱 06 00 00 00 00</p>
                    <p>🔗 linkedin.com/in/pseudo</p>
                </section>

                <section>
                    <h3>Compétences</h3>
                    <ul>
                        <li>HTML5 / CSS3</li>
                        <li>JavaScript</li>
                        <li>Gestion de projet</li>
                    </ul>
                </section>
            </aside>

            <section class="experience">
                <h2>Expériences Professionnelles</h2>
                <div class="job">
                    <h4>Stage Développeur - Entreprise X</h4>
                    <p class="date">Janvier 2023 - Juin 2023</p>
                    <p>Mise à jour du site vitrine et correction de bugs.</p>
                </div>

                <h2>Formation</h2>
                <div class="edu">
                    <h4>BTS Informatique</h4>
                    <p class="date">2021 - 2023</p>
                </div>
            </section>
        </div>
    </div>

</body>
</html>
