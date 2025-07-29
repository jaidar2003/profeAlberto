from modelo.Ciudad import Ciudad

class cCiudad:
    def ingresos_totales(self):
        return sum(self.impuestos)

    def tiene_deficit(self):
        return self.gasto > self.ingresos_totales()

    def es_grande(self):
        return self.poblacion > 100_000
