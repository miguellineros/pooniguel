def consulta_select(campos, tabla):
    if campos != "" and tabla != "":
        consulta = f"SELECT {campos} FROM {tabla}"
        return consulta


def consulta_nombre_aerolinea(campos, tabla):
    if campos != "" and tabla != "":
        consulta = f"SELECT {campos} FROM {tabla} WHERE nombre_aerolinea LIKE CONCAT('%', %s, '%')"
        return consulta


def consulta_select_id(campos, tabla, campo):
    if campos != "" and tabla != "" and campo != "":
        consulta = f"SELECT {campos} FROM {tabla} WHERE {campo}=%s"
        return consulta


def consulta_insert(campos, tabla):
    if campos != "" and tabla != "":
        consulta = f"INSERT INTO {tabla} ({campos}) VALUES ("
        lista_campos = campos.split(",")
        for _ in range(len(lista_campos)):
            consulta = consulta + "%s,"
        consulta = consulta[:-1]
        consulta = consulta + ")"
        return consulta

def aerolinea_update():
    consulta = f"""
        UPDATE aerolineas SET 
        nombre_aerolinea=%s,
        web_aerolinea=%s
        WHERE id_aerolinea=%s"""
    return consulta

def aerolinea_delete():
    consulta = f"""
        DELETE FROM aerolineas
        WHERE id_aerolinea=%s"""
    return consulta

def pasajero_update():
    consulta = f"""
        UPDATE pasajeros SET 
        nombre_pasajero=%s,
        num_pasaporte=%s,
        fecha_nacimiento=%s 
        WHERE id_pasajero=%s"""
    return consulta

def pasajero_delete():
    consulta = f"""
        DELETE FROM pasajeros
        WHERE id_pasajero=%s"""
    return consulta

def avion_update():
    consulta = """
        UPDATE aviones SET 
        cod_avion=%s,
        tipo_avion=%s,
        capacidad_avion=%s,
        id_aerolinea=%s
        WHERE id_avion=%s"""
    return consulta

def avion_delete():
    consulta = """
        DELETE FROM aviones
        WHERE id_avion=%s"""
    return consulta

def consulta_reservas_general():
    consulta = """
        SELECT r.id_reserva, p.nombre_pasajero, p.num_pasaporte, a.num_asiento, v.cod_vuelo 
        FROM reservas r 
        JOIN pasajeros p ON r.id_pasajero = p.id_pasajero 
        JOIN asientos a ON r.id_asiento = a.id_asiento
        JOIN vuelos v ON a.id_vuelo = v.id_vuelo
        ORDER BY r.id_reserva
    """
    return consulta

def reserva_delete():
    consulta = "DELETE FROM reservas WHERE id_reserva=%s"
    return consulta

def vuelo_update():
    consulta = """
        UPDATE vuelos SET 
        fecha_hora_salida=%s,
        destino=%s,
        origen=%s,
        cod_vuelo=%s,
        id_avion=%s,
        tipo_vuelo=%s
        WHERE id_vuelo=%s"""
    return consulta

def vuelo_delete():
    consulta = "DELETE FROM vuelos WHERE id_vuelo=%s"
    return consulta


def localidad_update():
    consulta = """
        UPDATE localidades SET 
        nombre_localidad=%s,
        latitud=%s,
        longitud=%s
        WHERE id_localidad=%s"""
    return consulta

def localidad_delete():
    consulta = "DELETE FROM localidades WHERE id_localidad=%s"
    return consulta


def consulta_select_asientos_vuelo():
    consulta = """
        SELECT a.id_asiento, v.cod_vuelo, a.num_asiento, a.categoria 
        FROM asientos a
        JOIN vuelos v ON a.id_vuelo = v.id_vuelo
        ORDER BY v.cod_vuelo, a.num_asiento
    """
    return consulta

def asiento_update():
    consulta = """
        UPDATE asientos SET 
        num_asiento=%s,
        categoria=%s,
        id_vuelo=%s
        WHERE id_asiento=%s"""
    return consulta
def asiento_delete():
    consulta = "DELETE FROM asientos WHERE id_asiento=%s"
    return consulta