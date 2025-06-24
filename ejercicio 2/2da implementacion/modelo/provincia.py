class Provincia:
    def __init__(self, nombre: str, capital):
        self.nombre = nombre
        self.capital = capital
        self.ciudad = []
        self.provincias_limitrofes = []
        self.paises_limitrofes = []
