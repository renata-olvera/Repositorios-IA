# 14 - Monte Carlo para Cadenas de Markov
# Ejemplo: clima por simulación.
import random
random.seed(14)
trans = {
    "Frio": {"Frio": .60, "Templado": .30, "Caliente": .10},
    "Templado": {"Frio": .20, "Templado": .50, "Caliente": .30},
    "Caliente": {"Frio": .10, "Templado": .30, "Caliente": .60}
}

def avanzar(e):
    r = random.random()
    acum = 0
    for sig, p in trans[e].items():
        acum += p
        if r <= acum:
            return sig

estado = "Templado"
conteo = dict.fromkeys(trans, 0)
for _ in range(10000):
    estado = avanzar(estado)
    conteo[estado] += 1
print({e: round(c / 10000, 3) for e, c in conteo.items()})
