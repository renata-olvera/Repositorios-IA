# 42 - Recuperación de Datos
docs = {"doc1": "robot industrial vision artificial", "doc2": "red bayesiana probabilidad inferencia", "doc3": "sensor camara vision defecto", "doc4": "aprendizaje maquina datos"}
consulta = "vision camara"
def score(texto):
    return sum(1 for p in consulta.split() if p in texto.split())
print("consulta:", consulta)
for puntos, doc in sorted((score(t), d) for d, t in docs.items())[::-1]:
    print(doc, "puntaje:", puntos)
