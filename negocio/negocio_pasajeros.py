from prettytable import PrettyTable
from datos.consultas import consulta_select, consulta_select_id, consulta_insert, pasajero_update, pasajero_delete
from datos.conexion import leer_datos, leer_dato_individual, insertar_datos
from modelos.pasajero import Pasajero
from datetime import datetime


def obtener_datos_pasajeros():
    lista_pasajeros =[]
    tabla_pasajeros= PrettyTable()
    tabla_pasajeros.field_names = [
        'N°', 'Nombre','Pasaporte','Fecha Nacimiento']

    campos='id_pasajero,nombre_pasajero,num_pasaporte,fecha_nacimiento'
    tabla='pasajeros'
    consulta=consulta_select(campos, tabla)

    if consulta:
        resultado=leer_datos(consulta)
        if resultado:
            for data in resultado:
                pasajero=Pasajero(
                    data[0],data[1],data[2], data[3])  
                lista_pasajeros.append(pasajero)

        if len(lista_pasajeros)>0:
            for objeto in lista_pasajeros:
                tabla_pasajeros.add_row(
                    [objeto._id_pasajero, objeto._nombre_pasajero, objeto._num_pasaporte, objeto._fecha_nacimiento])
        print(tabla_pasajeros)


def crear_pasajero():
    print("\n Registrar Nuevo pasajero")
    campos='nombre_pasajero,num_pasaporte,fecha_nacimiento'
    tabla='pasajeros'
    nombre=input('Ingrese Nombre Pasajero: ')
    pasaporte=input('Ingrese Número Pasaporte: ')
    fecha_nacimiento_str=input('Ingrese Fecha Nacimiento (YYYY-MM-DD): ')
    
    try:
        fecha_nacimiento=datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d')
        if nombre and pasaporte:
            datos=(nombre.title(),pasaporte,fecha_nacimiento)
            consulta=consulta_insert(campos, tabla)
            insertar_datos(consulta, datos,'crear')
            print("Pasajero registrado exitosamente!")
        else:
            print("Error:Nombre y Pasaporte son obligatorios.")
    except ValueError:
        print("Error: Formato de fecha incorrecto.Use AAAA-MM-DD.")


def modificar_pasajero():
    obtener_datos_pasajeros()
    
    nombre_busqueda = input('Ingrese Nombre exacto del Pasajero a Editar: ')
    if nombre_busqueda !='':
        campos ='id_pasajero,nombre_pasajero,num_pasaporte,fecha_nacimiento'
        tabla= 'pasajeros'
        campo_filtro='nombre_pasajero'
        
        consulta =consulta_select_id(campos,tabla,campo_filtro)
        
        if consulta:
            pasajero_data=leer_dato_individual(consulta, nombre_busqueda)
            if pasajero_data:
                print(f"Editando a:{pasajero_data[1]}")
                nuevo_nombre =input('Nuevo Nombre (ENTER para conservar): ')
                nuevo_pasaporte=input('Nuevo Pasaporte (ENTER para conservar): ')
                nueva_fecha =input('Nueva Fecha (YYYY-MM-DD) (ENTER para conservar): ')
                
                nombre_final=nuevo_nombre.title() if nuevo_nombre else pasajero_data[1]
                pasaporte_final=nuevo_pasaporte if nuevo_pasaporte else pasajero_data[2]
                
                fecha_final=pasajero_data[3]
                if nueva_fecha:
                     try:
                        fecha_final=datetime.strptime(nueva_fecha, '%Y-%m-%d')
                     except ValueError:
                        print("Fecha inválida, se conservará la anterior.")

                datos=(nombre_final,pasaporte_final,fecha_final, pasajero_data[0])
                consulta_upd=pasajero_update()
                insertar_datos(consulta_upd,datos)
                print(f'Pasajero "{nombre_final}"modificado exitosamente!')
            else:
                print("Pasajero no encontrado.")

def eliminar_pasajero():
    obtener_datos_pasajeros()
    
    id_pasajero = input('Ingrese el N°(id) del Pasajero a eliminar: ')
    
    if id_pasajero!='':
        campos ='id_pasajero,nombre_pasajero'
        tabla='pasajeros'
        campo_filtro='id_pasajero'
        
        consulta =consulta_select_id(campos,tabla,campo_filtro)
        if consulta:
            pasajero_data =leer_dato_individual(consulta, id_pasajero)
            if pasajero_data:
                confirmacion=input(f"¿Seguro desea eliminar al pasajero {pasajero_data[1]}? (s/n): ")
                if confirmacion.lower() =='s':
                    consulta_del =pasajero_delete()
                    insertar_datos(consulta_del, (id_pasajero,))
                    print("Pasajero eliminado correctamente!")
            else:
                 print("ID no encontrado.")