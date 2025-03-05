import streamlit as st

import streamlit as st
from datetime import datetime

# Funktion zur Berechnung des Kalorienbedarfs
def calculate_calories(age, weight, height, gender, activity_level):
    if gender == "Männlich":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)

    # Aktivitätslevel-Faktoren
    activity_factors = {
        "Gering": 1.2,
        "Leicht aktiv": 1.375,
        "Moderat aktiv": 1.55,
        "Sehr aktiv": 1.725,
        "Extrem aktiv": 1.9
    }

    daily_calories = bmr * activity_factors[activity_level]

    return {"calories": round(daily_calories), "timestamp": datetime.now()}

# Streamlit UI
st.title("Kalorienrechner")
st.write("Dieser Kalorienrechner hilft deinen täglichen Energiebedarf basierend auf Geschlecht, Alter, Gewicht, Größe und Aktivitätslevel zu berechnen.")

# Eingabeformular mit Submit-Button
with st.form("Kalorienrechner Formular"):
    gender = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
    age = st.number_input("Alter (Jahre)", min_value=1, max_value=120, value=25, step=1)
    height = st.number_input("Größe (in Meter)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
    weight = st.number_input("Gewicht (in kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    activity_level = st.selectbox("Aktivitätslevel", ["Gering", "Leicht aktiv", "Moderat aktiv", "Sehr aktiv", "Extrem aktiv"])

    # WICHTIG: Submit-Button innerhalb des Formulars
    submitted = st.form_submit_button("Berechnen")

if submitted:
    result = calculate_calories(age, weight, height, gender, activity_level)

    # Ergebnisse ausgeben
    st.write(f"**Dein täglicher Kalorienbedarf:** {result['calories']} kcal")
    st.write(f"**Berechnet am:** {result['timestamp'].strftime('%d.%m.%Y %H:%M:%S')}")
