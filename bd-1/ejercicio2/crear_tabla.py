from conexion import *

def tabla():
    try:
    #Se crea la query para crear la tabla
        sql = "CREATE TABLE CLIENTS (CLIENT_ID INT unsigned NOT NULL AUTO_INCREMENT, NAME VARCHAR(50), LAST_NAME VARCHAR(70),"+\
        "ADDRESS VARCHAR(70), FOLIO_ID VARCHAR(20), AMOUNT NUMERIC(10,2), START_DATE DATE, PRIMARY KEY (CLIENT_ID));"
        mcapcursor.execute(sql)
        print("La tabla fue creada con exito")
    except:
        print("La tabla ya existe")