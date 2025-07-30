from persona import Persona

class Doctor(Persona):
    def __init__(self, nombre, especialidad, consultorio):
        super().__init__(nombre)
        self.especialidad = especialidad
        self.consultorio = consultorio
        self.turnos = []

