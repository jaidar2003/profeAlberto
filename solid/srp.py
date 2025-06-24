"""
Single Responsibility Principle (SRP)

"Una clase debe de tener un unico motivo de cambio, es decir, una unica responsabilidad."

Significa: una clase debe de encargarse de una sola tarea.
"""


print("❌ Violación de SRP: hace muchas cosas")
class Reporte:
    def generar(self, datos):
        # Genera un reporte
        print(f"Generando reporte con datos: {datos}")

    def guardar(self, archivo):
        # Guarda el reporte en un archivo
        print(f"Guardando reporte en {archivo}")

    def enviar(self, archivo):
        # Envía el reporte por correo electrónico
        print(f"Enviando reporte {archivo} por correo electrónico")


print("✅ Cumple con SRP: cada clase tiene una sola responsabilidad")
class ReporteGenerador:
    def generar(self, datos):
        return f"Generando reporte con datos: {datos}"

class ReporteGuardador:
    def guardar(self, reporte, archivo):
        print(f"Guardando reporte en {archivo}")

class ReporteEnviador:
    def enviar(self, archivo):
        print(f"Enviando reporte {archivo} por correo electrónico")

def generar_reporte(datos):
    generador = ReporteGenerador()
    return generador.generar(datos)

