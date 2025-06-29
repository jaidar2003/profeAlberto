from modelo.tipoAvion import TipoAvion

class ControladorTipoAvion:
    def crear_tipo_avion(self, modelo, capacidad, peso):
        return TipoAvion(modelo, capacidad, peso)