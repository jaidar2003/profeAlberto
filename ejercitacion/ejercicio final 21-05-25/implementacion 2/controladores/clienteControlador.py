from modelo.cliente import Cliente

class ClienteControlador:
    def __init__(self):
        self.clientes = []
    
    def crear_cliente(self, nombre, apellido, estadoIVA):
        cliente = Cliente(nombre, apellido, estadoIVA)
        self.clientes.append(cliente)
        return cliente
    
    def get_nombre(self, cliente):
        return cliente._nombre
    
    def get_apellido(self, cliente):
        return cliente._apellido
    
    def get_estadoIVA(self, cliente):
        return cliente._estadoIVA
    
    def agregar_factura(self, cliente, factura):
        cliente._facturas.append(factura)
    
    def formato_str(self, cliente):
        return f"{cliente._nombre} {cliente._apellido} ({cliente._estadoIVA})"
    
    def formato_repr(self, cliente):
        return f"Cliente: [nombre: {cliente._nombre}, apellido: {cliente._apellido}, estadoIVA: {cliente._estadoIVA}]"