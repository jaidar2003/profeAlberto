from modelo.ciudad import Ciudad
from modelo.provincia import Provincia
from modelo.pais import Pais

from controlador.controladorCiudad import ControladorCiudad
from controlador.controladorProvincia import ControladorProvincia
from controlador.controladorPais import ControladorPais

def main():
    # Crear controladores
    controlador_ciudad = ControladorCiudad()
    controlador_provincia = ControladorProvincia()
    controlador_pais = ControladorPais()

    # Crear ciudades
    c1 = Ciudad("Ciudad A", 150_000, {"imp1": 5000, "imp2": 4000, "imp3": 3000, "imp4": 2000, "imp5": 1000}, 18000)
    c2 = Ciudad("Ciudad B", 90_000, {"imp1": 3000, "imp2": 2000, "imp3": 1000, "imp4": 500, "imp5": 500}, 6000)
    c3 = Ciudad("Ciudad C", 200_000, {"imp1": 8000, "imp2": 7000, "imp3": 4000, "imp4": 2000, "imp5": 1000}, 25000)
    c4 = Ciudad("Ciudad D", 120_000, {"imp1": 1000, "imp2": 1000, "imp3": 1000, "imp4": 1000, "imp5": 1000}, 8000)

    # Crear provincias
    prov1 = Provincia("Provincia 1")
    controlador_provincia.agregar_ciudad(prov1, c1)
    controlador_provincia.agregar_ciudad(prov1, c2)

    prov2 = Provincia("Provincia 2")
    controlador_provincia.agregar_ciudad(prov2, c3)
    controlador_provincia.agregar_ciudad(prov2, c4)

    # Crear país
    pais = Pais("Mi País")
    controlador_pais.agregar_provincia(pais, prov1)
    controlador_pais.agregar_provincia(pais, prov2)

    # Reportes
    print(controlador_pais.formato_str(pais))

    print("Ciudades con déficit:")
    for ciudad in controlador_pais.ciudades_con_deficit(pais):
        print("-", ciudad.nombre)

    print("Provincias con mayoría de ciudades en déficit:")
    for provincia in controlador_pais.provincias_con_mayoria_en_deficit(pais):
        print("-", provincia.nombre)

    # Demostración de relaciones bidireccionales
    print("\nDemostración de relaciones bidireccionales:")
    print("Ciudad {} pertenece a la provincia {}".format(c1.nombre, c1.provincia.nombre))
    print("Ciudad {} pertenece al país {}".format(c3.nombre, controlador_ciudad.obtener_pais(c3).nombre))
    print("Provincia {} pertenece al país {}".format(prov2.nombre, prov2.pais.nombre))

    # Acceso a todas las ciudades de una provincia
    print("\nCiudades en {}:".format(prov1.nombre))
    for ciudad in prov1.ciudades:
        print("- {} (Pertenece a: {})".format(ciudad.nombre, ciudad.provincia.nombre))

if __name__ == "__main__":
    main()
