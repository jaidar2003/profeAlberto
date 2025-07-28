from biblioteca import Biblioteca
from libro import Libro
from socio import Socio
from prestamo import Prestamo


def main():
    biblio = Biblioteca("Biblioteca Central", "Av. Siempre Viva 123")

    # Crear libros
    libro1 = Libro("1984", "George Orwell", 1949, "Distopía")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Fábula")
    libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo Mágico")

    # Registrar libros
    biblio.registrar_libro(libro1)
    biblio.registrar_libro(libro2)
    biblio.registrar_libro(libro3)

    # Crear socios
    socio1 = Socio("Juan Pérez", 1)
    socio2 = Socio("Ana Gómez", 2)

    # Registrar socios
    biblio.registrar_socio(socio1)
    biblio.registrar_socio(socio2)

    # Prestar libros
    print(biblio.prestar_libro("1984", 1))
    print(biblio.prestar_libro("Cien años de soledad", 1))
    print(biblio.prestar_libro("El Principito", 1))
    print(biblio.prestar_libro("1984", 2))  # ya prestado

    # Estado de libro
    print(biblio.estado_libro("1984"))

    # Libros del socio
    print(biblio.libros_prestados_por_socio(1))

    # Devolver libro
    print(biblio.devolver_libro("1984", 1))
    print(biblio.estado_libro("1984"))

if __name__ == "__main__":
    main()