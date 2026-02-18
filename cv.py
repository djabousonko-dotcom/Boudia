.main {
        background-color: #f8f9fa;
    }
    .stProgress > div > div > div > div {
        background-color: #2ecc71;
    }
    h1 {
        color: #2c3e50;
    }
    h2 {
        color: #16a085;
        border-bottom: 2px solid #16a085;
        padding-bottom: 10px;
    }
    .job-date {
        float: right;
        font-style: italic;
        color: #7f8c8d;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENTÊTE ---
col1, col2 = st.columns([1, 3])
with col1:
    st.write("## 📍") # Tu pourras remplacer par st.image("photo.jpg")
with col2:
    st.title("VOTRE PRÉNOM NOM")
    st.write("**Étudiant en 2ème année de BTS Géomatique**")
    st.write("📧 email@exemple.com | 📱 06 00 00 00 00")

# --- FORMATION ---
st.header("🎓 Formation")
col_edu, col_date = st.columns([3, 1])
with col_edu:
    st.markdown("**BTS Géomatique (2ème année)**")
    st.write("Spécialité : Acquisition et traitement de données géographiques")
with col_date:
    st.write("  \n**2025 - 2026**")

# --- EXPÉRIENCES ---
st.header("💼 Expériences Professionnelles")

# Stage Topographie
st.markdown(f"**Stage en Topographie** <span class='job-date'>Été 2025</span>", unsafe_allow_html=True)
st.write("""
- Levés topographiques sur le terrain (Théodolite, GPS différentiel).
- Implantation d'ouvrages et calculs de polygonation.
- Traitement des données terrain et mise au plan.
""")

# Projet d'intégration
st.markdown(f"**Projet d'Intégration Géomatique** <span class='job-date'>2025</span>", unsafe_allow_html=True)
st.write("""
- Conception d'un Système d'Information Géographique (SIG) complet.
- Collecte, structuration et intégration de données hétérogènes.
- Analyse spatiale et production de cartes thématiques.
""")

# --- COMPÉTENCES TECHNIQUES ---
st.header("🛠️ Compétences Techniques")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Informatique")
    st.progress(85, text="Python (Streamlit, Pandas)")
    st.progress(75, text="HTML / CSS (Web mapping)")
    st.progress(90, text="Logiciels SIG (QGIS / ArcGIS)")

with c2:
    st.subheader("Topographie")
    st.write("- Levés GNSS et Station Totale")
    st.write("- DAO / CAO (AutoCAD)")
    st.write("- Photogrammétrie par drone")

# --- SECTION INTERACTIVE ---
st.sidebar.header("À propos")
st.sidebar.write("""
Passionné par la convergence entre la **géographie** et le **développement informatique**. 
Ce CV a été entièrement codé en **Python** via la bibliothèque **Streamlit**.
""")

if st.sidebar.button("Afficher ma motivation"):
    st.sidebar.success("Je suis à la recherche d'un stage de fin d'études ou d'une alternance pour perfectionner mes compétences en développement SIG !")

# --- BOUTON DE TÉLÉCHARGEMENT ---
st.write("---")
st.download_button(
    label="📄 Télécharger le CV (PDF)",
    data="Fichier PDF réel ici",
    file_name="CV_Geomatique_2025.pdf",
    mime="application/pdf"
)
