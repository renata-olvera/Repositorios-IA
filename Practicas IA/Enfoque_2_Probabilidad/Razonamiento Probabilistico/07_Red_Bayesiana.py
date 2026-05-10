# 07 - Red Bayesiana
# Ejemplo: lluvia, aspersor y pasto mojado.
p_lluvia = {True: .30, False: .70}
p_aspersor = {True: {True: .05, False: .95}, False: {True: .40, False: .60}}
p_mojado = {(True, True): .99, (True, False): .90, (False, True): .80, (False, False): .05}

def conjunta(lluvia, asp, mojado=True):
    p = p_lluvia[lluvia] * p_aspersor[lluvia][asp]
    q = p_mojado[(lluvia, asp)]
    return p * (q if mojado else 1 - q)

total = sum(conjunta(l, a) for l in [True, False] for a in [True, False])
print("P(pasto mojado):", round(total, 4))
