from datetime import date
from modelos.producto import Producto
from modelos.cliente import Cliente
from modelos.vendedor import Vendedor
from controladores.vendedor_controller import VendedorController

def main():
    # Crear productos y cliente
    producto1 = Producto("Producto A", 100)
    producto2 = Producto("Producto B", 200)
    cliente1 = Cliente("Cliente 1", "Direccion 1", "123456789", date(1990, 1, 1), date(2023, 1, 1))

    # Crear vendedor y controlador asociado
    vendedor_modelo = Vendedor("Vendedor 1", "Direccion Vendedor", "987654321", date(1985, 5, 5), "20-12345678-9", date(2023, 1, 1))
    vendedor_controller = VendedorController(vendedor_modelo)

    # Registrar cliente y ventas a través del controlador
    vendedor_controller.registrar_cliente(cliente1)
    vendedor_controller.registrar_venta(producto1, cliente1, date(2023, 2, 1))
    vendedor_controller.registrar_venta(producto2, cliente1, date(2023, 3, 1))

    # Calcular ventas desde fecha
    total_ventas = vendedor_controller.total_ventas_desde(date(2023, 1, 1))
    print(f"Total de ventas desde 2023-01-01: ${total_ventas}")

if __name__ == "__main__":
    main()
