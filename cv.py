import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Djabou Sonko", page_icon="🌍", layout="centered")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stHeader { color: #2c3e50; }
    .skill-tag {
        background-color: #e1f5fe;
        border-radius: 5px;
        padding: 5px 10px;
        margin: 5px;
        display: inline-block;
        color: #01579b;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (CONTACT) ---
with st.sidebar:
    st.title("📍 Contact")
    st.write("📞 +221 77 663 37 68")
    st.write("📧 djabousonko@gmail.com")
    st.write("🏠 Dakar, Patte d'Oie")
    st.write("---")
     st.header("🌐 Langues")
    st.write("- Anglais\n- Français\n- Wolof\n- Diola")
    st.header("🎨 Loisirs")
    st.write("- Lecture\n- Fitness")
   

# --- EN-TÊTE ---
st.title("DJABOU SONKO")
st.subheader("GEOMATICIENNE")
st.info("Technicienne en géomatique maîtrisant ArcGIS, QGIS et AutoCAD. Spécialisée en cartographie, collecte et analyse de données spatiales, avec expérience en utilisation de drones et outils bureautiques.")

# --- EXPERIENCE ---
st.header("🚀 Expérience Professionnelle")
st.markdown("""
- Réalisation de cartes thématiques sur QGIS.
- Projet universitaire : Collecte de données topographiques avec drone .
- Mission de terrain : Analyse de données spatiales pour un projet d'aménagement.
- Pilotage de drone et utilisation de Mobile Topographer.
- Confection de plans sur AutoCAD et Covadis.
- Réalisation d'une base de donnée avec Power AMC et Arcgis
""")

# --- EDUCATION ---
st.header("🎓 Éducation")
col1, col2 = st.columns(2)

with col1:
    st.write("2025")
    st.write("2019 - 2022")
    st.write("2023 - 2024")
    st.write("2022")

with col2:
    st.write("Attestation de stage en Topographie (CasaTopo)")
    st.write("Licence en Géographie (U. Assane Seck)")
    st.write ("Premier Année BTS en Géomatique (CEDT)")
    st.write("Attestation Hôtellerie & Restauration")

st.write("2019 : BAC | 2016 : BFEM")

# --- COMPÉTENCES ---
st.header("🛠 Compétences Techniques")
skills = ["ArcGIS", "QGIS", "AutoCAD","Covadis","Kobocollect", "PostgreSQL", "Wampserver", "Word", "Excel", "PowerPoint", "Access"]
skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
st.markdown(skill_html, unsafe_allow_html=True)

# --- TÉLÉCHARGEMENT ---
st.write("---")
st.download_button(
    label="📄 Télécharger le CV complet (PDF)",
    data=b"Le contenu de votre PDF ici", # À remplacer par le vrai fichier
    file_name="CV_Djabou_Sonko.pdf",
    mime="application/pdf",
)
