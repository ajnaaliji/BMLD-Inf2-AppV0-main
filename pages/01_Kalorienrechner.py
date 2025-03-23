import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from utils.calculator import calculate_calories  
from utils.login_manager import LoginManager
from utils.data_manager import DataManager  # <-- neu hinzugefügt für SWITCHdrive

st.set_page_config(
    page_title="Dein persönlicher Kalorienrechner",
    page_icon="🔥"
)

# ====== Start Login Block ======
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

st.title("Dein persönlicher Kalorienrechner")

# Zielauswahl
ziel = st.radio("📌 **Wähle dein Ziel:**", 
    ["Gewicht halten", "Abnehmen", "Zunehmen"])

ziel_beschreibungen = {
    "Gewicht halten": "Berechne deinen täglichen Kalorienbedarf, um dein aktuelles Gewicht stabil zu halten.",
    "Abnehmen": "Berechne deinen Kalorienbedarf mit einem Kaloriendefizit, um Gewicht zu verlieren.",
    "Zunehmen": "Berechne deinen Kalorienbedarf mit einem Kalorienüberschuss, um Gewicht zuzunehmen."
}
st.info(ziel_beschreibungen[ziel])

# Aktivitätsfaktoren für UI
activity_options = {
    "Gering (kaum Bewegung, Büroarbeit)": "Gering",
    "Leicht aktiv (1-3 Tage/Woche leichte Bewegung)": "Leicht aktiv",
    "Moderat aktiv (3-5 Tage Sport/Woche)": "Moderat aktiv",
    "Sehr aktiv (6-7 Tage intensives Training)": "Sehr aktiv",
    "Extrem aktiv (tägliches hartes Training, körperliche Arbeit)": "Extrem aktiv"
}

# Eingabeformular
with st.form("Kalorienrechner Formular"):
    gender = st.selectbox("⚧ Geschlecht", ["Männlich", "Weiblich"])
    age = st.number_input("📆 Alter (Jahre)", min_value=1, max_value=120, value=25, step=1)
    height = st.number_input("📏 Grösse (m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
    weight = st.number_input("⚖ Gewicht (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)

    # 🔥 Aktivitätslevel extrahieren
    activity_choice = st.selectbox("⚡ Aktivitätslevel", list(activity_options.keys()))
    activity_level = activity_options[activity_choice]

    submitted = st.form_submit_button("Kalorienbedarf berechnen")

# Session State initialisieren
if "calorie_data_df" not in st.session_state:
    st.session_state["calorie_data_df"] = pd.DataFrame()

# Verarbeitung nach Absenden des Formulars
if submitted:
    try:
        result = calculate_calories(age, weight, height, gender, activity_level)

        if not result or "calories" not in result:
            st.error("❌ Fehler: Die Berechnung hat keinen Kalorienwert zurückgegeben!")
        else:
            grundumsatz = result["bmr"]
            gesamtumsatz = result["calories"]

            if ziel == "Gewicht halten":
                consumed_calories = gesamtumsatz  
            elif ziel == "Abnehmen":
                consumed_calories = max(gesamtumsatz - 500, 1200)
            elif ziel == "Zunehmen":
                consumed_calories = gesamtumsatz + 300  

            new_data = {
                "timestamp": datetime.now(),
                "bmr": grundumsatz,
                "burned_calories": gesamtumsatz,  
                "consumed_calories": consumed_calories,
                "goal": ziel,
                "age": age,  
                "height": height,  
                "weight": weight,  
                "gender": gender,  
                "activity_level": activity_level
            }

            # Session State aktualisieren
            st.session_state["calorie_data_df"] = pd.concat(
                [st.session_state["calorie_data_df"], pd.DataFrame([new_data])],
                ignore_index=True
            )

            # 🔥 Daten dauerhaft speichern (SWITCHdrive)
            DataManager().append_record("calorie_data_df", new_data)

            # ✅ Erfolgsmeldung
            st.success(f" **Dein täglicher Kalorienbedarf beträgt:**\n\n### {int(consumed_calories)} kcal")
            st.info(f" **Ziel:** {ziel}")

            # 📊 Balkendiagramm
            st.subheader("Kalorienverbrauch mit & ohne Aktivität")

            labels = ["Grundumsatz (Ruhe)", "Gesamtbedarf (mit Aktivität)"]
            values = [grundumsatz, gesamtumsatz]

            fig, ax = plt.subplots()
            ax.bar(labels, values, color=["#74C0FC", "#FFB3C1"])  
            ax.set_ylabel("Kalorien")
            ax.set_title("Kalorienbedarf im Vergleich")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠ Ein unerwarteter Fehler ist aufgetreten: {e}")
