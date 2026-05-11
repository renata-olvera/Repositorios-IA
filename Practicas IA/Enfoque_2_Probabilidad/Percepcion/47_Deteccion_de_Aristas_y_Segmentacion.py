# 47 - Detección de Aristas y Segmentación
datos = [10, 11, 10, 12, 80, 82, 81, 15, 14]
umbral = 30
aristas = [i for i in range(1, len(datos)) if abs(datos[i] - datos[i-1]) >= umbral]
print("aristas:", aristas)
inicio, segmentos = 0, []
for c in aristas:
    segmentos.append(datos[inicio:c])
    inicio = c
segmentos.append(datos[inicio:])
print("segmentos:", segmentos)
