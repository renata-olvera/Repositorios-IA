# 36 - Retropropagación del Error
import math
def sig(x): return 1 / (1 + math.exp(-x))
x, y = 1.0, 0.0
w, b, lr = .8, .2, .5
for epoca in range(10):
    s = sig(w*x + b)
    err = y - s
    delta = err * s * (1 - s)
    w += lr * delta * x
    b += lr * delta
    print(epoca + 1, "salida", round(s, 4), "error", round(err, 4))
print("final:", round(w, 4), round(b, 4))
