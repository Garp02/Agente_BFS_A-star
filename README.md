<div align="right">
22 / 09 / 26
<br><br>
<strong>Fundamentos de IA</strong>
<br>
<strong>Autor(es): Ibrahim Munive Ramírez</strong>
</div>

# Tarea 3

En este repositorio se implementaron los algoritmos 
Breadth-First Search y $A^*$ al agente: El caballero 
y el Dragón.

--- 

## Marco teórico

### Agente base: El caballero y el Dragón

Se basa en un tablero donde un caballero parte de su 
estado inicial $s_0$; debe recoger una espada y cruzar 
por el puente para desvivir al dragón.

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/ae28d309-8cd4-425d-88f2-d252543cb50a" />

El problema se modela como un sistema de transición de estados 
$\Sigma = (S, A, E, \gamma)$:

- **Estado:** $s = (p, e, d)$, donde $p = (x, y)$ es la posición del 
  caballero, $e \in \{0, 1\}$ indica si tiene la espada y $d \in \{0, 1\}$ 
  indica si el dragón sigue vivo.
- **Acciones:** $A = \{\text{arriba}, \text{abajo}, \text{izq}, \text{der}, \text{tomar}, \text{matar}\}$.
- **Función de transición:** $\gamma(s, a) = s'$ si la acción $a$ es 
  aplicable en $s$, y vacío en caso contrario. `tomar` solo es aplicable 
  sobre la casilla de la espada y `matar` solo sobre la del dragón con la 
  espada en mano.
- **Estado inicial:** $s_i = ((0, 0), 0, 1)$.
- **Meta:** $g(s)$ se cumple cuando $d = 0$.

Un plan solución es la secuencia de 7 acciones: abajo, der, tomar, arriba, 
der, der, matar.

## Agente modificado

En base al agente anteriormente descrito, se tomarán algunas características y se 
implementarán nuevas, destacanto la implementación de los algoritmos **BFS** y $A^{*}$.

### Diseño de tablero
Se cambiará el tamaño del tablero a uno 7x7 para tener más 
libertad de movimiento. Además, se agregan reestricciones de 
posición, como un laberinto. Este diseño se quedará fijo por 
limitaciones de tiempo y porque no sé cómo resultaría hacer 
que todo esto se hiciera de forma aleatoria. Pero sería muy 
interesante ver el comportamiento de esto si en cada iteración, 
los items y barreras cambiaran de posición. O darle propiedades 
a los obstáculos.

<div align="center">

| | | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 🤺 |  | ⬛ |  |  |  | ⬛ |
|  |  | ⬛ |  | 🐉 |  |  |
|  |  | ⬛ |  | ⬛ |  |  |
|  | ⬛ |  |  |  |  |  |
|  |  |  |  |  | ⬛ |  |
|  |  |  | ⬛ |  | ⬛ |  |
|  | ⬛ |  | ⬛ | 🗡️ |  |  |

</div>

Elementos:
- 🤺: caballero 
- 🐉: dragón
- 🗡️: espada
- ⬛: obstáculo de libre interpretación para el usuario.

> Nota: los emojis son ilustrativos, en la implementación se cambiarán los símbolos por los 
siguientes: $\mathbf{C}$ (caballero), $\mathbf{D}$ (dragón), $\mathbf{E}$ (espada), 
$\mathbf{X}$ (obstáculo). 

### Posición inicial

A diferencia del agente base, en esta versión se podrá establecer 
la posición del estado inicial en donde e usuario indique, siempre 
y cuando sea una posición válida.  

Decimos que una posición es válido si: 

1. $p = (x,y) \backepsilon x,y\in[0,6]$.
2. No hay otro elemento en esa posición. 

#### Sistema de coordenadas

Pasamos de $\{\text{arriba}, \text{abajo}, \text{izq}, \text{der}, \text{tomar}, \text{matar}\}$ 
a $\{\text{norte}, \text{sur},\text{este}, \text{oeste}, \text{tomar}, \text{matar}\}$.

--- 

### Modelado del nuevo problema

Usaremos un sistema de transición de estados similar al del agente base, $\Sigma' = (S', A', E', \gamma')$

- **Estado:** $s = (p, e, d)$, donde $p = (x, y)$ es la posición del 
  caballero, $e \in \{0, 1\}$ indica si tiene la espada y $d \in \{0, 1\}$ 
  indica si el dragón sigue vivo.
- **Acciones:** $A' = \{\text{norte}, \text{sur}\text{este}, \text{oeste}, \text{tomar}, \text{matar}\}$.
- **Función de transición:** $\gamma'(s, a) = s'$ si $a$ es aplicable en $s$, y vacío en 
  caso contrario. `tomar` solo es aplicable 
  sobre la casilla de la espada y `matar` solo sobre la del dragón con la espada en mano.
- **Estado inicial:** $s_i = ((0, 0), 0, 1)$.
- **Meta:** $g(s)$ se cumple cuando $d = 0$.

---

### BFS
Breadth-First Search es un algoritmo de búsqueda no informada que 
explora el espacio de estados nivel por nivel, es decir, primero revisa 
todos los estados alcanzables a una distancia de un paso desde el estado 
inicial, luego los que están a dos pasos, y así sucesivamente.

El algoritmo mantiene una cola (FIFO) que inicia con el estado 
raíz. Mientras la cola no esté vacía, se hace "dequeue" del primer 
elemento y se revisa si es el estado objetivo; si no lo es, se generan 
sus estados sucesores (los estados accesibles desde él) y se agregan al 
final de la cola, evitando volver a encolar estados ya visitados. Este 
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
- $h(n)$: estimación heurística del costo restante desde $n$ hasta el estado objetivo.
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
Dijkstra (o BFS si los costos de transición son iguales).

--- 

### Referencias

- [Fundamentos de Inteligencia Artificial, 27-1](https://turing.iimas.unam.mx/~nohernan/teaching/fundamentos_ia/)

- [Repositorio fundamentos_ia](https://github.com/carlosricardocm/fundamentos_ia)

- [Medium - ¿Qué es Breadth First Search (BFS) y cómo utilizarlo?](https://medium.com/@leonardoingallshernandez/que-es-breadth-first-search-bfs-y-como-utilizarlo-5f9dae3e4de7)

- [Wikipedia - Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)

- [Wikipedia - A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)

- [GeeksforGeeks - A* Search Algorithm](https://www.geeksforgeeks.org/dsa/a-search-algorithm/)

- [Emojis - (🤺, 🐉, 🗡️, ⬛)](https://emojikeyboard.top/es/) 