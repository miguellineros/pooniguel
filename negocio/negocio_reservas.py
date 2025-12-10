from prettytable import PrettyTable
from datos.consultas import consulta_insert, reserva_delete, consulta_reservas_general, consulta_select_id
from datos.conexion import leer_datos, insertar_datos, leer_dato_individual
from negocio.negocio_pasajeros import obtener_datos_pasajeros

def obtener_datos_reservas():
    tabla_reservas=PrettyTable()
    tabla_reservas.field_names = ['ID Reserva','Pasajero','Pasaporte','Asiento','Vuelo']
    
    consulta=consulta_reservas_general()
    resultado=leer_datos(consulta)
    
    if resultado:
        for data in resultado:
            tabla_reservas.add_row([data[0], data[1], data[2], data[3], data[4]])
        print(tabla_reservas)
    else:
        print("No hay reservas registradas")

def crear_reserva():
    print("\Crear nueva reserva ")
   
    print("Lista de Pasajeros ")
    obtener_datos_pasajeros()
    id_pasajero=input('Ingrese el ID del Pasajero: ')
    id_asiento = input('Ingrese el ID del Asiento a reservar: ')
    
    if id_pasajero.isdigit() and id_asiento.isdigit():
        if _verificar_existencia('pasajeros','id_pasajero',id_pasajero) and \
           _verificar_existencia('asientos','id_asiento', id_asiento):
            
            campos='id_pasajero,id_asiento'
            tabla='reservas'
            datos=(id_pasajero, id_asiento)
            
            consulta=consulta_insert(campos, tabla)
            insertar_datos(consulta, datos, 'crear')
            print("Reserva creada exitosamente")
        else:
            print("Error:El Pasajero o el asiento no existen")
    else:
        print("Error:Los id deben ser números.")

def eliminar_reserva():
    obtener_datos_reservas()
    id_reserva=input('Ingrese el ID de la Reserva a cancelar: ')
    
    if id_reserva != '':
        if _verificar_existencia('reservas','id_reserva',id_reserva):
            consulta=reserva_delete()
            insertar_datos(consulta, (id_reserva,))
            print("reserva sacada exitosamente")
        else:
            print("ID de reserva no encontrado.")
            

def _verificar_existencia(tabla, campo_id, valor_id):
    campos=f"{campo_id}"
    consulta=consulta_select_id(campos, tabla, campo_id)
    resultado=leer_dato_individual(consulta, valor_id)
    return resultado is not None