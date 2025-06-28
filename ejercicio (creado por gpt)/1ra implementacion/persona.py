class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido
