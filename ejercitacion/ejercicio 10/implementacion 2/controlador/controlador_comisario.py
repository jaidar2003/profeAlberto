from modelo.comisario import Comisario


class ControladorComisario:
    def __init__(self, comisario):
        self.comisario = comisario  # Almacenar la referencia al modelo

    def agregar_evento(self, evento):
        self.comisario.eventos.append(evento)  # Manipular los datos del modelo