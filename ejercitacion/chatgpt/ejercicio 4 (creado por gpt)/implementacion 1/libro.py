class Libro:
    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.disponible = True
        self.prestado_a = None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado a {self.prestado_a.nombre}"
        return f"Libro: {self.titulo}, Autor: {self.autor}, Año: {self.anio}, Género: {self.genero}, Estado: {estado}"
