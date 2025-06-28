from controlador.alumnoControlador import ControladorAlumno
from controlador.profesorControlador import ControladorProfesor
from controlador.cursoControlador import ControladorCurso
from controlador.inscripcionControlador import ControladorInscripcion
from datetime import datetime

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def main():
    ctrl_alumno = ControladorAlumno()
    ctrl_profesor = ControladorProfesor()
    ctrl_curso = ControladorCurso()
    ctrl_inscripcion = ControladorInscripcion()

    alumno = ctrl_alumno.crear_alumno("Juan", "Pérez", "12345")
    profesor = ctrl_profesor.crear_profesor("Ana", "Gómez", "101")
    curso = ctrl_curso.crear_curso("MAT101", "Matemáticas Avanzadas", profesor)

    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    inscripcion = ctrl_inscripcion.crear_inscripcion(alumno, curso, fecha_actual)

    print(ctrl_curso.representar(curso))
    print("\nInscripciones:")
    for ins in curso.inscriptos:
        print(ctrl_inscripcion.representar(ins))

if __name__ == "__main__":
    main()
