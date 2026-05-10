# 06 - Regla de Bayes
# Ejemplo: probabilidad de enfermedad si la prueba salió positiva.
p_enf = .04
p_pos_enf = .95
p_pos_sano = .08
num = p_pos_enf * p_enf
den = num + p_pos_sano * (1 - p_enf)
print("P(enfermedad | positivo):", round(num / den, 4))
