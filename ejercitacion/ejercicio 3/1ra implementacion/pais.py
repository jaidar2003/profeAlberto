from provincia import Provincia

class Pais:
    def __init__(self, nombre):
        self.nombre = nombre
        self.provincias = []

    def agregar_provincia(self, provincia):
        self.provincias.append(provincia)
        provincia.pais = self  # Establecer la referencia al padre

    def ciudades_con_deficit(self):
        ciudades = []
        for provincia in self.provincias:
            ciudades.extend(provincia.ciudades_con_deficit())
        return ciudades

    def provincias_con_mayoria_en_deficit(self):
        return [p for p in self.provincias if p.tiene_mayoria_en_deficit()]

    def __str__(self):
        return f"{self.nombre}: {len(self.ciudades_con_deficit())} ciudades en déficit, {len(self.provincias_con_mayoria_en_deficit())} provincias con mayoría en déficit."
