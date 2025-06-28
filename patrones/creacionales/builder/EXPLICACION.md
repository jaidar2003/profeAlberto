
4. Builder
¿Qué hace?

Permite construir objetos complejos paso a paso, separando el proceso de construcción de la representación final.
Ejemplo simple

Armar una pizza eligiendo masa, salsa, ingredientes y cocción en cualquier orden.
Clases involucradas

    Director: controla el algoritmo de construcción usando el Builder.
    Builder (abstracto): define la interfaz para crear las partes del producto.
    ConcreteBuilder: implementa la interfaz Builder para construir y ensamblar partes del producto.
    Product: representa el objeto complejo que se está construyendo.
    Cliente: crea el Director y lo configura con el Builder deseado.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Director {
        +construct()
    }
    class Builder {
        +buildPartA()
        +buildPartB()
        +getResult() : Product
    }
    class ConcreteBuilder {
        +buildPartA()
        +buildPartB()
        +getResult() : Product
    }
    class Product
    class Cliente

    Builder <|-- ConcreteBuilder : Herencia
    Director o--> Builder : Asociación
    ConcreteBuilder ..> Product : Crea
    Cliente ..> Director : Usa
    Cliente ..> ConcreteBuilder : Crea
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Director
    participant ConcreteBuilder
    participant Product

    Cliente->>ConcreteBuilder: new ConcreteBuilder()
    Cliente->>Director: new Director(builder)
    Cliente->>Director: construct()
    activate Director
    Director->>ConcreteBuilder: buildPartA()
    ConcreteBuilder->>Product: setPartA()
    Director->>ConcreteBuilder: buildPartB()
    ConcreteBuilder->>Product: setPartB()
    deactivate Director
    Cliente->>ConcreteBuilder: getResult()
    ConcreteBuilder-->>Cliente: Product
````