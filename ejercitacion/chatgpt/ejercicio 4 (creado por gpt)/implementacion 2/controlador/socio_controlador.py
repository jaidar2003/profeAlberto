from modelo.socio import Socio

class SocioControlador:
    def libros_del_socio(self, socio):
        if not socio.libros_prestados:
            return f"{socio.nombre} no tiene libros prestados."
        titulos = [libro.titulo for libro in socio.libros_prestados]
        return f"{socio.nombre} tiene: " + ", ".join(titulos)
