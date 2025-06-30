class Socio:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.libros_prestados = []

    def __str__(self):
        libros = ', '.join([libro.titulo for libro in self.libros_prestados]) or "Ninguno"
        return f"Socio: {self.nombre} (#{self.numero}), Libros prestados: {libros}"



