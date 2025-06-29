from modelo.propietario import Propietario

class ControladorPropietario:
    def crear_propietario(self, nss, nombre, direccion, telefono, fecha_adquisicion):
        return Propietario(nss, nombre, direccion, telefono, fecha_adquisicion)