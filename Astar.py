#!/usr/bin/env python

"""
A* Algorithm

La funzione f(n) = g(n) + h(n) e' alla base dell'algoritmo:
- g(n) indica la distanza di <n> dal nodo start di partenza.
- h(n) stima la distanza da <n> al nodo goal di arrivo.

f(n) rappresenta il cammino meno costoso dal nodo <start> al nodo <goal>.

h(n) e' una funzione euristica che stima il costo
di un cammino dal nodo <n> al nodo <goal>.
La funzione si dice ammissibile se non sovrastima il costo.

Implementazione con restrizione monotonica --> serve una euristica 
con restrizione monotonica.
"""

import heapq

from EightPuzzleProblem import EightPuzzleProblem, State

#@profile
# Attivare profile per controllare l'utilizzo di memoria
# per utilizzare @profile il comando e':
# python -m memory_profiler example.py


def Astar(problem):
    start = problem.start
    goal = problem.goal

    c = 0
    # Crea un dizionario CLOSED ed una lista OPEN che verra' gestita come un heap ordinato in base a f(n) = g(n) + h(n).
    # Crea un dizionario OPENDICT per un accesso O(1) nelle fasi di verifica.

    OPEN = []
    CLOSED = {}

    c = 0  # contatore nodi considerati

    start.f = problem.heuristic(start)
    heapq.heappush(OPEN, start)

    OPEN_DICT = {}
    OPEN_DICT[start.content] = start
    c += 1

    while OPEN:
        n = heapq.heappop(OPEN)
        c += 1
        CLOSED[n.content] = n
        if n == goal:
            print 'GOAL!'
            return (problem.path(n, start), c)

        s = problem.successors(n)

        dist = n.g  # distanza del nodo n dal nodo start
        dist_suc = dist+1  # distanza di ogni successore di n dal nodo start

        for suc in s:
            # Per ogni successore imposta come genitore il nodo n,
            # incrementa di 1 la distanza da start e calcola f(n)
            suc.parent = n
            suc.g = dist_suc
            suc.f = problem.f(suc)

            conf = suc.content

            if not conf in OPEN_DICT and not conf in CLOSED:
                heapq.heappush(OPEN, suc)
                OPEN_DICT[conf] = suc
            else:
                if conf in OPEN_DICT and OPEN_DICT[conf].f - OPEN_DICT[conf].g - suc.f - suc.g > 1:
                    pass
                elif conf in CLOSED and CLOSED[conf].f - CLOSED[conf].g - suc.f - suc.g > 1:
                    del CLOSED[conf]
                else:
                    continue

                heapq.heapreplace(OPEN, suc)
                OPEN_DICT[conf] = suc
