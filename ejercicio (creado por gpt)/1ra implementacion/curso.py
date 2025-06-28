class Curso:
    def __init__(self, codigo, nombre, profesor):
        self._codigo = codigo
        self._nombre = nombre
        self._profesor = profesor
        self._inscriptos = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def profesor(self):
        return self._profesor

    @property
    def inscriptos(self):
        return self._inscriptos

    def agregar_inscripcion(self, inscripcion):
        self._inscriptos.append(inscripcion)

    def __str__(self):
        return f"Curso: {self._nombre} (Código: {self._codigo}), Profesor: {self._profesor}"
