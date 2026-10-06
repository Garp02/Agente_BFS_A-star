"""
Agente: El Caballero y el Dragón (modificado)

Sistema de transición de estados: Sigma' = (S', A', E', gamma')
Estado s = (p, e, d): p posición, e tiene espada, d dragón vivo
Acciones A' = {norte, sur, este, oeste, tomar, matar}
Problema de planeación P' = (Sigma', s_i, g)

Coordenadas (x, y): el origen está abajo a la izquierda, x crece hacia
el este y y crece hacia el norte.

  +---+---+---+---+---+---+---+
6 | C |   | X |   |   |   | X |
  +---+---+---+---+---+---+---+
5 |   |   | X |   | D |   |   |
  +---+---+---+---+---+---+---+
4 |   |   | X |   | X |   |   |
  +---+---+---+---+---+---+---+
3 |   | X |   |   |   |   |   |
  +---+---+---+---+---+---+---+
2 |   |   |   |   |   | X |   |
  +---+---+---+---+---+---+---+
1 |   |   |   | X |   | X |   |
  +---+---+---+---+---+---+---+
0 |   | X |   | X | E |   |   |
  +---+---+---+---+---+---+---+
    0   1   2   3   4   5   6
"""

# Definición del mundo
N = 7
POS_INICIAL_DEFECTO = (0, 6)
POS_ESPADA = (4, 0)
POS_DRAGON = (4, 5)
POS_OBSTACULOS = {(1, 0), (1, 3), (2, 4), (2, 5), (2, 6), (3, 0), 
                  (3, 1), (4, 4), (5, 1), (5, 2), (6, 6)}


# Posiciones
def es_valida(p):
    """Una posición es transitable si está en el tablero y no es obstáculo."""
    x, y = p
    
    return (0 <= x < N) and (0 <= y < N) and (p not in POS_OBSTACULOS)


def es_posicion_inicial_valida(p):
    """Válida si es transitable y no está ocupada por la espada o el dragón."""
    return es_valida(p) and p not in (POS_ESPADA, POS_DRAGON)


def pedir_posicion_inicial():
    """Pide x, y por teclado hasta que la posición sea válida."""
    while True:
        
        try:
        
            x = int(input('Ingrese la posición x inicial: '))
            y = int(input('Ingrese la posición y inicial: '))
        
        except ValueError:
        
            print('Ingrese números enteros.')
            continue

        if es_posicion_inicial_valida((x, y)): return (x, y)
        
        print('Posición inválida: fuera del tablero o con otro elemento.')


# Estado: s = (p, e, d)
def estado_inicial(p = POS_INICIAL_DEFECTO):
    """Estado inicial s_i = (p, 0, 1): sin espada y con el dragón vivo."""
    return (p, 0, 1)


def es_meta(s):
    """g(s): el dragón está morido, es decir, d = 0."""
    _, _, d = s
    return d == 0


# Acciones y función de transición gamma(s, a)
def _mover(dx, dy):

    def accion(s):
        
        (x, y), e, d = s
        nueva = (x + dx, y + dy)

        if es_valida(nueva): return (nueva, e, d)
        
        return None

    return accion

def _tomar(s):
    
    p, e, d = s

    if (p == POS_ESPADA) and (e == 0): return (p, 1, d)
    
    return None

def _matar(s):
    
    p, e, d = s

    if (p == POS_DRAGON) and (e == 1) and (d == 1): return (p, e, 0)
    
    return None

ACCIONES = {'norte': _mover(0, 1), 'sur': _mover(0, -1),
    'este': _mover(1, 0), 'oeste': _mover(-1, 0),
    'tomar': _tomar, 'matar': _matar}


def gamma(s, a):
    """gamma(s, a) regresa s' si a es aplicable en s, si no None (vacío)."""
    return ACCIONES[a](s)


def es_aplicable(s, a): return gamma(s, a) is not None


# Función sucesor Gamma(s)
def sucesores(s):
    """Regresa la lista de pares (acción, s') con acciones aplicables en s."""
    return [(a, s2) for a in ACCIONES if (s2 := gamma(s, a)) is not None]


# Planes: extensión de gamma a secuencias de acciones
def estados_de_plan(s, plan):
    """Regresa la lista de estados que recorre el plan, o None si falla."""
    estados = [s]
    for a in plan:
        
        s = gamma(s, a)
        
        if s is None: return None
        
        estados.append(s)
    
    return estados

def gamma_plan(s, plan):
    """gamma(s, pi): estado al que se llega aplicando el plan completo."""
    estados = estados_de_plan(s, plan)
    return None if estados is None else estados[-1]


# Heurística para A*
def distancia(p, q):
    """Distancia Manhattan entre dos posiciones."""
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def heuristica(s):
    """
    Estimación del número de acciones restantes, ignorando obstáculos.

    Sin espada: ir a la espada, tomarla, ir al dragón y matarlo.
    Con espada y dragón vivo: ir al dragón y matarlo.
    Es admisible y consistente porque cada acción cuesta 1 y cada
    movimiento cambia la distancia Manhattan en a lo más 1.
    """
    p, e, d = s

    if d == 0: return 0

    if e == 0: return distancia(p, POS_ESPADA) + distancia(POS_ESPADA, POS_DRAGON) + 2
    
    return distancia(p, POS_DRAGON) + 1

# Resultado común de los algoritmos de búsqueda
def armar_resultado(algoritmo, estados, plan, explorados):
    """Diccionario que consume tablero_con_recorrido."""
    return {'algoritmo': algoritmo, 'plan': plan, 'estados': estados,
        'explorados': explorados, 'pasos': len(explorados),}


# Visualización del recorrido
def tablero_con_recorrido(resultado):
    """
    Regresa un texto con el tablero, el recorrido y las opciones descartadas.

    resultado es un diccionario que debe regresar cada algoritmo de búsqueda:
      algoritmo: nombre del algoritmo
      plan: lista de acciones, o None si no hay solución
      estados: lista de estados del camino solución (vacía si no hay)
      explorados: estados extraídos de la frontera, en orden de exploración
      pasos: número de nodos explorados hasta encontrar la solución

    Los estados (p, e, d) se proyectan a su posición p. Una casilla
    descartada es una que el algoritmo exploró pero que no está en el
    camino solución.
    """
    camino = {p for p, _, _ in resultado['estados']}
    exploradas = {p for p, _, _ in resultado['explorados']}
    descartadas = exploradas - camino

    if resultado['estados']: inicio = resultado['estados'][0][0]
    
    elif resultado['explorados']: inicio = resultado['explorados'][0][0]
    
    else: inicio = None

    def simbolo(p):
        
        if p == inicio: return 'C'
        
        if p == POS_DRAGON: return 'D'
        
        if p == POS_ESPADA: return 'E'
        
        if p in POS_OBSTACULOS: return 'X'
        
        if p in camino: return '*'
        
        if p in descartadas: return 'o'
        
        return ' '

    separador = '  +' + '---+' * N
    lineas = []

    for y in range(N - 1, -1, -1):
    
        celdas = ' | '.join(simbolo((x, y)) for x in range(N))
        lineas.append(separador)
        lineas.append(f'{y} | {celdas} |')
    
    lineas.append(separador)
    lineas.append('    ' + '   '.join(str(x) for x in range(N)))

    plan = resultado['plan']
    lineas.append('')
    lineas.append('C: inicio\nD: dragón\nE: espada\nX: obstáculo\n*: camino \no: descartada\n : sin explorar')
    lineas.append(f"Algoritmo: {resultado['algoritmo']}")
    lineas.append(f"Pasos del algoritmo (nodos explorados): "
                  f"{resultado['pasos']}")
    lineas.append(f'Casillas descartadas: {len(descartadas)}')
    
    if plan is None: 
        
        lineas.append('No se encontró solución.')
    
    else:

        lineas.append(f'Longitud del plan: {len(plan)}')
        lineas.append('Plan: ' + ', '.join(plan))

    return '\n'.join(lineas)


# Plan de ejemplo desde la posición inicial por defecto
PLAN = ['sur', 'sur', 'sur', 'sur', 'este', 'este', 'este', 'este',
        'sur', 'sur', 'tomar', 'norte', 'norte', 'norte', 'este',
        'norte', 'norte', 'oeste', 'matar']

if __name__ == '__main__':

    s_i = estado_inicial()
    print(f'Estado inicial s_i = {s_i}')
    print(f'Plan pi (longitud {len(PLAN)})')

    s_final = gamma_plan(s_i, PLAN)
    print(f'gamma(s_i, pi) = {s_final}')

    if s_final is not None and es_meta(s_final): print('Satisface la meta g(s)\n')

    else: print('No satisface la meta g(s)\n')

    resultado = {
        'algoritmo': 'Plan manual',
        'plan': PLAN,
        'estados': estados_de_plan(s_i, PLAN),
        'explorados': [],
        'pasos': 0,
    }
  
    print(tablero_con_recorrido(resultado))