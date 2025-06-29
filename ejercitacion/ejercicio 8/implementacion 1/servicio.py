class Servicio:
    def __init__(self, fecha, horas, tipo_trabajo, avion, mecanico):
        self.fecha = fecha
        self.horas = horas
        self.tipo_trabajo = tipo_trabajo
        self.avion = avion
        self.mecanico = mecanico

    def crear_servicio(self, fecha, horas, tipo_trabajo, avion, mecanico):
        return Servicio(fecha, horas, tipo_trabajo, avion, mecanico)