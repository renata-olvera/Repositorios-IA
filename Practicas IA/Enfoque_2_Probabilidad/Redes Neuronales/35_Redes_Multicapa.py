# 35 - Redes Multicapa
import math
def sig(x): return 1 / (1 + math.exp(-x))
entrada = [1.0, .5]
W1 = [[.4, .7], [-.3, .8]]
W2 = [.6, -.2]
oculta = [sig(sum(x*w for x, w in zip(entrada, fila))) for fila in W1]
salida = sig(sum(h*w for h, w in zip(oculta, W2)))
print("oculta:", [round(x, 3) for x in oculta])
print("salida:", round(salida, 3))
