# 38 - Hamming, Hopfield, Hebb, Boltzmann
patron = [1, -1, 1, -1]
n = len(patron)
W = [[0 if i == j else patron[i] * patron[j] for j in range(n)] for i in range(n)]
entrada = [1, -1, -1, -1]
salida = []
for i in range(n):
    s = sum(W[i][j] * entrada[j] for j in range(n))
    salida.append(1 if s >= 0 else -1)
print("original:", patron)
print("entrada:", entrada)
print("recuperado:", salida)
