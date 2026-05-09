# 27 - Valor de la Informacion
# Compara decidir con y sin informacion perfecta.

sin_info = max(0.6 * 12000 + 0.4 * -2000, 0.6 * 6000 + 0.4 * 3000)
con_info = 0.6 * 12000 + 0.4 * 3000

print("Sin informacion:", sin_info)
print("Con informacion:", con_info)
print("Valor de informacion:", con_info - sin_info)
