🖨️ Patrón Proxy – Control de Acceso a Impresora

Se implementa el patrón de diseño Proxy para controlar el acceso a una impresora.
La clase Proxy actúa como intermediaria entre el usuario y la impresora real, verificando las credenciales antes de permitir la impresión.

### 📐 Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Impresora {
        <<interface>>
        +imprimir(documento: str)
    }

    class Realimpresora {
        +imprimir(documento: str)
    }

    class Proxy {
        +imprimir(documento: str, usuario: str, password: str)
        -verifica_usuario(usuario: str, password: str): bool
        -_real_impresora: Impresora
        -usuarios_autorizados: dict
    }

    Impresora <|-- Realimpresora
    Impresora <|-- Proxy
    Proxy --> Realimpresora : delega a
```
### 📐 Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Proxy
    participant Realimpresora

    Cliente->>Proxy: imprimir(documento, usuario, password)
    activate Proxy
    Proxy->>Proxy: verifica_usuario(usuario, password)
    alt usuario autorizado
        Proxy->>Realimpresora: imprimir(documento)
        Realimpresora-->>Proxy: OK
    else acceso denegado
        Proxy-->>Cliente: Acceso denegado
    end
    Proxy-->>Cliente: respuesta
    deactivate Proxy
```