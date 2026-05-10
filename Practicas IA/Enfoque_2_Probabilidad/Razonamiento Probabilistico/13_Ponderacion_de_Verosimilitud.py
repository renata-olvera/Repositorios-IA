# 13 - Ponderación de Verosimilitud
# Ejemplo: evidencia Pasto=True sin rechazar muestras.
import random
random.seed(13)

def evento(p): return random.random() < p
pesos = {True: 0.0, False: 0.0}
tabla = {(True, True): .99, (True, False): .85, (False, True): .75, (False, False): .05}

for _ in range(5000):
    lluvia = evento(.30)
    asp = evento(.10 if lluvia else .50)
    pesos[lluvia] += tabla[(lluvia, asp)]

z = pesos[True] + pesos[False]
print("P(Lluvia | Pasto=True) aprox:", round(pesos[True] / z, 4))
