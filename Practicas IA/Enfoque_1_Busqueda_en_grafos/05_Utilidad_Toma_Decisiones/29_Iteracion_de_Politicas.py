# 29 - Iteracion de Politicas
# Evalua y mejora una politica.

acciones = {
    "A": {"ir_B": ("B", -1), "ir_Meta": ("Meta", 4)},
    "B": {"ir_Meta": ("Meta", 9)},
    "Meta": {}
}

politica = {"A": "ir_Meta", "B": "ir_Meta", "Meta": None}
valores = {"A": 0, "B": 0, "Meta": 0}
gamma = 0.9

for _ in range(4):
    for estado in ["A", "B"]:
        sig, r = acciones[estado][politica[estado]]
        valores[estado] = r + gamma * valores[sig]

    for estado in ["A", "B"]:
        politica[estado] = max(acciones[estado], key=lambda a: acciones[estado][a][1] + gamma * valores[acciones[estado][a][0]])

print("Politica:", politica)
print("Valores:", valores)
