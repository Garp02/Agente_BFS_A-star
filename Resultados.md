# Resultados

Se ejecutaron BFS y $A^\ast$ sobre el tablero fijo de 7x7 con el caballero 
en la posición inicial $p_0 = (0, 6)$, es decir, $s_i = ((0, 6), 0, 1)$.

--- 

## Simbología

| Caracter | Significado |
|:---:|:---|
| `C` | Caballero |
| `D` | Dragón |
| `E` | Espada |
| `X` | Obstáculo |
| `*` | Camino recorrido |
| `o` | Casilla descartada |
| ` ` | Sin explorar |

> Nota: los estados $(p, e, d)$ se proyectan a su casilla $p$, por lo que una 
casilla explorada con y sin espada se dibuja una sola vez.

--- 

## Verificación del plan

Antes de usar los algoritmos se comprobó que un plan de 19 acciones, aplicado 
desde $s_i$, lleva a la meta:

$$\gamma(s_i, \pi) = ((4, 5), 1, 0)$$

El estado final cumple $g(s)$, pues $d = 0$.

--- 

## BFS

```text
  +---+---+---+---+---+---+---+
6 | C | o | X | o | o | o | X |
  +---+---+---+---+---+---+---+
5 | * | o | X | o | D | * | o |
  +---+---+---+---+---+---+---+
4 | * | o | X | o | X | * | o |
  +---+---+---+---+---+---+---+
3 | * | X | o | o | * | * | o |
  +---+---+---+---+---+---+---+
2 | * | * | * | * | * | X | o |
  +---+---+---+---+---+---+---+
1 | o | o | o | X | * | X | o |
  +---+---+---+---+---+---+---+
0 | o | X | o | X | E | o | o |
  +---+---+---+---+---+---+---+
    0   1   2   3   4   5   6
```

| Métrica | Valor |
|:---|:---:|
| Pasos del algoritmo | 70 |
| Casillas descartadas | 22 |
| Longitud del plan | 19 |

Plan:

```text
sur, sur, sur, sur, este, este, este, este, sur, sur, tomar,
norte, norte, norte, este, norte, norte, oeste, matar
```

--- 

## $A^\ast$

```text
  +---+---+---+---+---+---+---+
6 | C | o | X |   |   |   | X |
  +---+---+---+---+---+---+---+
5 | * | o | X | o | D | * |   |
  +---+---+---+---+---+---+---+
4 | * | o | X | o | X | * |   |
  +---+---+---+---+---+---+---+
3 | * | X | o | o | * | * |   |
  +---+---+---+---+---+---+---+
2 | * | * | * | * | * | X |   |
  +---+---+---+---+---+---+---+
1 | o | o | o | X | * | X |   |
  +---+---+---+---+---+---+---+
0 | o | X | o | X | E | o |   |
  +---+---+---+---+---+---+---+
    0   1   2   3   4   5   6
```

| Métrica | Valor |
|:---|:---:|
| Pasos del algoritmo | 37 |
| Casillas descartadas | 13 |
| Longitud del plan | 19 |

Plan:

```text
sur, sur, sur, sur, este, este, este, este, sur, sur, tomar,
norte, norte, norte, este, norte, norte, oeste, matar
```

--- 

## Comparación

| Métrica | BFS | $A^\ast$ |
|:---|:---:|:---:|
| Longitud del plan | 19 | 19 |
| Nodos explorados | 70 | 37 |
| Casillas descartadas | 22 | 13 |

Ambos algoritmos encuentran el mismo plan óptimo de 19 acciones, pero $A^\ast$ 
explora 33 nodos menos, ya que la heurística evita expandir las ramas que se 
alejan del dragón. Esto coincide con lo descrito en el marco teórico: con una 
heurística admisible y consistente, $A^\ast$ conserva la optimalidad de BFS 
con menos exploración.