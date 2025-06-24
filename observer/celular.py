from Pantalla import Pantalla

# Observador concretos
class PantallaCelular(Pantalla):
    def actualizar(self, temperatura, humedad, presion):
        print(f"[Celular] Temp: {temperatura}°C, Humedad: {humedad}%, Presión: {presion} hPa")

