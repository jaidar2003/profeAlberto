"""
Interface Segregation Principle (ISP)

"Los clientes no deben verse obligados a depender de interfaces que no utilizan."

Significa: una clase no debe depender de métodos que no utiliza, las interfaces deben ser específicas y no generales.
"""

print("❌ Violación de ISP: una interfaz grande obliga a las clases a implementar métodos que no utilizan")
class Trabajador:
    def programar(self):
        pass

    def cocinar(self):
        pass

class Cocinero(Trabajador):
    def cocinar(self):
        print("Cocinando...")

    def programar(self):
        raise NotImplementedError("No programa")

print("✅ Cumple con ISP: interfaces específicas para cada tipo de trabajador")
class Programador:
    def programar(self):
        pass

class Cocinero:
    def cocinar(self):
        pass

class Juan(Programador):
    def programar(self):
        print("Juan está programando")

class Pedro(Cocinero):
    def cocinar(self):
        print("Pedro está cocinando")