# 10 - Inferencia por Enumeración
# Ejemplo: P(Lluvia | Pasto=True).
p_lluvia = {True: .30, False: .70}
p_asp = {True: {True: .10, False: .90}, False: {True: .50, False: .50}}
p_pasto = {(True, True): .99, (True, False): .85, (False, True): .75, (False, False): .05}

def conj(l, a):
    return p_lluvia[l] * p_asp[l][a] * p_pasto[(l, a)]

val = {l: sum(conj(l, a) for a in [True, False]) for l in [True, False]}
z = sum(val.values())
print("P(Lluvia | Pasto=True):", round(val[True] / z, 4))
