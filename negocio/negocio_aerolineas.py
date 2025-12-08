from prettytable import PrettyTable
from datos.consultas import consulta_nombre_aerolinea, aerolinea_delete, aerolinea_update, consulta_insert, consulta_select, consulta_select_id
from datos.conexion import insertar_datos, leer_dato_individual, leer_datos
from interfaces.interface_aerolinea import solicitar_data_aerolinea
from modelos.aerolinea import Aerolinea


def obtener_datos_aerolineas():
    lista_aerolineas = []
    tabla_aerolineas = PrettyTable()
    tabla_aerolineas.field_names = ['N°', 'Nombre', 'Web']

    campos = 'id_aerolinea,nombre_aerolinea,web_aerolinea'
    tabla = 'aerolineas'
    consulta = consulta_select(campos, tabla)

    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                aerolinea = Aerolinea(
                    data[0], data[1], data[2])  # type: ignore
                lista_aerolineas.append(aerolinea)
        if len(lista_aerolineas) > 0:
            for objeto in lista_aerolineas:
                tabla_aerolineas.add_row(
                    [objeto._id_aerolinea, objeto._nombre_aerolinea, objeto._web_aerolinea])
        print(tabla_aerolineas)


def crear_aerolinea():
    campos = 'nombre_aerolinea,web_aerolinea'
    tabla = 'aerolineas'
    nombre, web = solicitar_data_aerolinea('crear')  # type: ignore
    if nombre != '' and web != '':
        datos = (nombre.title(), web)
        consulta = consulta_insert(campos, tabla)
        insertar_datos(consulta, datos, 'crear')


def modificar_aerolinea():
    obtener_datos_aerolineas()

    nombre = input('Ingrese Nombre Aerolínea a Editar: ')
    if nombre != '':
        campos = 'id_aerolinea,nombre_aerolinea,web_aerolinea'
        tabla = 'aerolineas'
        consulta = consulta_nombre_aerolinea(campos, tabla)
        if consulta:
            aerolinea = leer_dato_individual(consulta, nombre)
            if aerolinea:
                nuevo_nombre, nueva_web = solicitar_data_aerolinea()  # type: ignore

                if nuevo_nombre == '':
                    nuevo_nombre = str(aerolinea[1])  # type: ignore
                if nueva_web == '':
                    nueva_web = aerolinea[2]  # type: ignore

                datos = (nuevo_nombre.title(), nueva_web,
                        aerolinea[0])  # type: ignore
                consulta_update = aerolinea_update()
                insertar_datos(consulta_update, datos)
                print(f'¡Aerolínea "{str(aerolinea[1])}" modificada existosamente!')  # type: ignore


def eliminar_aerolinea():
    obtener_datos_aerolineas()

    nombre = input('Ingrese Nombre Aerolínea a Eliminar: ')
    if nombre != '':
        campos = 'id_aerolinea,nombre_aerolinea,web_aerolinea'
        tabla = 'aerolineas'
        consulta = consulta_nombre_aerolinea(campos, tabla)
        if consulta:
            aerolinea = leer_dato_individual(consulta, nombre)
            if aerolinea:
                datos = (aerolinea[0],)  # type: ignore
                consulta_delete = aerolinea_delete()
                insertar_datos(consulta_delete, datos)
                print(f'¡Aerolínea "{str(aerolinea[1])}" eliminada existosamente!')# type: ignore
