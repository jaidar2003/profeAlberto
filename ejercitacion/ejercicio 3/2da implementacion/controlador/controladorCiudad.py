from modelo.ciudad import Ciudad

class ControladorCiudad:

    def __init__(self):
        self.ciudades = []

    def recaudacion_total(self, ciudad):
        return sum(ciudad.impuestos.values())

    def tiene_deficit(self, ciudad):
        return ciudad.poblacion > 100_000 and ciudad.gasto_mantenimiento > self.recaudacion_total(ciudad)

    def obtener_pais(self, ciudad):
        if ciudad.provincia:
            return ciudad.provincia.pais
        return None

    def formato_str(self, ciudad):
        provincia_info = ", Provincia: {}".format(ciudad.provincia.nombre) if ciudad.provincia else ", Sin provincia"
        deficit_text = "Sí" if self.tiene_deficit(ciudad) else "No"
        return "{} (Población: {}, Recaudación: {}, Gasto: {}, Déficit: {}{})".format(
            ciudad.nombre, 
            ciudad.poblacion, 
            self.recaudacion_total(ciudad), 
            ciudad.gasto_mantenimiento, 
            deficit_text,
            provincia_info
        )
