from datetime import datetime
from areaDeporte import AreaDeporte
from evento import Evento
from complejoDeportivo import ComplejoDeportivo
from complejoUnideportivo import ComplejoUnideportivo
from complejoPolideportivo import Polideportivo
from sedeOlimpica import SedeOlimpica
from comisario import Comisario

def main():
    # Crear sede olímpica
    sede = SedeOlimpica(numero_complejos=2, presupuesto=5000000)

    # Crear complejos
    poli = Polideportivo(
        localizacion="Zona Norte",
        jefe_organizacion="María Gómez",
        area=12000.0,
        deportes=["fútbol", "básquet", "voley"]
    )

    uni = ComplejoUnideportivo(
        localizacion="Zona Sur",
        jefe_organizacion="Carlos Pérez",
        area=8000.0,
        deporte="natación"
    )

    # Crear áreas de deporte
    area1 = AreaDeporte(deporte="fútbol", ubicacion="centro")
    area2 = AreaDeporte(deporte="natación", ubicacion="esquina NE")

    poli.agregar_area(area1)
    uni.agregar_area(area2)

    # Crear comisarios
    com1 = Comisario("Laura Sánchez")
    com2 = Comisario("Javier Méndez")

    # Crear evento
    evento = Evento(
        fecha=datetime(2024, 7, 15, 10, 0),  # Fecha y hora del evento
        duracion=2.5,
        num_participantes=16,
        num_comisarios=2,
        materiales=["pelotas", "redes"]
    )

    evento.agregar_comisario(com1)
    evento.agregar_comisario(com2)

    # Asignar evento al complejo
    poli.agregar_evento(evento)

    # Agregar complejos a la sede
    sede.agregar_complejo(poli)
    sede.agregar_complejo(uni)

    # Mostrar información básica
    print("Sede Olímpica")
    print(f"Presupuesto: ${sede.presupuesto}")
    print(f"Cantidad de complejos: {len(sede.complejos)}")

    for complejo in sede.complejos:
        print(f"\nComplejo en {complejo.localizacion} dirigido por {complejo.jefe_organizacion}")
        print(f"Tipo: {complejo.__class__.__name__}")
        for area in complejo.areas_deporte:
            print(f" - Área de {area.deporte} ubicada en {area.ubicacion}")
        for evento in complejo.eventos:
            print(f" - Evento el {evento.fecha}, participantes: {evento.num_participantes}")
            print("   Comisarios:")
            for c in evento.comisarios:
                print(f"     - {c.nombre}")

if __name__ == "__main__":
    main()