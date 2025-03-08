import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
from utils.calculator import calculate_calories  

# 🔥 Page Config
st.set_page_config(
    page_title="Kalorienrechner",
    page_icon="🔥"
)

# 🏆 Titel & Einführung
st.title("Kalorienrechner")

# 🎯 Zielauswahl direkt im Formular
ziel = st.radio("📌 Wähle dein Ziel:", ["Gewicht halten", "Abnehmen", "Zunehmen"])

# 📌 Dynamische Erklärung je nach gewähltem Ziel
ziel_beschreibungen = {
    "Gewicht halten": "💡 Berechne deinen täglichen Kalorienbedarf, um dein aktuelles Gewicht zu stabilisieren.",
    "Abnehmen": "📉 Berechne deinen täglichen Kalorienbedarf mit einem Kaloriendefizit, um Gewicht zu verlieren.",
    "Zunehmen": "📈 Berechne deinen täglichen Kalorienbedarf mit einem Kalorienüberschuss, um Gewicht zuzunehmen."
}
st.info(ziel_beschreibungen[ziel])

# 🔢 Aktivitätsfaktoren mit detaillierten Beschreibungen
activity_factors = {
    "Gering (wenig bis keine Bewegung)": 1.2,
    "Leicht aktiv (leichte Bewegung 1–3 Tage/Woche)": 1.375,
    "Moderat aktiv (mäßige Bewegung 3–5 Tage/Woche)": 1.55,
    "Sehr aktiv (intensiver Sport 6–7 Tage/Woche)": 1.725,
    "Extrem aktiv (tägliches intensives Training, körperliche Arbeit)": 1.9
}

# 📝 Eingabeformular für Benutzerdaten
with st.form("Kalorienrechner Formular"):
    gender = st.selectbox("⚧ Geschlecht", ["Männlich", "Weiblich"])
    age = st.number_input("📆 Alter (Jahre)", min_value=1, max_value=120, value=25, step=1)
    height = st.number_input("📏 Größe (in Meter)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
    weight = st.number_input("⚖ Gewicht (in kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    activity_level = st.selectbox("🏋️ Aktivitätslevel", list(activity_factors.keys()))

    # 🚀 Berechnen-Button
    submitted = st.form_submit_button("🔥 Kalorienbedarf berechnen")

# 🔍 Verarbeitung nach Absenden des Formulars
if submitted:
    result = calculate_calories(age, weight, height, gender, activity_level)

    # 🔥 Anpassung der Kalorienberechnung je nach Ziel
    if "calories" in result:
        if ziel == "Abnehmen":
            result["calories"] -= 500  # Kaloriendefizit
        elif ziel == "Zunehmen":
            result["calories"] += 500  # Kalorienüberschuss

        # 🎯 Ergebnisse schön formatiert ausgeben
        st.success(f"🎯 **Dein täglicher Kalorienbedarf beträgt:** {result['calories']} kcal")
        st.info(f"📌 **Ziel:** {ziel}")

        # 📊 Visualisierung des Kalorienbedarfs als Balkendiagramm
        st.subheader("📊 Kalorienverbrauch nach Aktivitätslevel")
        st.write("Das Diagramm zeigt den Vergleich zwischen deinem **Grundumsatz** (Kalorienverbrauch im Ruhezustand) und deinem **Gesamtbedarf** (Kalorienverbrauch mit Aktivität).")

        labels = ["Grundumsatz", "Gesamtbedarf"]
        values = [result['calories'] / activity_factors[activity_level], result['calories']]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color=["lightblue", "pink"])
        ax.set_ylabel("Kalorien")
        ax.set_title("Kalorienbedarf Vergleich")

        # WICHTIG: Diagramm in Streamlit anzeigen
        st.pyplot(fig)
    else:
        st.error("❌ Fehler: Die Berechnung hat keinen Kalorienwert zurückgegeben!")

# 📥 Option: Ergebnis als CSV speichern
st.download_button(
    label="📥 Ergebnisse speichern",
    data=f"Kalorienbedarf: {result['calories']} kcal\nZiel: {ziel}",
    file_name="kalorienbedarf.txt",
    mime="text/plain"
)

