from prettytable import PrettyTable
from datos.consultas import consulta_select, consulta_select_id, consulta_insert, localidad_update, localidad_delete
from datos.conexion import leer_datos, leer_dato_individual, insertar_datos
from modelos.localidad import Localidad

def obtener_datos_localidades():
    lista_localidades = []
    tabla_localidades = PrettyTable()
    tabla_localidades.field_names = ['ID', 'Nombre', 'Latitud', 'Longitud']

    campos='id_localidad,nombre_localidad,latitud,longitud'
    tabla='localidades'
    consulta=consulta_select(campos, tabla)
    
    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                localidad = Localidad(data[0], data[1], data[2], data[3])
                lista_localidades.append(localidad)

        if len(lista_localidades) > 0:
            for objeto in lista_localidades:
                tabla_localidades.add_row(
                    [objeto._id_localidad, objeto._nombre_localidad, objeto._latitud, objeto._longitud])
        print(tabla_localidades)

def crear_localidad():
    print("Registrar Nueva Localidad ")
    nombre= input('Nombre Ciudad-Localidad:').title()
    lat=input('Latitud: ')
    lon=input('Longitud: ')
    
    if nombre !='':
        campos='nombre_localidad,latitud,longitud'
        tabla='localidades'
        try:
            lat_f=float(lat) if lat else 0.0
            lon_f=float(lon) if lon else 0.0
            
            datos=(nombre, lat_f, lon_f)
            consulta = consulta_insert(campos, tabla)
            insertar_datos(consulta, datos, 'crear')
            print("Localidad creada.")
        except ValueError:
            print("Error:Latitud y Longitud deben ser numeros.")

def modificar_localidad():
    obtener_datos_localidades()
    id_loc =input('Ingrese ID de Localidad a editar: ')
    
    if id_loc != '':
        campos= 'id_localidad,nombre_localidad,latitud,longitud'
        tabla ='localidades'
        consulta=consulta_select_id(campos, tabla, 'id_localidad')
        if consulta:
            data=leer_dato_individual(consulta, id_loc)
            if data:
                print(f"Editando: {data[1]}")
                n_nom =input(f'Nuevo Nombre (Enter para {data[1]}): ')
                n_lat=input(f'Nueva Latitud (Enter para {data[2]}): ')
                n_lon=input(f'Nueva Longitud (Enter para {data[3]}): ')
                
                nom_fin =n_nom.title() if n_nom else data[1]
                lat_fin=float(n_lat) if n_lat else data[2]
                lon_fin=float(n_lon) if n_lon else data[3]
                
                datos = (nom_fin, lat_fin, lon_fin, id_loc)
                insertar_datos(localidad_update(), datos)
                print("Localidad actualizada.")

def eliminar_localidad():
    obtener_datos_localidades()
    id_loc = input('Ingrese ID de Localidad a eliminar: ')
    if id_loc != '':
        if input("¿Seguro? (s/n): ").lower() == 's':
            insertar_datos(localidad_delete(),(id_loc,))
            print("Localidad eliminada.")