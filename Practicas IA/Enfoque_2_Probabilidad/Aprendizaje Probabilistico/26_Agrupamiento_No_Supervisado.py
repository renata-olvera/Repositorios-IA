# 26 - Agrupamiento No Supervisado
# Ejemplo: k-medias en una dimensión.
datos = [2, 3, 4, 12, 13, 14]
centros = [3, 13]
for i in range(5):
    grupos = [[], []]
    for d in datos:
        grupos[0 if abs(d-centros[0]) <= abs(d-centros[1]) else 1].append(d)
    centros = [sum(g)/len(g) for g in grupos]
    print("grupos:", grupos, "centros:", centros)
