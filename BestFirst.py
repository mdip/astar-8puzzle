#!/usr/bin/env python

"""

Best First Search

Graph Search con ordinamento di OPEN rispetto ad h(n).

"""

import heapq

from EightPuzzleProblem import EightPuzzleProblem, State


#@profile
def BestFirstSearch(problem):

    start = problem.start
    goal = problem.goal

    # Crea un dizionario CLOSED ed una lista OPEN che verra' gestita
    # come un heap ordinato in base a f(n) = g(n) + h(n).

    OPEN = []
    CLOSED = {}

    c = 0  # contatore nodi considerati

    start.f = problem.f(start)
    heapq.heappush(OPEN, start)

    while OPEN:
        n = heapq.heappop(OPEN)
        CLOSED[n.content] = n
        c += 1

        if n == goal:
            print 'GOAL!'
            return (problem.path(n, start), c)

        s = problem.successors(n)

        for suc in s:
            # Per ogni successore imposta come genitore il nodo n,
            # calcola f(n) considerando solamente h(n)
            suc.parent = n
            suc.f = problem.f(suc)

            conf = suc.content

            if suc == goal:
                print 'GOAL!'
                return (problem.path(suc, start), c)
            elif conf not in CLOSED:
                heapq.heappush(OPEN, suc)
