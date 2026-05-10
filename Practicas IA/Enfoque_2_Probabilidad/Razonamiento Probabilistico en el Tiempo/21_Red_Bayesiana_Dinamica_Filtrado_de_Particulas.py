# 21 - Red Bayesiana Dinámica: Filtrado de Partículas
import random
random.seed(21)
particulas = [random.randint(0, 10) for _ in range(100)]

def mover(p):
    return max(0, min(10, p + random.choice([-1, 0, 1])))

def peso(p, obs):
    return 1 / (1 + abs(p - obs))

for obs in [3, 4, 6, 7]:
    particulas = [mover(p) for p in particulas]
    pesos = [peso(p, obs) for p in particulas]
    particulas = random.choices(particulas, weights=pesos, k=len(particulas))
    print("obs:", obs, "estimacion:", round(sum(particulas) / len(particulas), 2))
