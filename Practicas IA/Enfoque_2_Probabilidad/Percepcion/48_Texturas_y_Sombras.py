# 48 - Texturas y Sombras
liso = [[10,11,10],[11,10,11],[10,11,10]]
rugoso = [[5,40,8],[35,10,45],[7,42,9]]
def var(m):
    v = [x for fila in m for x in fila]
    p = sum(v) / len(v)
    return sum((x-p)**2 for x in v) / len(v)
print("variacion liso:", round(var(liso), 2))
print("variacion rugoso:", round(var(rugoso), 2))
