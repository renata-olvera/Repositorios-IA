"""
==================================================
Nombre: Búsqueda en Profundidad Limitada (DLS)
Autor: Renata Alejandra Olvera Flores
Materia: Inteligencia Artificial
Fecha: 17/04/2026

Enfoque: Búsqueda en Grafos
Subtema: Búsqueda No Informada

Descripción:
Este algoritmo es una variante de DFS que limita la profundidad de exploración,
evitando recorrer el grafo más allá de un nivel definido.

Funcionamiento:
1. Se realiza una búsqueda en profundidad.
2. Se lleva un control de la profundidad actual.
3. Si se alcanza el límite, se detiene la exploración en esa rama.
4. Se continúa con otras ramas disponibles.

Entradas:
- grafo: Diccionario que representa el grafo
- nodo: Nodo actual
- limite: Profundidad máxima permitida

Salidas:
- Lista con los nodos visitados hasta el límite

Complejidad:
- Tiempo: O(b^l)
- Espacio: O(b*l)
==================================================
"""

# FUNCIÓN DEL ALGORITMO DLS

def profundidad_limitada(grafo, nodo, limite, visitados=None, profundidad=0):
    """
    Realiza una búsqueda en profundidad con límite.

    Parámetros:
    - grafo: Diccionario del grafo
    - nodo: Nodo actual
    - limite: Profundidad máxima
    - visitados: Lista de nodos visitados
    - profundidad: Nivel actual

    Retorna:
    - Lista de nodos visitados
    """

    # Inicializar lista si es primera llamada
    if visitados is None:
        visitados = []

    # Marcar nodo como visitado
    visitados.append(nodo)

    # Verificar si se alcanzó el límite
    if profundidad >= limite:
        return visitados

    # Explorar vecinos
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            profundidad_limitada(grafo, vecino, limite, visitados, profundidad + 1)

    return visitados

# BLOQUE PRINCIPAL


if __name__ == "__main__":
    print("Ejecutando: Búsqueda en Profundidad Limitada")

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

    # Límite de profundidad
    limite = 2

    # EJECUCIÓN

    resultado = profundidad_limitada(grafo, inicio, limite)

    # RESULTADO

    print("Recorrido con límite:", resultado)