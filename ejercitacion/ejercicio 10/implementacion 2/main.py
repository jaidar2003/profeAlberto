from datetime import datetime

# Importar modelos
from modelo.sedeOlimpica import SedeOlimpica
from modelo.complejoDeportivo import ComplejoDeportivo
from modelo.complejoPolideportivo import Polideportivo
from modelo.complejoUnideportivo import ComplejoUnideportivo
from modelo.areaDeporte import AreaDeporte
from modelo.evento import Evento
from modelo.comisario import Comisario

# Importar controladores
from controlador.controlador_sedeOlimpica import ControladorSedeOlimpica
from controlador.controlador_complejoDeportivo import ControladorComplejoDeportivo
from controlador.controlador_complejoPolideportivo import ControladorComplejoPolideportivo
from controlador.controlador_complejoUnideportivo import ControladorComplejoUnideportivo
from controlador.controlador_areaDeporte import ControladorAreaDeporte
from controlador.controlador_evento import ControladorEvento
from controlador.controlador_comisario import ControladorComisario


def main():
    # Crear sede olímpica
    sede = SedeOlimpica(numero_complejos=2, presupuesto=5000000)
    ctrl_sede = ControladorSedeOlimpica(sede)

    # Crear complejos
    poli = Polideportivo(
        localizacion="Zona Norte",
        jefe_organizacion="María Gómez",
        area=12000.0,
        deportes=["fútbol", "básquet", "voley"]
    )
    ctrl_poli = ControladorComplejoPolideportivo(poli)

    uni = ComplejoUnideportivo(
        localizacion="Zona Sur",
        jefe_organizacion="Carlos Pérez",
        area=8000.0,
        deporte="natación"
    )
    ctrl_uni = ControladorComplejoUnideportivo(uni)

    # Crear áreas de deporte
    area1 = AreaDeporte(deporte="fútbol", ubicacion="centro")
    area2 = AreaDeporte(deporte="natación", ubicacion="esquina NE")
    ctrl_area1 = ControladorAreaDeporte(area1)
    ctrl_area2 = ControladorAreaDeporte(area2)

    # Agregar áreas a los complejos
    ctrl_poli.agregar_area(area1)
    ctrl_uni.agregar_area(area2)

    # Crear comisarios
    com1 = Comisario("Laura Sánchez")
    com2 = Comisario("Javier Méndez")
    ctrl_com1 = ControladorComisario(com1)
    ctrl_com2 = ControladorComisario(com2)

    # Crear evento
    evento = Evento(
        fecha=datetime(2024, 7, 15, 10, 0),  # Fecha y hora del evento
        duracion=2.5,
        num_participantes=16,
        num_comisarios=2,
        materiales=["pelotas", "redes"]
    )
    ctrl_evento = ControladorEvento(evento)

    # Agregar comisarios al evento
    ctrl_evento.agregar_comisario(com1)
    ctrl_evento.agregar_comisario(com2)

    # Asignar evento al complejo
    ctrl_poli.agregar_evento(evento)

    # Agregar complejos a la sede
    ctrl_sede.agregar_complejo(poli)
    ctrl_sede.agregar_complejo(uni)

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