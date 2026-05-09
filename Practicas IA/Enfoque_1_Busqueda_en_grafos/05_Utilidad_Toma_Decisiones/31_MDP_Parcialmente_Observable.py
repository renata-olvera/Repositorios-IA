# 31 - MDP Parcialmente Observable
# Se decide usando creencias del estado real.

creencia = {"seguro": 0.65, "peligro": 0.35}

recompensa = {
    "avanzar": {"seguro": 8, "peligro": -10},
    "retirarse": {"seguro": 2, "peligro": 2}
}

def utilidad(accion):
    return sum(creencia[e] * recompensa[accion][e] for e in creencia)

for accion in recompensa:
    print(accion, round(utilidad(accion), 2))

print("Mejor:", max(recompensa, key=utilidad))
