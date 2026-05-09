# 18 - Problemas de Satisfaccion de Restricciones
# Variables con dominios y reglas.

dominios = {"X": [1, 2, 3], "Y": [1, 2, 3]}

for x in dominios["X"]:
    for y in dominios["Y"]:
        if x != y:
            print("Valido:", {"X": x, "Y": y})
