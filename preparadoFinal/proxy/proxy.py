from impresora import Impresora

# Proxy (Implementación)
class Proxy(Impresora):
    def __init__(self, real_impresora: Impresora):
        self._real_impresora = real_impresora

        self.usuarios_autorizados = {
            "usuario1": "password1",
            "usuario2": "password2",
            "admin": "admin123"
        }


    def verifica_usuario(self, usuario, password):
        if usuario in self.usuarios_autorizados and self.usuarios_autorizados[usuario] == password:
            return True
        return False

    def imprimir(self, documento: str, usuario: str, password: str) -> None:
        if self.verifica_usuario(usuario, password):
            self._real_impresora.imprimir(documento)
        else:
            print(f"Acceso denegado para el usuario {usuario}.")

