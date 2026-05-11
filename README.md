# ==========================================
# Proyecto: Metodologías 
# Autor: Renata Alejandra Olvera Flores
# ==========================================

# Contenido del trabajo
contenido = """
¿Qué metodología de proyecto es la mejor para llevar a cabo los proyectos de investigación y práctica para la materia de IA?

La metodología más adecuada es Agile, específicamente usando Scrum, ya que permite trabajar de manera flexible, iterativa y adaptarse a los cambios constantes que existen en los proyectos de inteligencia artificial.

Esto es importante porque en la IA:

- No siempre se conocen los resultados desde el inicio
- Se necesita experimentar con datos y modelos
- Es común tener que corregir y mejorar varias veces

Con Agile, el proyecto se divide en pequeñas etapas llamadas sprints, donde en cada una se avanza, se prueba y se mejora el sistema. Esto facilita el aprendizaje práctico y el desarrollo progresivo del proyecto.

¿Cuáles otras metodologías son compatibles?

Además de Agile, existen otras metodologías que se pueden usar en conjunto para mejorar el desarrollo de proyectos de IA:

1. CRISP-DM
Es una metodología especializada en proyectos de datos e inteligencia artificial.
Ayuda a organizar el trabajo en fases como:
- Comprensión del problema
- Análisis de datos
- Modelado
- Evaluación

Es muy útil para estructurar la parte técnica del proyecto.

2. Lean
Se enfoca en optimizar recursos y eliminar procesos innecesarios.

En IA ayuda a:
- Evitar uso excesivo de datos
- Reducir tiempo de entrenamiento
- Hacer el proyecto más eficiente

3. Waterfall
Es una metodología tradicional y secuencial.

Aunque no es ideal para IA, puede servir para:
- Planeación inicial
- Documentación del proyecto

4. Six Sigma
Se enfoca en mejorar la calidad y reducir errores.

En IA se puede aplicar para:
- Mejorar la precisión de modelos
- Reducir fallos en resultados
"""

# Crear archivo
with open("Metodologias_IA.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print("Archivo generado correctamente: Metodologias_IA.txt")