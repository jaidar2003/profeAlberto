class DetalleFactura:
    def __init__(self, cantidad, producto):
        self._cantidad = cantidad
        self._producto = producto
        self._subtotal = 0