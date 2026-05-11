# 51 - Etiquetados de Líneas
lineas = [((0,0),(5,0)), ((5,0),(5,4)), ((5,4),(0,4)), ((0,4),(0,0))]
def etiqueta(a,b):
    if a[1] == b[1]: return "horizontal"
    if a[0] == b[0]: return "vertical"
    return "diagonal"
for i, (a,b) in enumerate(lineas, 1):
    print("linea", i, etiqueta(a,b))
