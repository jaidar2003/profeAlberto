from modelo.pais import Pais
from controlador.controladorProvincia import ControladorProvincia

class ControladorPais:

    def __init__(self):
        self.paises = []

    def agregar_provincia(self, pais, provincia):
        pais.provincias.append(provincia)
        provincia.pais = pais

    def ciudades_con_deficit(self, pais):
        controlador_provincia = ControladorProvincia()
        ciudades = []
        for provincia in pais.provincias:
            ciudades.extend(controlador_provincia.ciudades_con_deficit(provincia))
        return ciudades

    def provincias_con_mayoria_en_deficit(self, pais):
        controlador_provincia = ControladorProvincia()
        return [p for p in pais.provincias if controlador_provincia.tiene_mayoria_en_deficit(p)]

    def formato_str(self, pais):
        return "{}: {} ciudades en déficit, {} provincias con mayoría en déficit.".format(
            pais.nombre,
            len(self.ciudades_con_deficit(pais)),
            len(self.provincias_con_mayoria_en_deficit(pais))
        )
