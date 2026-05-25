# Versiune 6 - Final simplificat

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contoare Inventory", layout="wide")

st.title("🛠️ Gestionare Stoc Contoare")
st.subheader("Recomandări Comenzi China")

st.sidebar.header("📤 Upload Fișiere (4 fișiere)")

stoc_file = st.sidebar.file_uploader("1. Stoc curent", type=None)
v3_file = st.sidebar.file_uploader("2. Vânzări 3 luni", type=None)
v6_file = st.sidebar.file_uploader("3. Vânzări 6 luni", type=None)
v9_file = st.sidebar.file_uploader("4. Vânzări 9 luni", type=None)

if stoc_file and v3_file and v6_file and v9_file:
    try:
        with st.spinner("Se procesează..."):
            df_stoc = pd.read_excel(stoc_file)
            df_v3 = pd.read_excel(v3_file)
            
            st.success("✅ Fișiere încărcate cu succes!")
            st.balloons()

            st.subheader("📊 Statistici")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Rânduri Stoc", len(df_stoc))
            with col2:
                st.metric("Rânduri Vânzări 3 luni", len(df_v3))

            st.info("Aplicația funcționează. Următorul pas: logica completă de agregare.")

    except Exception as e:
        st.error(f"Eroare: {e}")
else:
    st.warning("Încarcă toate 4 fișierele.")

st.caption("contoare-streamlit")
