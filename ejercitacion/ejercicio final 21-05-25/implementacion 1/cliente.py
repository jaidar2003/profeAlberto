from persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, apellido, estadoIVA):
        super().__init__(nombre, apellido)
        self._estadoIVA = estadoIVA

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def estadoIVA(self):
        return self._estadoIVA

    def __str__(self):
        return f"{self._nombre} {self._apellido} ({self._estadoIVA})"

    def __repr__(self):
        return f"Cliente: [nombre: {self._nombre}, apellido: {self._apellido}, estadoIVA: {self._estadoIVA}]"
