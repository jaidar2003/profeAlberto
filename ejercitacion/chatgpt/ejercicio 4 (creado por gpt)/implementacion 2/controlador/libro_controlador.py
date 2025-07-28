from modelo.libro import Libro

class LibroControlador:
    def mostrar_estado(self, libro):
        if libro.disponible:
            return f"'{libro.titulo}' está disponible."
        return f"'{libro.titulo}' está prestado a {libro.prestado_a.nombre}."
