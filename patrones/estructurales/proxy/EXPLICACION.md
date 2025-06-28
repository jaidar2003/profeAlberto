
7. Proxy
¿Qué hace?

Proporciona un sustituto o representante de otro objeto para controlar el acceso a este.
Ejemplo simple

Un proxy de impresora que verifica permisos antes de enviar a imprimir.
Clases involucradas

    Subject (interfaz): define la interfaz común para RealSubject y Proxy.
    RealSubject: define el objeto real que el Proxy representa.
    Proxy: mantiene una referencia al RealSubject y controla el acceso a él.
    Cliente: interactúa con el Subject sin conocer si está usando el RealSubject o el Proxy.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Subject {
        +request()
    }
    class RealSubject {
        +request()
    }
    class Proxy {
        -realSubject: RealSubject
        +request()
    }
    class Cliente

    Subject <|-- RealSubject : Implementa
    Subject <|-- Proxy : Implementa
    Proxy o--> RealSubject : Referencia
    Cliente ..> Subject : Usa
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Proxy
    participant RealSubject

    Cliente->>Proxy: request()
    activate Proxy
    Proxy->>Proxy: verificar acceso
    Proxy->>RealSubject: request()
    RealSubject-->>Proxy: resultado
    Proxy-->>Cliente: resultado
    deactivate Proxy
````