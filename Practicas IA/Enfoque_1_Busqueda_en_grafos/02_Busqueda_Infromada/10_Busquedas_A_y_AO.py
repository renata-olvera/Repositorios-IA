# 10 - Busquedas A* y AO*
# A* usa f(n) = g(n) + h(n).

grafo = {"A": [("B", 2), ("C", 4)], "B": [("Meta", 6)], "C": [("Meta", 2)], "Meta": []}
h = {"A": 5, "B": 4, "C": 1, "Meta": 0}

abiertos = [("A", 0, ["A"])]

while abiertos:
    abiertos.sort(key=lambda x: x[1] + h[x[0]])
    nodo, costo, ruta = abiertos.pop(0)

    if nodo == "Meta":
        print("Ruta:", ruta)
        print("Costo:", costo)
        break

    for vecino, paso in grafo[nodo]:
        abiertos.append((vecino, costo + paso, ruta + [vecino]))

print("AO* se usa en estructuras AND-OR.")
