from representante import RepresentanteVenta

class Lider(RepresentanteVenta):
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento, cuit_cuil, fecha_ingreso, fecha_promocion):
        super().__init__(nombre, direccion, telefono, fecha_nacimiento, cuit_cuil, fecha_ingreso)
        self.fecha_promocion = fecha_promocion
        self.equipo_vendedores = []

