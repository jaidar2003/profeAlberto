class Factura:
    def __init__(self, fecha, tipo, total, administrativo, cliente):
        self._fecha = fecha
        self._tipo = tipo
        self._total = total
        self._detalles = []
        self._administativo = administrativo
        self._cliente = cliente