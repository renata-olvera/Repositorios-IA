# 03 - Probabilidad Condicionada y Normalización
# Ejemplo: actualizar probabilidad de falla si un sensor marca alerta.
prior = {"normal": .85, "falla": .15}
p_alerta = {"normal": .10, "falla": .80}
sin_norm = {e: prior[e] * p_alerta[e] for e in prior}
z = sum(sin_norm.values())
posterior = {e: sin_norm[e] / z for e in sin_norm}
print("Posterior con alerta:")
for estado, p in posterior.items():
    print(estado, round(p, 3))
print("Suma:", round(sum(posterior.values()), 3))
