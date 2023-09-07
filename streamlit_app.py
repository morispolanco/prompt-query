Copyimport streamlit as st
import pandas as pd

def excel_to_database(file_path):
    # Leer el archivo Excel
    df = pd.read_excel(file_path)

    # Crear una base de datos usando SQLite en memoria
    import sqlite3
    conn = sqlite3.connect(':memory:')
    
    # Guardar el DataFrame en la base de datos como una tabla llamada 'data'
    df.to_sql('data', conn, index=False)
    
    return conn

def search_database(conn, query):
    # Ejecutar la consulta en la base de datos
    results = pd.read_sql_query(query, conn)
    return results

# Configurar la aplicación Streamlit
st.title("Hoja de Excel a Base de Datos")
st.write("Cargue un archivo de Excel para convertirlo en una base de datos searchable")

# Cargar el archivo de Excel
file = st.file_uploader("Cargar archivo de Excel", type=["xls", "xlsx"])

if file:
    conn = excel_to_database(file)
    st.write("Hoja de Excel cargada correctamente")
    
    # Ingrese la consulta de búsqueda
    query = st.text_input("Ingrese una consulta de búsqueda")
    
    if st.button("Buscar"):
        results = search_database(conn, query)
        
        # Mostrar los resultados de la búsqueda
        if len(results) > 0:
            st.write("Resultados de búsqueda:")
            st.dataframe(results)
        else:
            st.write("No se encontraron resultados")
