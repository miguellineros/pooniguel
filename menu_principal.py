from interfaces.opciones_menu import opciones_menu, opciones_sub_menu,menu_asientos
from negocio.negocio_aerolineas import obtener_datos_aerolineas,crear_aerolinea,modificar_aerolinea,eliminar_aerolinea
from negocio.negocio_aviones import obtener_datos_aviones
from negocio.negocio_pasajeros import obtener_datos_pasajeros, crear_pasajero,modificar_pasajero


def menu_principal():
    print('Sistema de Gestión de Aerolínea')
    print('===============================')
    while True:
        opciones_menu()
        opcion = input('Seleccione su opción [0-7]: ')
        if opcion == '1':
            while True:
                opciones_sub_menu('Aerolínea')
                opcion_aerolinea = input('Seleccione su opción [0-4]: ')
                if opcion_aerolinea == '1':
                    obtener_datos_aerolineas()
                elif opcion_aerolinea == '2':
                    crear_aerolinea()
                elif opcion_aerolinea == '3':
                    modificar_aerolinea()
                elif opcion_aerolinea == '4':
                    eliminar_aerolinea()
                elif opcion_aerolinea == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '2':
            while True:
                menu_asientos()
                opcion_asiento = input('Seleccione su opción [0-4]: ')
                if opcion_asiento == '1':
                    pass
                elif opcion_asiento == '2':
                    pass
                elif opcion_asiento == '3':
                    pass
                elif opcion_asiento == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '3':
            while True:
                opciones_sub_menu('Avión')
                opcion_avion = input('Seleccione su opción [0-4]: ')
                if opcion_avion == '1':
                    obtener_datos_aviones()
                elif opcion_avion == '2':
                    pass
                elif opcion_avion == '3':
                    pass
                elif opcion_avion == '4':
                    pass
                elif opcion_avion == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '4':
            while True:
                opciones_sub_menu('Localidad')
                opcion_localidad = input('Seleccione su opción [0-4]: ')
                if opcion_localidad == '1':
                    pass
                elif opcion_localidad == '2':
                    pass
                elif opcion_localidad == '3':
                    pass
                elif opcion_localidad == '4':
                    pass
                elif opcion_localidad == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '5':
            while True:
                opciones_sub_menu('Pasajero')
                opcion_pasajero = input('Seleccione su opción [0-4]: ')
                if opcion_pasajero == '1':
                    obtener_datos_pasajeros()
                elif opcion_pasajero == '2':
                    crear_pasajero()
                elif opcion_pasajero == '3':
                    modificar_pasajero()
                elif opcion_pasajero == '4':
                    pass
                elif opcion_pasajero == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '6':
            while True:
                opciones_sub_menu('Reserva')
                opcion_reserva = input('Seleccione su opción [0-4]: ')
                if opcion_reserva == '1':
                    pass
                elif opcion_reserva == '2':
                    pass
                elif opcion_reserva == '3':
                    pass
                elif opcion_reserva == '4':
                    pass
                elif opcion_reserva == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '7':
            while True:
                opciones_sub_menu('Vuelo')
                opcion_vuelo = input('Seleccione su opción [0-4]: ')
                if opcion_vuelo == '1':
                    pass
                elif opcion_vuelo == '2':
                    pass
                elif opcion_vuelo == '3':
                    pass
                elif opcion_vuelo == '4':
                    pass
                elif opcion_vuelo == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '0':
            print('Saliendo de sistema...')
            break
        else:
            print('Opción incorrecta, intente nuevamente...')
