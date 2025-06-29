from modelo.servicio import Servicio

class ControladorServicio:
    def crear_servicio(self, fecha, horas, tipo_trabajo, avion, mecanico):
        return Servicio(fecha, horas, tipo_trabajo, avion, mecanico)