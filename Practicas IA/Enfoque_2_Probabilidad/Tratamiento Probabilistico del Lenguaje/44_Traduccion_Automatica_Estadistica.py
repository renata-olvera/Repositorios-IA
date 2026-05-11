# 44 - Traducción Automática Estadística
tabla = {"the": {"el": .70, "la": .30}, "robot": {"robot": 1}, "detects": {"detecta": .80, "encuentra": .20}, "part": {"pieza": .90, "parte": .10}}
oracion = "the robot detects part"
trad = []
for p in oracion.split():
    opciones = tabla.get(p, {p: 1})
    trad.append(max(opciones, key=opciones.get))
print("original:", oracion)
print("traduccion:", " ".join(trad))
