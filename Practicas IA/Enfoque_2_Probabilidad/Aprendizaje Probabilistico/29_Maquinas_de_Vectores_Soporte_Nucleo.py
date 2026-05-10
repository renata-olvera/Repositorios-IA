# 29 - Máquinas de Vectores Soporte con Núcleo
# Ejemplo: kernel RBF.
import math
soportes = [((1,1), -1, .8), ((2,1), -1, .6), ((4,4), 1, .7), ((5,4), 1, .9)]
def rbf(a, b, gamma=.5):
    return math.exp(-gamma * ((a[0]-b[0])**2 + (a[1]-b[1])**2))
punto = (4.2, 3.8)
valor = sum(peso * y * rbf(punto, x) for x, y, peso in soportes)
print("valor decision:", round(valor, 4))
print("clase:", 1 if valor >= 0 else -1)
