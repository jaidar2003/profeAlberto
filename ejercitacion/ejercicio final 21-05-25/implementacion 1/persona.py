from abc import ABC


class Persona(ABC):
    def __init__(self, nombre, apellido):
        super().__init__()
        self._nombre = nombre
        self._apellido = apellido
        self._facturas = []

    @property
    def facturas(self):
        return self._facturas

    def agregar_factura(self, factura):
        self._facturas.append(factura)