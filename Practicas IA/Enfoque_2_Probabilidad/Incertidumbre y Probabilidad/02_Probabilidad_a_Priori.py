# 02 - Probabilidad a Priori
# Ejemplo: probabilidad inicial de que una pieza sea defectuosa.
piezas_buenas = 92
piezas_malas = 8
total = piezas_buenas + piezas_malas
print("P(pieza buena):", round(piezas_buenas / total, 3))
print("P(pieza defectuosa):", round(piezas_malas / total, 3))
