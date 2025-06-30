from modelo.profesor import Profesor

class ControladorProfesor:
    def crear_profesor(self, nombre, apellido, legajo):
        return Profesor(nombre, apellido, legajo)

    def representar(self, profesor):
        return f"{profesor.nombre} {profesor.apellido} (Legajo: {profesor.legajo})"
