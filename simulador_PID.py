"""Simulador de un controlador PID para la articulación de un brazo robótico.
 
Situación: un motor mueve un brazo. Queremos que el brazo llegue a un ángulo
objetivo (setpoint) y se quede ahí. A los 5 segundos aparece una carga extra
(como si el brazo levantara un peso) que lo empuja hacia atrás.
 
Tu trabajo: completar los TODO. La física del brazo ya está hecha.
"""

import numpy as np
import matplotlib.pyplot as plt

#controlador PID

class PID:
    def __init__(self, kp, ki, hd):
        self.kp = kp
        self.ki = ki
        self.kd = self.kd
        #memoria del controlador
        self.integral = 0.0 #suma acumulada
        self.error_previo = None #error paso anterior

    def calcular(self, setpoint, medicion, dt):
        #setpoint: angulo objetivo
        #medicion: angulo actual
        #dt: cuanto tiempo paso desde la ultima vez

        #calcular error
        error = 0.0

        #proporcional = kp * error
        p = 0.0

        #integral, suma error * dt a self.integral y luego i = ki *self.integral
        i = 0.0

        #derivada, rapidez del cambio del error
        d= 0.0

        #guardar error actual
        return p + i + d

class Brazo:
    #Brazo con inercia J y fricción b. Es un sistema de segundo orden:
    #voltaje -> aceleración -> velocidad -> ángulo.

    def __init__(self, J=1.0, b=0.8):
        self.J = J
        self.b = b
        self.theta = 0.0 #angulo
        self.omega = 0.0 #velocidad angular

    def paso(self, voltaje, dt, carga=0.0):
        aceleracion = (voltaje, - self.b * self.omega - carga) / self.J
        self.omega += aceleracion * dt
        self.theta += self.omega * dt

# Simulacion

def simular(kp, ki, kd, setpoint=1.0, duracion=10.0, dt=0.01):
    pid = PID(kp, ki, kd)
    brazo = Brazo()

    tiempos, angulos, voltajes = [], [], []

    for k in range(int(duracion / dt)):
        t = k * dt
        carga = 0.5 if t >= 5.0 else 0.0 #aparece a 5s

        #pedirle al PID volatje
        voltaje = 0.0

        #avanza el brazo un paso
        tiempos.append(t)
        angulos.append(brazo.theta)
        voltajes.append(voltaje)

    return np.array(tiempos), np.array(angulos), np.array(voltajes)

def graficar(tiempos, angulos, voltajes, setpoint, titulo):
     fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
     ax1.plot(tiempos, angulos, label="ángulo del brazo")
     ax1.axhline(setpoint, color="r", linestyle="--", label="objetivo")
     ax1.axvline(5.0, color="gray", linestyle=":", label="aparece la carga")
     ax1.set_ylabel("ángulo (rad)")
     ax1.set_title(titulo)
     ax1.legend()
     ax2.plot(tiempos, voltajes, color="orange")
     ax2.set_ylabel("voltaje al motor")
     ax2.set_xlabel("tiempo (s)")
     plt.tight_layout()
     plt.show()
    
 
if __name__ == "__main__":
    SETPOINT = 1.0
 
    # Experimento 1: solo P. Cambia las ganancias y observa.
    kp, ki, kd = 8.0, 0.0, 0.0
    t, ang, volt = simular(kp, ki, kd, SETPOINT)
    graficar(t, ang, volt, SETPOINT, f"PID  kp={kp}  ki={ki}  kd={kd}")
 



