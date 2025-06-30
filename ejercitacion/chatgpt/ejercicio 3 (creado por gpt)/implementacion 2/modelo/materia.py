class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.profesores = []

    def agregar_profesor(self, profesor):
        if profesor not in self.profesores:
            self.profesores.append(profesor)
            profesor.agregar_materia(self)

    def __str__(self):
        profes_str = ', '.join([p.nombre for p in self.profesores]) if self.profesores else "Ninguno"
        return f"Materia: {self.nombre}, Créditos: {self.creditos}, Profesores: {profes_str}"