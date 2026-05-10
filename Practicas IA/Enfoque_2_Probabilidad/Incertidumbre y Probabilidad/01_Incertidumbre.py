# 01 - Incertidumbre
# Ejemplo: decidir si conviene salir con paraguas.
escenarios = {"soleado": .50, "nublado": .35, "lluvia": .15}
costo_sin = {"soleado": 0, "nublado": 1, "lluvia": 9}
costo_con = {"soleado": 2, "nublado": 2, "lluvia": 1}

def esperado(tabla):
    total = 0
    for estado, prob in escenarios.items():
        total += prob * tabla[estado]
    return total

a = esperado(costo_sin)
b = esperado(costo_con)
print("Costo sin paraguas:", round(a, 2))
print("Costo con paraguas:", round(b, 2))
print("Mejor decision:", "llevar paraguas" if b < a else "no llevar paraguas")
