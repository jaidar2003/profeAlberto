class Vehiculo:
    def __init__(self, modelo, anio, precio: float, vendido: bool = False):
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.vendido = vendido