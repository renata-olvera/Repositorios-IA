# 25 - Algoritmo EM
# Ejemplo simplificado: estimar dos centros en datos 1D.
datos = [1.0, 1.2, 1.4, 5.0, 5.2, 5.4]
centros = [1.5, 4.8]
for i in range(6):
    grupos = [[], []]
    for x in datos:
        idx = 0 if abs(x - centros[0]) < abs(x - centros[1]) else 1
        grupos[idx].append(x)
    centros = [sum(g) / len(g) for g in grupos]
    print("iteracion", i + 1, [round(c, 3) for c in centros])
