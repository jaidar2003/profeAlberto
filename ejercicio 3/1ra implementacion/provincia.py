from ciudad import Ciudad

class Provincia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudades = []
        self.pais = None  # Referencia al país padre

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)
        ciudad.provincia = self  # Establecer la referencia al padre

    def ciudades_con_deficit(self):
        return [c for c in self.ciudades if c.tiene_deficit()]

    def tiene_mayoria_en_deficit(self):
        ciudades_validas = [c for c in self.ciudades if c.poblacion > 100_000]
        if not ciudades_validas:
            return False
        return len(self.ciudades_con_deficit()) > len(ciudades_validas) / 2

    def __str__(self):
        pais_info = f", País: {self.pais.nombre}" if self.pais else ", Sin país"
        return f"{self.nombre} (Mayoría con déficit: {self.tiene_mayoria_en_deficit()}{pais_info})"
