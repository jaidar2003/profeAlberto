class Continente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paises = []

    def agregar_pais(self, pais):
        if pais not in self.paises:
            self.paises.append(pais)
            # Make bidirectional
            if pais.continente != self:
                pais.set_continente(self)

    def __str__(self):
        paises_str = ", ".join([pais.nombre for pais in self.paises])
        return f"Continente: {self.nombre}, Países: {paises_str}"
