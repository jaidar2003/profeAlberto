# Interfaz Observer
from abc import ABC, abstractmethod

class Pantalla(ABC):  # Clase abstracta = interfaz
    @abstractmethod
    def actualizar(self, temperatura, humedad, presion):
        raise Exception("Este método debe ser implementado por las subclases")