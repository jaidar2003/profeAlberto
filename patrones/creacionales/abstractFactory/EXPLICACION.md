
2. Abstract Factory
¿Qué hace?

Define una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas.
Permite crear objetos que siguen un patrón común y son compatibles entre sí.
Ejemplo simple

Una interfaz gráfica puede tener tema claro y tema oscuro, con distintos botones y menús.
Clases involucradas

    AbstractFactory: define la interfaz para crear los diferentes tipos de productos.
    ConcreteFactory: implementa la creación de productos concretos.
    AbstractProductA/B: define la interfaz para un tipo de producto.
    ConcreteProductA/B: implementa la interfaz del producto específico.
    Cliente: utiliza las interfaces declaradas por AbstractFactory y AbstractProduct.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class AbstractFactory {
        +createProductA()
        +createProductB()
    }
    class ConcreteFactory {
        +createProductA()
        +createProductB()
    }
    class AbstractProductA {
        +operationA()
    }
    class AbstractProductB {
        +operationB()
    }
    class ConcreteProductA {
        +operationA()
    }
    class ConcreteProductB {
        +operationB()
    }
    class Cliente

    AbstractFactory <|-- ConcreteFactory : Herencia
    AbstractProductA <|-- ConcreteProductA : Herencia
    AbstractProductB <|-- ConcreteProductB : Herencia
    ConcreteFactory ..> ConcreteProductA : Crea
    ConcreteFactory ..> ConcreteProductB : Crea
    Cliente ..> AbstractFactory : Usa
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant ConcreteFactory
    participant ConcreteProductA
    participant ConcreteProductB

    Cliente->>ConcreteFactory: createProductA()
    activate ConcreteFactory
    ConcreteFactory->>ConcreteProductA: crear
    ConcreteFactory-->>Cliente: ProductA
    deactivate ConcreteFactory

    Cliente->>ConcreteFactory: createProductB()
    activate ConcreteFactory
    ConcreteFactory->>ConcreteProductB: crear
    ConcreteFactory-->>Cliente: ProductB
    deactivate ConcreteFactory
````