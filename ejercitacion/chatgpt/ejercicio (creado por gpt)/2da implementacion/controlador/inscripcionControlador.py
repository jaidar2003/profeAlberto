from modelo.inscripcion import Inscripcion

class ControladorInscripcion:
    def crear_inscripcion(self, alumno, curso, fecha):
        inscripcion = Inscripcion(alumno, curso, fecha)
        curso.inscriptos.append(inscripcion)
        return inscripcion

    def representar(self, inscripcion):
        return f"Inscripción: Alumno: {inscripcion.alumno.nombre} {inscripcion.alumno.apellido}, Curso: {inscripcion.curso.nombre}, Fecha: {inscripcion.fecha}"
