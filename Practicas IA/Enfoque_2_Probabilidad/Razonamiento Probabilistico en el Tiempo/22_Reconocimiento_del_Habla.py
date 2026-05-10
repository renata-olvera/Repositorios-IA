# 22 - Reconocimiento del Habla
# Ejemplo: elegir palabra por sonidos observados.
palabras = {"casa": ["ka", "sa"], "taza": ["ta", "sa"], "masa": ["ma", "sa"]}
sonidos = {"ka": {"ka": .80, "ta": .10, "ma": .10}, "ta": {"ka": .15, "ta": .75, "ma": .10}, "ma": {"ka": .10, "ta": .10, "ma": .80}, "sa": {"sa": .90}}
obs = ["ka", "sa"]
puntajes = {}
for palabra, reales in palabras.items():
    p = 1
    for r, o in zip(reales, obs):
        p *= sonidos[r].get(o, .01)
    puntajes[palabra] = p
print("Puntajes:", puntajes)
print("Reconocida:", max(puntajes, key=puntajes.get))
