from modelo.complejoPolideportivo import Polideportivo
from controlador.controlador_complejoDeportivo import ControladorComplejoDeportivo

class ControladorComplejoPolideportivo(ControladorComplejoDeportivo):
    def __init__(self, polideportivo):
        super().__init__(polideportivo)
        self.polideportivo = polideportivo
