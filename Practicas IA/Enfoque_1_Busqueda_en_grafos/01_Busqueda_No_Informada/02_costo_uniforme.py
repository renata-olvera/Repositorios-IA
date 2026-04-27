"""
==================================================
Nombre: Búsqueda de Costo Uniforme (UCS)
Autor: [Tu nombre]
Materia: Inteligencia Artificial
Fecha: 17/04/2026

Enfoque: Búsqueda en Grafos
Subtema: Búsqueda No Informada

Descripción:
Este algoritmo encuentra el camino de menor costo desde un nodo inicial
hasta todos los demás nodos en un grafo ponderado.

Funcionamiento:
1. Se utiliza una cola de prioridad.
2. Se expande el nodo con menor costo acumulado.
3. Se actualizan los costos de los vecinos.
4. Se evita explorar nodos con mayor costo.

Entradas:
- grafo: Diccionario con vecinos y costos
- inicio: Nodo inicial

Salidas:
- Diccionario con el costo mínimo a cada nodo

Complejidad:
- Tiempo: O((n + e) log n)
- Espacio: O(n)
==================================================
"""

import heapq  # Para usar cola de prioridad

# FUNCIÓN UCS

def costo_uniforme(grafo, inicio):
    """
    Implementa búsqueda de costo uniforme.

    Parámetros:
    - grafo: Diccionario {nodo: [(vecino, costo)]}
    - inicio: Nodo inicial

    Retorna:
    - Diccionario con costos mínimos
    """

    # Cola de prioridad (costo, nodo)
    frontera = [(0, inicio)]

    # Costos mínimos conocidos
    costos = {inicio: 0}

    # Mientras haya nodos por explorar
    while frontera:
        # Extraer nodo con menor costo
        costo_actual, nodo = heapq.heappop(frontera)

        # Explorar vecinos
        for vecino, costo in grafo[nodo]:
            nuevo_costo = costo_actual + costo

            # Si no se ha visitado o encontramos un mejor camino
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                heapq.heappush(frontera, (nuevo_costo, vecino))

    return costos


# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("Ejecutando: Búsqueda de Costo Uniforme")

    # GRAFO CON COSTOS

    grafo = {
        'A': [('B', 1), ('C', 5)],
        'B': [('D', 2), ('E', 4)],
        'C': [('F', 1)],
        'D': [],
        'E': [],
        'F': []
    }

    # Nodo inicial
    inicio = 'A'

    # EJECUCIÓN

    resultado = costo_uniforme(grafo, inicio)

    # RESULTADO

    print("Costos mínimos desde A:")
    for nodo, costo in resultado.items():
        print(f"{nodo}: {costo}")