from datetime import date
from cliente import Cliente
from lider import Lider
from producto import Producto
from representante import RepresentanteVenta
from ticket import TicketVenta
from vendedor import Vendedor
from reunion import ReunionGeneral

def main():
    # Crear productos
    producto1 = Producto("Producto A", 100)
    producto2 = Producto("Producto B", 200)

    # Crear cliente
    cliente1 = Cliente("Cliente 1", "Direccion 1", "123456789", date(1990, 1, 1), date(2023, 1, 1))

    # Crear representante de ventas
    representante = Vendedor("Vendedor 1", "Direccion Vendedor", "987654321", date(1985, 5, 5), "20-12345678-9", date(2023, 1, 1))

    # Registrar cliente y ventas
    representante.registrar_cliente(cliente1)
    representante.registrar_venta(producto1, cliente1, date(2023, 2, 1))
    representante.registrar_venta(producto2, cliente1, date(2023, 3, 1))

    # Calcular total de ventas desde una fecha
    total_ventas = representante.total_ventas_desde(date(2023, 1, 1))
    print(f"Total de ventas desde 2023-01-01: ${total_ventas}")

if __name__ == "__main__":
    main()