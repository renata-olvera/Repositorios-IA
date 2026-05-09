# 15 - Algoritmos Geneticos
# Usa seleccion, cruza y mutacion.

import random

random.seed(15)

def aptitud(individuo):
    return individuo.count("1")

poblacion = ["0101", "1001", "1110", "0001"]

for gen in range(5):
    poblacion.sort(key=aptitud, reverse=True)

    padre1 = poblacion[0]
    padre2 = poblacion[1]

    hijo = padre1[:2] + padre2[2:]

    pos = random.randrange(len(hijo))
    hijo = hijo[:pos] + ("1" if hijo[pos] == "0" else "0") + hijo[pos + 1:]

    poblacion[-1] = hijo
    print("Generacion", gen + 1, poblacion)

print("Mejor:", max(poblacion, key=aptitud))
