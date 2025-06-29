from modelo.alumno import Alumno

class ControladorAlumno:
    def crear_alumno(self, nombre, apellido, dni):
        return Alumno(nombre, apellido, dni)

    def representar(self, alumno):
        return f"{alumno.nombre} {alumno.apellido} (DNI: {alumno.dni})"
