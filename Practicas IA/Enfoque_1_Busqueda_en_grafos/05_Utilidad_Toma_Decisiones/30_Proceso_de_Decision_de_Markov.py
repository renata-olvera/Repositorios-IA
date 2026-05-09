# 30 - Proceso de Decision de Markov
# Las acciones tienen resultados probables.

acciones = {
    "avanzar": [("cerca", 0.8, 5), ("inicio", 0.2, -1)],
    "esperar": [("inicio", 1.0, 0)]
}

valores = {"inicio": 0, "cerca": 7}
gamma = 0.9

for accion, casos in acciones.items():
    utilidad = 0

    for estado, prob, recompensa in casos:
        utilidad += prob * (recompensa + gamma * valores[estado])

    print(accion, round(utilidad, 2))
