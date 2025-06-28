
12. Template Method
¿Qué hace?

Define el esqueleto de un algoritmo en una operación, delegando algunos pasos a las subclases. Permite que las subclases redefinan ciertos pasos sin cambiar la estructura del algoritmo.
Ejemplo simple

Un proceso de "generar reporte" que siempre sigue los mismos pasos generales, pero algunos pasos varían según el tipo de reporte.
Clases involucradas

    AbstractClass: define operaciones primitivas abstractas que las subclases concretas implementarán, e implementa un método plantilla que define el esqueleto del algoritmo.
    ConcreteClass: implementa las operaciones primitivas para llevar a cabo los pasos específicos del algoritmo.
    Cliente: utiliza las clases concretas a través de la interfaz de la clase abstracta.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class AbstractClass {
        +templateMethod()
        +primitiveOperation1()
        +primitiveOperation2()
        +hook()
    }
    class ConcreteClass {
        +primitiveOperation1()
        +primitiveOperation2()
        +hook()
    }
    class Cliente

    AbstractClass <|-- ConcreteClass : Herencia
    Cliente ..> AbstractClass : Usa
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant ConcreteClass

    Cliente->>ConcreteClass: templateMethod()
    activate ConcreteClass
    ConcreteClass->>ConcreteClass: primitiveOperation1()
    ConcreteClass->>ConcreteClass: primitiveOperation2()
    ConcreteClass->>ConcreteClass: hook()
    ConcreteClass-->>Cliente: resultado final
    deactivate ConcreteClass
````