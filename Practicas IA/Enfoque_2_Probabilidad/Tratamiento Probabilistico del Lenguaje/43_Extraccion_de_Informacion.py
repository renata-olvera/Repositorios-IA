# 43 - Extracción de Información
import re
texto = "Soporte: soporte@empresa.com, Ventas: ventas@empresa.com, Tel: 3312345678 y 3322221111"
correos = re.findall(r"[\w.]+@[\w.]+", texto)
telefonos = re.findall(r"\b\d{10}\b", texto)
print("correos:", correos)
print("telefonos:", telefonos)
