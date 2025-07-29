from modelos.turno import Turno

class TurnoController:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno: Turno):
        self.turnos.append(turno)

    def obtener_turnos(self):
        return self.turnos

    def eliminar_turno(self, turno: Turno):
        if turno in self.turnos:
            self.turnos.remove(turno)
            return True
        return False