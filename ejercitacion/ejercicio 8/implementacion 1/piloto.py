from persona import Persona

class Piloto(Persona):
    def __init__(self, nss, nombre, direccion, telefono, licencia, restricciones):
        super().__init__(nss, nombre, direccion, telefono)
        self.licencia = licencia
        self.restricciones = restricciones
        self.tipos_autorizados = []  # Lista de TipoAvion


    def crear_piloto(self, nss, nombre, direccion, telefono, licencia, restricciones):
        return Piloto(nss, nombre, direccion, telefono, licencia, restricciones)

    def autorizar_tipo(self, piloto, tipo_avion):
        piloto.tipos_autorizados.append(tipo_avion)
