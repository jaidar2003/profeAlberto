class Ciudad:
    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = poblacion
        self.provincia = None  # Reference to the province it belongs to

    def get_poblacion(self):
        return self.poblacion

    def set_provincia(self, provincia):
        if self.provincia != provincia:
            self.provincia = provincia
            # Don't call provincia.agregar_ciudad to avoid infinite recursion
            if self not in provincia.ciudades:
                provincia.agregar_ciudad(self)

    def __str__(self):
        provincia_str = f", Provincia: {self.provincia.nombre}" if self.provincia else ""
        return f"Ciudad: {self.nombre}, Población: {self.poblacion}{provincia_str}"
