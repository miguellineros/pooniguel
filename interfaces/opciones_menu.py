def opciones_menu():
    print()
    print('Menú Principal')
    print('==============')
    print('[1] Gestion Aerolíneas.')
    print('[2] Gestion Asientos.')
    print('[3] Gestion Aviones.')
    print('[4] Gestion Localidades.')
    print('[5] Gestion Pasajeros.')
    print('[6] Gestion Reservas.')
    print('[7] Gestion Vuelos.')
    print('[0] Salir.')


def opciones_sub_menu(tipo_menu):
    plural = tipo_menu
    singular = tipo_menu
    if tipo_menu == 'Avión':
        plural = 'Avione'
    elif tipo_menu == 'Localidad':
        plural = 'Localidade'

    print()
    print(f'Menú {plural}s')
    print('===============')
    print(f'[1] Listado {plural}s.')
    print(f'[2] Agregar {singular}.')
    print(f'[3] Modificar {singular}.')
    print(f'[4] Eliminar {singular}.')
    print(f'[0] Volver al menú principal.')


def menu_asientos():
    print()
    print('Menú Gestión de Asientos (Inventario)')
    print('=====================================')
    print('[1] Listado de Asientos.')
    print('[2] Crear/Agregar Asiento a Vuelo.')
    print('[3] Modificar Asiento.')
    print('[4] Eliminar Asiento.')
    print('[0] Volver al menú principal.')