from modelos.empleado import Empleado

class EmpleadoController:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, nombre: str, dni: int, rol: str) -> Empleado:
        nuevo_empleado = Empleado(nombre, dni, rol)
        self.empleados.append(nuevo_empleado)
        return nuevo_empleado

    def obtener_empleados(self):
        return self.empleados

    def buscar_empleado_por_dni(self, dni: int) -> Empleado:
        for empleado in self.empleados:
            if empleado.dni == dni:
                return empleado
        return None