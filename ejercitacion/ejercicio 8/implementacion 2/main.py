# Importar los controladores
from controlador.controladorAvion import ControladorAvion
from controlador.controladorTipoAvion import ControladorTipoAvion
from controlador.controladorHangar import ControladorHangar
from controlador.controladorPropietario import ControladorPropietario
from controlador.controladorMecanico import ControladorMecanico
from controlador.controladorPiloto import ControladorPiloto
from controlador.controladorServicio import ControladorServicio

# Crear instancias de los controladores
controlador_avion = ControladorAvion()
controlador_tipo_avion = ControladorTipoAvion()
controlador_hangar = ControladorHangar()
controlador_propietario = ControladorPropietario()
controlador_mecanico = ControladorMecanico()
controlador_piloto = ControladorPiloto()
controlador_servicio = ControladorServicio()

# Crear hangares
hangar1 = controlador_hangar.crear_hangar(1, 10, "Terminal A")
hangar2 = controlador_hangar.crear_hangar(2, 15, "Terminal B")
print(f"Hangar creado: {hangar1.numero}, Capacidad: {hangar1.capacidad}, Ubicación: {hangar1.ubicacion}")
print(f"Hangar creado: {hangar2.numero}, Capacidad: {hangar2.capacidad}, Ubicación: {hangar2.ubicacion}")
print()

# Crear tipos de avión
tipo_avion1 = controlador_tipo_avion.crear_tipo_avion("Boeing 737", 150, 70000)
tipo_avion2 = controlador_tipo_avion.crear_tipo_avion("Airbus A320", 180, 75000)
print(f"Tipo de avión creado: {tipo_avion1.modelo}, Capacidad: {tipo_avion1.capacidad}, Peso: {tipo_avion1.peso}")
print(f"Tipo de avión creado: {tipo_avion2.modelo}, Capacidad: {tipo_avion2.capacidad}, Peso: {tipo_avion2.peso}")
print()

# Crear aviones
avion1 = controlador_avion.crear_avion("LV-ABC", tipo_avion1, hangar1)
avion2 = controlador_avion.crear_avion("LV-XYZ", tipo_avion2, hangar2)
print(f"Avión creado: {avion1.matricula}, Tipo: {avion1.tipo.modelo}, Hangar: {avion1.hangar.numero}")
print(f"Avión creado: {avion2.matricula}, Tipo: {avion2.tipo.modelo}, Hangar: {avion2.hangar.numero}")
print()

# Crear propietarios
propietario1 = controlador_propietario.crear_propietario("12345678", "Juan Pérez", "Calle 123", "555-1234", "2022-01-15")
propietario2 = controlador_propietario.crear_propietario("87654321", "María López", "Avenida 456", "555-5678", "2022-02-20")
print(f"Propietario creado: {propietario1.nombre}, NSS: {propietario1.nss}, Fecha de adquisición: {propietario1.fecha_adquisicion}")
print(f"Propietario creado: {propietario2.nombre}, NSS: {propietario2.nss}, Fecha de adquisición: {propietario2.fecha_adquisicion}")
print()

# Asignar propietarios a aviones
controlador_avion.asignar_propietario(avion1, propietario1)
controlador_avion.asignar_propietario(avion2, propietario2)
print(f"Propietario {propietario1.nombre} asignado al avión {avion1.matricula}")
print(f"Propietario {propietario2.nombre} asignado al avión {avion2.matricula}")
print()

# Crear mecánicos
mecanico1 = controlador_mecanico.crear_mecanico("23456789", "Carlos Rodríguez", "Calle 789", "555-9012", 50000, "Mañana")
mecanico2 = controlador_mecanico.crear_mecanico("34567890", "Ana Martínez", "Avenida 012", "555-3456", 55000, "Tarde")
print(f"Mecánico creado: {mecanico1.nombre}, NSS: {mecanico1.nss}, Salario: {mecanico1.salario}, Turno: {mecanico1.turno}")
print(f"Mecánico creado: {mecanico2.nombre}, NSS: {mecanico2.nss}, Salario: {mecanico2.salario}, Turno: {mecanico2.turno}")
print()

# Autorizar tipos de avión a mecánicos
controlador_mecanico.autorizar_tipo(mecanico1, tipo_avion1)
controlador_mecanico.autorizar_tipo(mecanico2, tipo_avion2)
print(f"Mecánico {mecanico1.nombre} autorizado para el tipo de avión {tipo_avion1.modelo}")
print(f"Mecánico {mecanico2.nombre} autorizado para el tipo de avión {tipo_avion2.modelo}")
print()

# Crear pilotos
piloto1 = controlador_piloto.crear_piloto("45678901", "Pedro Gómez", "Calle 345", "555-7890", "P12345", "Ninguna")
piloto2 = controlador_piloto.crear_piloto("56789012", "Laura Sánchez", "Avenida 678", "555-2345", "P67890", "Ninguna")
print(f"Piloto creado: {piloto1.nombre}, NSS: {piloto1.nss}, Licencia: {piloto1.licencia}, Restricciones: {piloto1.restricciones}")
print(f"Piloto creado: {piloto2.nombre}, NSS: {piloto2.nss}, Licencia: {piloto2.licencia}, Restricciones: {piloto2.restricciones}")
print()

# Autorizar tipos de avión a pilotos
controlador_piloto.autorizar_tipo(piloto1, tipo_avion1)
controlador_piloto.autorizar_tipo(piloto2, tipo_avion2)
print(f"Piloto {piloto1.nombre} autorizado para el tipo de avión {tipo_avion1.modelo}")
print(f"Piloto {piloto2.nombre} autorizado para el tipo de avión {tipo_avion2.modelo}")
print()

# Crear servicios
servicio1 = controlador_servicio.crear_servicio("2023-05-10", 5, "Mantenimiento", avion1, mecanico1)
servicio2 = controlador_servicio.crear_servicio("2023-05-15", 3, "Reparación", avion2, mecanico2)
print(f"Servicio creado: Fecha: {servicio1.fecha}, Horas: {servicio1.horas}, Tipo: {servicio1.tipo_trabajo}")
print(f"Servicio creado: Fecha: {servicio2.fecha}, Horas: {servicio2.horas}, Tipo: {servicio2.tipo_trabajo}")
print()

# Asignar servicios a aviones
controlador_avion.asignar_servicio(avion1, servicio1)
controlador_avion.asignar_servicio(avion2, servicio2)
print(f"Servicio de fecha {servicio1.fecha} asignado al avión {avion1.matricula}")
print(f"Servicio de fecha {servicio2.fecha} asignado al avión {avion2.matricula}")
print()

# Mostrar información completa de los aviones
print("Información completa de los aviones:")
print(f"Avión: {avion1.matricula}")
print(f"  Tipo: {avion1.tipo.modelo}")
print(f"  Hangar: {avion1.hangar.numero} ({avion1.hangar.ubicacion})")
print(f"  Propietarios:")
for propietario in avion1.propietarios:
    print(f"    - {propietario.nombre}")
print(f"  Servicios:")
for servicio in avion1.servicios:
    print(f"    - Fecha: {servicio.fecha}, Tipo: {servicio.tipo_trabajo}, Mecánico: {servicio.mecanico.nombre}")
print()

print(f"Avión: {avion2.matricula}")
print(f"  Tipo: {avion2.tipo.modelo}")
print(f"  Hangar: {avion2.hangar.numero} ({avion2.hangar.ubicacion})")
print(f"  Propietarios:")
for propietario in avion2.propietarios:
    print(f"    - {propietario.nombre}")
print(f"  Servicios:")
for servicio in avion2.servicios:
    print(f"    - Fecha: {servicio.fecha}, Tipo: {servicio.tipo_trabajo}, Mecánico: {servicio.mecanico.nombre}")