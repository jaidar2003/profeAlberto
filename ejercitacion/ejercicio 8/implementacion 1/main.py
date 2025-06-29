from avion import Avion
from hangar import Hangar
from mecanico import Mecanico
from persona import Persona
from piloto import Piloto
from propietario import Propietario
from servicio import Servicio
from tipoAvion import TipoAvion

def main():
    # Crear instancias de los objetos
    tipo_avion = TipoAvion("Jet", 200, 1000)
    hangar = Hangar("Hangar A", 123, "4567890123")

    avion = Avion("ABC123", tipo_avion, hangar)

    propietario = Propietario("123456789", "Juan Perez", "456 Elm St", "555-5678", "2023-01-01")
    avion.agregar_propietario(propietario)

    piloto = Piloto("987654321", "Ana Gomez", "789 Oak St", "555-8765", "Licencia A", "Ninguna")
    mecanico = Mecanico("456789123", "Luis Torres", "321 Pine St", "555-4321", 3000, "Diurno")

    servicio = Servicio("2023-10-01", 3, "Mantenimiento", avion, mecanico)
    avion.agregar_servicio(servicio)

    # Autorizar tipos de avión
    piloto.autorizar_tipo(piloto, tipo_avion)
    mecanico.autorizar_tipo(mecanico, tipo_avion)

    # Mostrar información del avión
    print(f"Avión: {avion.matricula}, Tipo: {avion.tipo.modelo}, Propietario: {propietario.nombre}, Servicio: {servicio.tipo_trabajo}")

if __name__ == "__main__":
    main()
