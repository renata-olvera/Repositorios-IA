# 35 - Q-Learning
# Actualiza el valor Q de cada accion.

q = {("A", "B"): 0, ("A", "Meta"): 0, ("B", "Meta"): 0}
experiencias = [("A", "B", -1, "B"), ("B", "Meta", 10, "Meta"), ("A", "Meta", 4, "Meta")]
alpha = 0.5
gamma = 0.9

def mejor_q(estado):
    valores = [v for (e, a), v in q.items() if e == estado]
    return max(valores) if valores else 0

for e, a, r, sig in experiencias:
    q[(e, a)] += alpha * (r + gamma * mejor_q(sig) - q[(e, a)])

print(q)
