from representante import RepresentanteVenta
class Lider(RepresentanteVenta):
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento, cuit_cuil, fecha_ingreso, fecha_promocion):
        super().__init__(nombre, direccion, telefono, fecha_nacimiento, cuit_cuil, fecha_ingreso)
        self.fecha_promocion = fecha_promocion
        self.equipo_vendedores = []

    def agregar_vendedor(self, vendedor):
        self.equipo_vendedores.append(vendedor)

    def total_equipo_ventas_desde(self, desde_fecha):
        total = 0
        for vendedor in self.equipo_vendedores:
            total += vendedor.total_ventas_desde(desde_fecha)
        return total