import mysql.connector

class CrudPersonas:

    def connect(self):
        conexion = mysql.connector.connect(host="localhost",
        user="root",
        passwd="1705",
        database="personasdb")
        return conexion


    def registro(self,datos):
        cone = self.connect()
        cursor = cone.cursor()
        sql = "insert into personas(nombre, edad, correo, telefono) values (%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "select nombre,edad,correo,telefono from personas where id=%s"
        cursor.execute(sql, datos)
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def consulta_todos(self):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "select * from personas"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def eliminar_persona(self, datos):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "delete from personas where id=%s"
        cursor.execute(sql, datos)
        conn.commit()
        num_del = cursor.rowcount
        cursor.close()
        return num_del 

    def actualizar_persona(self, datos):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "update personas set nombre=%s, edad=%s, correo=%s, telefono=%s where id=%s"
        cursor.execute(sql, datos)
        conn.commit()
        mod = cursor.rowcount
        conn.close()
        return mod 