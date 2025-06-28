from modelo.persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, apellido, cargo="Administrativo"):
        super().__init__(nombre, apellido)
        self._cargo = cargo