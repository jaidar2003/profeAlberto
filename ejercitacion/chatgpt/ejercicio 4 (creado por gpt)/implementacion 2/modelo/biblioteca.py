class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.libros = []
        self.socios = []
        self.catalogo = set()  # Usamos un set para evitar duplicados en los géneros

