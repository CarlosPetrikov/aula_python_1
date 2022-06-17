import pyodbc
import os

def query_sql(query, option=0):
    """Permite a execução de queries no banco SQL Server,
        seguindo os padrões da documentação do pyodbc"""

    #Inicialização da variável db_query
    db_query = None

    #0 - INSERT/UPDATE/DELETE
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=192.168.0.112;'
                      'Database=;'
                      f"UID={os.environ.get('DB_User')};"
                      f"PWD={os.environ.get('DB_Pass')}", timeout = 5)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute((query))

    if option == 1:
        db_query = cursor.fetchone()
    elif option == 2:
        db_query = cursor.fetchall()

    cursor.close()
    conn.close()

    return db_query