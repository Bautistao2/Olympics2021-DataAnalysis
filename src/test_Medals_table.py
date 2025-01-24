import sqlite3
import pandas as pd

def check_table_structure(table_name='Medals', db_name='olympics.db'):
    """
    Prints the structure (columns) of a table in the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Query to get table information
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    conn.close()

    print(f"Structure of table {table_name}:")
    for column in columns:
        print(f"Column: {column[1]}, Type: {column[2]}")

def preview_table(table_name='Medals', db_name='olympics.db'):
    """
    Prints the first few rows of a table in the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    query = f"SELECT * FROM {table_name} LIMIT 5;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(f"Preview of table {table_name}:")
    print(df)

# Ejecutar inspecciones
if __name__ == '__main__':
    check_table_structure()
    preview_table()
