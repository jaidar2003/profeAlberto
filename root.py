from persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, apellido, cargo="Administrativo"):
        super().__init__(nombre, apellido)
        self._cargo = cargo

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_cargo(self):
        return self._cargo

    def __str__(self):
        return f"{self._nombre} {self._apellido} ({self._cargo})"

    def __repr__(self):
        return f"Administrativo(nombre={self._nombre}, apellido={self._apellido}, cargo={self._cargo})"
from persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, apellido, estadoIVA):
        super().__init__(nombre, apellido)
        self._estadoIVA = estadoIVA

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def estadoIVA(self):
        return self._estadoIVA

    def __str__(self):
        return f"{self._nombre} {self._apellido} ({self._estadoIVA})"

    def __repr__(self):
        return f"Cliente: [nombre: {self._nombre}, apellido: {self._apellido}, estadoIVA: {self._estadoIVA}]"
class DetalleFactura():
    def __init__(self, cantidad, producto):
        self._cantidad = cantidad
        self._producto = producto
        self._subtotal = producto.precio * cantidad

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def subtotal(self):
        return self._subtotal

    @property
    def producto(self):
        return self._producto

    def __str__(self):
        return f"{self._producto} x {self._cantidad} = ${self._subtotal:.2f}"

    def __repr__(self):
        return f"Detalle: [producto: {self._producto}, cantidad: {self._cantidad}, subtotal: {self._subtotal}]"
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
from cliente import Cliente
from administrativo import Administrativo
from producto import Producto
from factura import Factura
from detalleFactura import DetalleFactura

if __name__ == "__main__":
    cliente = Cliente("Matias", "Buta", "No Inscripto")
    administrativo = Administrativo("Juan Manuel", "Aidar", "Gerente")

    producto1 = Producto("Leche", 100, 10)
    producto2 = Producto("Arroz", 50, 20)
    producto3 = Producto("Café", 200, 10)

    factura = Factura("15/05/2025",
                      "C",
                      850,
                      administrativo,
                      cliente
                      )

    detalle1 = DetalleFactura(5, producto1)
    detalle2 = DetalleFactura(3, producto2)
    detalle3 = DetalleFactura(1, producto3)

    factura.agregar_detalle(detalle1)
    factura.agregar_detalle(detalle2)
    factura.agregar_detalle(detalle3)

    cliente.agregar_factura(factura)
    administrativo.agregar_factura(factura)

    print(factura)
from abc import ABC


class Persona(ABC):
    def __init__(self, nombre, apellido):
        super().__init__()
        self._nombre = nombre
        self._apellido = apellido
        self._facturas = []

    @property
    def facturas(self):
        return self._facturas

    def agregar_factura(self, factura):
        self._facturas.append(factura)

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def __str__(self):
        return f"{self._nombre} (${self._precio:.2f})"

    def __repr__(self):
        return f"Producto: [nombre: {self._nombre}, precio: {self._precio}, cantidad: {self._cantidad}]"
