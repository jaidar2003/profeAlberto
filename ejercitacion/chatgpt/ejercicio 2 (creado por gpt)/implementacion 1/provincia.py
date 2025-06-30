class Provincia:
    def __init__(self, nombre, capital_provincial, pais):
        self.nombre = nombre
        self.ciudades = []
        self.capital_provincial = capital_provincial
        self.pais = None  # Initialize to None to avoid circular reference in constructor
        self.provincias_vecinas = []
        self.paises_limitrofes = []

        # Agregar la capital como ciudad de la provincia
        self.agregar_ciudad(capital_provincial)

        # Set the bidirectional relationship with the country
        self.set_pais(pais)

    def set_pais(self, pais):
        if self.pais != pais:
            self.pais = pais
            # Don't call pais.agregar_provincia to avoid infinite recursion
            if self not in pais.provincias:
                pais.agregar_provincia(self)

    def agregar_ciudad(self, ciudad):
        if ciudad not in self.ciudades:
            self.ciudades.append(ciudad)
            # Make bidirectional
            if ciudad.provincia != self:
                ciudad.set_provincia(self)

    def agregar_provincia_vecina(self, provincia):
        if provincia not in self.provincias_vecinas:
            self.provincias_vecinas.append(provincia)
            # Relación bidireccional
            if self not in provincia.provincias_vecinas:
                provincia.agregar_provincia_vecina(self)

    def agregar_pais_limitrofe(self, pais):
        if pais not in self.paises_limitrofes:
            self.paises_limitrofes.append(pais)
            # Make bidirectional - add this province to the country's border provinces
            if hasattr(pais, 'provincias_limitrofes'):
                if self not in pais.provincias_limitrofes:
                    pais.agregar_provincia_limitrofe(self)

    def __str__(self):
        ciudades_str = ", ".join([ciudad.nombre for ciudad in self.ciudades])
        provincias_vecinas_str = ", ".join([prov.nombre for prov in self.provincias_vecinas])
        paises_limitrofes_str = ", ".join([pais.nombre for pais in self.paises_limitrofes])

        return (f"Provincia: {self.nombre}, "
                f"Capital: {self.capital_provincial.nombre}, "
                f"Ciudades: {ciudades_str}, "
                f"País: {self.pais.nombre}, "
                f"Provincias Vecinas: {provincias_vecinas_str}, "
                f"Países Limítrofes: {paises_limitrofes_str}")
