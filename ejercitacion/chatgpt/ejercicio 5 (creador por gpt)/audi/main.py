from datetime import datetime
from audi.turno import Turno
from audi.cliente import Cliente
from audi.empleado import Empleado
from audi.taller import Taller

def main():
    cliente1 = Cliente("Juanma", 12345678, "Calle Falsa 123", ["Audi A4", "Audi Q5"])
    cliente2 = Cliente("Maria", 87654321, "Avenida Siempre Viva 456", ["Audi A3"])

    mecanico1 = Empleado("Carlos", 1232453, "Mecánico Jefe")
    mecanico2 = Empleado("Ana", 9876543, "Mecánica Asistente")

    turno1 = Turno(cliente1, datetime(2023, 10, 1, 10, 0), mecanico1)
    turno2 = Turno(cliente2, datetime(2023, 10, 2, 11, 0), mecanico2)

    taller = Taller([turno1, turno2])

    for t in taller.turnos:
        print(f"Turno: {t.fecha} - Cliente: {t.cliente.nombre} - Mecanico: {t.mecanico.nombre}")

if __name__ == "__main__":
    main()