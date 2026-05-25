import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contoare Inventory", layout="wide")

st.title("🛠️ Gestionare Stoc Contoare")
st.subheader("Recomandări Comenzi China")

st.sidebar.header("📤 Upload Fișiere (4 fișiere)")

stoc_file = st.sidebar.file_uploader("1. Stoc curent", type=["xlsx"])
v3_file = st.sidebar.file_uploader("2. Vânzări 3 luni", type=["xlsx"])
v6_file = st.sidebar.file_uploader("3. Vânzări 6 luni", type=["xlsx"])
v9_file = st.sidebar.file_uploader("4. Vânzări 9 luni", type=["xlsx"])

if stoc_file and v3_file and v6_file and v9_file:
    with st.spinner("Se încarcă și se procesează cele 4 fișiere..."):
        st.success("✅ Toate 4 fișierele au fost încărcate!")
        
        st.info("""
        **Următorul pas important:**
        - Citirea datelor din cele 4 fișiere
        - Agregarea codurilor similare
        - Calculul COM ACUM
        """)
        st.balloons()
else:
    st.warning("📌 Te rog să încarci **toate 4 fișierele** pentru a începe analiza.")

st.caption("Aplicație Streamlit • contoare-streamlit")
