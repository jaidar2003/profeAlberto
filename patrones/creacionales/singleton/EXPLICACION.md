
3. Singleton
¿Qué hace?

Asegura que una clase tenga una sola instancia y proporciona un punto de acceso global a ella.
Ejemplo simple

Una única instancia de conexión a base de datos para toda la aplicación.
Clases involucradas

    Singleton: contiene un método estático getInstance() que devuelve la misma instancia.


# Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class Singleton {
        -static instancia: Singleton
        -constructor()
        +static getInstance(): Singleton
        +operacion()
    }
````

# Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Cliente
    participant Singleton

    Cliente->>Singleton: getInstance()
    activate Singleton
    Singleton-->>Cliente: instancia única
    deactivate Singleton
    
    Cliente->>Singleton: operacion()
````