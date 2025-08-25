import streamlit as st
import random
from datetime import datetime

condizioni = [
    "☀️ Soleggiato",
    "🌧 Pioggia",
    "⛈ Temporale",
    "🌤 Parzialmente nuvoloso",
    "🌥 Nuvoloso",
    "❄️ Neve",
    "🌫 Nebbia",
    "💨 Vento forte"
]

def genera_temperatura():
    return random.randint(-5, 40)

def genera_umidita():
    return random.randint(20, 100)

def genera_meteo():
    condizione = random.choice(condizioni)
    temp = genera_temperatura()
    umidita = genera_umidita()
    return condizione, temp, umidita

st.set_page_config(page_title="Meteo Casuale", page_icon="🌦")

st.title("🌦 Simulatore Meteo Casuale")
st.write("Ogni volta che premi il pulsante, verrà generato un meteo diverso!")

if st.button("Genera Meteo"):
    condizione, temp, umidita = genera_meteo()
    st.subheader(f"Meteo di oggi ({datetime.now().strftime('%d/%m/%Y %H:%M')})")
    st.write(f"**Condizione:** {condizione}")
    st.write(f"🌡 **Temperatura:** {temp}°C")
    st.write(f"💧 **Umidità:** {umidita}%")
else:
    st.info("Premi il pulsante per generare il meteo 🌍")
