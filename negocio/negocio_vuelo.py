from prettytable import PrettyTable
from datos.consultas import consulta_select, consulta_select_id, consulta_insert, vuelo_update, vuelo_delete
from datos.conexion import leer_datos, leer_dato_individual, insertar_datos
from modelos.vuelo import Vuelo
from datetime import datetime
from negocio.negocio_aviones import obtener_datos_aviones
from negocio.negocio_localidades import obtener_datos_localidades

def obtener_datos_vuelos():
    lista_vuelos=[]
    tabla_vuelos = PrettyTable()
    tabla_vuelos.field_names =['ID','Código','Salida','Origen','Destino','Avión','Tipo']
    
    campos ='id_vuelo,fecha_hora_salida,destino,origen,cod_vuelo,id_avion,tipo_vuelo'
    tabla ='vuelos'
    consulta = consulta_select(campos, tabla)
    
    if consulta:
        resultado=leer_datos(consulta)
        if resultado:
            for data in resultado:
                vuelo =Vuelo(data[0], data[1], data[2], data[3], data[4], data[5], data[6], 0)
                lista_vuelos.append(vuelo)

        if len(lista_vuelos)>0:
            for v in lista_vuelos:
                tipo_str ='Nacional' if v._tipo_vuelo == 1 else 'Internacional'
                tabla_vuelos.add_row([
                    v._id_vuelo, v._cod_vuelo, v._fecha_hora_salida, 
                    v._origen, v._destino, v._id_avion, tipo_str
                ])
        print(tabla_vuelos)

def crear_vuelo():
    print("\nProgramar Nuevo Vuelo")
    cod = input('Código de Vuelo:').upper()
    fecha_str=input('Fecha y Hora de Salida: ')
    print("\nLocalidades Disponibles")
    obtener_datos_localidades()
    origen=input('ID Origen:')
    destino=input('ID Destino: ')
    
    print("\n Aviones Disponibles")
    obtener_datos_aviones()
    id_avion=input('ID Avión:')
    
    tipo =input('Tipo de Vuelo [1] Nacional | [2] Internacional:')
    
    if cod and origen.isdigit() and destino.isdigit() and id_avion.isdigit():
        try:
            datetime.strptime(fecha_str, '%Y-%m-%d %H:%M') 
            campos='fecha_hora_salida,destino,origen,cod_vuelo,id_avion,tipo_vuelo'
            tabla='vuelos'
            datos=(fecha_str, int(destino),int(origen),cod,int(id_avion),int(tipo))
            consulta = consulta_insert(campos,tabla)
            insertar_datos(consulta,datos,'crear')
            print("Vuelo programado exitosamente")
        except ValueError:
            print("Error:Formato de fecha incorrecto.")
    else:
        print("Error:Datos faltantes o ID no numéricos.")

def modificar_vuelo():
    obtener_datos_vuelos()
    id_vuelo =input('Ingrese ID del Vuelo a modificar: ')
    
    if id_vuelo!= '':
        campos='id_vuelo,fecha_hora_salida,destino,origen,cod_vuelo,id_avion,tipo_vuelo'
        tabla ='vuelos'
        consulta=consulta_select_id(campos, tabla, 'id_vuelo')
        
        if consulta:
            data=leer_dato_individual(consulta, id_vuelo)
            if data:
                print(f"Editando Vuelo {data[4]}")
                nueva_fecha = input(f'Nueva Fecha (Enter para {data[1]}): ')
                nuevo_cod = input(f'Nuevo Código (Enter para {data[4]}): ')
                
                fecha_final=nueva_fecha if nueva_fecha else data[1]
                cod_final=nuevo_cod if nuevo_cod else data[4]
                 
                datos=(fecha_final,data[2],data[3],cod_final,data[5],data[6],id_vuelo)
                
                consulta_upd = vuelo_update()
                insertar_datos(consulta_upd, datos)
                print("Vuelo actualizado")

def eliminar_vuelo():
    obtener_datos_vuelos()
    id_vuelo=input('Ingrese ID del Vuelo a cancelar: ')
    
    if id_vuelo!='':
        campos='id_vuelo'
        tabla='vuelos'
        consulta=consulta_select_id(campos, tabla, 'id_vuelo')
        if consulta and leer_dato_individual(consulta, id_vuelo):
            confirmar= input("¿Seguro eliminar este vuelo? (s/n): ")
            if confirmar.lower() == 's':
                consulta_del = vuelo_delete()
                insertar_datos(consulta_del, (id_vuelo,))
                print("Vuelo eliminado.")
        else:
            print("Vuelo no encontrado.")