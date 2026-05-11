# 39 - Modelo Probabilístico del Lenguaje: Corpus
corpus = ["el robot avanza", "el robot gira", "la camara detecta", "el sensor detecta"]
conteo = {}
for frase in corpus:
    for p in frase.split():
        conteo[p] = conteo.get(p, 0) + 1
total = sum(conteo.values())
for p in sorted(conteo):
    print(p, round(conteo[p] / total, 3))
