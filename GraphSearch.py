#!/usr/bin/env python
"""
    Generalized Graph Search.

    Deque OPEN e dizionario CLOSED.
"""

from collections import deque


from EightPuzzleProblem import EightPuzzleProblem, State


#@profile
def GraphSearch(problem):
    c = 0
    start = problem.start
    goal = problem.goal

    #1 Crea una lista OPEN ed inserisci il nodo start.
    OPEN = deque()
    OPEN.append(start)

    #2 Crea un dizionario CLOSED inizialmente vuoto.
    CLOSED = {}

    #3 Se OPEN e' vuota, esci con fallimento.
    while OPEN:
        #4 pop della coda OPEN
        n = OPEN.popleft()
        c += 1
        #5 inserisce n in CLOSED
        CLOSED[n.content] = n

        #6 se il goal e' stato raggiunto, restituisci il percorso solutivo
        if n == goal:
            print 'GOAL!'
            return (problem.path(n, start), c)

        #7 genera i successori del nodo n
        s = problem.successors(n)

        #8 per ogni successore di n, se non e' un nodo goal
        #oppure non e' in CLOSED, aggiungilo in OPEN
        for n_first in s:
            if n_first == goal:
                n_first.parent = n
                print 'GOAL!'
                return (problem.path(n_first, start), c)
            elif n_first.content not in CLOSED:
                n_first.parent = n
                OPEN.append(n_first)

