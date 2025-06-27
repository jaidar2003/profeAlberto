from abc import ABC, abstractmethod

# Subject (Interfaz)
@abstractmethod
class Impresora(ABC):
    def imprimir(self, documento: str) -> None:
        pass
