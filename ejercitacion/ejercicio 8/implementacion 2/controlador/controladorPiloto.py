from modelo.piloto import Piloto

class ControladorPiloto:
    def crear_piloto(self, nss, nombre, direccion, telefono, licencia, restricciones):
        return Piloto(nss, nombre, direccion, telefono, licencia, restricciones)

    def autorizar_tipo(self, piloto, tipo_avion):
        piloto.tipos_autorizados.append(tipo_avion)