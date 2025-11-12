class Pasajero:
    def __init__(self, id_pasajero, nombre_pasajero, num_pasaporte, fecha_nacimiento):
        self._id_pasajero = id_pasajero
        self._nombre_pasajero = nombre_pasajero
        self._num_pasaporte = num_pasaporte
        self._fecha_nacimiento = fecha_nacimiento

    def obtener_nombre_pasajero(self):
        return self._nombre_pasajero

    def obtener_pasaporte_pasajero(self):
        return self._num_pasaporte
