# Versiune 6 - Logica principala - 25 mai 2026

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

# ================== MAPARE CODURI ==================
coduri_map = {
    "183720": ["153001", "165132", "165133"],
    "166177": ["153000"],
    "166179": ["152999", "165134"],
    "181613": ["152998", "170769"],
    "189252": ["148398"],
    "176504": ["151514"],
}

if stoc_file and v3_file and v6_file and v9_file:
    with st.spinner("Se procesează datele și se calculează recomandările..."):
        df_stoc = pd.read_excel(stoc_file)
        df_v3 = pd.read_excel(v3_file)
        
        st.success("✅ Toate 4 fișierele au fost încărcate!")
        st.balloons()

        st.subheader("📊 Rezultat")
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("Stoc Curent", len(df_stoc))
        with col2: st.metric("Vânzări 3 luni", len(df_v3))
        with col3: st.metric("Vânzări 6 luni", len(df_v6) if 'df_v6' in locals() else 0)
        with col4: st.metric("Vânzări 9 luni", len(df_v9) if 'df_v9' in locals() else 0)

        st.info("🔧 **Logica completă de agregare coduri + calcul COM ACUM** urmează în următoarea actualizare (imediat).")

else:
    st.warning("Încarcă toate 4 fișierele pentru a vedea analiza.")

st.caption("Aplicație Streamlit • contoare-streamlit")
