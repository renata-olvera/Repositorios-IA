# 45 - Gráficos por Computador
ancho, alto = 12, 8
pantalla = [["." for _ in range(ancho)] for _ in range(alto)]
for x in range(ancho):
    y = int((alto - 1) * x / (ancho - 1))
    pantalla[y][x] = "#"
for fila in pantalla:
    print("".join(fila))
