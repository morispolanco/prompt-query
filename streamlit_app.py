import streamlit as st
import pandas as pd

# Cargar el archivo de Excel usando Streamlit
uploaded_file = st.file_uploader("Cargar archivo de Excel", type=["xlsx"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Mostrar el DataFrame en la interfaz de usuario
    st.write(df)

    # Barra de búsqueda
    search_term = st.text_input("Buscar")
    search_results = df[df.astype(str).apply(lambda x: x.str.contains(search_term, case=False)).any(axis=1)]

    # Mostrar los resultados de la búsqueda
    st.write("Resultados de la búsqueda:")
    st.write(search_results)
