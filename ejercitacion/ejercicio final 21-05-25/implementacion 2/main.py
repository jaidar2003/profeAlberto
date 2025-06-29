from controladores.administrativoControlador import AdministrativoControlador
from controladores.clienteControlador import ClienteControlador
from controladores.productoControlador import ProductoControlador
from controladores.facturaControlador import FacturaControlador
from controladores.detalleFacturaControlador import DetalleFacturaControlador
from controladores.personaControlador import PersonaControlador

def main():

    ctrl_persona = PersonaControlador()
    ctrl_admin = AdministrativoControlador()
    ctrl_cliente = ClienteControlador()
    ctrl_producto = ProductoControlador()
    ctrl_factura = FacturaControlador()
    ctrl_detalle = DetalleFacturaControlador()
    

    cliente = ctrl_cliente.crear_cliente("Matias", "Buta", "No Inscripto")
    administrativo = ctrl_admin.crear_administrativo("Juan Manuel", "Aidar", "Gerente")
    
    producto1 = ctrl_producto.crear_producto("Leche", 100, 10)
    producto2 = ctrl_producto.crear_producto("Arroz", 50, 20)
    producto3 = ctrl_producto.crear_producto("Café", 200, 10)
    

    factura = ctrl_factura.crear_factura("15/05/2025", "C", 0, administrativo, cliente)
    

    detalle1 = ctrl_detalle.crear_detalle(5, producto1)
    detalle2 = ctrl_detalle.crear_detalle(3, producto2)
    detalle3 = ctrl_detalle.crear_detalle(1, producto3)
    
    ctrl_factura.agregar_detalle(factura, detalle1)
    ctrl_factura.agregar_detalle(factura, detalle2)
    ctrl_factura.agregar_detalle(factura, detalle3)
    

    ctrl_cliente.agregar_factura(cliente, factura)
    ctrl_admin.agregar_factura(administrativo, factura)

    print(ctrl_factura.formato_str(factura, ctrl_cliente, ctrl_admin, ctrl_detalle, ctrl_producto))
    

    print(f"\nFacturas del cliente {ctrl_cliente.formato_str(cliente)}: {len(ctrl_persona.get_facturas(cliente))}")
    print(f"Facturas del administrativo {ctrl_admin.formato_str(administrativo)}: {len(ctrl_persona.get_facturas(administrativo))}")

if __name__ == "__main__":
    main()