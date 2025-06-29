class SedeOlimpica:
    def __init__(self, numero_complejos, presupuesto):
        self.numero_complejos = numero_complejos
        self.presupuesto = presupuesto
        self.complejos = []  # Lista de complejos deportivos

    def agregar_complejo(self, complejo):
        self.complejos.append(complejo)
