from ciudad import Ciudad
from provincia import Provincia
from pais import Pais
from continente import Continente


def main():
    # Crear ciudades
    buenos_aires = Ciudad("Buenos Aires", 3000000)
    cordoba = Ciudad("Córdoba", 1500000)
    rosario = Ciudad("Rosario", 1200000)
    la_plata = Ciudad("La Plata", 800000)

    # Crear países (inicialmente sin provincias)
    argentina = Pais("Argentina", buenos_aires)
    chile = Pais("Chile", Ciudad("Santiago", 5000000))
    brasil = Pais("Brasil", Ciudad("Brasilia", 3000000))

    # Crear provincias
    buenos_aires_prov = Provincia("Buenos Aires", la_plata, argentina)
    cordoba_prov = Provincia("Córdoba", cordoba, argentina)
    santa_fe = Provincia("Santa Fe", rosario, argentina)

    # Agregar ciudades a provincias
    buenos_aires_prov.agregar_ciudad(buenos_aires)

    # Establecer relaciones entre provincias
    buenos_aires_prov.agregar_provincia_vecina(cordoba_prov)
    buenos_aires_prov.agregar_provincia_vecina(santa_fe)

    # Agregar provincias a países
    argentina.agregar_provincia(buenos_aires_prov)
    argentina.agregar_provincia(cordoba_prov)
    argentina.agregar_provincia(santa_fe)

    # Establecer países vecinos
    argentina.agregar_vecino(chile)
    argentina.agregar_vecino(brasil)

    # Establecer países limítrofes para provincias
    buenos_aires_prov.agregar_pais_limitrofe(chile)

    # Crear continente
    america_sur = Continente("América del Sur")
    america_sur.agregar_pais(argentina)
    america_sur.agregar_pais(chile)
    america_sur.agregar_pais(brasil)

    # Mostrar información
    print(america_sur)
    print(argentina)
    print(buenos_aires_prov)
    print(cordoba_prov)
    print(santa_fe)
    print(buenos_aires)
    print(cordoba)
    print(rosario)
    print(la_plata)



if __name__ == "__main__":
    main()