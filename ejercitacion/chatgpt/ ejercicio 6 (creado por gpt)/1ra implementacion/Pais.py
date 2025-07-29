class Pais:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudades = []
        self.provincias = []

    def agregarCiudad(self, ciudad):
        self.ciudades.append(ciudad)
        ciudad.pais = self
