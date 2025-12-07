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