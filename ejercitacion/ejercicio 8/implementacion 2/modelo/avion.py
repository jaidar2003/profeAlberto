class Avion:
    def __init__(self, matricula, tipo, hangar):
        self.matricula = matricula
        self.tipo = tipo          # TipoAvion
        self.hangar = hangar      # Hangar
        self.propietarios = []    # Lista de Propietario
        self.servicios = []       # Lista de Servicio

    def agregar_propietario(self, propietario):
        self.propietarios.append(propietario)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
