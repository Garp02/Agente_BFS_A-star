"""
Búsqueda en anchura (Breadth First Search) para el agente
El Caballero y el Dragón.

Se busca sobre estados completos s = (p, e, d). La prueba de objetivo se
hace al sacar el nodo de la frontera, como se describe en el README.
"""
from collections import deque
from agente import (armar_resultado, es_meta, estado_inicial, pedir_posicion_inicial, 
                    sucesores, tablero_con_recorrido)

class Nodo:

    def __init__(self, estado, padre = None, accion = None):

        self.estado = estado  # (p, e, d)
        self.padre = padre  # Nodo padre
        self.accion = accion  # Acción que llevó a este estado


def reconstruir_camino(nodo):
    """Regresa (estados, acciones) desde el nodo raíz hasta el nodo dado."""
    estados = []
    acciones = []

    while nodo.padre is not None:
        estados.append(nodo.estado)
        acciones.append(nodo.accion)
        nodo = nodo.padre

    estados.append(nodo.estado)
    estados.reverse()
    acciones.reverse()

    return estados, acciones


def bfs(s_i):
    """BFS desde el estado inicial s_i. Regresa el diccionario de resultado."""

    # Frontera como cola FIFO
    frontera = deque([Nodo(s_i)])
    visitados = {s_i}
    explorados = []

    while frontera:

        # Extracción FIFO
        nodo = frontera.popleft()
        explorados.append(nodo.estado)

        # Prueba de objetivo
        if es_meta(nodo.estado):

            estados, plan = reconstruir_camino(nodo)
            return armar_resultado('BFS', estados, plan, explorados)

        # Expandir sucesores
        for accion, s2 in sucesores(nodo.estado):

            if s2 not in visitados:
                
                visitados.add(s2)
                frontera.append(Nodo(s2, nodo, accion))

    return armar_resultado('BFS', [], None, explorados)


# Ejecución principal
if __name__ == '__main__':

    s_i = estado_inicial(pedir_posicion_inicial())
    print(tablero_con_recorrido(bfs(s_i)))