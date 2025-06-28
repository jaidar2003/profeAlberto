class PersonaControlador:
    def __init__(self):
        self.personas = []
    
    def get_nombre(self, persona):
        return persona._nombre
    
    def get_apellido(self, persona):
        return persona._apellido
    
    def get_facturas(self, persona):
        return persona._facturas
    
    def agregar_factura(self, persona, factura):
        persona._facturas.append(factura)
    
    def formato_str(self, persona):
        return f"{persona._nombre} {persona._apellido}"
    
    def formato_repr(self, persona):
        return f"Persona(nombre={persona._nombre}, apellido={persona._apellido})"