from Ciudad import Ciudad
from Pais import Pais
from Provincias import Provincia
from Continente import Continente

def main():
    # Crear un continente
    america = Continente("América")

    # Crear un país
    argentina = Pais("Argentina", "CABA", america)

    # Crear provincias
    provincia1 = Provincia("Mendoza", "Mendoza")
    provincia2 = Provincia("Córdoba", "Córdoba")

    # Agregar provincias al país
    argentina.agregar_provincia(provincia1)
    argentina.agregar_provincia(provincia2)

    # Crear ciudades
    ciudad1 = Ciudad("Maipu")
    ciudad2 = Ciudad("Villa Carlos Paz")

    # Agregar ciudades a las provincias
    provincia1.agregar_ciudad(ciudad1)
    provincia2.agregar_ciudad(ciudad2)

    # Imprimir información del país y sus provincias
    print(f"País: {argentina.nombre}, Capital: {argentina.capital}")
    for provincia in argentina.provincias:
        print(f"  Provincia: {provincia.nombre}, Capital: {provincia.capital}")
        for ciudad in provincia.ciudades:
            print(f"    Ciudad: {ciudad.nombre}")


if __name__ == "__main__":
    main()