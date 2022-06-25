import mysql.connector


class CrudProductos:

    # Clase que realiza la conexión a la Base de Datos
    def abrir(self):
        conexion = mysql.connector.connect(host="localhost",
                                           user="root",
                                           passwd="Curso123",
                                           database="articulosDB")
        return conexion

    # Funcion para el alta de productos
    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)  # Inserta los datos en una tabla
        cone.commit()
        cone.close()

    # Funcion para obtener un producto específico
    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        data = cursor.fetchall()  # Retorna los datos en una lista
        cone.close()
        return data

    # Funcion para obtner todos los productos
    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        data = cursor.fetchall()  # Retorna todos los datos de la tabla
        cone.close()
        return data

    # Funcion para eliminar un producto
    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        num_del = cursor.rowcount
        cone.close()
        return num_del  # retorna la cantidad de filas borradas

    # Funcion para actualizar un producto
    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        num_mod = cursor.rowcount
        cone.close()
        return num_mod  # retorna la cantidad de filas modificadas
