from prettytable import PrettyTable
from datos.consultas import consulta_insert, consulta_select_asientos_vuelo, asiento_update, asiento_delete, consulta_select_id
from datos.conexion import leer_datos, leer_dato_individual, insertar_datos
from negocio.negocio_vuelos import obtener_datos_vuelos

def obtener_datos_asientos():
    tabla = PrettyTable()
    tabla.field_names =['ID Asiento','Vuelo','Asiento','Categoría']
    
    consulta=consulta_select_asientos_vuelo()
    resultado=leer_datos(consulta)
    
    if resultado:
        for row in resultado:
            cat_str ="Económica" if row[3] == 1 else "Business" if row[3] == 2 else "Primera"
            tabla.add_row([row[0],row[1],row[2],cat_str])
        print(tabla)
    else:
        print("No hay asientos registrados.")

def crear_asiento():
    print("\n--- Agregar Asiento a un Vuelo ---")
    obtener_datos_vuelos()
    id_vuelo =input('ID del Vuelo: ')
    
    num_asiento= input('Número de Asiento (ej: 1A, 12B): ')
    cat = input('Categoría [1] Económica | [2] Business | [3] Primera: ')
    
    if id_vuelo.isdigit() and num_asiento and cat in ['1','2','3']:
        campos='id_vuelo,num_asiento,categoria'
        tabla='asientos'
        datos=(int(id_vuelo),num_asiento.upper(),int(cat))
        
        insertar_datos(consulta_insert(campos,tabla), datos,'crear')
        print("Asiento agregado al vuelo.")
    else:
        print("Datos inválidos")

def modificar_asiento():
    obtener_datos_asientos()
    id_asiento=input('ID Asiento a modificar: ')
    
    if id_asiento:
        consulta=consulta_select_id('id_asiento,id_vuelo,num_asiento,categoria','asientos','id_asiento')
        data=leer_dato_individual(consulta, id_asiento)
        if data:
            print(f"Asiento {data[2]} del vuelo ID {data[1]}")
            n_num=input(f"Nuevo N° (Enter para {data[2]}): ")
            n_cat=input(f"Nueva Cat [1/2/3] (Enter para {data[3]}): ")
            
            num_fin=n_num.upper() if n_num else data[2]
            cat_fin=int(n_cat) if n_cat else data[3]
        
            insertar_datos(asiento_update(), (num_fin, cat_fin, data[1], id_asiento))
            print("Asiento modificado.")

def eliminar_asiento():
    obtener_datos_asientos()
    id_asiento=input('ID Asiento a eliminar: ')
    if id_asiento:
        if input("¿Eliminar?(s/n): ").lower() == 's':
            insertar_datos(asiento_delete(),(id_asiento,))
            print("Asiento eliminado")