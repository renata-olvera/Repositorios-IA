# 20 - Comprobacion Hacia Adelante
# Reduce opciones futuras al asignar un valor.

dominios = {"A": ["rojo"], "B": ["rojo", "verde"], "C": ["rojo", "verde"]}
vecinos = {"A": ["B", "C"]}

for vecino in vecinos["A"]:
    if "rojo" in dominios[vecino]:
        dominios[vecino].remove("rojo")

print("Dominios reducidos:")
for v, d in dominios.items():
    print(v, d)
