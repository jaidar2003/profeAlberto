class Provincia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudades = []
        self.pais = None  # Referencia al país padre