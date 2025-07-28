class Profesor:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.materias = []

    def agregar_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)

    def __str__(self):
        materias_str = ', '.join([m.nombre for m in self.materias]) if self.materias else "Ninguna"
        return f"Profesor: {self.nombre}, Legajo: {self.legajo}, Materias que dicta: {materias_str}"