# 11 - Busqueda de Ascension de Colinas
# Avanza al vecino que mejora el resultado.

def f(x):
    return -(x - 5) ** 2 + 25

x = 0

while True:
    actual = f(x)
    vecino = x + 1

    if f(vecino) > actual:
        x = vecino
    else:
        break

    print("x:", x, "valor:", f(x))

print("Mejor punto:", x)
