from modelos.vuelo import Vuelo


class Asiento(Vuelo):
    def __init__(self, id_asiento, id_vuelo, categoria, num_asiento):
        Vuelo().__init__(id_vuelo)  # type: ignore
        self._id_asiento = id_asiento
        self._categoria = categoria
        self._num_asiento = num_asiento
