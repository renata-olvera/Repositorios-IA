"""
==================================================
Nombre: Búsqueda Bidireccional
Autor: Renata Alejandra Olvera Flores
Materia: Inteligencia Artificial
Fecha: 17/04/2026

Enfoque: Búsqueda en Grafos
Subtema: Búsqueda No Informada

Descripción:
Este algoritmo realiza una búsqueda simultánea desde el nodo inicial
y desde el nodo objetivo, hasta encontrar un punto de intersección.

Funcionamiento:
1. Se inicializan dos búsquedas tipo BFS:
   - Una desde el inicio
   - Otra desde el objetivo
2. Ambas avanzan nivel por nivel.
3. Se verifica si hay intersección entre los nodos visitados.
4. Si se encuentran, se detiene la búsqueda.

Entradas:
- grafo: Diccionario que representa el grafo
- inicio: Nodo inicial
- objetivo: Nodo destino

Salidas:
- Nodo donde se encuentran ambas búsquedas (intersección)

Complejidad:
- Tiempo: O(b^(d/2))
- Espacio: O(b^(d/2))
==================================================
"""

# FUNCIÓN AUXILIAR BFS

def bfs_nivel(grafo, cola, visitados):
    """
    Expande un nivel en la búsqueda BFS.
    """

    siguiente_cola = []

    for nodo in cola:
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                siguiente_cola.append(vecino)

    return siguiente_cola


# FUNCIÓN BIDIRECCIONAL

def busqueda_bidireccional(grafo, inicio, objetivo):
    """
    Realiza búsqueda bidireccional.
    """

    # Si inicio es igual al objetivo
    if inicio == objetivo:
        return inicio

    # Conjuntos de visitados
    visitados_inicio = set([inicio])
    visitados_objetivo = set([objetivo])

    # Colas para cada búsqueda
    cola_inicio = [inicio]
    cola_objetivo = [objetivo]

    # Mientras ambas colas tengan elementos
    while cola_inicio and cola_objetivo:

        # Expandir desde el inicio
        cola_inicio = bfs_nivel(grafo, cola_inicio, visitados_inicio)

        # Verificar intersección
        interseccion = visitados_inicio.intersection(visitados_objetivo)
        if interseccion:
            return interseccion.pop()

        # Expandir desde el objetivo
        cola_objetivo = bfs_nivel(grafo, cola_objetivo, visitados_objetivo)

        # Verificar intersección nuevamente
        interseccion = visitados_inicio.intersection(visitados_objetivo)
        if interseccion:
            return interseccion.pop()

    return None


# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("Ejecutando: Búsqueda Bidireccional")

    # GRAFO DE EJEMPLO

    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'G'],
        'F': ['C'],
        'G': ['E']
    }

    inicio = 'A'
    objetivo = 'G'

    # EJECUCIÓN

    resultado = busqueda_bidireccional(grafo, inicio, objetivo)

    # RESULTADO

    print("Nodo de intersección:", resultado)