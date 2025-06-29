from persona import Persona

class Mecanico(Persona):
    def __init__(self, nss, nombre, direccion, telefono, salario, turno):
        super().__init__(nss, nombre, direccion, telefono)
        self.salario = salario
        self.turno = turno
        self.tipos_autorizados = []  # Lista de TipoAvion

    def crear_mecanico(self, nss, nombre, direccion, telefono, salario, turno):
        return Mecanico(nss, nombre, direccion, telefono, salario, turno)

    def autorizar_tipo(self, mecanico, tipo_avion):
        mecanico.tipos_autorizados.append(tipo_avion)