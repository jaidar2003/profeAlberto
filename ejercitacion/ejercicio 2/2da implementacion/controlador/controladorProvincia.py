from modelo.provincia import Provincia

class ControladorProvincia:
    def __init__(self):
        self.provincias = []

    def crear_provincia(self, nombre: str, capital):
        provincia = Provincia(nombre, capital)
        self.provincias.append(provincia)
        return provincia

    def agregar_ciudad(self, provincia, ciudad):
        provincia.ciudad.append(ciudad)

    def agregar_provincia_limitrofe(self, provincia, otra):
        provincia.provincias_limitrofes.append(otra)

    def agregar_pais_limitrofe(self, provincia, pais):
        provincia.paises_limitrofes.append(pais)

    def listar_provincias(self):
        return self.provincias
