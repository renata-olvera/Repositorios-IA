# 16 - Busqueda Online
# El agente decide mientras descubre el camino.

entorno = {"A": ["B"], "B": ["A", "C"], "C": ["B", "Meta"], "Meta": []}

actual = "A"
visitados = set()

while actual != "Meta":
    print("Estoy en:", actual)
    visitados.add(actual)

    opciones = [n for n in entorno[actual] if n not in visitados]
    actual = opciones[0] if opciones else entorno[actual][0]

print("Llegue a Meta")
