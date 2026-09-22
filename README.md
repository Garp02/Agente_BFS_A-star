<div align="right">
22 / 09 / 26
<br><br>
<strong>Fundamentos de IA</strong>
<br>
<strong>Autor(es): Ibrahim Munive Ramírez</strong>
</div>

# Tarea 3
En este repositorio se diseñó un agente con la implementación de 
Breadth-First Search y $A^*$.

--- 

## Marco teórico

### BFS
Breadth-First Search (BFS) es un algoritmo de búsqueda no informada que 
explora el espacio de estados nivel por nivel, es decir, primero revisa 
todos los estados alcanzables a una distancia de un paso desde el estado 
inicial, luego los que están a dos pasos, y así sucesivamente.

El algoritmo mantiene una cola (estructura FIFO) que inicia con el estado 
raíz. Mientras la cola no esté vacía, se hace "dequeue" del primer 
elemento y se revisa si es el estado objetivo; si no lo es, se generan 
sus estados sucesores (los estados accesibles desde él) y se agregan al 
final de la cola, evitando volver a encerar estados ya visitados. Este 
proceso continúa hasta encontrar el estado objetivo o hasta agotar todos 
los estados alcanzables.

Como explora nivel por nivel, BFS garantiza encontrar la solución con el 
menor número de pasos (camino más corto en número de transiciones), 
siempre que el costo de cada transición entre estados sea uniforme. Su 
principal desventaja es el consumo de memoria, ya que debe almacenar 
todos los nodos de cada nivel antes de avanzar al siguiente.

### A*
$A^*$ es un algoritmo de búsqueda informada que combina las ventajas de BFS 
(garantía de encontrar una solución) con el uso de una heurística que 
guía la exploración hacia el estado objetivo, en lugar de expandir los 
estados de manera "ciega" nivel por nivel.

En vez de una cola simple, $A^*$ utiliza una cola de prioridad, donde cada 
estado n se ordena según una función de evaluación:

$$f(n) = g(n) + h(n)$$

- $g(n)$: costo real acumulado para llegar del estado inicial al estado $n$.
- $h(n)$: estimación heurística del costo restante desde $n$ hasta el 
  estado objetivo.
- $f(n)$: costo estimado total del camino que pasa por $n$.

En cada iteración, $A^*$ expande el estado con el menor valor de $f(n)$ de 
la cola de prioridad, genera sus sucesores accesibles, calcula su g y h 
correspondientes, y los agrega a la cola. El proceso termina cuando el 
estado extraído es el estado objetivo.

Si la heurística $h(n)$ es admisible (nunca sobreestima el costo real 
restante) y consistente, $A^*$ garantiza encontrar el camino óptimo, al 
igual que BFS, pero explorando en general muchos menos estados, ya que 
la heurística evita expandir ramas que se alejan del objetivo. Cuando 
$h(n) = 0$ para todo estado, $A^*$ se reduce exactamente a una búsqueda tipo 
Dijkstra (o a BFS si además los costos de transición son uniformes).

--- 

### Referencias

- [Medium - ¿Qué es Breadth First Search (BFS) y cómo utilizarlo?](https://medium.com/@leonardoingallshernandez/que-es-breadth-first-search-bfs-y-como-utilizarlo-5f9dae3e4de7)

- [Wikipedia - Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)

- [Wikipedia - A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)

- [GeeksforGeeks - A* Search Algorithm](https://www.geeksforgeeks.org/dsa/a-search-algorithm/)