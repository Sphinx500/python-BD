import mysql.connector

mcapdb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1705",
    database = "ejemplo"
    )


mcapcursor = mcapdb.cursor()