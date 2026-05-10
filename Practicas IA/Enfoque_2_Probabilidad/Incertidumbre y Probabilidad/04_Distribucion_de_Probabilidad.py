# 04 - Distribución de Probabilidad
# Ejemplo: ventas posibles de una tienda en un día.
ventas = {20: .10, 30: .25, 40: .35, 50: .20, 60: .10}
media = sum(v * p for v, p in ventas.items())
print("Distribucion:")
for v, p in ventas.items():
    print(v, "ventas ->", p)
print("Suma de probabilidades:", sum(ventas.values()))
print("Valor esperado:", media)
