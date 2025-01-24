import sqlite3

def execute_sql_file(sql_file, db_name='olympics.db'):
    """
    Executes an SQL file to create tables or perform operations in the SQLite database.

    Parameters:
        sql_file (str): Path to the SQL file.
        db_name (str): Name of the SQLite database file.
    """
    # Connect to the SQLite database (creates the database file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Read the SQL file
    with open(sql_file, 'r') as file:  # Ensure sql_file is passed correctly
        sql_script = file.read()
    
    # Execute the SQL script
    try:
        cursor.executescript(sql_script)
        print(f"SQL script {sql_file} executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Close the database connection
    conn.close()

if __name__ == '__main__':
    # Path to the SQL file
    execute_sql_file('sql/create_table.sql')
