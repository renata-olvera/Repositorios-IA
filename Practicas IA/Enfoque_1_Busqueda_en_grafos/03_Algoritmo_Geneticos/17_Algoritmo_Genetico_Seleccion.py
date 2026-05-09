# 17 - Algoritmo Genetico
# Muestra seleccion por aptitud.

individuos = {"A": 4, "B": 9, "C": 3, "D": 6}
total = sum(individuos.values())

for nombre, valor in individuos.items():
    prob = valor / total
    print(nombre, "probabilidad:", round(prob, 3))

print("Mas apto:", max(individuos, key=individuos.get))
