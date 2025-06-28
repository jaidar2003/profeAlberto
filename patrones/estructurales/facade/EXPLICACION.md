
6. Facade
¿Qué hace?

Proporciona una interfaz unificada y simplificada para un conjunto de interfaces en un subsistema.
Ejemplo simple

Un solo método para imprimir un documento, aunque implique varias operaciones internas (abrir archivo, formatear, enviar a impresora).
Clases involucradas

    Facade: proporciona una interfaz simplificada al subsistema.
    SubSistemaA/B/C: implementan la funcionalidad del subsistema.
    Cliente: utiliza la Facade para interactuar con el subsistema.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Facade {
        +operacionSimple()
    }
    class SubSistemaA {
        +operacionA()
    }
    class SubSistemaB {
        +operacionB()
    }
    class SubSistemaC {
        +operacionC()
    }
    class Cliente

    Facade ..> SubSistemaA : Usa
    Facade ..> SubSistemaB : Usa
    Facade ..> SubSistemaC : Usa
    Cliente ..> Facade : Usa
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Facade
    participant SubSistemaA
    participant SubSistemaB
    participant SubSistemaC

    Cliente->>Facade: operacionSimple()
    activate Facade
    Facade->>SubSistemaA: operacionA()
    Facade->>SubSistemaB: operacionB()
    Facade->>SubSistemaC: operacionC()
    Facade-->>Cliente: resultado
    deactivate Facade
````