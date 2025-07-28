from controladores.representante_controller import RepresentanteController

class VendedorController(RepresentanteController):
    def total_ventas_desde(self, desde_fecha):
        total = 0
        for venta in self.representante.ventas:
            if venta.fecha >= desde_fecha:
                total += venta.precio
        return total
