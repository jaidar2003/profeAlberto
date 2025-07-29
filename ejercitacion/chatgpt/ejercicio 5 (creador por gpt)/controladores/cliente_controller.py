from modelos.cliente import Cliente

class ClienteController:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def obtener_clientes(self):
        return self.clientes

    def buscar_cliente_por_dni(self, dni: int):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def eliminar_cliente(self, dni: int):
        cliente = self.buscar_cliente_por_dni(dni)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False