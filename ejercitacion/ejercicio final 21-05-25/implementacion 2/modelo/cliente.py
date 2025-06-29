from modelo.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, estadoIVA):
        super().__init__(nombre, apellido)
        self._estadoIVA = estadoIVA