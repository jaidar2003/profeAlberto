from modelo.Provincia import Provincia

class cProvincia:
    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)

    def ciudades_grandes(self):
        return [c for c in self.ciudades if c.es_grande()]

    def ciudades_grandes_en_deficit(self):
        return [c for c in self.ciudades_grandes() if c.tiene_deficit()]

    def mas_de_mitad_grandes_en_deficit(self):
        grandes = self.ciudades_grandes()
        if not grandes:
            return False
        return len(self.ciudades_grandes_en_deficit()) > len(grandes) / 2