class ReunionController:
    def calcular_comision(self, representante):
        total = representante.total_ventas_desde(self.fecha_ultima)
        comision = total * self.porcentaje_comision
        if isinstance(representante, Lider):
            total_equipo = representante.total_equipo_ventas_desde(self.fecha_ultima)
            comision += total_equipo * self.porcentaje_comision
        return comision