# 17 - Filtrado, Predicción, Suavizado y Explicación
# Ejemplo de filtrado con clima oculto.
def normalizar(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}

T = {"Sol": {"Sol": .70, "Lluvia": .30}, "Lluvia": {"Sol": .30, "Lluvia": .70}}
E = {"Sol": {"paraguas": .20, "sin": .80}, "Lluvia": {"paraguas": .90, "sin": .10}}
b = {"Sol": .60, "Lluvia": .40}

for obs in ["paraguas", "paraguas", "sin"]:
    pred = {e: sum(b[a] * T[a][e] for a in b) for e in b}
    b = normalizar({e: pred[e] * E[e][obs] for e in pred})
    print(obs, {k: round(v, 3) for k, v in b.items()})
