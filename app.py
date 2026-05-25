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
    with st.spinner("Se procesează toate fișierele..."):
        try:
            df_stoc = pd.read_excel(stoc_file)
            df_v3 = pd.read_excel(v3_file)
            df_v6 = pd.read_excel(v6_file)
            df_v9 = pd.read_excel(v9_file)

            st.success("✅ Toate 4 fișierele au fost încărcate cu succes!")

            # Afișăm statistici de bază
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📦 Stoc curent", len(df_stoc))
            with col2:
                st.metric("📈 Vânzări 3 luni", len(df_v3))
            with col3:
                st.metric("📈 Vânzări 6 luni", len(df_v6))
            with col4:
                st.metric("📈 Vânzări 9 luni", len(df_v9))

            st.info("🔧 Următorul pas: Agregarea codurilor similare + Calcul COM ACUM (V3×4 - Stoc - Pe drum)")

            # Afișăm primele rânduri din fiecare fișier
            st.subheader("Previzualizare Stoc")
            st.dataframe(df_stoc.head(10))

        except Exception as e:
            st.error(f"Eroare la citirea fișierelor: {str(e)}")
else:
    st.warning("📌 Încarcă **toate 4 fișierele** pentru a începe analiza completă.")

st.caption("Aplicație Streamlit • contoare-streamlit")
