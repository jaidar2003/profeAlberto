from datetime import datetime

class Evento:
    def __init__(self, fecha, duracion, num_participantes, num_comisarios, materiales):
        self.fecha = fecha
        self.duracion = duracion
        self.num_participantes = num_participantes
        self.num_comisarios = num_comisarios
        self.materiales = materiales  # Lista de strings
        self.comisarios = []  # Lista de objetos Comisario

    def agregar_comisario(self, comisario):
        self.comisarios.append(comisario)
        comisario.agregar_evento(self)