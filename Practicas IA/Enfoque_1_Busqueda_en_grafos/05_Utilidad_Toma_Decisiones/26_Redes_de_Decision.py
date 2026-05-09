# 26 - Redes de Decision
# Usa utilidad esperada para decidir.

decisiones = {"invertir": [(0.7, 9000), (0.3, -1000)], "esperar": [(1.0, 3000)]}

def esperado(casos):
    return sum(p * u for p, u in casos)

for decision in decisiones:
    print(decision, esperado(decisiones[decision]))

print("Decision:", max(decisiones, key=lambda d: esperado(decisiones[d])))
