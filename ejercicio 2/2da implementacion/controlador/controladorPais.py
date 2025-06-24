from modelo.pais import Pais

class ControladorPais:
    def __init__(self):
        self.paises = []

    def crear_pais(self, nombre: str, capital, continente):
        pais = Pais(nombre, capital, continente)
        self.paises.append(pais)
        return pais

    def agregar_provincia(self, pais, provincia):
        pais.provincia.append(provincia)

    def agregar_pais_limitrofe(self, pais, pais_vecino):
        pais.paises_vecinos.append(pais_vecino)

    def listar_paises(self):
        return self.paises
