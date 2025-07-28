from modelos.ticket_venta import TicketVenta

class RepresentanteController:
    def __init__(self, representante):
        self.representante = representante

    def registrar_cliente(self, cliente):
        self.representante.cartera_clientes.append(cliente)

    def registrar_venta(self, producto, cliente, fecha):
        ticket = TicketVenta(fecha, producto, producto.precio)
        ticket.asignar_cliente(cliente)
        self.representante.ventas.append(ticket)
