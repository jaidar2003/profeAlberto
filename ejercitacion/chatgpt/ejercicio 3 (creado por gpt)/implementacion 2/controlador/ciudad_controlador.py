from modelo.ciudad import Ciudad

class CiudadControlador:
    def agregar_universidad(self, universidad):
        if universidad not in self.universidades:
            self.universidades.append(universidad)

    def __str__(self):
        return f"Ciudad: {self.nombre}, Universidades: {', '.join([u.nombre for u in self.universidades])}"