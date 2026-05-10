# 24 - Naïve Bayes
# Ejemplo: clasificar mensaje.
datos = [("gana premio ahora", "spam"), ("oferta premio gratis", "spam"), ("reunion de proyecto", "normal"), ("avance del proyecto", "normal")]
clases = ["spam", "normal"]
vocab = set(" ".join(t for t, _ in datos).split())
conteo = {c: {p: 1 for p in vocab} for c in clases}
base = {c: 0 for c in clases}
for texto, c in datos:
    base[c] += 1
    for p in texto.split():
        conteo[c][p] += 1

def clasificar(texto):
    punt = {}
    for c in clases:
        prob = base[c] / len(datos)
        total = sum(conteo[c].values())
        for p in texto.split():
            prob *= conteo[c].get(p, 1) / total
        punt[c] = prob
    return max(punt, key=punt.get), punt

print(clasificar("premio gratis"))
