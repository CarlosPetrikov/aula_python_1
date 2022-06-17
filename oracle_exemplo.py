import cx_Oracle
import os

ora_user = os.environ.get('ORA_User')
ora_pass = os.environ.get('ORA_Pass')

def query_oracle(query,  option=0, service = ''): 
    """Permite a execução de queries no banco Oracle,
        seguindo os padrões da documentação do cx_Oracle"""
    
    #Inicialização da variável db
    db = []
    
    conn = cx_Oracle.connect(ora_user, ora_pass, service)
    
    cursor = conn.cursor()

    cursor.execute(query)
    
    for row in cursor:
        db.append(row)
        
    #Retornar None, caso não tenha nenhum valor no cursor
    if db == []:
        db = None
    #Caso a opção seja 1, retornar apenas o primeiro elemento da primeira linha
    elif option == 1:
        db = db[0][0]
    #opção  2, retornar apenas a primeira linha
    elif option == 2:
        db = db[0]

    cursor.close()
    conn.close()
    
    return db