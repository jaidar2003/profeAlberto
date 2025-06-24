from modelo.ciudad import Ciudad

class ControladorCiudad:
    def __init__(self):
        self.ciudades = []

    def crear_ciudad(self, nombre: str):
        ciudad = Ciudad(nombre)
        self.ciudades.append(ciudad)
        return ciudad

    def listar_ciudades(self):
        return self.ciudades
