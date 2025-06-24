from Continente import Continente


class Pais:
    def __init__(self, nombre: str, capital: str, continente: Continente):
        # Atributos simples
        self.nombre = nombre
        self.capital = capital
        self.continente = continente

        # Relaciones
        self.provincias = []  # Lista de provincias asociadas al país
        self.paisesLimitrofes = []  # Lista de países limítrofes

        # Bidirecciónalmente, agregar el país a su continente
        continente.pais.append(self)

    def agregar_provincia(self, provincia):
        self.provincias.append(provincia)

    def agregar_pais_limitrofe(self, pais):
        self.paisesLimitrofes.append(pais)