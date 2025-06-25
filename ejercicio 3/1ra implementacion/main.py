from ciudad import Ciudad
from provincia import Provincia
from pais import Pais

def main():
    # Crear ciudades
    c1 = Ciudad("Ciudad A", 150_000, {"imp1": 5000, "imp2": 4000, "imp3": 3000, "imp4": 2000, "imp5": 1000}, 18000)
    c2 = Ciudad("Ciudad B", 90_000, {"imp1": 3000, "imp2": 2000, "imp3": 1000, "imp4": 500, "imp5": 500}, 6000)
    c3 = Ciudad("Ciudad C", 200_000, {"imp1": 8000, "imp2": 7000, "imp3": 4000, "imp4": 2000, "imp5": 1000}, 25000)
    c4 = Ciudad("Ciudad D", 120_000, {"imp1": 1000, "imp2": 1000, "imp3": 1000, "imp4": 1000, "imp5": 1000}, 8000)

    # Crear provincias
    prov1 = Provincia("Provincia 1")
    prov1.agregar_ciudad(c1)
    prov1.agregar_ciudad(c2)

    prov2 = Provincia("Provincia 2")
    prov2.agregar_ciudad(c3)
    prov2.agregar_ciudad(c4)

    # Crear país
    pais = Pais("Mi País")
    pais.agregar_provincia(prov1)
    pais.agregar_provincia(prov2)

    # Reportes
    print(pais)

    print("Ciudades con déficit:")
    for ciudad in pais.ciudades_con_deficit():
        print("-", ciudad.nombre)

    print("Provincias con mayoría de ciudades en déficit:")
    for provincia in pais.provincias_con_mayoria_en_deficit():
        print("-", provincia.nombre)

    # Demostración de relaciones bidireccionales
    print("\nDemostración de relaciones bidireccionales:")
    print(f"Ciudad {c1.nombre} pertenece a la provincia {c1.provincia.nombre}")
    print(f"Ciudad {c3.nombre} pertenece al país {c3.pais().nombre}")
    print(f"Provincia {prov2.nombre} pertenece al país {prov2.pais.nombre}")

    # Acceso a todas las ciudades de una provincia
    print(f"\nCiudades en {prov1.nombre}:")
    for ciudad in prov1.ciudades:
        print(f"- {ciudad.nombre} (Pertenece a: {ciudad.provincia.nombre})")

if __name__ == "__main__":
    main()
