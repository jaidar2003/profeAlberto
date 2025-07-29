# Ciudad.py
class Ciudad:
    def __init__(self, nombre, poblacion, impuestos, gasto):
        self.nombre = nombre
        self.poblacion = poblacion
        self.impuestos = impuestos
        self.gasto = gasto
        self.pais = None
        self.provincias = None

    def ingresos_totales(self):
        return sum(self.impuestos)

    def tiene_deficit(self):
        return self.gasto > self.ingresos_totales()

    def es_grande(self):
        return self.poblacion > 100_000