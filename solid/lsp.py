"""
Liskov Substitution Principle (LSP)

"Si una clase A reemplaza a una clase B(PADRE), entonces los objetos de la clase B deben poder ser reemplazados por objetos de la clase A sin alterar el comportamiento del programa.",

Significa: una clase hija debe poder ser utilizada en lugar de su clase padre sin alterar el comportamiento del programa.
"""

print("❌ Violación de LSP: la clase hija no cumple con el contrato de la clase padre")
class Pajaro:
    def volar(self):
        return "Volando"

class Aguila(Pajaro):
    def volar(self):
        return "El águila vuela alto"

class Pinguino(Pajaro):
    def volar(self):
        raise Exception("El pinguino no vuela")

print("✅ Cumple con LSP: la clase hija cumple con el contrato de la clase padre")
class Animal:
    pass

class Pajaro(Animal):
    def poner_huevo(self):
        print("Puso un huevo")

class Volador:
    def volar(self):
        pass

class Nadador:
    def nadar(self):
        pass

class Aguila(Pajaro, Volador):
    def volar(self):
        return "El águila vuela"

class Pinguino(Pajaro, Nadador):
    def nadar(self):
        return "El pingüino nada"
