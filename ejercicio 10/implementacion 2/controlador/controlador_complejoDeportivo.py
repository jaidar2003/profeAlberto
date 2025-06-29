from modelo.complejoDeportivo import ComplejoDeportivo

class ControladorComplejoDeportivo:
    def __init__(self, complejo_deportivo):
        self.complejo_deportivo = complejo_deportivo

    def agregar_area(self, area_deporte):
        self.complejo_deportivo.areas_deporte.append(area_deporte)

    def agregar_evento(self, evento):
        self.complejo_deportivo.eventos.append(evento)