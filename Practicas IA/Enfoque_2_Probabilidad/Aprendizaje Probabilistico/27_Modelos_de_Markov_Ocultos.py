# 27 - Modelos de Markov Ocultos
# Ejemplo: probabilidad de observaciones en HMM.
estados = ["Alta", "Baja"]
obs = ["venta", "venta", "no_venta"]
ini = {"Alta": .50, "Baja": .50}
T = {"Alta": {"Alta": .70, "Baja": .30}, "Baja": {"Alta": .40, "Baja": .60}}
E = {"Alta": {"venta": .80, "no_venta": .20}, "Baja": {"venta": .30, "no_venta": .70}}
actual = {e: ini[e] * E[e][obs[0]] for e in estados}
for o in obs[1:]:
    actual = {e: E[e][o] * sum(actual[a] * T[a][e] for a in estados) for e in estados}
print("Probabilidad de la secuencia:", round(sum(actual.values()), 5))
