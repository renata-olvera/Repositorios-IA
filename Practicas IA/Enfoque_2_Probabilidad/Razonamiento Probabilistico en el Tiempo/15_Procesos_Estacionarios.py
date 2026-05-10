# 15 - Procesos Estacionarios
# Ejemplo: distribución que se estabiliza.
P = [[.70, .30], [.40, .60]]
d = [.50, .50]

for t in range(12):
    d = [d[0] * P[0][0] + d[1] * P[1][0], d[0] * P[0][1] + d[1] * P[1][1]]
    print(t + 1, [round(x, 4) for x in d])
