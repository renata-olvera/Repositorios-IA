"""
==================================================
Nombre: Búsqueda en Anchura (BFS)
Autor: Renata Alejandra Olvera Flores 
Materia: Inteligencia Artificial
Fecha: 17/04/2026

Enfoque: Búsqueda en Grafos
Subtema: Búsqueda No Informada

Descripción:
Este programa implementa el algoritmo de Búsqueda en Anchura (Breadth-First Search),
el cual recorre un grafo explorando primero los nodos más cercanos al nodo inicial.

Funcionamiento:
1. Se utiliza una cola (FIFO) para almacenar los nodos por visitar.
2. Se comienza desde un nodo inicial.
3. Se visitan todos los vecinos antes de avanzar al siguiente nivel.
4. Se evita repetir nodos ya visitados.

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
# FUNCIÓN DEL ALGORITMO BFS


def busqueda_anchura(grafo, inicio):
    """
    Realiza un recorrido BFS en un grafo.

    Parámetros:
    - grafo: Diccionario con listas de adyacencia
    - inicio: Nodo inicial

    Retorna:
    - Lista de nodos visitados en orden BFS
    """

    # Lista donde se guardarán los nodos visitados
    visitados = []

    # Cola para manejar los nodos pendientes (FIFO)
    cola = [inicio]

    # Mientras haya nodos en la cola
    while cola:
        # Se extrae el primer nodo de la cola
        nodo = cola.pop(0)

        # Si el nodo no ha sido visitado
        if nodo not in visitados:
            # Se marca como visitado
            visitados.append(nodo)

            # Se agregan sus vecinos a la cola
            cola.extend(grafo[nodo])

    # Se devuelve el recorrido completo
    return visitados

# BLOQUE PRINCIPAL


if __name__ == "__main__":
    print("Ejecutando algoritmo: Búsqueda en Anchura (BFS)")

 # DEFINICIÓN DEL GRAFO

    # Representación del grafo usando diccionario
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
    
    resultado = busqueda_anchura(grafo, inicio)

# RESULTADO

    print("Recorrido BFS:", resultado)