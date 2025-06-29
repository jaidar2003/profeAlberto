from persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, apellido, cargo="Administrativo"):
        super().__init__(nombre, apellido)
        self._cargo = cargo

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_cargo(self):
        return self._cargo

    def __str__(self):
        return f"{self._nombre} {self._apellido} ({self._cargo})"

    def __repr__(self):
        return f"Administrativo(nombre={self._nombre}, apellido={self._apellido}, cargo={self._cargo})"
