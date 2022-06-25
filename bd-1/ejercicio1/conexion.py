import mysql.connector

mcapdb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1705",
    database = "animales"
    )


mcapcursor = mcapdb.cursor()

# sql = "INSERT INTO FELINOS_001 (NOMBRE,ESPECIE,POBLACION, " + \
#         "LUGAR_ORIGEN,PESO_PROMEDIO,ESPERANZA_VIDA)" + \
#         "VALUES (%s, %s, %s, %s, %s, %s)"

# val = ("Gail","pantera",15000,"África",80,20)


# mcapcursor.execute(sql, val)

# mcapdb.commit()

