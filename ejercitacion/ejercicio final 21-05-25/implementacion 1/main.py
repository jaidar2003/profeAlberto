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