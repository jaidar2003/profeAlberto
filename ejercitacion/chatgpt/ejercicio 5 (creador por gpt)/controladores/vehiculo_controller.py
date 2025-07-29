from modelos.vehiculo import Vehiculo

class VehiculoController:
    def __init__(self):
        self.vehiculos = []

    def asignar_duenio(self, vehiculo: Vehiculo, duenio: str):
        vehiculo.duenio = duenio

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self):
        return self.vehiculos

    def buscar_vehiculo(self, modelo: str):
        for vehiculo in self.vehiculos:
            if vehiculo.modelo == modelo:
                return vehiculo
        return None

    def eliminar_vehiculo(self, modelo: str):
        vehiculo = self.buscar_vehiculo(modelo)
        if vehiculo:
            self.vehiculos.remove(vehiculo)
            return True
        return False
