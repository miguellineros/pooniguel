from prettytable import PrettyTable
from datos.consultas import consulta_select
from datos.conexion import leer_datos
from modelos.localidad import Localidad


def obtener_datos_localidades():
    lista_localidades = []
    tabla_localidades = PrettyTable()
    tabla_localidades.field_names = ['N°', 'Nombre', 'Latitud', 'Longitud']

    campos = 'id_localidad,nombre_localidad,latitud,longitud'
    tabla = 'localidades'
    consulta = consulta_select(campos, tabla)
    
    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                localidad = Localidad(
                    data[0], data[1], data[2], data[3])  # type: ignore
                lista_localidades.append(localidad)

        if len(lista_localidades) > 0:
            for objeto in lista_localidades:
                tabla_localidades.add_row(
                    [objeto._id_localidad, objeto._nombre_localidad, objeto._latitud, objeto._longitud])
        print(tabla_localidades)