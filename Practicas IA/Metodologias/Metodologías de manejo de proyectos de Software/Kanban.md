def generar_reporte():
    contenido = """

5. KANBAN

¿Qué es?
Es un sistema visual para gestionar tareas.

¿Para qué sirve?
Sirve para organizar el flujo de trabajo.

¿Cómo funciona?
Se usa un tablero con columnas como pendiente, en proceso y terminado.

Ejemplo:
Uso de herramientas como Trello para organizar tareas.
"""
    
    with open("reporte.txt", "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print("Reporte generado.")

generar_reporte()