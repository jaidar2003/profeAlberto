class Universidad:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.facultades = []
        self.convenios = []

    def agregar_facultad(self, facultad):
        if facultad not in self.facultades:
            self.facultades.append(facultad)
            facultad.asignar_universidad(self)

    def agregar_convenio(self, universidad):
        if universidad not in self.convenios:
            self.convenios.append(universidad)

    def __str__(self):
        fac_str = ', '.join([f.nombre for f in self.facultades]) if self.facultades else "Ninguna"
        conv_str = ', '.join([u.nombre for u in self.convenios]) if self.convenios else "Ninguno"
        return f"Universidad: {self.nombre}, Ciudad: {self.ciudad.nombre}, Facultades: {fac_str}, Convenios: {conv_str}"