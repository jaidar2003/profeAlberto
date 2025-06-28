from abc import ABC

class Persona(ABC):
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
        self._facturas = []