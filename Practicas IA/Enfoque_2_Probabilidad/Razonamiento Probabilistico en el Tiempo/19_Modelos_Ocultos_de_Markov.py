# 19 - Modelos Ocultos de Markov
# Ejemplo: Viterbi para clima.
estados = ["Sol", "Lluvia"]
obs = ["camina", "compra", "compra"]
ini = {"Sol": .60, "Lluvia": .40}
T = {"Sol": {"Sol": .70, "Lluvia": .30}, "Lluvia": {"Sol": .40, "Lluvia": .60}}
E = {"Sol": {"camina": .70, "compra": .30}, "Lluvia": {"camina": .20, "compra": .80}}
score = {e: ini[e] * E[e][obs[0]] for e in estados}
ruta = {e: [e] for e in estados}
for o in obs[1:]:
    ns, nr = {}, {}
    for e in estados:
        ant = max(estados, key=lambda a: score[a] * T[a][e])
        ns[e] = score[ant] * T[ant][e] * E[e][o]
        nr[e] = ruta[ant] + [e]
    score, ruta = ns, nr
final = max(score, key=score.get)
print("Ruta mas probable:", ruta[final])
print("Probabilidad:", round(score[final], 5))
