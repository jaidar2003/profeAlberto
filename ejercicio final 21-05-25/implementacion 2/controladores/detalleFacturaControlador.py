from modelo.detalleFactura import DetalleFactura

class DetalleFacturaControlador:
    def __init__(self):
        self.detalles = []
    
    def crear_detalle(self, cantidad, producto):
        detalle = DetalleFactura(cantidad, producto)
        detalle._subtotal = producto._precio * cantidad
        self.detalles.append(detalle)
        return detalle
    
    def get_cantidad(self, detalle):
        return detalle._cantidad
    
    def get_producto(self, detalle):
        return detalle._producto
    
    def get_subtotal(self, detalle):
        return detalle._subtotal
    
    def formato_str(self, detalle, producto_controlador):
        producto_str = producto_controlador.formato_str(detalle._producto)
        return f"{producto_str} x {detalle._cantidad} = ${detalle._subtotal:.2f}"
    
    def formato_repr(self, detalle):
        return f"Detalle: [producto: {detalle._producto}, cantidad: {detalle._cantidad}, subtotal: {detalle._subtotal}]"