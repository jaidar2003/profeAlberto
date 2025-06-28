from persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    def __str__(self):
        return f"{self._nombre} {self._apellido} (DNI: {self._dni})"
