from prettytable import PrettyTable
from datos.consultas import consulta_select
from datos.conexion import leer_datos
from modelos.avion import Avion

def obtener_datos_aviones():
    lista_aviones = []
    tabla_aviones = PrettyTable()
    tabla_aviones.field_names = ['N°', 'Código', 'Tipo', 'Capacidad']
    
    campos = 'id_avion,cod_avion,tipo_avion,capacidad_avion'
    tabla = 'aviones'
    consulta = consulta_select(campos, tabla)
    
    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                avion = Avion(
                    data[0], data[1], data[2], data[3])  # type: ignore
                lista_aviones.append(avion)

        if len(lista_aviones) > 0:
            for objeto in lista_aviones:
                tipo = ''
                capacidad = ''
                if objeto._tipo_avion == 1:
                    tipo = 'Carga'
                    capacidad = f'{objeto._capacidad_avion} Ton'
                else:
                    tipo = 'Pasajeros'
                    capacidad = f'{objeto._capacidad_avion} Pasajeros'
                tabla_aviones.add_row(
                    [objeto._id_avion, objeto._cod_avion, tipo, capacidad])
        print(tabla_aviones)