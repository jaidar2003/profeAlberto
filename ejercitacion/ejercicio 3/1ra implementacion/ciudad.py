class Ciudad:
    def __init__(self, nombre, poblacion, impuestos, gasto_mantenimiento):
        self.nombre = nombre
        self.poblacion = poblacion
        self.impuestos = impuestos  # Diccionario con imp1..imp5
        self.gasto_mantenimiento = gasto_mantenimiento
        self.provincia = None  # Referencia a la provincia padre

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
