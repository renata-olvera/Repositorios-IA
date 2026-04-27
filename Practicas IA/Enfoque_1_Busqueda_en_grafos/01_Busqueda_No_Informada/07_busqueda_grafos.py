"""
==================================================
Nombre: Búsqueda en Grafos (General)
Autor: Renata Alejandra Olvera Flores 
Materia: Inteligencia Artificial
Fecha: [Fecha]

Enfoque: Búsqueda en Grafos
Subtema: Búsqueda No Informada

Descripción:
Este algoritmo implementa una búsqueda general en grafos utilizando
una estructura de frontera y un conjunto de nodos explorados para
evitar ciclos y repeticiones.

Funcionamiento:
1. Se inicializa una frontera con el nodo inicial.
2. Se extrae un nodo de la frontera.
3. Si no ha sido explorado, se procesa.
4. Se agregan sus vecinos a la frontera.
5. Se repite hasta vaciar la frontera.

Entradas:
- grafo: Diccionario que representa el grafo
- inicio: Nodo inicial

Salidas:
- Lista con el orden de los nodos explorados

Complejidad:
- Tiempo: O(n + e)
- Espacio: O(n)
==================================================
"""

# FUNCIÓN BÚSQUEDA GENERAL

def busqueda_grafo(grafo, inicio):
    """
    Realiza una búsqueda general en grafos.

    Parámetros:
    - grafo: Diccionario con listas de adyacencia
    - inicio: Nodo inicial

    Retorna:
    - Lista de nodos explorados
    """

    # Frontera: nodos pendientes por explorar
    frontera = [inicio]

    # Conjunto de nodos ya explorados
    explorados = set()

    # Lista para guardar el recorrido
    recorrido = []

    # Mientras haya nodos en la frontera
    while frontera:
        # Sacar el primer nodo (puede cambiar según estrategia)
        nodo = frontera.pop(0)

        # Si no ha sido explorado
        if nodo not in explorados:
            # Marcar como explorado
            explorados.add(nodo)

            # Agregar al recorrido
            recorrido.append(nodo)

            # Agregar vecinos a la frontera
            for vecino in grafo[nodo]:
                if vecino not in explorados:
                    frontera.append(vecino)

    return recorrido


# BLOQUE PRINCIPAL

if __name__ == "__main__":
    print("Ejecutando: Búsqueda en Grafos (General)")

    # GRAFO DE EJEMPLO

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

    # EJECUCIÓN

    resultado = busqueda_grafo(grafo, inicio)

    # RESULTADO

    print("Recorrido:", resultado)