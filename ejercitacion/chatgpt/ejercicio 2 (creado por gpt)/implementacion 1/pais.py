class Pais:
    def __init__(self, nombre, capital, provincias=list, vecinos=list):
        self.nombre = nombre
        self.capital = capital
        self.provincias = []
        self.vecinos = []
        self.provincias_limitrofes = []  # New attribute for border provinces
        self.continente = None  # Reference to the continent it belongs to

    def set_continente(self, continente):
        if self.continente != continente:
            self.continente = continente
            # Don't call continente.agregar_pais to avoid infinite recursion
            if self not in continente.paises:
                continente.agregar_pais(self)

    def agregar_provincia(self, provincia):
        if provincia not in self.provincias:
            self.provincias.append(provincia)
            # Make bidirectional
            if provincia.pais != self:
                provincia.set_pais(self)

    def agregar_provincia_limitrofe(self, provincia):
        if provincia not in self.provincias_limitrofes:
            self.provincias_limitrofes.append(provincia)
            # Make bidirectional
            if self not in provincia.paises_limitrofes:
                provincia.agregar_pais_limitrofe(self)

    def agregar_vecino(self, pais):
        if pais not in self.vecinos:
            self.vecinos.append(pais)
            # Relación bidireccional
            if self not in pais.vecinos:
                pais.agregar_vecino(self)

    def __str__(self):
        provincias_str = ", ".join([prov.nombre for prov in self.provincias])
        vecinos_str = ", ".join([pais.nombre for pais in self.vecinos])
        provincias_limitrofes_str = ", ".join([prov.nombre for prov in self.provincias_limitrofes])
        continente_str = f", Continente: {self.continente.nombre}" if self.continente else ""

        return (f"País: {self.nombre}, "
                f"Capital: {self.capital.nombre}, "
                f"Provincias: {provincias_str}, "
                f"Países Vecinos: {vecinos_str}, "
                f"Provincias Limítrofes: {provincias_limitrofes_str}{continente_str}")
