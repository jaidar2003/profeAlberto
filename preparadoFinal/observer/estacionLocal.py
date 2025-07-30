# estacion_local.py
from estacionabstracta import EstacionMeteorologica

class EstacionLocal(EstacionMeteorologica):
    def __init__(self):
        self.observadores = []

    def registrar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self):
        for obs in self.observadores:
            obs.actualizar(25, 60, 1013)

    def cambiar_datos(self, temperatura, humedad, presion):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion
        self.notificar_observadores()