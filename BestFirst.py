#!/usr/bin/env python

"""

Best First Search

Graph Search whit oreded OPEN list according to h(n).

"""

import heapq

from EightPuzzleProblem import EightPuzzleProblem, State


#@profile
def BestFirstSearch(problem):

    start = problem.start
    goal = problem.goal

    # Create a dictionery CLOSED.
    # Create a list OPEN that will be managed as an ordered heap according to f(n) = g(n) + h(n).

    OPEN = []
    CLOSED = {}

    c = 0  # counter of considered nodes

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
            # for every successor set the node n as the parent node,
            # calculate f(n) considering only h(n)
            suc.parent = n
            suc.f = problem.f(suc)

            conf = suc.content

            if suc == goal:
                print 'GOAL!'
                return (problem.path(suc, start), c)
            elif conf not in CLOSED:
                heapq.heappush(OPEN, suc)
