# Clase Sujeto

class EstacionMeteorologica:
    def __init__(self):
        self.observadores = []
        self._temperatura = None
        self._humedad = None
        self._presion = None

    def registrar(self, observador):
        self.observadores.append(observador)

    def quitar(self, observador):
        self.observadores.remove(observador)

    def notificar(self):
        for obs in self.observadores:
            obs.actualizar(self._temperatura, self._humedad, self._presion)

    def cambiar_datos(self, temperatura, humedad, presion):
        print("\n🌡️ Cambiando datos meteorológicos...")
        self._temperatura = temperatura
        self._humedad = humedad
        self._presion = presion
        self.notificar()