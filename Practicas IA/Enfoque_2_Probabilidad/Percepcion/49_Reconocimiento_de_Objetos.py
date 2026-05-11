# 49 - Reconocimiento de Objetos
objetos = {"moneda": {"redondez": .95, "tamano": 2}, "tarjeta": {"redondez": .20, "tamano": 8}, "boton": {"redondez": .85, "tamano": 1}}
detectado = {"redondez": .90, "tamano": 2}
def dist(a,b): return abs(a["redondez"] - b["redondez"]) + abs(a["tamano"] - b["tamano"])
mejor = min(objetos, key=lambda k: dist(detectado, objetos[k]))
print("objeto reconocido:", mejor)
