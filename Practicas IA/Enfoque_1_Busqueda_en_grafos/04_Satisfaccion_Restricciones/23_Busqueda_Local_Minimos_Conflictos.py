# 23 - Busqueda Local: Minimos Conflictos
# Cambia el valor que produce menos conflictos.

asignacion = {"A": "rojo", "B": "rojo", "C": "verde"}
colores = ["rojo", "verde", "azul"]
vecinos = {"B": ["A", "C"]}

def conflictos(color):
    total = 0

    for vecino in vecinos["B"]:
        if asignacion[vecino] == color:
            total += 1

    return total

mejor = min(colores, key=conflictos)
asignacion["B"] = mejor

print("Nueva asignacion:", asignacion)
