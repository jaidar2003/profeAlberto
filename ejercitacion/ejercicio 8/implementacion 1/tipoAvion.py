class TipoAvion:
    def __init__(self, modelo, capacidad, peso):
        self.modelo = modelo
        self.capacidad = capacidad
        self.peso = peso

    def crear_tipo_avion(self, modelo, capacidad, peso):
        return TipoAvion(modelo, capacidad, peso)