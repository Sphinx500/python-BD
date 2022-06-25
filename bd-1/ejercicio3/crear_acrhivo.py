def crear():
    import os
    archivo = "ejercicio3/CLIENTES_IVA.txt"
    if os.path.isfile(archivo):
        print("el fichero ya existe")
    f = open(archivo, 'w')
    f.close()
    return 'Se ha creado el fichero.\n'

