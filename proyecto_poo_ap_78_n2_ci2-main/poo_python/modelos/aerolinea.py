# Definición de clase Aerolínea
class Aerolinea:
    # Constructor de la clase
    def __init__(self,id_aerolinea,nombre_aerolinea,web_aerolinea):
        # atributos privados
        self._id_aerolinea = id_aerolinea
        self._nombre_aerolinea = nombre_aerolinea
        self._web_aerolinea = web_aerolinea
    
    # Métodos públicos de acceso a un atributos privados
    def obtener_nombre_aerolinea(self):
        return self._nombre_aerolinea
    
    def obtener_web_aerolinea(self):
        return self._web_aerolinea