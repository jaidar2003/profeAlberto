class RepresentanteVenta:
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento, cuit_cuil, fecha_ingreso):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.cuit_cuil = cuit_cuil
        self.fecha_ingreso = fecha_ingreso
        self.cartera_clientes = []
        self.ventas = []