# 05 - Independencia Condicional
# Ejemplo: dos sensores independientes si se conoce el estado de la máquina.
p_temp = {"normal": .05, "caliente": .90}
p_vib = {"normal": .10, "caliente": .75}
estado = "caliente"
p_ambos = p_temp[estado] * p_vib[estado]
print("Estado conocido:", estado)
print("P(alerta temperatura y vibracion | estado):", round(p_ambos, 3))
