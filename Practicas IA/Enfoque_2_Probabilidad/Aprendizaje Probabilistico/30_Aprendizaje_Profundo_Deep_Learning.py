# 30 - Aprendizaje Profundo
# Ejemplo: neurona entrenada con descenso de gradiente.
import math
def sig(x): return 1 / (1 + math.exp(-x))
datos = [(0,0), (1,1), (2,1), (3,1)]
w, b, lr = .1, 0, .2
for _ in range(100):
    for x, y in datos:
        s = sig(w*x + b)
        err = y - s
        w += lr * err * x
        b += lr * err
print("w:", round(w, 3), "b:", round(b, 3))
for x, y in datos:
    print(x, round(sig(w*x+b), 3), "esperado", y)
