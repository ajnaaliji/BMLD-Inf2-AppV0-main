import streamlit as st

# Page Config
st.set_page_config(page_title="Kalorienrechner", page_icon="🔥")

# 🏆 Titel mit Design
st.markdown("<h1 style='text-align: center;'> Kalorienrechner</h1>", unsafe_allow_html=True)

# 📌 Einführung mit farblicher Hervorhebung
st.info("""
Mit diesem Kalorienrechner kannst du deinen täglichen Energiebedarf berechnen 
egal, ob du dein Gewicht halten, abnehmen oder zunehmen möchtest. 
Gib einfach deine Daten ein und erhalte eine individuelle Empfehlung für deinen Kalorienbedarf!
""")

# 🎯 Wähle dein Ziel
st.markdown("""
### 🎯 **Wähle dein Ziel:**
- **⚖ Gewicht halten** → Berechnung für den täglichen Kalorienbedarf, um dein aktuelles Gewicht stabil zu halten.
- **📉 Abnehmen** → Berechnung mit einem Kaloriendefizit, um Gewicht zu verlieren.
- **📈 Zunehmen** → Berechnung mit einem Kalorienüberschuss, um Gewicht zuzunehmen.
""")

# ⚠ Hinweis als gelbe Box für mehr Sichtbarkeit
st.warning("⚠ **Hinweis:** Die hier berechneten Kalorienwerte sind **nur Richtwerte** und dienen nicht als medizinische oder ernährungswissenschaftliche Beratung.")

# 🛠 Entwicklerinfos in zwei Spalten für bessere Lesbarkeit
st.markdown("---")  # Trennlinie für bessere Übersicht

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    #### Entwickler:
     **Ajna Aliji**  
    [alijiajn@students.zhaw.ch](mailto:alijiajn@students.zhaw.ch)
    """)

with col2:
    st.markdown("""
     **Melisa Dedukic**  
    [dedukmel@students.zhaw.ch](mailto:dedukmel@students.zhaw.ch)
    """)

# Navigation zum Kalorienrechner
st.markdown("### Starte jetzt deine Berechnung!")

import streamlit as st

# CSS für das Styling des Buttons
st.markdown("""
    <style>
    .stButton>button {
        background-color: #007BFF !important; /* Blau */
        color: white !important;  /* Weiße Schrift */
        font-size: 20px !important; /* Größere Schrift */
        font-weight: bold !important; /* Fettschrift */
        text-decoration: underline !important; /* Unterstrichen */
        border-radius: 8px !important;
        padding: 12px !important;
        width: 100% !important;
        border: none !important;
        cursor: pointer !important;
    }
    .stButton>button:hover {
        background-color: #0056b3 !important; /* Dunkleres Blau beim Hover */
    }
    </style>
""", unsafe_allow_html=True)

# Funktionaler Button für den Seitenwechsel
if st.button("Zum Kalorienrechner"):
    st.switch_page("pages/1_Kalorienrechner.py")
