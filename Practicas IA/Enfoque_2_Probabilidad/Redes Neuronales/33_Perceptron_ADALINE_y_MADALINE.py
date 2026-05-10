# 33 - Perceptrón, ADALINE y MADALINE
# Ejemplo: perceptrón para compuerta OR.
datos = [([0,0],0), ([0,1],1), ([1,0],1), ([1,1],1)]
w = [0, 0]
b = 0
lr = .2
for _ in range(8):
    for x, y in datos:
        s = 1 if b + x[0]*w[0] + x[1]*w[1] >= 0 else 0
        e = y - s
        w[0] += lr * e * x[0]
        w[1] += lr * e * x[1]
        b += lr * e
print("pesos:", w, "sesgo:", round(b, 2))
for x, y in datos:
    print(x, 1 if b + x[0]*w[0] + x[1]*w[1] >= 0 else 0)
