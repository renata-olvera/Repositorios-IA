# 40 - Gramáticas Probabilísticas Independientes del Contexto
import random
random.seed(40)
G = {"S": [(["NP","VP"],1)], "NP": [(["el","robot"],.5), (["la","camara"],.5)], "VP": [(["detecta","pieza"],.6), (["avanza"],.4)]}
def elegir(reglas):
    r, a = random.random(), 0
    for exp, p in reglas:
        a += p
        if r <= a:
            return exp
def generar(s):
    if s not in G: return [s]
    out = []
    for x in elegir(G[s]):
        out += generar(x)
    return out
print(" ".join(generar("S")))
