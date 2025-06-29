from modelo.ciudad import Ciudad

class ControladorCiudad:
    def __init__(self):
        self.ciudades = []

    def recaudacion_total(self):
        return sum(self.impuestos.values())

    def tiene_deficit(self):
        return self.poblacion > 100_000 and self.gasto_mantenimiento > self.recaudacion_total()

    def pais(self):
        if self.provincia:
            return self.provincia.pais
        return None

    def __str__(self):
        provincia_info = f", Provincia: {self.provincia.nombre}" if self.provincia else ", Sin provincia"
        return f"{self.nombre} (Población: {self.poblacion}, Recaudación: {self.recaudacion_total()}, Gasto: {self.gasto_mantenimiento}, Déficit: {'Sí' if self.tiene_deficit() else 'No'}{provincia_info})"

