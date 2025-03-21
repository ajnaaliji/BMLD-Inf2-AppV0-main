import streamlit as st
import pandas as pd

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

st.title('Kalorienverlauf')

# 📌 **Daten aus Session State abrufen**
if "calorie_data_df" not in st.session_state or st.session_state["calorie_data_df"].empty:
    st.info('Keine Kaloriendaten vorhanden. Erfassen Sie Ihre Kalorien auf der Startseite.')
    st.stop()

data_df = st.session_state["calorie_data_df"]

# 🔹 Sicherstellen, dass der Timestamp das richtige Format hat
if "timestamp" in data_df.columns:
    data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors='coerce')
    data_df["timestamp"] = data_df["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")

# 🔹 **Option zur Anzeige**
st.markdown("### Wähle deine Ansicht:")
ansicht = st.radio("Welche Daten möchtest du sehen?", ["Kompakte Ansicht", "Detaillierte Ansicht"])

kompakt_spalten = ["timestamp", "burned_calories", "consumed_calories", "goal"]
detaillierte_spalten = ["timestamp", "burned_calories", "consumed_calories", "goal", "age", "height", "weight", "gender", "activity_level"]

verfügbare_spalten = [col for col in detaillierte_spalten if col in data_df.columns]

if ansicht == "Kompakte Ansicht":
    st.dataframe(data_df[kompakt_spalten])
else:
    if len(verfügbare_spalten) > 4:
        st.dataframe(data_df[verfügbare_spalten])
    else:
        st.warning("⚠ Keine detaillierten Daten gefunden.")