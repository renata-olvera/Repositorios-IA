# 13 - Busqueda de Temple Simulado
# Puede aceptar un peor movimiento al inicio.

import random
import math

random.seed(13)

def f(x):
    return -(x - 6) ** 2 + 36

x = 0
temp = 10

for i in range(15):
    vecino = x + random.choice([-1, 1])
    cambio = f(vecino) - f(x)

    if cambio > 0 or random.random() < math.exp(cambio / temp):
        x = vecino

    temp *= 0.85
    print("Paso", i + 1, "x:", x, "valor:", f(x))

print("Solucion aproximada:", x)
