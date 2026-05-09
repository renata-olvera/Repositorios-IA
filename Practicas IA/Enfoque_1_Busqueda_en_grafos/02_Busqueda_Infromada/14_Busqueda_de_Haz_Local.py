# 14 - Busqueda de Haz Local
# Mantiene varias soluciones y conserva las mejores.

def f(x):
    return -(x - 7) ** 2 + 49

haz = [1, 4, 10]

for i in range(6):
    candidatos = []

    for x in haz:
        candidatos += [x - 1, x, x + 1]

    candidatos = list(set(candidatos))
    candidatos.sort(key=f, reverse=True)

    haz = candidatos[:3]
    print("Iteracion", i + 1, "haz:", haz)

print("Mejor:", haz[0])
