class Hangar:
    def __init__(self, numero, capacidad, ubicacion):
        self.numero = numero
        self.capacidad = capacidad
        self.ubicacion = ubicacion

    def crear_hangar(self, numero, capacidad, ubicacion):
        return Hangar(numero, capacidad, ubicacion)

