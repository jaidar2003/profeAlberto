from modelo.mecanico import Mecanico

class ControladorMecanico:
    def crear_mecanico(self, nss, nombre, direccion, telefono, salario, turno):
        return Mecanico(nss, nombre, direccion, telefono, salario, turno)

    def autorizar_tipo(self, mecanico, tipo_avion):
        mecanico.tipos_autorizados.append(tipo_avion)