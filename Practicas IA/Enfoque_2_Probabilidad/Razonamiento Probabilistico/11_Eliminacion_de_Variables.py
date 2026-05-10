# 11 - Eliminación de Variables
# Ejemplo: eliminar Aspersor para obtener P(Pasto=True).
p_lluvia = {True: .30, False: .70}
p_asp = {True: {True: .10, False: .90}, False: {True: .50, False: .50}}
p_pasto = {(True, True): .99, (True, False): .85, (False, True): .75, (False, False): .05}

def factor_pasto(l):
    return sum(p_asp[l][a] * p_pasto[(l, a)] for a in [True, False])

prob = sum(p_lluvia[l] * factor_pasto(l) for l in [True, False])
print("P(Pasto=True):", round(prob, 4))
