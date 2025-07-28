from modelo.prestamo import Prestamo

class PrestamoControlador:
    def prestar(self, biblioteca, titulo, numero_socio):
        libro = next((l for l in biblioteca.libros if l.titulo == titulo), None)
        socio = next((s for s in biblioteca.socios if s.numero == numero_socio), None)

        if not libro:
            return f"Libro '{titulo}' no encontrado."
        if not socio:
            return f"Socio #{numero_socio} no encontrado."
        if not libro.disponible:
            return f"El libro '{titulo}' ya está prestado."
        if len(socio.libros_prestados) >= 3:
            return f"{socio.nombre} ya tiene 3 libros prestados."

        libro.disponible = False
        libro.prestado_a = socio
        socio.libros_prestados.append(libro)
        return f"Libro '{titulo}' prestado correctamente a {socio.nombre}."

    def devolver(self, biblioteca, titulo, numero_socio):
        socio = next((s for s in biblioteca.socios if s.numero == numero_socio), None)
        if not socio:
            return f"Socio #{numero_socio} no encontrado."

        libro = next((l for l in socio.libros_prestados if l.titulo == titulo), None)
        if not libro:
            return f"{socio.nombre} no tiene el libro '{titulo}'."

        libro.disponible = True
        libro.prestado_a = None
        socio.libros_prestados.remove(libro)
        return f"Libro '{titulo}' devuelto correctamente por {socio.nombre}."
