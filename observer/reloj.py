from Pantalla import Pantalla

# Observador concretos
class PantallaReloj(Pantalla):
    def actualizar(self, temperatura, humedad, presion):
        print(f"[SmartWatch] {temperatura}°C y {humedad}% humedad")