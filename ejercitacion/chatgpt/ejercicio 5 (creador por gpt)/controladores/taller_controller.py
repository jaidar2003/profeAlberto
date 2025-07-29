from modelos.taller import Taller

class TallerController:
    def __init__(self):
        self.taller = Taller([])

    def asignar_jefe_taller(self, jefe_taller):
        self.taller.jefe_taller = jefe_taller

    def asignar_horario(self, horario):
        self.taller.horario = horario
