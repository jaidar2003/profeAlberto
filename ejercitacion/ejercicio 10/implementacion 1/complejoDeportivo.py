class ComplejoDeportivo:
    def __init__(self, localizacion, jefe_organizacion, area):
        self.localizacion = localizacion
        self.jefe_organizacion = jefe_organizacion
        self.area = area
        self.areas_deporte = []  # Lista de AreaDeporte
        self.eventos = []        # Lista de Evento

    def agregar_area(self, area_deporte):
        self.areas_deporte.append(area_deporte)

    def agregar_evento(self, evento):
        self.eventos.append(evento)