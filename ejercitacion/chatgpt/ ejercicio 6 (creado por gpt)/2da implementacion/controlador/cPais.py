from modelo.Pais import Pais

class cPais:
    def agregarCiudad(self, ciudad):
        self.ciudades.append(ciudad)
        ciudad.pais = self

