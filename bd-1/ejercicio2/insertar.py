
from conexion import *

def insertar():
    try:
        sql = "INSERT INTO CLIENTS (NAME, LAST_NAME, " + \
            "ADDRESS, FOLIO_ID, AMOUNT, START_DATE)" + \
        "VALUES (%s, %s, %s, %s, %s, %s)"

        archivo = "ejercicio2/NUEVOS_CLIENTES.txt"
        with open(archivo, "r") as f:
            val =  [tuple(map(str, i.split(';'))) for i in f]
            print(val)
            mcapcursor.executemany(sql,val)
            mcapdb.commit()
            print(mcapcursor.rowcount,"Se insertaron los registros")
        #print("Los datos fueron insertados")      
    except FileNotFoundError:
            return('¡El fichero ' + archivo + ' no existe!\n')
    except ValueError as error:
        print(error)

    finally:
        f.close()



