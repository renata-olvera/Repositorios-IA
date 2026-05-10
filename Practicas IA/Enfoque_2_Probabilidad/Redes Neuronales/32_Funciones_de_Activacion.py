# 32 - Funciones de Activación
import math
def escalon(x): return 1 if x >= 0 else 0
def relu(x): return max(0, x)
def sigmoide(x): return 1 / (1 + math.exp(-x))
for x in [-2, -.5, 0, .5, 2]:
    print(x, "escalon", escalon(x), "relu", relu(x), "sigmoide", round(sigmoide(x), 3))
