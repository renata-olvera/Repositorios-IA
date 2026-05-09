# 09 - Busqueda Voraz Primero el Mejor
# Elige primero el nodo con menor heuristica.

grafo = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": ["Meta"], "Meta": []}
h = {"A": 6, "B": 5, "C": 3, "D": 4, "E": 1, "Meta": 0}

frontera = ["A"]
visitados = set()

while frontera:
    frontera.sort(key=lambda n: h[n])
    nodo = frontera.pop(0)
    print("Visitando:", nodo)

    if nodo == "Meta":
        break

    visitados.add(nodo)

    for vecino in grafo[nodo]:
        if vecino not in visitados and vecino not in frontera:
            frontera.append(vecino)
