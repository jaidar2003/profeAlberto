from celular import PantallaCelular
from pantalla import Pantalla
from reloj import PantallaReloj
from estacionLocal import EstacionLocal
from estacionRemota import EstacionRemota

def main():
    # Crear la estación meteorológica
    estacion = EstacionLocal()
    estacion2 = EstacionRemota()  # Fixed variable name

    # Crear observadores
    pantalla_celular = PantallaCelular()
    pantalla_reloj = PantallaReloj()

    # Registrar observadores en la estación
    estacion.registrar_observador(pantalla_celular)
    estacion.registrar_observador(pantalla_reloj)
    estacion2.registrar_observador(pantalla_celular)
    estacion2.registrar_observador(pantalla_reloj)

    # Cambiar datos meteorológicos
    estacion.cambiar_datos(25, 60, 1013)
    estacion2.cambiar_datos(30, 50, 1010)

if __name__ == "__main__":
    main()