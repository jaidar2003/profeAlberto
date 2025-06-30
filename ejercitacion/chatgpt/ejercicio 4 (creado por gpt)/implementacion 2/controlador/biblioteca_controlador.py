from modelo.biblioteca import Biblioteca

class BibliotecaControlador:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def registrar_libro(self, libro):
        self.biblioteca.libros.append(libro)
        self.biblioteca.catalogo.add(libro.genero)

    def registrar_socio(self, socio):
        self.biblioteca.socios.append(socio)

    def listar_libros(self):
        return self.biblioteca.libros

    def listar_socios(self):
        return self.biblioteca.socios

    def mostrar_catalogo(self):
        return sorted(self.biblioteca.catalogo)
