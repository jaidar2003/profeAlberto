class Prestamo:
    def __init__(self, libro, socio, fecha_inicio, fecha_devolucion):
        self.libro = libro
        self.socio = socio
        self.fecha_inicio = fecha_inicio
        self.fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f"Préstamo: {self.libro.titulo} a {self.socio.nombre} desde {self.fecha_inicio} hasta {self.fecha_devolucion}"