# 31 - Computación Neuronal
entradas = [.7, .2, .9]
pesos = [.5, -.4, .8]
sesgo = -.3
suma = sesgo + sum(x*w for x, w in zip(entradas, pesos))
print("suma:", round(suma, 3))
print("salida:", 1 if suma >= 0 else 0)
