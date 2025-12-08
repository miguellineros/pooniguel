def solicitar_data_aerolinea(proceso=''):
    while True:
        mensaje_nombre = 'Ingrese Nombre Aerolínea (o ENTER para conservar): '
        mensaje_web = 'Ingrese Web Aerolínea (o ENTER para conservar): '
        if proceso != None:
            mensaje_nombre = 'Ingrese Nombre Aerolínea: '
            mensaje_web = 'Ingrese Web Aerolínea: '
        nombre = input(mensaje_nombre)
        web = input(mensaje_web)
        if nombre != '' and web != '':
            return nombre, web


def solicitar_data_eliminar_aerolinea():
    while True:
        nombre = input('Ingrese Nombre Aerolínea a Eliminar: ')
        if nombre != '':
            return nombre
