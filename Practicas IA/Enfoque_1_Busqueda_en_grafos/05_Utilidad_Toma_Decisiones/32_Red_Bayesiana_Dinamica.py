# 32 - Red Bayesiana Dinamica
# Actualiza una creencia con una observacion.

creencia = {"normal": 0.8, "falla": 0.2}

transicion = {
    "normal": {"normal": 0.85, "falla": 0.15},
    "falla": {"normal": 0.3, "falla": 0.7}
}

sensor = {"normal": 0.1, "falla": 0.8}
pred = {"normal": 0, "falla": 0}

for e in creencia:
    for sig in pred:
        pred[sig] += creencia[e] * transicion[e][sig]

posterior = {e: pred[e] * sensor[e] for e in pred}
total = sum(posterior.values())

for e in posterior:
    posterior[e] /= total

print(posterior)
