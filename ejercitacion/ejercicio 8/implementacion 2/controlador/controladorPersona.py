from modelo.persona import Persona

class ControladorPersona:
    def crear_persona(self, nss, nombre, direccion, telefono):
        return Persona(nss, nombre, direccion, telefono)