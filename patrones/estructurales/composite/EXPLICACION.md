
5. Composite
¿Qué hace?

Permite tratar objetos individuales y composiciones de objetos de manera uniforme.
Ejemplo simple

Un menú de aplicación: una opción simple ("Salir") o un submenú con más opciones.
Clases involucradas

    Component (abstracto): declara la interfaz común para objetos simples y compuestos.
    Leaf: representa objetos simples que no tienen hijos.
    Composite: representa objetos compuestos que pueden tener hijos.
    Cliente: manipula los objetos a través de la interfaz Component.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Component {
        +operation()
        +add(Component)
        +remove(Component)
        +getChild(int)
    }
    class Leaf {
        +operation()
    }
    class Composite {
        +operation()
        +add(Component)
        +remove(Component)
        +getChild(int)
    }
    class Cliente

    Component <|-- Leaf : Herencia
    Component <|-- Composite : Herencia
    Composite o-- Component : Composición
    Cliente ..> Component : Usa
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Composite
    participant Leaf1 as "Leaf 1"
    participant Leaf2 as "Leaf 2"

    Cliente->>Composite: operation()
    activate Composite
    Composite->>Leaf1: operation()
    Leaf1-->>Composite: resultado1
    Composite->>Leaf2: operation()
    Leaf2-->>Composite: resultado2
    Composite-->>Cliente: resultado combinado
    deactivate Composite
````