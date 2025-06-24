from modelo.continente import Continente

class ControladorContinente:
    def __init__(self):
        self.continentes = []

    def crear_continente(self, nombre: str):
        continente = Continente(nombre)
        self.continentes.append(continente)
        return continente

    def listar_continentes(self):
        return self.continentes
