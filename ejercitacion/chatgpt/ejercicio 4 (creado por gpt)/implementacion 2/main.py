from modelo.biblioteca import Biblioteca
from modelo.libro import Libro
from modelo.socio import Socio
from controlador.biblioteca_controlador import BibliotecaControlador
from controlador.prestamo_controlador import PrestamoControlador
from controlador.libro_controlador import LibroControlador
from controlador.socio_controlador import SocioControlador

def main():
    # Crear la biblioteca y su controlador
    biblio = Biblioteca("Biblioteca Central", "Av. Siempre Viva 123")
    biblio_controller = BibliotecaControlador(biblio)

    # Crear libros
    libro1 = Libro("1984", "George Orwell", 1949, "Distopía")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Fábula")
    libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo Mágico")

    # Registrar libros
    biblio_controller.registrar_libro(libro1)
    biblio_controller.registrar_libro(libro2)
    biblio_controller.registrar_libro(libro3)

    # Crear socios
    socio1 = Socio("Juan Pérez", 1)
    socio2 = Socio("Ana Gómez", 2)

    # Registrar socios
    biblio_controller.registrar_socio(socio1)
    biblio_controller.registrar_socio(socio2)

    # Prestar libros
    prestamo_controller = PrestamoControlador()
    print(prestamo_controller.prestar(biblio, "1984", 1))
    print(prestamo_controller.prestar(biblio, "Cien años de soledad", 1))
    print(prestamo_controller.prestar(biblio, "El Principito", 1))
    print(prestamo_controller.prestar(biblio, "1984", 2))  # ya prestado

    # Estado de libro
    libro_controller = LibroControlador()
    libro = next((l for l in biblio.libros if l.titulo == "1984"), None)
    print(libro_controller.mostrar_estado(libro))

    # Libros del socio
    socio_ctrl = SocioControlador()
    print(socio_ctrl.libros_del_socio(socio1))

    # Devolver libro
    print(prestamo_controller.devolver(biblio, "1984", 1))
    print(libro_controller.mostrar_estado(libro))

if __name__ == "__main__":
    main()
