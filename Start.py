import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kalorienrechner", page_icon="🔥")

st.title("Kalorienrechner")


"""
Dieser Kalorienrechner hilft dir, deinen täglichen Energiebedarf zu berechnen, basierend auf Geschlecht, Alter, Gewicht, Grösse und Aktivitätslevel.

🎯 Wähle dein Ziel:

- Gewicht halten → Berechnung für den täglichen Kalorienbedarf, um dein aktuelles Gewicht zu stabilisieren.
- Abnehmen → Berechnung mit einem Kaloriendefizit, um Gewicht zu verlieren.
- Zunehmen → Berechnung mit einem Kalorienüberschuss, um Gewicht zuzunehmen.

Gib einfach deine Daten ein und erhalte eine Schätzung deines optimalen Kalorienbedarfs!
"""

import streamlit as st
st. info("⚠ Hinweis: Die hier berechneten Kalorienwerte sind nur Richtwerte und dienen nicht als medizinische oder ernährungswissenschaftliche Beratung.")

st.write("Klicke in der Sidebar auf Kalorienrechner oder nutze den Button unten, um deine Berechnung zu starten!") 

if st.button("🔥 Zum Kalorienrechner"):
    st.switch_page("pages/1_Kalorienrechner.py") 

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Ajna Aliji (alijiajn@students.zhaw.ch)
- Melisa Dedukic (dedukmel@students.zhaw.ch)"
""" 