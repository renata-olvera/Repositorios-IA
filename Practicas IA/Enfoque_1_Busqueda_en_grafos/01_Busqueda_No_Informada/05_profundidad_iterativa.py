"""
==================================================
Nombre: Búsqueda en Profundidad Iterativa (IDDFS)
Autor: Renata Alejandra Olvera Flores 
Materia: Inteligencia Artificial
Fecha: 17/04/2026

Enfoque: Búsqueda en Grafos
Subtema: Búsqueda No Informada

Descripción:
Este algoritmo combina DFS y BFS realizando múltiples búsquedas en profundidad
limitada, incrementando el límite en cada iteración hasta encontrar la solución.

Funcionamiento:
1. Se inicia con un límite de profundidad = 0.
2. Se ejecuta una búsqueda en profundidad limitada (DLS).
3. Se incrementa el límite y se repite el proceso.
4. Se detiene cuando se alcanza el nivel deseado.

Entradas:
- grafo: Diccionario que representa el grafo
- inicio: Nodo inicial
- max_profundidad: Límite máximo de búsqueda

Salidas:
- Lista con el recorrido acumulado

Complejidad:
- Tiempo: O(b^d)
- Espacio: O(d)
==================================================
"""

# FUNCIÓN DLS (reutilizada)

def dls(grafo, nodo, limite, visitados=None, profundidad=0):
    """
    Búsqueda en profundidad limitada.
    """

    if visitados is None:
        visitados = []

    visitados.append(nodo)

    if profundidad >= limite:
        return visitados

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dls(grafo, vecino, limite, visitados, profundidad + 1)

    return visitados


# FUNCIÓN IDDFS

def profundidad_iterativa(grafo, inicio, max_profundidad):
    """
    Ejecuta búsqueda en profundidad iterativa.
    """

    resultado_total = []

    # Iterar desde 0 hasta el límite máximo
    for limite in range(max_profundidad + 1):
        print(f"Iteración con límite: {limite}")

        visitados = dls(grafo, inicio, limite)

        # Guardar resultados (sin repetir)
        for nodo in visitados:
            if nodo not in resultado_total:
                resultado_total.append(nodo)

    return resultado_total


# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("Ejecutando: Búsqueda en Profundidad Iterativa")

    # GRAFO DE EJEMPLO

    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G'],
        'E': [],
        'F': [],
        'G': []
    }

    # Nodo inicial
    inicio = 'A'

    # Profundidad máxima
    max_profundidad = 3

    # EJECUCIÓN

    resultado = profundidad_iterativa(grafo, inicio, max_profundidad)

    # RESULTADO

    print("Recorrido IDDFS:", resultado)