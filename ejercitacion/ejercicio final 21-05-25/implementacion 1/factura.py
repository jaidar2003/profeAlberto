class Factura():
    def __init__(self, fecha, tipo, total, administrativo, cliente):
        self._fecha = fecha
        self._tipo = tipo
        self._total = total
        self._detalles = []
        self._administativo = administrativo
        self._cliente = cliente

    @property
    def fecha(self):
        return self._fecha

    @property
    def tipo(self):
        return self._tipo

    @property
    def total(self):
        return self._total

    @property
    def detalles(self):
        return self._detalles

    @property
    def administrativo(self):
        return self._administativo

    @property
    def cliente(self):
        return self._cliente

    def agregar_detalle(self, detalle):
        self._detalles.append(detalle)

    def __str__(self):
        # Crear una cadena para los detalles con formato
        detalles_str = "\n".join([f"    {detalle}" for detalle in self._detalles])

        return f"""
=== FACTURA TIPO {self._tipo} ===
Fecha: {self._fecha}
Cliente: {self._cliente}
Administrativo: {self._administativo}

DETALLES:
{detalles_str}

TOTAL: ${self._total:.2f}
"""

    def __repr__(self):
        return f"Factura: [fecha: {self._fecha}, tipo: {self._tipo}, total: {self._total}, administrativo: {self._administativo}, cliente: {self._cliente}, detalles: {self._detalles}]"
