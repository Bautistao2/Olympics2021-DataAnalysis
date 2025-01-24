import sqlite3

def check_tables(db_name='olympics.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Obtener nombres de tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tablas en la base de datos:")
    for table in tables:
        print(f"- {table[0]}")
    
    # Mostrar algunas filas de cada tabla
    for table in tables:
        print(f"\nDatos de la tabla {table[0]}:")
        cursor.execute(f"SELECT * FROM {table[0]} LIMIT 5;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
    conn.close()

if __name__ == '__main__':
    check_tables()
