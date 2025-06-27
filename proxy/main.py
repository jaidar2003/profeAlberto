from impresora import Impresora
from realimpresora import Realimpresora
from proxy import Proxy


def main():
    # Crear una instancia de la impresora real
    impresora_real = Realimpresora("HP LaserJet")

    # Crear un proxy que envuelve la impresora real
    proxy_impresora = Proxy(impresora_real)

    # Intentar imprimir con diferentes usuarios
    documentos = [
        ("Documento 1", "usuario1", "password1"),
        ("Documento 2", "usuario3", "wrongpassword")
    ]

    for documento, usuario, password in documentos:
        print(f"Intentando imprimir '{documento}' con usuario '{usuario}':")
        proxy_impresora.imprimir(documento, usuario, password)
        print("-" * 40)

if __name__ == "__main__":
    main()