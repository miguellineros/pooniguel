import mysql.connector
from mysql.connector import errorcode


def generar_conexion():
    config = {
        'host': "localhost",
        'port': 3306,
        'user': "root",
        'password': "",
        'database': "aerolinea",
        'use_pure': True
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion and conexion.is_connected():
            return conexion
        else:
            print("No fue posible conectarse a la base de datos.")

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado, usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print(error)
    else:
        conexion.close()


def leer_datos(consulta):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        else:
            print("Su búsqueda no arrojó resultados...")
        conexion.close()

def leer_dato_individual(consulta,dato):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            cursor.execute(consulta,(dato,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        else:
            print("Su búsqueda no arrojó resultados...")
        conexion.close()


def insertar_datos(consulta,datos,proceso=''):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            cursor.execute(consulta,datos)
            conexion.commit()
            cursor.close()
            if proceso == 'crear':
                id = cursor.lastrowid
                print(f"Id registro insertado = {id}")
        else:
            print("Su búsqueda no arrojó resultados...")
        conexion.close()