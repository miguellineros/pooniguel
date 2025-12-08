from modelos.aerolinea import Aerolinea


class Avion(Aerolinea):
    def __init__(self, id_avion=0, cod_avion='', tipo_avion=0, capacidad_avion=0, id_aerolinea=0):
        super().__init__(id_aerolinea)  # type: ignore
        self._id_avion = id_avion
        self._cod_avion = cod_avion
        self._tipo_avion = tipo_avion
        self._capacidad_avion = capacidad_avion

    def obtener_info_avion(self):
        return f'{self._cod_avion} {self._tipo_avion} {self._capacidad_avion}'
