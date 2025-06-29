class Comisario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.eventos = []  # Lista de eventos en los que participa

    def agregar_evento(self, evento):
        self.eventos.append(evento)

