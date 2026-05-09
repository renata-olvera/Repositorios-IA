# 34 - Aprendizaje por Refuerzo Pasivo
# Evalua una politica con retornos observados.

episodios = [["A", "B", "Meta"], ["A", "Meta"], ["A", "B", "Meta"]]
recompensa = {"A": -1, "B": -1, "Meta": 10}
suma = {}
conteo = {}

for episodio in episodios:
    retorno = 0

    for estado in reversed(episodio):
        retorno += recompensa[estado]
        suma[estado] = suma.get(estado, 0) + retorno
        conteo[estado] = conteo.get(estado, 0) + 1

for estado in suma:
    print(estado, round(suma[estado] / conteo[estado], 2))
