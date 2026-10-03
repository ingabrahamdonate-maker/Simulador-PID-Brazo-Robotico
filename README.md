#Simulador de controlador PID

Simulación en Python de un controlador PID que mueve la articulación de un
brazo robótico hasta un ángulo objetivo. A los 5 segundos aparece una carga
extra que empuja el brazo hacia atrás, para ver cómo reacciona el controlador.

## Cómo correrlo

```
pip install -r requirements.txt
python simulador_pid.py
```

Se abre una gráfica con el ángulo del brazo y el voltaje que manda el controlador.

## Qué es un PID

El controlador mira el **error** (objetivo menos lo que tengo) y calcula una
salida sumando tres partes:

- **P (proporcional):** reacciona al error de ahora. `kp * error`.
- **I (integral):** reacciona al error acumulado en el tiempo. Elimina el error
  permanente que se queda cuando hay una carga constante.
- **D (derivativa):** reacciona a qué tan rápido cambia el error. Amortigua
  las oscilaciones.

## Experimentos

Cambia las ganancias en `simulador_pid.py` y anota qué ves en la gráfica.

| kp | ki | kd | Qué observé |
|----|----|----|-------------|
| 8  | 0  | 0  |             |
| 8  | 0  | 4  |             |
| 8  | 4  | 4  |             |
| 2  | 0  | 0  |             |
| 20 | 10 | 8  |             |

## Qué aprendí

-
