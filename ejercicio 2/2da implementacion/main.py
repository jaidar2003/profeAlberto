from controlador.controladorCiudad import ControladorCiudad
from controlador.controladorContinente import ControladorContinente
from controlador.controladorPais import ControladorPais
from controlador.controladorProvincia import ControladorProvincia

# Instancias de controladores
ctrl_ciudad = ControladorCiudad()
ctrl_continente = ControladorContinente()
ctrl_pais = ControladorPais()
ctrl_provincia = ControladorProvincia()

# Crear objetos base
america = ctrl_continente.crear_continente("América del Sur")
bs_as = ctrl_ciudad.crear_ciudad("Buenos Aires")

# Crear país
argentina = ctrl_pais.crear_pais("Argentina", bs_as, america)

# Crear provincia y asociarla
cordoba = ctrl_provincia.crear_provincia("Córdoba", ctrl_ciudad.crear_ciudad("Córdoba Capital"))
ctrl_pais.agregar_provincia(argentina, cordoba)

# Mostrar
print(f"País: {argentina.nombre}, capital: {argentina.capital.nombre}")
print("Provincias:", [p.nombre for p in argentina.provincia])
