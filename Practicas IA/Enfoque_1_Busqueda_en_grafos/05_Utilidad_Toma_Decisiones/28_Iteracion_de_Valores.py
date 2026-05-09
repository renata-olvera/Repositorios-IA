# 28 - Iteracion de Valores
# Actualiza valores de estados.

estados = ["A", "B", "Meta"]
acciones = {"A": [("B", -1), ("Meta", 4)], "B": [("Meta", 9)], "Meta": []}
valores = {e: 0 for e in estados}
gamma = 0.9

for _ in range(8):
    nuevos = valores.copy()

    for e in estados:
        if acciones[e]:
            nuevos[e] = max(r + gamma * valores[s] for s, r in acciones[e])

    valores = nuevos

print(valores)
