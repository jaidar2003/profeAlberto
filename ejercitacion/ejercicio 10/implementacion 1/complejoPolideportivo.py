from complejoDeportivo import ComplejoDeportivo

class Polideportivo(ComplejoDeportivo):
    def __init__(self, localizacion, jefe_organizacion, area, deportes):
        super().__init__(localizacion, jefe_organizacion, area)
        self.deportes = deportes  # Lista de strings