from controlador.cCiudad import cCiudad
from controlador.cProvincia import cProvincia
from controlador.cPais import cPais

def main():
    pais = cPais("República de Ejemplo")

    andes = cProvincia("Andes", pais)
    andes.agregar_ciudad(cCiudad("Nevada", 120000, [100000, 110000, 105000, 95000, 90000], 520000))
    andes.agregar_ciudad(cCiudad("Valle Azul", 80000, [50000, 55000, 45000, 60000, 40000], 200000))
    andes.agregar_ciudad(cCiudad("Piedra Alta", 150000, [110000, 100000, 95000, 105000, 90000], 480000))

    llanura = cProvincia("Llanura", pais)
    llanura.agregar_ciudad(cCiudad("Campo Verde", 200000, [120000, 130000, 110000, 140000, 100000], 580000))
    llanura.agregar_ciudad(cCiudad("Laguna Sur", 220000, [100000, 90000, 85000, 95000, 80000], 520000))

    provincias = [andes, llanura]

    ciudades_deficit = []
    for provincia in provincias:
        for ciudad in provincia.ciudades_grandes_en_deficit():
            ciudades_deficit.append(f"{ciudad.nombre} ({provincia.nombre})")

    provincias_mas_mitad_deficit = [p.nombre for p in provincias if p.mas_de_mitad_grandes_en_deficit()]

    print("Ciudades grandes con déficit fiscal:")
    for nombre in ciudades_deficit:
        print("-", nombre)

    print("\nProvincias con más de la mitad de sus ciudades grandes en déficit:")
    for nombre in provincias_mas_mitad_deficit:
        print("-", nombre)

if __name__ == "__main__":
    main()