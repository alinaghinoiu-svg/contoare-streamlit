import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contoare Inventory", layout="wide")

st.title("🛠️ Gestionare Stoc Contoare")
st.subheader("Recomandări Comenzi China")

# ================== MAPARE CODURI ==================
coduri_map = {
    "183720": ["153001", "165132", "165133"],
    "166177": ["153000"],
    "166179": ["152999", "165134"],
    "181613": ["152998", "170769"],
    "189252": ["148398"],
    "176504": ["151514"],
}

st.sidebar.header("📤 Upload Fișiere")
statistica_file = st.sidebar.file_uploader("1. Statistica AI analysis.xlsx", type=["xlsx"])
stoc_file = st.sidebar.file_uploader("2. Situație stoc curent", type=["xlsx"])

if statistica_file and stoc_file:
    with st.spinner("Se procesează datele..."):
        df = pd.read_excel(statistica_file, sheet_name="analiza statistica")
        
        st.success("✅ Fișiere încărcate cu succes!")
        
        st.subheader("📊 Previzualizare Statistica")
        st.dataframe(df.head(20))
        
        st.info("""
        🔧 **Următorul pas**: 
        - Agregare coduri similare
        - Calcul COM ACUM = (V3 × 4) - (Stoc + Pe drum)
        - Recomandări complete de comandă
        """)
        st.balloons()

else:
    st.info("📌 Te rog să încarci cele două fișiere Excel (Statistica + Stoc curent) pentru a începe analiza.")

st.caption("Aplicație Streamlit • contoare-streamlit")
