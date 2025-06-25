from modelo.provincia import Provincia
from modelo.ciudad import Ciudad
from controlador.controladorCiudad import ControladorCiudad

class ControladorProvincia:
    def __init__(self):
        self.provincias = []

    def agregar_provincia(self, pais, provincia):
        pais.provincias.append(provincia)
        provincia.pais = pais

    def agregar_ciudad(self, provincia, ciudad):
        provincia.ciudades.append(ciudad)
        ciudad.provincia = provincia

    def ciudades_con_deficit(self, provincia):
        controlador_ciudad = ControladorCiudad()
        return [c for c in provincia.ciudades if controlador_ciudad.tiene_deficit(c)]

    def tiene_mayoria_en_deficit(self, provincia):
        controlador_ciudad = ControladorCiudad()
        ciudades_validas = [c for c in provincia.ciudades if c.poblacion > 100_000]
        if not ciudades_validas:
            return False
        ciudades_deficit = [c for c in ciudades_validas if controlador_ciudad.tiene_deficit(c)]
        return len(ciudades_deficit) > len(ciudades_validas) / 2
