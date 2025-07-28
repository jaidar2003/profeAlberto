# modelos/ticket_venta.py
class TicketVenta:
    def __init__(self, producto, cliente, fecha):
        self.producto = producto
        self.cliente = cliente
        self.fecha = fecha