# 25 - Funcion de Utilidad
# Calcula una calificacion total con pesos.

opciones = {"A": {"precio": 8, "calidad": 6}, "B": {"precio": 5, "calidad": 9}, "C": {"precio": 7, "calidad": 7}}
pesos = {"precio": 0.4, "calidad": 0.6}

def utilidad(opcion):
    return sum(opciones[opcion][c] * pesos[c] for c in pesos)

for opcion in opciones:
    print(opcion, round(utilidad(opcion), 2))

print("Mejor:", max(opciones, key=utilidad))
