# 37 - Aprendizaje por Refuerzo Activo
# El agente aprende al elegir acciones.

q = {"avanzar": 0, "esperar": 0}
recompensa = {"avanzar": 6, "esperar": 1}
alpha = 0.4

for i in range(6):
    accion = max(q, key=q.get)
    q[accion] += alpha * (recompensa[accion] - q[accion])
    print("Intento", i + 1, accion, round(q[accion], 2))

print("Q final:", q)
