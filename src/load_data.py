import os
import pandas as pd
import sqlite3

# Definir la ruta a la carpeta de datos
DATA_FOLDER = 'Data/'

# Archivos CSV y sus tablas correspondientes
FILES = {
    'Athletes': 'Athletes.csv',
    'Coaches': 'Coaches.csv',
    'EntriesGender': 'EntriesGender.csv',
    'Medals': 'Medals.csv',
    'Teams': 'Teams.csv'
}

def load_data_to_sqlite(db_name='olympics.db'):
    """
    Carga los datos desde archivos CSV en una base de datos SQLite.
    
    Parámetros:
    db_name (str): Nombre de la base de datos SQLite.
    """
    # Verificar que la carpeta de datos exista
    if not os.path.exists(DATA_FOLDER):
        print(f"Error: La carpeta '{DATA_FOLDER}' no existe.")
        return
    
    # Conectar a SQLite
    conn = sqlite3.connect(db_name)
    
    for table_name, file_name in FILES.items():
        file_path = os.path.join(DATA_FOLDER, file_name)
        
        if not os.path.exists(file_path):
            print(f"Error: El archivo '{file_path}' no existe.")
            continue
        
        try:
            # Cargar cada archivo CSV en un DataFrame
            df = pd.read_csv(file_path, encoding='latin1')
            
            # Cargar los datos en SQLite
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"Datos de '{table_name}' cargados exitosamente.")
        except Exception as e:
            print(f"Error al cargar los datos de '{table_name}': {e}")
    
    # Cerrar la conexión
    conn.close()
    print("Todos los datos han sido procesados.")

if __name__ == '__main__':
    load_data_to_sqlite()
