class ComplejoDeportivo:
    def __init__(self, localizacion, jefe_organizacion, area):
        self.localizacion = localizacion
        self.jefe_organizacion = jefe_organizacion
        self.area = area
        self.areas_deporte = []  # Lista de AreaDeporte
        self.eventos = []        # Lista de Evento