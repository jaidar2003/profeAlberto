from modelo.hangar import Hangar

class ControladorHangar:
    def crear_hangar(self, numero, capacidad, ubicacion):
        return Hangar(numero, capacidad, ubicacion)