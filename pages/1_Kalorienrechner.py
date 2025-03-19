# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
from utils.calculator import calculate_calories  

# Page Config
st.set_page_config(
    page_title="Dein persönlicher Kalorienrechner",
    page_icon="🔥"
)

# Titel
st.title("Dein persönlicher Kalorienrechner ")

# Zielauswahl
ziel = st.radio("📌 **Wähle dein Ziel:**", 
    ["Gewicht halten", "Abnehmen", "Zunehmen"])

# Erklärung zum gewählten Ziel
ziel_beschreibungen = {
    "Gewicht halten": "Berechne deinen täglichen Kalorienbedarf, um dein aktuelles Gewicht stabil zu halten.",
    "Abnehmen": "Berechne deinen Kalorienbedarf mit einem Kaloriendefizit, um Gewicht zu verlieren.",
    "Zunehmen": "Berechne deinen Kalorienbedarf mit einem Kalorienüberschuss, um Gewicht zuzunehmen."
}
st.info(ziel_beschreibungen[ziel])

# Aktivitätsfaktoren mit detaillierter Beschreibung
activity_options = {
    "Gering (kaum Bewegung, Büroarbeit)": "Gering",
    "Leicht aktiv (1-3 Tage/Woche leichte Bewegung)": "Leicht aktiv",
    "Moderat aktiv (3-5 Tage Sport/Woche)": "Moderat aktiv",
    "Sehr aktiv (6-7 Tage intensives Training)": "Sehr aktiv",
    "Extrem aktiv (tägliches hartes Training, körperliche Arbeit)": "Extrem aktiv"
}

activity_factors = {
    "Gering": 1.2,
    "Leicht aktiv": 1.375,
    "Moderat aktiv": 1.55,
    "Sehr aktiv": 1.725,
    "Extrem aktiv": 1.9
}

# Eingabeformular mit besseren Icons
with st.form("Kalorienrechner Formular"):
    gender = st.selectbox("⚧ Geschlecht", ["Männlich", "Weiblich"])
    age = st.number_input("📆 Alter (Jahre)", min_value=1, max_value=120, value=25, step=1)
    height = st.number_input("📏 Grösse (m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
    weight = st.number_input("⚖ Gewicht (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    
    activity_choice = st.selectbox("⚡ Aktivitätslevel", list(activity_options.keys()))
    activity_level = activity_options[activity_choice]  # Kurzname speichern

    submitted = st.form_submit_button("Kalorienbedarf berechnen")

# Verarbeitung nach Absenden des Formulars
if submitted:
    try:
        result = calculate_calories(age, weight, height, gender, activity_level)

        if not result or "calories" not in result:
            st.error("❌ Fehler: Die Berechnung hat keinen Kalorienwert zurückgegeben!")
        else:
            # 🔥 Kalorienanpassung je nach Ziel mit Sicherheitscheck (keine negativen Werte)
            if ziel == "Abnehmen":
                result["calories"] = max(result["calories"] - 500, 800)  # Mindestens 800 kcal
            elif ziel == "Zunehmen":
                result["calories"] += 500  

            # Formatierte Ausgabe mit besserer Lesbarkeit
            st.success(f" **Dein täglicher Kalorienbedarf beträgt:**\n\n### {result['calories']} kcal")
            st.info(f" **Ziel:** {ziel}")

            # Diagramm: Vergleich zwischen Grundumsatz & Gesamtbedarf
            st.subheader("Kalorienverbrauch nach Aktivitätslevel")
            st.write("Hier siehst du den Vergleich zwischen deinem **Grundumsatz** (Ruhezustand) und deinem **Gesamtbedarf** (mit Aktivität).")

            labels = ["Grundumsatz", "Gesamtbedarf"]
            values = [result['calories'] / activity_factors[activity_level], result['calories']]

            fig, ax = plt.subplots()
            ax.bar(labels, values, color=["#74C0FC", "#FFB3C1"])  # Klare, sanfte Farben
            ax.set_ylabel("Kalorien")
            ax.set_title("Kalorienbedarf Vergleich")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠ Ein unerwarteter Fehler ist aufgetreten: {e}")