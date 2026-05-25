import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contoare Inventory", layout="wide")

st.title("🛠️ Gestionare Stoc Contoare")
st.subheader("Recomandări Comenzi China")

st.sidebar.header("Upload Fișiere")
statistica_file = st.sidebar.file_uploader("1. Statistica AI analysis.xlsx", type=["xlsx"])
stoc_file = st.sidebar.file_uploader("2. Situație stoc curent", type=["xlsx"])

if statistica_file and stoc_file:
    st.success("✅ Fișiere încărcate cu succes!")
    st.info("🔄 Se procesează datele... Logica completă va fi adăugată în curând.")
    st.balloons()
else:
    st.info("📌 Încarcă cele două fișiere Excel pentru a începe analiza.")

st.caption("Aplicație Streamlit • contoare-streamlit")
