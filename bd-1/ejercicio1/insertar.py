from conexion import *

class Felino():

    def __init__(self):
        self.nombre = input("Ingrese el nombre del felino: ")
        self.especie = input("Ingrese la especie del felino: ")
        self.poblacion = 0
        self.lugar_origen = ""
        self.peso_promedio = 0
        self.esperanza_vida = 0
    
    def validar(self):
        try:
            if self.especie == "gato":
                self.nombre = self.nombre
                self.especie = "gato"
                self.poblacion = 20000000
                self.lugar_origen = "Japón"
                self.peso_promedio = 4
                self.esperanza_vida = 15

                sql = "INSERT INTO FELINOS_001(nombre,especie,poblacion," +\
                    "lugar_origen,peso_promedio,esperanza_vida)" +\
                    "VALUES(%s, %s, %s, %s, %s, %s)"
                val = (self.nombre,self.especie,self.poblacion,self.lugar_origen,self.peso_promedio,self.esperanza_vida)

                try:
                    mcapcursor.execute(sql, val)
                    mcapdb.commit()
                    print(mcapcursor.rowcount, "Se inserto registro")
                except:
                    print("no se inserto el registro")



            elif self.especie == "leon":
                self.nombre = self.nombre
                self.especie = "leon"
                self.poblacion = 15000
                self.lugar_origen = "África"
                self.peso_promedio = 80
                self.esperanza_vida = 20
                
                
                sql = "INSERT INTO FELINOS_001(nombre,especie,poblacion," +\
                    "lugar_origen,peso_promedio,esperanza_vida)" +\
                    "VALUES(%s, %s, %s, %s, %s, %s)"
                val = (self.nombre,self.especie,self.poblacion,self.lugar_origen,self.peso_promedio,self.esperanza_vida)

                try:
                    mcapcursor.execute(sql, val)
                    mcapdb.commit()
                    print(mcapcursor.rowcount, "Se inserto registro")
                except:
                    print("no se inserto el registro")

            elif self.especie == "pantera":
                self.nombre = self.nombre
                self.especie = "pantera"
                self.poblacion = 10000
                self.lugar_origen = "Australia"
                self.peso_promedio = 50
                self.esperanza_vida = 10
                
                
                sql = "INSERT INTO FELINOS_001(nombre,especie,poblacion," +\
                    "lugar_origen,peso_promedio,esperanza_vida)" +\
                    "VALUES(%s, %s, %s, %s, %s, %s)"
                val = (self.nombre,self.especie,self.poblacion,self.lugar_origen,self.peso_promedio,self.esperanza_vida)

                try:
                    mcapcursor.execute(sql, val)
                    mcapdb.commit()
                    print(mcapcursor.rowcount, "Se inserto registro")
                except:
                    print("no se inserto el registro")

            elif self.especie == "jaguar":
                self.nombre = self.nombre
                self.especie = "jaguar"
                self.poblacion = 1500
                self.lugar_origen = "México"
                self.peso_promedio = 40
                self.esperanza_vida = 5

                
                sql = "INSERT INTO FELINOS_001(nombre,especie,poblacion," +\
                    "lugar_origen,peso_promedio,esperanza_vida)" +\
                    "VALUES(%s, %s, %s, %s, %s, %s)"
                val = (self.nombre,self.especie,self.poblacion,self.lugar_origen,self.peso_promedio,self.esperanza_vida)
                try:
                    mcapcursor.execute(sql, val)
                    mcapdb.commit()
                    print(mcapcursor.rowcount, "Se inserto registro")
                except:
                    print("no se inserto el registro")
        
        except:
            print("No hay datos disponibles de esa especie")

