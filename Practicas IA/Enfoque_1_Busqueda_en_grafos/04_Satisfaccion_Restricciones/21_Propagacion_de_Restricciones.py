# 21 - Propagacion de Restricciones
# Extiende restricciones para limpiar dominios.

dominios = {"A": ["azul"], "B": ["azul", "verde"], "C": ["azul", "rojo"]}
arcos = [("A", "B"), ("A", "C")]

for origen, destino in arcos:
    if len(dominios[origen]) == 1:
        fijo = dominios[origen][0]

        if fijo in dominios[destino]:
            dominios[destino].remove(fijo)

print(dominios)
