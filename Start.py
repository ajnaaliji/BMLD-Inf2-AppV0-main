# ====== Start Init Block ======
# This needs to copied on top of the entry point of the app (Start.py)

import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )
# ====== End Init Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

# Page Config
st.set_page_config(page_title="Kalorienrechner", page_icon="🔥")

# Titel
st.title("Kalorienrechner")

# Einführungstext
st.markdown("""
<div style="background-color: #E7F3FF; padding: 15px; border-radius: 8px;">
Mit diesem Kalorienrechner kannst du deinen täglichen Energiebedarf berechnen egal, ob du dein Gewicht halten, abnehmen oder zunehmen möchtest. Gib einfach deine Daten ein und erhalte eine individuelle Empfehlung für deinen Kalorienbedarf!
</div>
""", unsafe_allow_html=True)

st.write("")  # Leerzeile für Abstand

# Abschnitt: So funktioniert es 
st.markdown("### So funktioniert es:")
st.markdown("""
1. Gib deine persönlichen Daten ein (Alter, Gewicht, Grösse etc.).
2. Der Rechner bestimmt deinen individuellen Kalorienbedarf und gibt dir eine Empfehlung.
""")

st.write("")  # Leerzeile für Abstand

st.markdown(" **Jetzt Ziel wählen und Berechnung starten:**")

st.write("")  # Leerzeile für Abstand

# Abschnitt: Wähle dein Ziel
st.markdown("### 🎯 Wähle dein Ziel:")

st.markdown("""
-  **Gewicht halten** → Berechnung für den täglichen Kalorienbedarf, um dein aktuelles Gewicht stabil zu halten.
-  **Abnehmen** → Berechnung mit einem Kaloriendefizit, um Gewicht zu verlieren.
-  **Zunehmen** → Berechnung mit einem Kalorienüberschuss, um Gewicht zuzunehmen.
""")

st.write("")  # Leerzeile für Abstand


# Hinweis
st.markdown("""
<div style="background-color: #FFF3CD; padding: 15px; border-radius: 8px;">
⚠️ <strong>Hinweis:</strong> Die hier berechneten Kalorienwerte sind <strong>nur Richtwerte</strong> und dienen nicht als medizinische oder ernährungswissenschaftliche Beratung.
</div>
""", unsafe_allow_html=True)


st.write("")  # Leerzeile für Abstand

# Start der Berechnung
st.markdown("## 🚀 Starte jetzt deine Berechnung!")

# Stilisiertes Button-Design
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
if st.button(" Zum Kalorienrechner"):
    st.switch_page("pages/1_Kalorienrechner.py")

st.write("")  # Leerzeile für Abstand

st.markdown("---")

# Entwicklerinformationen untereinander anzeigen
st.markdown("""
#### Entwickler:
**Ajna Aliji**  
 [alijiajn@students.zhaw.ch](mailto:alijiajn@students.zhaw.ch)  

**Melisa Dedukic**  
 [dedukmel@students.zhaw.ch](mailto:dedukmel@students.zhaw.ch)  
""")