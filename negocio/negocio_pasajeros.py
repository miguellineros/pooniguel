from prettytable import PrettyTable
from datos.consultas import consulta_select, consulta_select_id, consulta_insert,pasajero_update
from datos.conexion import leer_datos, leer_dato_individual, insertar_datos
from modelos.pasajero import Pasajero
from datetime import datetime


def obtener_datos_pasajeros():
    lista_pasajeros = []
    tabla_pasajeros = PrettyTable()
    tabla_pasajeros.field_names = [
        'N°', 'Nombre', 'Pasaporte', 'Fecha Nacimiento']

    campos = 'id_pasajero,nombre_pasajero,num_pasaporte,fecha_nacimiento'
    tabla = 'pasajeros'
    consulta = consulta_select(campos, tabla)

    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                pasajero = Pasajero(
                    data[0], data[1], data[2], data[3])  # type: ignore
                lista_pasajeros.append(pasajero)

        if len(lista_pasajeros) > 0:
            for objeto in lista_pasajeros:
                tabla_pasajeros.add_row(
                    [objeto._id_pasajero, objeto._nombre_pasajero, objeto._num_pasaporte, objeto._fecha_nacimiento])
        print(tabla_pasajeros)


def crear_pasajero():
    campos = 'nombre_pasajero,num_pasaporte,fecha_nacimiento'
    tabla = 'pasajeros'
    nombre = input('Ingrese Nombre Pasajero: ')
    pasaporte = input('Ingrese Número Pasaporte: ')
    fecha_nacimiento = input('Ingrese Fecha Nacimiento (YYYY-MM-dd): ')
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    datos = (nombre.title(), pasaporte, fecha_nacimiento)
    consulta = consulta_insert(campos, tabla)
    insertar_datos(consulta, datos,'crear')


def modificar_pasajero():
    obtener_datos_pasajeros()
    
    nombre = input('Ingrese Nombre Pasajero a Editar: ')
    if nombre != '':
        campos = 'id_pasajero,nombre_pasajero,num_pasaporte,fecha_nacimiento'
        tabla = 'pasajeros'
        campo = 'nombre_pasajero'
        consulta = consulta_select_id(campos, tabla, campo)
        if consulta:
            pasajero = leer_dato_individual(consulta, nombre)
            if pasajero:
                nuevo_nombre = input(
                    'Ingrese Nombre Pasajero (o ENTER para conservar): ')
                nuevo_pasaporte = input(
                    'Ingrese Número Pasaporte (o ENTER para conservar): ')
                nueva_fecha_nacimiento = input(
                    'Ingrese Fecha Nacimiento (YYYY-MM-dd) (o ENTER para conservar): ')
                
                if nuevo_nombre == '':
                    nuevo_nombre = str(pasajero[1])  # type: ignore
                if nuevo_pasaporte == '':
                    nuevo_pasaporte = pasajero[2]  # type: ignore
                if nueva_fecha_nacimiento == '':
                    nueva_fecha_nacimiento = pasajero[3]  # type: ignore
                else:
                    nueva_fecha_nacimiento = datetime.strptime(
                    nueva_fecha_nacimiento, '%Y-%m-%d')
                datos = (nuevo_nombre.title(), nuevo_pasaporte,
                        nueva_fecha_nacimiento, pasajero[0])  # type: ignore
                consulta_update = pasajero_update()
                insertar_datos(consulta_update, datos)
                print(f'Pasajero {str(pasajero[1])} modificado existosamente!') # type: ignore
