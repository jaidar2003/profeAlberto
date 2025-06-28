
11. State
¿Qué hace?

Permite que un objeto altere su comportamiento cuando su estado interno cambia, pareciendo que cambia de clase.
Ejemplo simple

Un reproductor de música cambia entre "Play", "Pause" y "Stop", con comportamientos diferentes en cada estado.
Clases involucradas

    Context: define la interfaz de interés para los clientes y mantiene una instancia del ConcreteState.
    State (abstracto): define una interfaz para encapsular el comportamiento asociado con un estado particular.
    ConcreteState: implementa el comportamiento asociado con un estado del Context.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Context {
        -state: State
        +setState(State)
        +request()
    }
    class State {
        +handle(Context)
    }
    class ConcreteStateA {
        +handle(Context)
    }
    class ConcreteStateB {
        +handle(Context)
    }

    State <|-- ConcreteStateA : Herencia
    State <|-- ConcreteStateB : Herencia
    Context o--> State : Contiene
    ConcreteStateA ..> Context : Cambia estado
    ConcreteStateB ..> Context : Cambia estado
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Context
    participant ConcreteStateA
    participant ConcreteStateB

    Cliente->>Context: request()
    activate Context
    Context->>ConcreteStateA: handle(context)
    activate ConcreteStateA
    ConcreteStateA->>Context: setState(new ConcreteStateB())
    deactivate ConcreteStateA
    deactivate Context
    
    Cliente->>Context: request()
    activate Context
    Context->>ConcreteStateB: handle(context)
    deactivate Context
````