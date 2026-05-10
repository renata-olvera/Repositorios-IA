# 12 - Muestreo Directo y por Rechazo
# Ejemplo: estimar P(Lluvia | Pasto=True).
import random
random.seed(12)

def evento(p): return random.random() < p

def muestra():
    lluvia = evento(.30)
    asp = evento(.10 if lluvia else .50)
    tabla = {(True, True): .99, (True, False): .85, (False, True): .75, (False, False): .05}
    pasto = evento(tabla[(lluvia, asp)])
    return lluvia, pasto

aceptadas = lluvia_con_pasto = 0
for _ in range(5000):
    lluvia, pasto = muestra()
    if pasto:
        aceptadas += 1
        lluvia_con_pasto += int(lluvia)
print("Estimacion:", round(lluvia_con_pasto / aceptadas, 4))
