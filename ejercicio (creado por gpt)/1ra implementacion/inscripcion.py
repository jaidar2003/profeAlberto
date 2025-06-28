class Inscripcion:
    def __init__(self, alumno, curso, fecha):
        self._alumno = alumno
        self._curso = curso
        self._fecha = fecha
        # Add the inscription to the course
        curso.agregar_inscripcion(self)

    @property
    def alumno(self):
        return self._alumno

    @property
    def curso(self):
        return self._curso

    @property
    def fecha(self):
        return self._fecha

    def __str__(self):
        return f"Inscripción: Alumno: {self._alumno}, Curso: {self._curso.nombre}, Fecha: {self._fecha}"
