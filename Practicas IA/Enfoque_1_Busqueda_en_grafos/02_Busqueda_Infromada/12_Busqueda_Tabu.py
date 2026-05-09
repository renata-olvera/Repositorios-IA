# 12 - Busqueda Tabu
# Guarda movimientos recientes para no repetirlos.

def f(x):
    return -(x - 4) ** 2 + 16

actual = 0
tabu = []

for _ in range(8):
    vecinos = [actual - 1, actual + 1]
    candidatos = [v for v in vecinos if v not in tabu]

    if not candidatos:
        break

    mejor = max(candidatos, key=f)
    tabu.append(actual)

    if len(tabu) > 3:
        tabu.pop(0)

    actual = mejor
    print("Actual:", actual, "Tabu:", tabu)

print("Resultado:", actual)
