import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contoare Inventory", layout="wide")

st.title("🛠️ Gestionare Stoc Contoare")
st.subheader("Recomandări Comenzi China")

st.sidebar.header("📤 Upload Fișiere")

stoc_file = st.sidebar.file_uploader("1. Stoc curent", type=None)
v3_file = st.sidebar.file_uploader("2. Vânzări 3 luni", type=None)
v6_file = st.sidebar.file_uploader("3. Vânzări 6 luni", type=None)
v9_file = st.sidebar.file_uploader("4. Vânzări 9 luni", type=None)

if stoc_file and v3_file and v6_file and v9_file:
    st.success("✅ Fișiere încărcate!")
    st.info("Toate fișierele au fost detectate.")
else:
    st.warning("Încarcă toate 4 fișierele.")

st.caption("Test - All Files")
