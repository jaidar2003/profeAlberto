class Cliente:
    def __init__(self, nombre: str, dni: int, direccion: str, vehiculo: list[str], turnos: list = None):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.vehiculo = vehiculo
        self.turnos = turnos if turnos is not None else []



