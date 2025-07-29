from fachada import ConcesionarioFacade

def main():
    facade = ConcesionarioFacade()

    facade.registrar_cliente("Juanma", 12345678, "Calle Falsa 123")
    facade.registrar_cliente("Maria", 87654321, "Av Siempre Viva 456")

    facade.agregar_vehiculo("Audi A3", 2022, 40000)
    facade.agregar_vehiculo("Audi Q5", 2023, 60000)

    facade.vender_vehiculo("Audi A3", 12345678)

    facade.agregar_empleado("Carlos", 11223344, "Mecanico")
    facade.agregar_empleado("Ana", 55667788, "Mecanica")

    from datetime import datetime
    facade.asignar_turno(12345678, datetime(2023, 10, 1, 10, 0), 11223344)
    facade.asignar_turno(87654321, datetime(2023, 10, 2, 11, 0), 55667788)

    facade.mostrar_datos()

if __name__ == "__main__":
    main()
