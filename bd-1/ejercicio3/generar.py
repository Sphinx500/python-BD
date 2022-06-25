from conexion import *
from datetime import datetime

def generar():
    try:
        archivo = "ejercicio3/CLIENTES_IVA.txt"
        r = input("Desea generar todos los registros o uno? uno/todos: ")
        if r == "uno":
            values = input("Ingrese el numero de folio a insertar: ")
            sql = "SELECT NAME,FOLIO_ID,AMOUNT,START_DATE FROM CLIENTS WHERE FOLIO_ID =" + str(values)
            mcapcursor.execute(sql)
            result = mcapcursor.fetchall()
            try: 
                f = open(archivo, 'a')
                encabezado = ("|NOMBRE             "+\
                            "|FOLIO             "+\
                            "|MONTO   |FECHA   \n")
                f.write(encabezado)
            except FileNotFoundError:
                print('¡El fichero ' + archivo + ' no existe!\n')
            else:

                for x in result:
                    fecha = datetime.strftime(x[3],'%d-%m-%Y')
                    linea =str(x[0] + "|        "+ str(x[1]).rjust(20) + "|     " + str(x[2]).rjust(4)+ "|  " + fecha + "\n")
                    f.write(linea)
                print(x)
                f.close()
                
                print('El registro se ha añadido.\n')

        elif r == "todos":
            try: 
                f = open(archivo, 'a')
                encabezado = ("|NOMBRE             "+\
                            "|FOLIO             "+\
                            "|MONTO   |FECHA   \n")
                f.write(encabezado)
            except FileNotFoundError:
                print('¡El fichero ' + archivo + ' no existe!\n')
            else:
                sql = "SELECT NAME,FOLIO_ID,AMOUNT,START_DATE FROM CLIENTS"
                mcapcursor.execute(sql)
                result = mcapcursor.fetchall()
                for x in result:
                    fecha = datetime.strftime(x[3],'%d-%m-%Y')
                    linea =str(x[0] + "|        "+ str(x[1]).rjust(20) + "|     " + str(x[2]).rjust(4)+ "|  " + fecha + "\n")
                    f.write(linea)
                print(x)
                f.close()
                print("Se han añadido los registros")

    except ValueError as error:
        print(error)