from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, legajo):
        super().__init__(nombre, apellido)
        self._legajo = legajo

    @property
    def legajo(self):
        return self._legajo

    def __str__(self):
        return f"{self._nombre} {self._apellido} (Legajo: {self._legajo})"
