# 24 - Acondicionamiento de Corte
# Fija una variable clave y simplifica el problema.

colores = ["rojo", "verde", "azul"]
asignacion = {"A": "rojo"}

for variable in ["B", "C"]:
    for color in colores:
        if color != asignacion["A"]:
            asignacion[variable] = color
            break

print("Solucion con variable de corte:", asignacion)
