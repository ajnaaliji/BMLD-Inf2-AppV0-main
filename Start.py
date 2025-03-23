import streamlit as st  # MUSS als erster Streamlit-Befehl stehen!
st.set_page_config(page_title="Kalorienrechner", page_icon="🔥")

# ====== Start Init Block ======
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App_Melinja")  # SWITCHdrive

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# ✅ Daten aus SWITCHdrive laden (mit Fehlerbehandlung!)
try:
    data_manager.load_user_data(
    session_state_key='calorie_data_df',
    file_name='data.csv',
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp'],
    date_parser=lambda col: pd.to_datetime(col, errors='coerce')
)
except UnicodeDecodeError:
    st.warning("⚠️ Die Datei 'data.csv' konnte nicht gelesen werden und wurde zurückgesetzt.")
    st.session_state["calorie_data_df"] = pd.DataFrame()
# ====== End Init Block ======

# ------------------------------------------------------------
# Hier startet die eigentliche App

# Titel
st.title("Kalorienrechner")

# Einführungstext
st.markdown("""
<div style="background-color: #E7F3FF; padding: 15px; border-radius: 8px;">
Mit diesem Kalorienrechner kannst du deinen täglichen Energiebedarf berechnen – egal, ob du dein Gewicht halten, abnehmen oder zunehmen möchtest. Gib einfach deine Daten ein und erhalte eine individuelle Empfehlung für deinen Kalorienbedarf!
</div>
""", unsafe_allow_html=True)

st.write("")

# Abschnitt: So funktioniert es 
st.markdown("### So funktioniert es:")
st.markdown("""
1. Gib deine persönlichen Daten ein (Alter, Gewicht, Grösse etc.).
2. Der Rechner bestimmt deinen individuellen Kalorienbedarf und gibt dir eine Empfehlung.
""")

st.write("")

st.markdown(" **Jetzt Ziel wählen und Berechnung starten:**")

st.write("")

# Abschnitt: Wähle dein Ziel
st.markdown("### 🎯 Wähle dein Ziel:")

st.markdown("""
-  **Gewicht halten** → Berechnung für den täglichen Kalorienbedarf, um dein aktuelles Gewicht stabil zu halten.  
-  **Abnehmen** → Berechnung mit einem Kaloriendefizit, um Gewicht zu verlieren.  
-  **Zunehmen** → Berechnung mit einem Kalorienüberschuss, um Gewicht zuzunehmen.
""")

st.write("")

# Hinweis
st.markdown("""
<div style="background-color: #FFF3CD; padding: 15px; border-radius: 8px;">
⚠️ <strong>Hinweis:</strong> Die hier berechneten Kalorienwerte sind <strong>nur Richtwerte</strong> und dienen nicht als medizinische oder ernährungswissenschaftliche Beratung.
</div>
""", unsafe_allow_html=True)

st.write("")

# Start der Berechnung
st.markdown("## 🚀 Starte jetzt deine Berechnung!")

# Stilisiertes Button-Design
st.markdown("""
    <style>
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        text-decoration: underline !important;
        border-radius: 8px !important;
        padding: 12px !important;
        width: 100% !important;
        border: none !important;
        cursor: pointer !important;
    }
    .stButton>button:hover {
        background-color: #0056b3 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Button zum Kalorienrechner
if st.button(" Zum Kalorienrechner"):
    st.switch_page("pages/01_Kalorienrechner.py")

st.write("")
st.markdown("---")

# Entwicklerinformationen
st.markdown("""
#### Entwickler:
**Ajna Aliji**  
[alijiajn@students.zhaw.ch](mailto:alijiajn@students.zhaw.ch)  

**Melisa Dedukic**  
[dedukmel@students.zhaw.ch](mailto:dedukmel@students.zhaw.ch)  
""")
