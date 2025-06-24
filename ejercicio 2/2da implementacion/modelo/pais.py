class Pais:
    def __init__(self, nombre: str, capital: str, continente: str):
        self.nombre = nombre
        self.capital = capital
        self.continente = continente
        self.provincia = []
        self.paises_vecinos = []

        continente.pais.append(self)