from modelo.persona import Persona

class Mecanico(Persona):
    def __init__(self, nss, nombre, direccion, telefono, salario, turno):
        super().__init__(nss, nombre, direccion, telefono)
        self.salario = salario
        self.turno = turno
        self.tipos_autorizados = []  # Lista de TipoAvion
