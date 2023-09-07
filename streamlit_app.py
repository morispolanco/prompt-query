import streamlit as st
import pandas as pd

st.title("4000 prompts de neocios")

# Ruta al archivo de Excel predefinido
excel_file_path = "excel.xlsx"

# Leer el archivo de Excel en un DataFrame
try:
    df = pd.read_excel(excel_file_path, engine='openpyxl')

    # Mostrar los primeros registros del DataFrame
    st.subheader("Primeros registros del DataFrame:")
    st.write(df)

    # Crear una barra de búsqueda para filtrar los datos
    search_term = st.text_input("Buscar en la base de datos:")

    # Filtrar los datos según el término de búsqueda
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

    # Mostrar los resultados de la búsqueda
    st.subheader("Resultados de la búsqueda:")
    st.write(filtered_df)

    # Descargar los resultados de la búsqueda como un nuevo archivo CSV
    if st.button("Descargar resultados de búsqueda como CSV"):
        csv_data = filtered_df.to_csv(index=False)
        st.download_button(
            label="Descargar CSV",
            data=csv_data,
            file_name="resultados_busqueda.csv",
            mime="text/csv",
        )
except FileNotFoundError:
    st.error(f"No se pudo encontrar el archivo de Excel en la ruta: {excel_file_path}")
