from Pais import Pais

class Provincia:
    def __init__(self, nombre, capital):
        # Atributos simples
        self.nombre = nombre
        self.capital = capital

        # Relaciones
        self.ciudades = []
        self.provinciasLimitrofes = []
        self.paisesLimitrofes = []

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)

    def agregar_provincia_limitrofe(self, provincia):
        self.provinciasLimitrofes.append(provincia)

    def agregar_pais_limitrofe(self, pais):
        self.paisesLimitrofes.append(pais)
