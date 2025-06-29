from modelo.avion import Avion

class ControladorAvion:
    def crear_avion(self, matricula, tipo, hangar):
        return Avion(matricula, tipo, hangar)

    def asignar_propietario(self, avion, propietario):
        avion.agregar_propietario(propietario)

    def asignar_servicio(self, avion, servicio):
        avion.agregar_servicio(servicio)