import streamlit as st
import pandas as pd

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

st.title('Kalorien Verlauf')

if "calorie_data_df" not in st.session_state or st.session_state["calorie_data_df"].empty:
    st.info('Keine Kalorien-Daten vorhanden. Erfassen Sie Ihre Kalorien auf der Startseite.')
    st.stop()

data_df = st.session_state["calorie_data_df"]
data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors="coerce")
data_df = data_df.set_index("timestamp").sort_index()

st.line_chart(data=data_df[["burned_calories", "consumed_calories"]], use_container_width=True)
st.caption("Verbrannte vs. aufgenommene Kalorien über Zeit")

data_df["calorie_balance"] = data_df["consumed_calories"] - data_df["burned_calories"]
st.line_chart(data=data_df["calorie_balance"], use_container_width=True)
st.caption("Kalorienbilanz über Zeit")
