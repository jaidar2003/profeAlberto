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

    def crear_avion(self, matricula, tipo, hangar):
        return Avion(matricula, tipo, hangar)

    def asignar_propietario(self, avion, propietario):
        avion.agregar_propietario(propietario)

    def asignar_servicio(self, avion, servicio):
        avion.agregar_servicio(servicio)
