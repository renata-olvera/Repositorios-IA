# 19 - Busqueda de Vuelta Atras
# Si una asignacion falla, se regresa.

variables = ["A", "B", "C"]
colores = ["rojo", "verde"]
vecinos = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}

def valido(var, color, asignacion):
    for vecino in vecinos[var]:
        if asignacion.get(vecino) == color:
            return False
    return True

def resolver(asignacion):
    if len(asignacion) == len(variables):
        return asignacion

    var = next(v for v in variables if v not in asignacion)

    for color in colores:
        if valido(var, color, asignacion):
            asignacion[var] = color
            sol = resolver(asignacion)

            if sol:
                return sol

            del asignacion[var]

print("Solucion:", resolver({}))
