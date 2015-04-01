#!/usr/bin/env python

"""
A* Algorithm

The function f(n) = g(n) + h(n) is the bases of this algorithm:
- g(n) is the distance of the node <n> from the start node.
- h(n) estimates the distance of node <n> to the goal node.

f(n) is the best path from <start> to <goal>, under certain conditions.

h(n) if an heuristic function and it should never overestimate the cost of the path to be an admissible function.

If h(n) =< d(n,g) + h(g) for every edge (n,g) then A* works better because you are using a monothonic
function that will not consider a node more than one time.

This implementation is oriented to time optimization; it will be used more space.

"""

import heapq

from EightPuzzleProblem import EightPuzzleProblem, State

#@profile
# Enable this annotation to check the memory usage.
# To enable @profile start python in this way:
# python -m memory_profiler example.py


def Astar(problem):
    start = problem.start
    goal = problem.goal

    c = 0
    # Create a dictionary CLOSED.
    # Create a list OPEN that will be managed as an ordered heap according to f(n) = g(n) + h(n).
    # Create a dictionary OPENDICT to access in O(1) in the check phases.

    OPEN = []
    CLOSED = {}

    c = 0  # counter of considered nodes

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

        dist = n.g  # distance of node n from start node
        dist_suc = dist+1  # distance of every successor of n from start node

        for suc in s:
            # for every successor sets the node n as parent node,
            # increment by 1 the distance from start and calculate f(n)
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
