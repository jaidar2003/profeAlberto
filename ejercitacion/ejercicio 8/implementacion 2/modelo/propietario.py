from modelo.persona import Persona

class Propietario(Persona):
    def __init__(self, nss, nombre, direccion, telefono, fecha_adquisicion):
        super().__init__(nss, nombre, direccion, telefono)
        self.fecha_adquisicion = fecha_adquisicion
