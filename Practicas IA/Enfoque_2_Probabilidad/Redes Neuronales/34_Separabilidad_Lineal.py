# 34 - Separabilidad Lineal
puntos = [((1,1), -1), ((2,1), -1), ((4,4), 1), ((5,3), 1)]
w, b = (1, 1), -5
aciertos = 0
for p, y in puntos:
    pred = 1 if w[0]*p[0] + w[1]*p[1] + b >= 0 else -1
    aciertos += pred == y
    print(p, "real", y, "pred", pred)
print("aciertos:", aciertos, "de", len(puntos))
