# 22 - Salto Atras Dirigido por Conflictos
# Regresa a la variable que causo el choque.

asignacion = {"A": "rojo", "B": "verde"}
intento = {"C": "verde"}

if asignacion["B"] == intento["C"]:
    print("Conflicto con B")
    print("Saltar directamente hacia B")
else:
    print("Sin conflicto")
