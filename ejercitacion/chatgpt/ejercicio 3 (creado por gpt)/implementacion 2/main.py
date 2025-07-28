from modelo.ciudad import Ciudad
from modelo.universidad import Universidad
from modelo.facultad import Facultad
from modelo.carrera import Carrera
from modelo.profesor import Profesor
from modelo.materia import Materia
from controlador.ciudad_controlador import CiudadControlador
from controlador.universidad_controlador import UniversidadControlador
from controlador.facultad_controlador import FacultadControlador
from controlador.carrera_controlador import CarreraControlador
from controlador.profesor_controlador import ProfesorControlador
from controlador.materia_controlador import MateriaControlador

def main():
    # Crear ciudades
    ciudad_bsas = Ciudad("Buenos Aires")
    ciudad_cba = Ciudad("Córdoba")

    # Crear profesores
    prof_ana = Profesor("Ana García", "123")
    prof_juan = Profesor("Juan López", "456")
    prof_lucia = Profesor("Lucía Gómez", "789")

    # Crear materias
    algebra = Materia("Álgebra", 6)
    fisica = Materia("Física I", 5)
    quimica = Materia("Química", 4)

    # Asignar profesores a materias
    algebra.agregar_profesor(prof_ana)
    fisica.agregar_profesor(prof_juan)
    quimica.agregar_profesor(prof_lucia)
    quimica.agregar_profesor(prof_ana)  # Lucía y Ana comparten esta

    # Crear carreras
    carrera_sistemas = Carrera("Ingeniería en Sistemas", director=prof_ana)
    carrera_quimica = Carrera("Licenciatura en Química", director=prof_lucia)


    carrera_sistemas.agregar_materia(algebra)
    carrera_sistemas.agregar_materia(fisica)
    carrera_quimica.agregar_materia(quimica)

    # Crear facultades
    fac_ing = Facultad("Facultad de Ingeniería", decano=prof_juan)
    fac_cs = Facultad("Facultad de Ciencias Exactas", decano=prof_lucia)
    fac_cj = Facultad("Facultad de Ciencias Jurídicas", decano=prof_ana)  # Nueva facultad para completar el ejemplo


    fac_ing.agregar_carrera(carrera_sistemas)
    fac_cs.agregar_carrera(carrera_quimica)

    # Crear universidades
    uba = Universidad("Universidad de Buenos Aires", ciudad_bsas)
    unc = Universidad("Universidad Nacional de Córdoba", ciudad_cba)

    uba.agregar_facultad(fac_ing)
    uba.agregar_facultad(fac_cs)
    uba.agregar_facultad(fac_cj)  # La UBA también tiene facultad de ciencias jurídicas

    unc.agregar_facultad(fac_ing)  # La UNC también tiene facultad de ingeniería
    unc.agregar_facultad(fac_cs)  # La UNC también tiene facultad de ciencias exactas
    unc.agregar_facultad(fac_cj)  # La UNC también tiene facultad de ciencias jurídicas


    # Convenios
    uba.agregar_convenio(unc)
    unc.agregar_convenio(uba)

    # Relación universidad-ciudad
    ciudad_bsas.agregar_universidad(uba)
    ciudad_cba.agregar_universidad(unc)

    # Imprimir resultados
    print("--- Ciudades ---")
    print(ciudad_bsas)
    print(ciudad_cba)

    print("\n--- Universidades ---")
    print(uba)
    print(unc)

    print("\n--- Facultades ---")
    print(fac_ing)
    print(fac_cs)

    print("\n--- Carreras ---")
    print(carrera_sistemas)
    print(carrera_quimica)

    print("\n--- Materias ---")
    print(algebra)
    print(fisica)
    print(quimica)

    print("\n--- Profesores ---")
    print(prof_ana)
    print(prof_juan)
    print(prof_lucia)
if __name__ == "__main__":
    main()