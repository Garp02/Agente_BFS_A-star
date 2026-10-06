"""
Algoritmo A* para el agente El Caballero y el Dragón.

Cada acción cuesta 1, por lo que g(n) es el número de acciones desde el
estado inicial. La heurística h(n) está definida en agente.py.
"""
import heapq
from itertools import count

from BFS import Nodo, bfs, reconstruir_camino
from agente import (armar_resultado, es_meta, estado_inicial, heuristica,
                    pedir_posicion_inicial, sucesores,tablero_con_recorrido)


def a_estrella(s_i):
    """A* desde el estado inicial s_i. Regresa el diccionario de resultado."""

    # Frontera como cola de prioridad con (f, desempate, g, nodo)
    contador = count()
    frontera = [(heuristica(s_i), next(contador), 0, Nodo(s_i))]
    mejor_g = {s_i: 0}
    explorados = []

    while frontera:
        _, _, g, nodo = heapq.heappop(frontera)

        # Entrada obsoleta: ya se encontró un camino mejor a este estado
        if g > mejor_g[nodo.estado]:
            continue

        explorados.append(nodo.estado)

        # Prueba de objetivo
        if es_meta(nodo.estado):

            estados, plan = reconstruir_camino(nodo)

            return armar_resultado('A*', estados, plan, explorados)

        # Expandir sucesores
        for accion, s2 in sucesores(nodo.estado):

            g2 = g + 1

            if g2 < mejor_g.get(s2, float('inf')):

                mejor_g[s2] = g2
                f2 = g2 + heuristica(s2)
                heapq.heappush(frontera, (f2, next(contador), g2, Nodo(s2, nodo, accion)))

    return armar_resultado('A*', [], None, explorados)

# Ejecución principal
if __name__ == '__main__':

    s_i = estado_inicial(pedir_posicion_inicial())
    res_bfs = bfs(s_i)
    res_astar = a_estrella(s_i)

    print(tablero_con_recorrido(res_bfs))
    print('\n')
    print(tablero_con_recorrido(res_astar))

    if res_bfs['plan'] is not None and res_astar['plan'] is not None:
        
        print('\nComparación')
        print(f"Longitud del plan: BFS {len(res_bfs['plan'])}, "
              f"A* {len(res_astar['plan'])}")
        print(f"Nodos explorados: BFS {res_bfs['pasos']}, "
              f"A* {res_astar['pasos']}")