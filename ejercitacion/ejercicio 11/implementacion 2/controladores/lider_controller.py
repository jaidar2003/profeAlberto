class LiderController:
    def agregar_vendedor(self, vendedor):
        self.equipo_vendedores.append(vendedor)

    def total_equipo_ventas_desde(self, desde_fecha):
        total = 0
        for vendedor in self.equipo_vendedores:
            total += vendedor.total_ventas_desde(desde_fecha)
        return total



