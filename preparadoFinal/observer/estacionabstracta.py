# estacionmeteorologica.py
from abc import ABC, abstractmethod

class EstacionMeteorologica(ABC):
    @abstractmethod
    def registrar_observador(self, observador):
        pass

    @abstractmethod
    def eliminar_observador(self, observador):
        pass

    @abstractmethod
    def notificar_observadores(self):
        pass