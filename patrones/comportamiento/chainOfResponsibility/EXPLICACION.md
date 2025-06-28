
8. Chain of Responsibility
¿Qué hace?

Permite pasar solicitudes a lo largo de una cadena de manejadores, donde cada uno decide si procesa la solicitud o la pasa al siguiente.
Ejemplo simple

Un sistema de soporte donde la consulta escala de operador a supervisor y luego a gerente si nadie la resuelve antes.
Clases involucradas

    Handler (abstracto): define la interfaz para manejar solicitudes y mantener el siguiente manejador.
    ConcreteHandler: implementa el manejo de solicitudes y decide si pasa la solicitud al siguiente.
    Cliente: inicia la solicitud a un manejador concreto en la cadena.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Handler {
        -successor: Handler
        +setNext(Handler): Handler
        +handle(request)
    }
    class ConcreteHandlerA {
        +handle(request)
    }
    class ConcreteHandlerB {
        +handle(request)
    }
    class Cliente

    Handler <|-- ConcreteHandlerA : Herencia
    Handler <|-- ConcreteHandlerB : Herencia
    Handler o--> Handler : Referencia al sucesor
    Cliente ..> Handler : Usa
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant HandlerA as "ConcreteHandlerA"
    participant HandlerB as "ConcreteHandlerB"

    Cliente->>HandlerA: handle(request)
    activate HandlerA
    HandlerA->>HandlerA: ¿Puedo manejar?
    HandlerA->>HandlerB: handle(request)
    activate HandlerB
    HandlerB->>HandlerB: ¿Puedo manejar?
    HandlerB-->>HandlerA: resultado
    deactivate HandlerB
    HandlerA-->>Cliente: resultado final
    deactivate HandlerA
````