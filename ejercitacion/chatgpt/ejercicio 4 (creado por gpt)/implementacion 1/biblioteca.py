class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.libros = []
        self.socios = []
        self.catalogo = set()  # Usamos un set para evitar duplicados en los géneros

    def registrar_libro(self, libro):
        self.libros.append(libro)
        self.catalogo.add(libro.genero)

    def registrar_socio(self, socio):
        self.socios.append(socio)

    def prestar_libro(self, titulo, numero_socio):
        libro = next((l for l in self.libros if l.titulo == titulo), None)
        socio = next((s for s in self.socios if s.numero == numero_socio), None)

        if not libro:
            return f"Libro '{titulo}' no encontrado."
        if not socio:
            return f"Socio #{numero_socio} no encontrado."
        if not libro.disponible:
            return f"El libro '{titulo}' ya está prestado."
        if len(socio.libros_prestados) >= 3:
            return f"El socio {socio.nombre} ya tiene 3 libros prestados."

        libro.disponible = False
        libro.prestado_a = socio
        socio.libros_prestados.append(libro)
        return f"Libro '{titulo}' prestado correctamente a {socio.nombre}."

    def devolver_libro(self, titulo, numero_socio):
        socio = next((s for s in self.socios if s.numero == numero_socio), None)
        if not socio:
            return f"Socio #{numero_socio} no encontrado."

        libro = next((l for l in socio.libros_prestados if l.titulo == titulo), None)
        if not libro:
            return f"El socio {socio.nombre} no tiene el libro '{titulo}'."

        libro.disponible = True
        libro.prestado_a = None
        socio.libros_prestados.remove(libro)
        return f"Libro '{titulo}' devuelto correctamente."

    def libros_prestados_por_socio(self, numero_socio):
        socio = next((s for s in self.socios if s.numero == numero_socio), None)
        if not socio:
            return f"Socio #{numero_socio} no encontrado."
        return socio.__str__()

    def estado_libro(self, titulo):
        libro = next((l for l in self.libros if l.titulo == titulo), None)
        if not libro:
            return f"Libro '{titulo}' no encontrado."
        return libro.__str__()

    def __str__(self):
        return f"Biblioteca: {self.nombre}, Dirección: {self.direccion}, Libros: {len(self.libros)}, Socios: {len(self.socios)}"