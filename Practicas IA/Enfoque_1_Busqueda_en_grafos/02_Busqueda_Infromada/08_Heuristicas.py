# 08 - Heuristicas
# Estima que tan cerca esta cada nodo de la meta.

valores_h = {"A": 9, "B": 6, "C": 4, "D": 2, "Meta": 0}

print("Valores heurísticos:")
for nodo, valor in valores_h.items():
    print(nodo, "->", valor)

mejor = min(valores_h, key=valores_h.get)
print("Nodo más prometedor:", mejor)
