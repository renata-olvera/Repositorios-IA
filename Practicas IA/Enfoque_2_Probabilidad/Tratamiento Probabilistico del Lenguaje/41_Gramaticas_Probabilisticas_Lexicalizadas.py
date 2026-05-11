# 41 - Gramáticas Probabilísticas Lexicalizadas
reglas = {"robot": {"robot avanza rapido": .60, "robot toma pieza": .40}, "camara": {"camara detecta defecto": .70, "camara revisa etiqueta": .30}}
clave = "camara"
mejor = max(reglas[clave], key=reglas[clave].get)
print("palabra principal:", clave)
print("frase:", mejor)
print("probabilidad:", reglas[clave][mejor])
