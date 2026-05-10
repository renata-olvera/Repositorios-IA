# 08 - Regla de la Cadena
# Ejemplo: P(estudia, duerme bien, aprueba).
p_estudia = {True: .65, False: .35}
p_duerme = {True: {True: .70, False: .30}, False: {True: .40, False: .60}}
p_aprueba = {(True, True): .95, (True, False): .75, (False, True): .50, (False, False): .20}
e, d, a = True, True, True
prob = p_estudia[e] * p_duerme[e][d] * (p_aprueba[(e, d)] if a else 1 - p_aprueba[(e, d)])
print("Probabilidad conjunta:", round(prob, 4))
