class Ciudad:
    def __init__(self, nombre, poblacion, impuestos, gasto_mantenimiento):
        self.nombre = nombre
        self.poblacion = poblacion
        self.impuestos = impuestos  # Diccionario con imp1..imp5
        self.gasto_mantenimiento = gasto_mantenimiento
        self.provincia = None  # Referencia a la provincia padre