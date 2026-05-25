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
        # Citire date
        df = pd.read_excel(statistica_file, sheet_name="analiza statistica")
        
        st.success("✅ Fișiere încărcate cu succes!")
        st.info("🔄 Se calculează agregările și recomandările...")
        
        # Afișare tabel inițial (pentru moment)
        st.subheader("Previzualizare Date")
        st.dataframe(df.head(15))
        
        st.warning("🚧 Logica completă de agregare, COM ACUM și recomandări va fi implementată în următorul pas.")
        st.balloons()
        
else:
    st.info("📌 Te rog să încarci cele două fișiere Excel pentru a începe analiza.")

st.caption("Aplicație Streamlit • contoare-streamlit")
