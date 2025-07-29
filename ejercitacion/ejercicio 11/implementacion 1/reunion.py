class ReunionGeneral:
    def __init__(self, fecha_ultima, fecha_proxima, porcentaje_comision):
        self.fecha_ultima = fecha_ultima
        self.fecha_proxima = fecha_proxima
        self.porcentaje_comision = porcentaje_comision

    def calcular_comision(self, representante):
        total = representante.total_ventas_desde(self.fecha_ultima)
        comision = total * self.porcentaje_comision
        if isinstance(representante, Lider):
            total_equipo = representante.total_equipo_ventas_desde(self.fecha_ultima)
            comision += total_equipo * self.porcentaje_comision
        return comision