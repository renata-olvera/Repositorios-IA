# 18 - Algoritmo Hacia Delante-Atrás
# Ejemplo HMM pequeño para suavizar.
estados = ["Sano", "Resfriado"]
obs = ["tos", "tos", "normal"]
ini = {"Sano": .80, "Resfriado": .20}
T = {"Sano": {"Sano": .85, "Resfriado": .15}, "Resfriado": {"Sano": .40, "Resfriado": .60}}
E = {"Sano": {"tos": .10, "normal": .90}, "Resfriado": {"tos": .80, "normal": .20}}

def norm(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}

f = [norm({e: ini[e] * E[e][obs[0]] for e in estados})]
for t in range(1, len(obs)):
    f.append(norm({e: E[e][obs[t]] * sum(f[t-1][a] * T[a][e] for a in estados) for e in estados}))
print("Mensajes hacia delante:")
for x in f:
    print({k: round(v, 3) for k, v in x.items()})
