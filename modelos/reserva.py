from modelos.pasajero import Pasajero
from modelos.asiento import Asiento


class Reserva(Pasajero, Asiento):
    def __init__(self, id_reserva, id_pasajero, id_asiento):
        Pasajero().__init__(id_pasajero)  # type: ignore
        Asiento().__init__(id_asiento)  # type: ignore
        self._id_reserva = id_reserva
