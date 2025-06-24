"""
Dependency Inversion Principle (DIP)

"Las clases de alto nivel no deben de depender de clases de bajo nivel, deben de depender de abstracciones"

Significa: no debes acoplarte a implementaciones concretas, sino trabajar con interfaces o abstracciones
"""

print("❌ Violación de DIP")
class NotificadorEmail:
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")

class ServicioUsuario:
    def __init__(self):
        self.notificador = NotificadorEmail()  # Acoplamiento fuerte


print("✅ Cumple DIP")
class Notificador:
    def enviar(self, mensaje):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f"Email: {mensaje}")

class NotificadorSMS(Notificador):
    def enviar(self, mensaje):
        print(f"SMS: {mensaje}")

class ServicioUsuario:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def registrar(self):
        self.notificador.enviar("Bienvenido al sistema")
