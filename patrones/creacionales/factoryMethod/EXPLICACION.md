
1. Factory Method
¿Qué hace?

Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar.
Permite la creación de objetos sin especificar su clase concreta.
Ejemplo simple

Un juego crea enemigos distintos (zombie, vampiro) según el nivel.
Clases involucradas

    Creator: define el metodo de creacion factoryMethod()
    ConcreteCreator: implementa el factoryMethod() para crear un tipo específico de producto.
    Product (abstracto): define la interfaz del producto.
    ConcreteProduct: implementa la interfaz del producto.
    Cliente: utiliza el Creator para obtener productos sin conocer su clase concreta.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Creator {
        +factoryMethod()
    }
    class ConcreteCreator {
        +factoryMethod()
    }
    class Product
    class ConcreteProduct
    class Cliente

    Creator <|-- ConcreteCreator : Herencia
    Product <|-- ConcreteProduct : Herencia
    Cliente ..> Creator : Dependencia
    ConcreteCreator ..> ConcreteProduct : Dependencia
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant ConcreteCreator
    participant ConcreteProduct

    Cliente->>ConcreteCreator: factoryMethod()
    activate ConcreteCreator
    ConcreteCreator->>ConcreteProduct: crear instancia
    ConcreteCreator-->>Cliente: retorna Product
    deactivate ConcreteCreator
````