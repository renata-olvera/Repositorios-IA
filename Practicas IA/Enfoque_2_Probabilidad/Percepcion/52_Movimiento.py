# 52 - Movimiento
posiciones = [(2,3), (4,4), (7,6), (11,7)]
vel = []
for i in range(1, len(posiciones)):
    x1, y1 = posiciones[i-1]
    x2, y2 = posiciones[i]
    vel.append((x2-x1, y2-y1))
print("vectores:", vel)
print("movimiento promedio:", (round(sum(v[0] for v in vel)/len(vel), 2), round(sum(v[1] for v in vel)/len(vel), 2)))
