from modelo.evento import Evento


class ControladorEvento:
    def __init__(self, evento):
        self.evento = evento

    def agregar_comisario(self, comisario):
        self.evento.comisarios.append(comisario)
        comisario.eventos.append(self.evento)