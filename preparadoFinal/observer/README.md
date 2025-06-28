## 🛰️ Patrón Observer – Estación Meteorológica

Se implementa el patrón de diseño **Observer** aplicándolo a una Estación Meteorológica. La clase `EstacionMeteorologica` actúa como **Sujeto**, notificando a múltiples observadores (`PantallaCelular`, `PantallaReloj`) cuando cambian los datos de temperatura, humedad y presión.

### 📐 Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    class EstacionMeteorologica {
        - observadores: List<Pantalla>
        - temperatura: float
        - humedad: float
        - presion: float
        + registrar(obs: Pantalla)
        + quitar(obs: Pantalla)
        + notificar()
        + cambiar_datos(temp: float, hum: float, pres: float)
    }

    class Pantalla {
        <<interface>>
        + actualizar(temp: float, hum: float, pres: float)
    }

    class PantallaCelular {
        + actualizar(temp: float, hum: float, pres: float)
    }

    class PantallaSmartWatch {
        + actualizar(temp: float, hum: float, pres: float)
    }

    EstacionMeteorologica --> Pantalla : notifica a
    Pantalla <|-- PantallaCelular
    Pantalla <|-- PantallaSmartWatch
```
### 📐 Diagrama de Secuencia (Mermaid)

```mermaid
sequenceDiagram
    participant Estacion as EstacionMeteorologica
    participant Celular as PantallaCelular
    participant Reloj as PantallaSmartWatch

    Estacion->>Celular: actualizar(temp, hum, pres)
    Estacion->>Reloj: actualizar(temp, hum, pres)
```
