import streamlit as st

import streamlit as st
from datetime import datetime

import matplotlib.pyplot as plt
from utils.calculator import calculate_calories  

# 🔥 Page Config
st.set_page_config(
    page_title="Kalorienrechner",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/3/3c/Fire_Icon.svg" 
)

# Streamlit UI
st.title("Kalorienrechner")
st.write("Dieser Kalorienrechner hilft deinen täglichen Energiebedarf basierend auf Geschlecht, Alter, Gewicht, Grösse und Aktivitätslevel zu berechnen.")

# Aktivitätsfaktoren als globale Variable definieren 
activity_factors = {
    "Gering": 1.2,
    "Leicht aktiv": 1.375,
    "Moderat aktiv": 1.55,
    "Sehr aktiv": 1.725,
    "Extrem aktiv": 1.9
}

# Eingabeformular mit Submit-Button
with st.form("Kalorienrechner Formular"):
    gender = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
    age = st.number_input("Alter (Jahre)", min_value=1, max_value=120, value=25, step=1)
    height = st.number_input("Grösse (in Meter)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
    weight = st.number_input("Gewicht (in kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    activity_level = st.selectbox("Aktivitätslevel", list(activity_factors.keys()))  # Vermeidet KeyError

    # WICHTIG: Submit-Button innerhalb des Formulars
    submitted = st.form_submit_button("Berechnen")

if submitted:
    result = calculate_calories(age, weight, height, gender, activity_level)

    # Ergebnisse ausgeben
    st.subheader("Ergebnis")
    st.write(f"**Dein täglicher Kalorienbedarf:** {result['calories']} kcal")
    st.write(f"**Berechnet am:** {result['timestamp'].strftime('%d.%m.%Y %H:%M:%S')}")

    # Debugging-Ausgabe 
    st.write(f"Aktivitätslevel: {activity_level}")
    st.write(f"Aktivitätsfaktor: {activity_factors.get(activity_level, 'Nicht gefunden')}")
    st.write(f"Berechnete Kalorien: {result['calories']}")

    # Visualisierung als Balkendiagramm (nur wenn Aktivitätslevel gültig ist)
    if activity_level in activity_factors:
        st.subheader("Kalorienverbrauch nach Aktivitätslevel")

        labels = ["Grundumsatz", "Gesamtbedarf"]
        values = [result['calories'] / activity_factors[activity_level], result['calories']]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color=["lightblue", "pink"])
        ax.set_ylabel("Kalorien")
        ax.set_title("Kalorienbedarf Vergleich")

        

