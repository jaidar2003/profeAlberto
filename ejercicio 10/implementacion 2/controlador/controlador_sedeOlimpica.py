from modelo.sedeOlimpica import SedeOlimpica


class ControladorSedeOlimpica:
    def __init__(self, sede_olimpica):
        self.sede_olimpica = sede_olimpica

    def agregar_complejo(self, complejo):
        self.sede_olimpica.complejos.append(complejo)