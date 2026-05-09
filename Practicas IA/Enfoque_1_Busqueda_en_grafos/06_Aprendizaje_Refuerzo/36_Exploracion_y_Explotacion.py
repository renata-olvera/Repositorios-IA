# 36 - Exploracion y Explotacion
# Epsilon-greedy decide entre probar o usar lo conocido.

import random

random.seed(36)

q = {"izquierda": 3, "derecha": 8, "arriba": 4}
epsilon = 0.25

if random.random() < epsilon:
    accion = random.choice(list(q.keys()))
    print("Exploracion:", accion)
else:
    accion = max(q, key=q.get)
    print("Explotacion:", accion)
