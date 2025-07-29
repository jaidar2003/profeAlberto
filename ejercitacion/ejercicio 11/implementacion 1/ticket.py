class TicketVenta:
    def __init__(self, fecha, producto, precio):
        self.fecha = fecha
        self.producto = producto
        self.precio = precio
        self.cliente = None  # se completa después

    def asignar_cliente(self, cliente):
        self.cliente = cliente