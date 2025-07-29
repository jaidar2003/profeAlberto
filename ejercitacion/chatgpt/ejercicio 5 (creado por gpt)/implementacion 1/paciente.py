from persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, dni, obraSocial):
        super().__init__()
        self.obraSocial = obraSocial
        self.turnos = []

