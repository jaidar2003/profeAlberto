from complejoDeportivo import ComplejoDeportivo

class ComplejoUnideportivo(ComplejoDeportivo):
    def __init__(self, localizacion, jefe_organizacion, area, deporte):
        super().__init__(localizacion, jefe_organizacion, area)
        self.deporte = deporte