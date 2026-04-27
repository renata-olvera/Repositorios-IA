"""
==================================================
Nombre: Búsqueda en Profundidad (DFS)
Autor: Renata Alejandra Olvera Flores
Materia: Inteligencia Artificial
Fecha:17/04/2026

Enfoque: Búsqueda en Grafos
Subtema: Búsqueda No Informada

Descripción:
Este programa implementa el algoritmo de Búsqueda en Profundidad (Depth-First Search),
el cual recorre un grafo explorando lo más profundo posible antes de retroceder.

Funcionamiento:
1. Se utiliza recursión (o una pila).
2. Se comienza desde un nodo inicial.
3. Se visita un nodo y luego se explora uno de sus vecinos.
4. Si no hay más vecinos, se regresa al nodo anterior.

Entradas:
- grafo: Diccionario que representa el grafo
- inicio: Nodo desde donde comienza la búsqueda

Salidas:
- Lista con el orden de los nodos visitados

Complejidad:
- Tiempo: O(n + e)
- Espacio: O(n)
==================================================
"""

# FUNCIÓN DEL ALGORITMO DFS

def busqueda_profundidad(grafo, nodo, visitados=None):
    """
    Realiza un recorrido DFS en un grafo.

    Parámetros:
    - grafo: Diccionario con listas de adyacencia
    - nodo: Nodo actual
    - visitados: Lista de nodos visitados

    Retorna:
    - Lista de nodos visitados en orden DFS
    """

    # Si es la primera llamada, inicializar lista
    if visitados is None:
        visitados = []

    # Marcar el nodo como visitado
    visitados.append(nodo)

    # Recorrer los vecinos del nodo
    for vecino in grafo[nodo]:
        # Si el vecino no ha sido visitado
        if vecino not in visitados:
            # Llamada recursiva
            busqueda_profundidad(grafo, vecino, visitados)

    # Retornar lista de visitados
    return visitados


# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("Ejecutando algoritmo: Búsqueda en Profundidad (DFS)")

    # DEFINICIÓN DEL GRAFO


    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    # Nodo inicial
    inicio = 'A'

    # EJECUCIÓN DEL ALGORITMO
    
    resultado = busqueda_profundidad(grafo, inicio)

    # RESULTADO

    print("Recorrido DFS:", resultado)