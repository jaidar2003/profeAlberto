from ticket import TicketVenta

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

    def registrar_cliente(self, cliente):
        self.cartera_clientes.append(cliente)

    def registrar_venta(self, producto, cliente, fecha):
        ticket = TicketVenta(fecha, producto, producto.precio)
        ticket.asignar_cliente(cliente)
        self.ventas.append(ticket)

    def total_ventas_desde(self, desde_fecha):
        total = 0
        for venta in self.ventas:
            if venta.fecha >= desde_fecha:
                total += venta.precio
        return total