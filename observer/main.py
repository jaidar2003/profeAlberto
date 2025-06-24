from celular import PantallaCelular
from pantalla import Pantalla
from reloj import PantallaReloj
from estacion import EstacionMeteorologica

def main():
    # Crear la estación meteorológica
    estacion = EstacionMeteorologica()

    # Crear observadores
    pantalla_celular = PantallaCelular()
    pantalla_reloj = PantallaReloj()

    # Registrar observadores en la estación
    estacion.registrar(pantalla_celular)
    estacion.registrar(pantalla_reloj)

    # Cambiar datos meteorológicos
    estacion.cambiar_datos(25, 60, 1013)
    estacion.cambiar_datos(30, 50, 1010)

# Ejecutar la función main si este script se ejecuta directamente
if __name__ == "__main__":
    main()
