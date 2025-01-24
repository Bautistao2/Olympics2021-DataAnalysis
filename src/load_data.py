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
    # Conectar a SQLite
    conn = sqlite3.connect(db_name)
    
    for table_name, file_name in FILES.items():
        # Cargar cada archivo CSV en un DataFrame
        file_path = DATA_FOLDER + file_name
        df = pd.read_csv(file_path, encoding='latin1')
        
        # Cargar los datos en SQLite
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Datos de {table_name} cargados exitosamente.")
    
    # Cerrar la conexión
    conn.close()

if __name__ == '__main__':
    load_data_to_sqlite()
