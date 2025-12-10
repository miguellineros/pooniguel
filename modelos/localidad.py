class Localidad:
    def __init__(self, id_localidad=None, nombre_localidad=None, latitud=None, longitud=None):
        self._id_localidad = id_localidad
        self._nombre_localidad = nombre_localidad
        self._latitud = latitud
        self._longitud = longitud

    def obtener_info_localidad(self):
        return f'{self._nombre_localidad} {self._latitud} {self._longitud}'
