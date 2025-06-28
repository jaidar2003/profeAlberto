
9. Command
¿Qué hace?

Encapsula una solicitud como un objeto, permitiendo parametrizar clientes con diferentes solicitudes, encolar solicitudes, y soportar operaciones reversibles.
Ejemplo simple

Un botón "Deshacer" en un editor de texto que revierte la última acción.
Clases involucradas

    Command (interfaz): declara una interfaz para ejecutar una operación.
    ConcreteCommand: implementa la interfaz Command y define la vinculación entre el Receiver y una acción.
    Invoker: solicita al Command que ejecute la petición.
    Receiver: sabe cómo realizar las operaciones asociadas a una petición.
    Cliente: crea un ConcreteCommand y establece su Receiver.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Command {
        +execute()
        +undo()
    }
    class ConcreteCommand {
        -receiver: Receiver
        +execute()
        +undo()
    }
    class Invoker {
        -command: Command
        +setCommand(Command)
        +executeCommand()
    }
    class Receiver {
        +action()
    }
    class Cliente

    Command <|-- ConcreteCommand : Implementa
    Invoker o--> Command : Contiene
    ConcreteCommand o--> Receiver : Referencia
    Cliente ..> ConcreteCommand : Crea
    Cliente ..> Receiver : Crea
    Cliente ..> Invoker : Configura
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Invoker
    participant ConcreteCommand
    participant Receiver

    Cliente->>ConcreteCommand: new ConcreteCommand(receiver)
    Cliente->>Invoker: setCommand(command)
    Cliente->>Invoker: executeCommand()
    activate Invoker
    Invoker->>ConcreteCommand: execute()
    activate ConcreteCommand
    ConcreteCommand->>Receiver: action()
    Receiver-->>ConcreteCommand: resultado
    ConcreteCommand-->>Invoker: resultado
    deactivate ConcreteCommand
    Invoker-->>Cliente: resultado
    deactivate Invoker
````