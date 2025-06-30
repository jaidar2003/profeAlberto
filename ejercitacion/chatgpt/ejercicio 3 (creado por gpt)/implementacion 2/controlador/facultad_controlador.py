from modelo.facultad import Facultad

class FacultadControlador:
    def agregar_carrera(self, carrera):
        if carrera not in self.carreras:
            self.carreras.append(carrera)
            carrera.asignar_facultad(self)

    def asignar_universidad(self, universidad):
        self.universidad = universidad

    def __str__(self):
        carreras_str = ', '.join([c.nombre for c in self.carreras]) if self.carreras else "Ninguna"
        return f"Facultad: {self.nombre}, Decano: {self.decano.nombre}, Carreras: {carreras_str}"