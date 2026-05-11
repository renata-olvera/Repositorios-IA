# 46 - Preprocesado: Filtros
senal = [10, 12, 50, 13, 12, 11, 52, 10, 9]
salida = []
for i in range(len(senal)):
    ini, fin = max(0, i-1), min(len(senal), i+2)
    salida.append(sum(senal[ini:fin]) / (fin - ini))
print("original:", senal)
print("filtrada:", [round(x, 2) for x in salida])
