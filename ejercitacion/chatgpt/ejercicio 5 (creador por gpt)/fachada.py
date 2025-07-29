from modelos.cliente import Cliente
from modelos.vehiculo import Vehiculo
from modelos.empleado import Empleado
from modelos.turno import Turno
from modelos.taller import Taller
from datetime import datetime

from controladores.cliente_controller import ClienteController
from controladores.vehiculo_controller import VehiculoController
from controladores.empleado_controller import EmpleadoController
from controladores.turno_controller import TurnoController
from controladores.taller_controller import TallerController

class ConcesionarioFacade:
    def __init__(self):
        self.cliente_controller = ClienteController()
        self.vehiculo_controller = VehiculoController()
        self.empleado_controller = EmpleadoController()
        self.turno_controller = TurnoController()
        self.taller_controller = TallerController()

    def registrar_cliente(self, nombre, dni, direccion, vehiculos=None):
        if vehiculos is None:
            vehiculos = []
        cliente = Cliente(nombre, dni, direccion, vehiculos)
        self.cliente_controller.agregar_cliente(cliente)
        return cliente

    def agregar_vehiculo(self, modelo, anio, precio):
        vehiculo = Vehiculo(modelo, anio, precio)
        self.vehiculo_controller.agregar_vehiculo(vehiculo)
        return vehiculo

    def vender_vehiculo(self, modelo, cliente_dni):
        vehiculo = self.vehiculo_controller.buscar_vehiculo(modelo)
        cliente = self.cliente_controller.buscar_cliente_por_dni(cliente_dni)
        if vehiculo and cliente:
            vehiculo.vendido = True
            vehiculo.duenio = cliente.nombre
            cliente.vehiculo.append(vehiculo)

    def agregar_empleado(self, nombre, dni, rol):
        return self.empleado_controller.agregar_empleado(nombre, dni, rol)

    def asignar_turno(self, cliente_dni, fecha: datetime, mecanico_dni):
        cliente = self.cliente_controller.buscar_cliente_por_dni(cliente_dni)
        mecanico = self.empleado_controller.buscar_empleado_por_dni(mecanico_dni)
        if cliente and mecanico:
            turno = Turno(cliente, fecha, mecanico)
            self.turno_controller.agregar_turno(turno)
            self.taller_controller.taller.turnos.append(turno)

    def mostrar_datos(self):
        print("\n\U0001F4CB Vehículos en stock:")
        for v in self.vehiculo_controller.listar_vehiculos():
            estado = "Vendido" if v.vendido else "Disponible"
            print(f"{v.modelo} - {v.anio} - ${v.precio} - {estado} - Dueño: {v.duenio or 'Sin asignar'}")

        print("\n\U0001F464 Clientes registrados:")
        for c in self.cliente_controller.obtener_clientes():
            autos = ', '.join([a.modelo for a in c.vehiculo]) if c.vehiculo else "Ninguno"
            print(f"{c.nombre} ({c.dni}) - {c.direccion} - Vehículos: {autos}")

        print("\n\U0001F527 Turnos asignados:")
        for t in self.turno_controller.obtener_turnos():
            print(f"{t.fecha} - Cliente: {t.cliente.nombre} - Mecánico: {t.mecanico.nombre}")

