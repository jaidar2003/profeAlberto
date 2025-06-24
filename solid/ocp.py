"""
Open/Closed Principle (OCP)

"Una clase debe de estar abierta a la extensión, pero cerrada a la modificación."

Significa: una clase debe de poder ser extendida sin necesidad de modificar su código original.
"""

print("❌ Violación de OCP: modificando la clase para agregar nuevas funcionalidades")
class CalculadoraDescuento:
    def calcular_descuento(self, tipo_cliente):
        if tipo_cliente == "regular":
            return 0.1
        elif tipo_cliente == "vip":
            return 0.2
        else:
            return 0


print("✅ Cumple con OCP: extendiendo la clase sin modificarla")
class EstrategiaDescuento:
    def calcular(self):
        return 0

class DescuentoRegular(EstrategiaDescuento):
    def calcular(self):
        return 0.

class DescuentoVIP(EstrategiaDescuento):
    def calcular(self):
        return 0.2

def aplicar_descuento(estrategia: EstrategiaDescuento):
    return estrategia.calcular()