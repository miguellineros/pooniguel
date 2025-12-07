from modelos.localidad import Localidad
from modelos.avion import Avion


class Vuelo(Localidad, Avion):
    def __init__(self, id_vuelo, fecha_hora_salida, destino, origen, cod_vuelo, id_avion, tipo_vuelo, id_localidad):
        Localidad().__init__(id_localidad)  # type: ignore
        Avion().__init__(id_avion)  # type: ignore
        self._id_vuelo = id_vuelo
        self._fecha_hora_salida = fecha_hora_salida
        self._destino = destino
        self._origen = origen
        self._cod_vuelo = cod_vuelo
        self._tipo_vuelo = tipo_vuelo
