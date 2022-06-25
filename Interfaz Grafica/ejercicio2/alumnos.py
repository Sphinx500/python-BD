import mysql.connector

class CrudAlumnos:

    def connect(self):
        conexion = mysql.connector.connect(host="localhost",
        user="root",
        passwd="1705",
        database="alumnosdb")
        return conexion


    def registro(self,datos):
        cone = self.connect()
        cursor = cone.cursor()
        sql = "insert into alumnos(nombre, carrera, promedio) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "select nombre,carrera,promedio from alumnos where id=%s"
        cursor.execute(sql, datos)
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def consulta_todos(self):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "select * from alumnos"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def eliminar_alumno(self, datos):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "delete from alumnos where id=%s"
        cursor.execute(sql, datos)
        conn.commit()
        num_del = cursor.rowcount
        cursor.close()
        return num_del 

    def actualizar_alumno(self, datos):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "update alumnos set nombre=%s, carrera=%s, promedio=%s where id=%s"
        cursor.execute(sql, datos)
        conn.commit()
        mod = cursor.rowcount
        conn.close()
        return mod 