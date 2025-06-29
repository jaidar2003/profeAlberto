from alumno import Alumno
from curso import Curso
from persona import Persona
from profesor import Profesor
from inscripcion import Inscripcion
from datetime import datetime

def main():
    # Crear instancias de las clases
    alumno1 = Alumno("Juan", "Pérez", "12345")
    profesor1 = Profesor("Ana", "Gómez", "101")
    curso1 = Curso("MAT101", "Matemáticas Avanzadas", profesor1)

    # Crear una inscripción
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    inscripcion1 = Inscripcion(alumno1, curso1, fecha_actual)

    # Mostrar información del curso
    print(curso1)

    # Mostrar inscripciones
    print("\nInscripciones:")
    for inscripcion in curso1.inscriptos:
        print(inscripcion)

if __name__ == "__main__":
    main()
