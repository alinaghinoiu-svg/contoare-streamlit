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
    with st.spinner("Se procesează fișierele..."):
        st.success("✅ Toate fișierele au fost încărcate!")

        try:
            df_stoc = pd.read_excel(stoc_file)
            df_v3 = pd.read_excel(v3_file)
            df_v6 = pd.read_excel(v6_file)
            df_v9 = pd.read_excel(v9_file)

            st.subheader("📊 Informații despre fișiere")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Stoc curent", len(df_stoc))
                st.write("Coloane:", list(df_stoc.columns))
            with col2:
                st.metric("Vânzări 3 luni", len(df_v3))
                st.write("Coloane:", list(df_v3.columns))
            with col3:
                st.metric("Vânzări 6 luni", len(df_v6))
                st.write("Coloane:", list(df_v6.columns))
            with col4:
                st.metric("Vânzări 9 luni", len(df_v9))
                st.write("Coloane:", list(df_v9.columns))

        except Exception as e:
            st.error(f"Eroare la citirea fișierelor: {str(e)}")

else:
    st.info("Încarcă toate 4 fișierele pentru a vedea detaliile.")

st.caption("Aplicație Streamlit • contoare-streamlit")
