"""
- Crear un proceso que cree la tabla que se describe en el ejemplo.
- Crear otro proceso que lea el archivo NUEVOS_CLIENTES.txt e inserte el contenido en la tabla creada.
El orden de los campos en el archivo es: NOMBRE, APELLIDO, DIRECCION, FOLIO, MONTO, FECHA.
- Mostrar un mensaje que diga que se insertaron los registros, deben insertarse todos en una sola ejecución.
- Mostrar que en la tabla sí se hayan insertado los registros

"""

from crear_tabla import tabla
from insertar import insertar

#CREAR LA TABLA
mi_tabla = tabla()

#INSERTAR LOS DATOS
datos = insertar()
