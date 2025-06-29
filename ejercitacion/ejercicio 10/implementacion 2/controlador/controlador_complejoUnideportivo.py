from modelo.complejoUnideportivo import ComplejoUnideportivo
from controlador.controlador_complejoDeportivo import ControladorComplejoDeportivo

class ControladorComplejoUnideportivo(ControladorComplejoDeportivo):
    def __init__(self, complejo_unideportivo):
        super().__init__(complejo_unideportivo)
        self.complejo_unideportivo = complejo_unideportivo
