
10. Observer
¿Qué hace?

Define una dependencia uno-a-muchos entre objetos, de modo que cuando un objeto cambia su estado, todos sus dependientes son notificados y actualizados automáticamente.
Ejemplo simple

Suscripción a un canal de YouTube: los usuarios reciben notificaciones de nuevos videos.
Clases involucradas

    Subject (abstracto): conoce a sus observadores y proporciona métodos para añadir y eliminar observadores.
    ConcreteSubject: almacena el estado de interés para los observadores y envía notificaciones.
    Observer (abstracto): define una interfaz de actualización para los objetos que deben ser notificados.
    ConcreteObserver: implementa la interfaz de actualización para mantener su estado consistente con el Subject.
    Cliente: crea los objetos ConcreteSubject y ConcreteObserver y registra los observadores.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Subject {
        -observers: List<Observer>
        +attach(Observer)
        +detach(Observer)
        +notify()
    }
    class ConcreteSubject {
        -state
        +getState()
        +setState(state)
    }
    class Observer {
        +update()
    }
    class ConcreteObserver {
        -state
        -subject: ConcreteSubject
        +update()
    }
    class Cliente

    Subject <|-- ConcreteSubject : Herencia
    Observer <|-- ConcreteObserver : Herencia
    Subject o--> Observer : Observa
    ConcreteObserver --> ConcreteSubject : Referencia
    Cliente ..> ConcreteSubject : Crea
    Cliente ..> ConcreteObserver : Crea
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant ConcreteSubject
    participant ConcreteObserver1 as "ConcreteObserver 1"
    participant ConcreteObserver2 as "ConcreteObserver 2"

    Cliente->>ConcreteSubject: setState(newState)
    activate ConcreteSubject
    ConcreteSubject->>ConcreteSubject: notify()
    ConcreteSubject->>ConcreteObserver1: update()
    activate ConcreteObserver1
    ConcreteObserver1->>ConcreteSubject: getState()
    ConcreteSubject-->>ConcreteObserver1: state
    deactivate ConcreteObserver1
    
    ConcreteSubject->>ConcreteObserver2: update()
    activate ConcreteObserver2
    ConcreteObserver2->>ConcreteSubject: getState()
    ConcreteSubject-->>ConcreteObserver2: state
    deactivate ConcreteObserver2
    deactivate ConcreteSubject
````