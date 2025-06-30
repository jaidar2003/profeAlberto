from modelo.carrera import Carrera

class CarreraControlador:
    def agregar_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)

    def asignar_facultad(self, facultad):
        self.facultad = facultad

    def __str__(self):
        materias_str = ', '.join([m.nombre for m in self.materias]) if self.materias else "Ninguna"
        director_str = self.director.nombre if self.director else "No asignado"
        return f"Carrera: {self.nombre}, Director: {director_str}, Materias: {materias_str}"