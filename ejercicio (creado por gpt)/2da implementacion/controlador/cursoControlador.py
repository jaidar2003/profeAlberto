from modelo.curso import Curso

class ControladorCurso:
    def crear_curso(self, codigo, nombre, profesor):
        return Curso(codigo, nombre, profesor)

    def agregar_inscripcion(self, curso, inscripcion):
        curso.inscriptos.append(inscripcion)

    def representar(self, curso):
        return f"Curso: {curso.nombre} (Código: {curso.codigo}), Profesor: {curso.profesor.nombre} {curso.profesor.apellido}"
