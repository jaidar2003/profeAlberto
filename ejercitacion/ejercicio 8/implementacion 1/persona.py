from abc import ABC, abstractmethod

@abstractmethod
class Persona(ABC):
    def __init__(self, nss, nombre, direccion, telefono):
        self.nss = nss
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def crear_persona(self, nss, nombre, direccion, telefono):
        return Persona(nss, nombre, direccion, telefono)