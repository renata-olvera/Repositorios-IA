# 20 - Filtros de Kalman
# Ejemplo 1D para estimar posición.
mediciones = [10.2, 10.8, 11.1, 11.9, 12.2]
x, P = 10.0, 1.0
Q, R = .05, .40

for z in mediciones:
    P = P + Q
    K = P / (P + R)
    x = x + K * (z - x)
    P = (1 - K) * P
    print("medicion:", z, "estimacion:", round(x, 3), "incertidumbre:", round(P, 3))
