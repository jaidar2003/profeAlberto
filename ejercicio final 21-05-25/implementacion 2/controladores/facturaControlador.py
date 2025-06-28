from modelo.factura import Factura

class FacturaControlador:
    def __init__(self):
        self.facturas = []
    
    def crear_factura(self, fecha, tipo, total, administrativo, cliente):
        factura = Factura(fecha, tipo, total, administrativo, cliente)
        self.facturas.append(factura)
        return factura
    
    def get_fecha(self, factura):
        return factura._fecha
    
    def get_tipo(self, factura):
        return factura._tipo
    
    def get_total(self, factura):
        return factura._total
    
    def get_administrativo(self, factura):
        return factura._administativo
    
    def get_cliente(self, factura):
        return factura._cliente
    
    def get_detalles(self, factura):
        return factura._detalles
    
    def agregar_detalle(self, factura, detalle):
        factura._detalles.append(detalle)
        # Update the total of the invoice
        factura._total += detalle._subtotal
    
    def calcular_total(self, factura):
        total = 0
        for detalle in factura._detalles:
            total += detalle._subtotal
        return total
    
    def formato_str(self, factura, cliente_controlador, administrativo_controlador, detalle_controlador, producto_controlador):
        cliente_str = cliente_controlador.formato_str(factura._cliente)
        admin_str = administrativo_controlador.formato_str(factura._administativo)
        
        # Create a string for the details with formatting
        detalles_str = "\n".join([f"    {detalle_controlador.formato_str(detalle, producto_controlador)}" for detalle in factura._detalles])
        
        return f"""
=== FACTURA TIPO {factura._tipo} ===
Fecha: {factura._fecha}
Cliente: {cliente_str}
Administrativo: {admin_str}

DETALLES:
{detalles_str}

TOTAL: ${factura._total:.2f}
"""
    
    def formato_repr(self, factura):
        return f"Factura: [fecha: {factura._fecha}, tipo: {factura._tipo}, total: {factura._total}, administrativo: {factura._administativo}, cliente: {factura._cliente}, detalles: {factura._detalles}]"