import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mon CV Interactif", page_icon="📄", layout="centered")

# --- SECTION ENTÊTE ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    # Si vous avez une photo, remplacez par : st.image("photo.jpg", width=150)
    st.write("📸") 

with col2:
    st.title("VOTRE NOM ET PRÉNOM")
    st.write("Développeur Python | Data Analyst")
    st.write("📍 Paris, France")
    st.write("📧 email@exemple.com")

# --- BARRE LATÉRALE (Contact & Liens) ---
st.sidebar.title("Contact")
st.sidebar.info("""
- [LinkedIn](https://linkedin.com)
- [GitHub](https://github.com)
- [Portfolio](https://mon-site.com)
""")

# --- RÉSUMÉ / PROFIL ---
st.write("---")
st.subheader("Profil Professionnel")
st.write("""
Développeur passionné par la création d'outils interactifs et l'analyse de données. 
Expert en Python avec une forte capacité à résoudre des problèmes complexes.
""")

# --- COMPÉTENCES ---
st.write("---")
st.subheader("Compétences")
col_c1, col_c2 = st.columns(2)

with col_c1:
    st.write("**Langages**")
    st.progress(95, text="Python")
    st.progress(80, text="SQL")
    st.progress(70, text="JavaScript")

with col_c2:
    st.write("**Outils**")
    st.write("- Streamlit, Pandas, NumPy")
    st.write("- Docker, Git, VS Code")
    st.write("- AWS / Google Cloud")

# --- EXPÉRIENCES ---
st.write("---")
st.subheader("Expériences Professionnelles")

with st.expander("Développeur Junior - Tech Corp (2022 - Présent)"):
    st.write("""
    - Développement d'interfaces de visualisation de données.
    - Automatisation de rapports via des scripts Python.
    - Collaboration en équipe agile (Scrum).
    """)

with st.expander("Stage Data Analyst - Startup X (2021)"):
    st.write("""
    - Nettoyage de bases de données avec Pandas.
    - Création de tableaux de bord interactifs.
    """)

# --- FORMATION ---
st.write("---")
st.subheader("Formation")
st.write("**Master en Informatique** - Université de Paris (2021)")
st.write("**Licence Mathématiques Appliquées** - (2019)")

# --- BOUTON DE TÉLÉCHARGEMENT (Simulé) ---
st.write("---")
st.download_button(
    label="⬇️ Télécharger mon CV au format PDF",
    data="Contenu fictif du PDF",
    file_name="mon_cv.pdf",
    mime="application/pdf",
)
