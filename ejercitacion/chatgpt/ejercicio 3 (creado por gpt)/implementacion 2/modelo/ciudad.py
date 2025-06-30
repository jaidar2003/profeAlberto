class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.universidades = []

    def agregar_universidad(self, universidad):
        if universidad not in self.universidades:
            self.universidades.append(universidad)

    def __str__(self):
        return f"Ciudad: {self.nombre}, Universidades: {', '.join([u.nombre for u in self.universidades])}"
