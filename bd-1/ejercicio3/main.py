"""
Se generará un archivo de texto con los datos que se insertaron en la tabla en el ejercicio 2.
- Crear un proceso que pregunte al usuario si desea generar el archivo con todos los registros de la tabla o quiere generarlo con un único registro.
- Si es un único registro, deberá solicitar al usuario un número de folio para buscar en la tabla (FOLIO_ID).
En caso de que el folio no exista, mostrar un mensaje en pantalla que diga que no existe y generar archivo sólo con la cabecera.
Si quiere todos los registros entonces no se le pedirá el folio.

- El archivo deberá tener el siguiente layout (con cabecera):
'00000000000000000001'
- El nombre del archivo será CLIENTES_IVA.txt

"""

from crear_acrhivo import crear
from generar import generar

print("Validar la creacion del archivo")

creacion = crear()
print("--------------------------")
print("Inserción de datos en txt")

nuevo = generar()