from modelo.persona import Persona

class Piloto(Persona):
    def __init__(self, nss, nombre, direccion, telefono, licencia, restricciones):
        super().__init__(nss, nombre, direccion, telefono)
        self.licencia = licencia
        self.restricciones = restricciones
        self.tipos_autorizados = []  # Lista de TipoAvion
