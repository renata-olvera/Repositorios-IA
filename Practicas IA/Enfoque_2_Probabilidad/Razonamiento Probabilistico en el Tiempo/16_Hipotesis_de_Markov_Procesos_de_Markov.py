# 16 - Hipótesis de Markov: Procesos de Markov
# El futuro depende del presente, no de todo el historial.
trans = {
    "Dormido": {"Dormido": .65, "Despierto": .35},
    "Despierto": {"Dormido": .20, "Despierto": .80}
}
actual = "Despierto"
print("Estado actual:", actual)
print("Distribucion del siguiente estado:", trans[actual])
