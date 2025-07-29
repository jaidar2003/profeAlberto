from datetime import datetime

class Turno:
    def __init__(self, cliente, fecha: datetime, mecanico):
        self.cliente = cliente
        self.fecha = fecha
        self.mecanico = mecanico
