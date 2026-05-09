# 33 - Teoria de Juegos
# Busca equilibrio de Nash.

acciones = ["alto", "bajo"]

pagos = {
    ("alto", "alto"): (8, 8),
    ("alto", "bajo"): (3, 10),
    ("bajo", "alto"): (10, 3),
    ("bajo", "bajo"): (5, 5)
}

def nash(a, b):
    p1, p2 = pagos[(a, b)]

    for otra in acciones:
        if pagos[(otra, b)][0] > p1:
            return False

    for otra in acciones:
        if pagos[(a, otra)][1] > p2:
            return False

    return True

for a in acciones:
    for b in acciones:
        if nash(a, b):
            print("Equilibrio:", a, b, pagos[(a, b)])
