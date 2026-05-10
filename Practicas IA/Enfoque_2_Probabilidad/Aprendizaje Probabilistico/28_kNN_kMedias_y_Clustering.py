# 28 - k-NN, k-Medias y Clustering
# Ejemplo k-NN para frutas.
datos = [((150, 7), "manzana"), ((160, 8), "manzana"), ((120, 5), "pera"), ((115, 4), "pera")]
nuevo = (140, 6)
def dist(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** .5
vecinos = sorted((dist(nuevo, p), e) for p, e in datos)[:3]
votos = {}
for _, e in vecinos:
    votos[e] = votos.get(e, 0) + 1
print("vecinos:", vecinos)
print("clase:", max(votos, key=votos.get))
