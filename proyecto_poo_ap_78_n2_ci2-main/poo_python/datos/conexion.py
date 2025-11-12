import mysql.connector

#connect to server
conexion = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="aerolinea",
)

#get a cursor
cur = conexion.cursor()

#execute a query
cur.execute("SELECT CURDATE()")

#fetch one result
row = cur.fetchone()
print(f"fecha actual:{row}")

#close connection
conexion.close()