from impresora import Impresora

# Real Subject (Implementación Real)
class Realimpresora(Impresora):
    def __init__(self, nombre):
        self.nombre = nombre

    def imprimir(self, documento):
        print(f"Impresora {self.nombre} imprimiendo: {documento}")