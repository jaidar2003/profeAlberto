from modelo.administrativo import Administrativo

class AdministrativoControlador:
    def __init__(self):
        self.administrativos = []
    
    def crear_administrativo(self, nombre, apellido, cargo="Administrativo"):
        administrativo = Administrativo(nombre, apellido, cargo)
        self.administrativos.append(administrativo)
        return administrativo
    
    def get_nombre(self, administrativo):
        return administrativo._nombre
    
    def get_apellido(self, administrativo):
        return administrativo._apellido
    
    def get_cargo(self, administrativo):
        return administrativo._cargo
    
    def agregar_factura(self, administrativo, factura):
        administrativo._facturas.append(factura)
    
    def formato_str(self, administrativo):
        return f"{administrativo._nombre} {administrativo._apellido} ({administrativo._cargo})"
    
    def formato_repr(self, administrativo):
        return f"Administrativo(nombre={administrativo._nombre}, apellido={administrativo._apellido}, cargo={administrativo._cargo})"