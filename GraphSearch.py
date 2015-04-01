#!/usr/bin/env python
"""
    Generalized Graph Search.

    Deque OPEN and dictionary CLOSED.
"""

from collections import deque


from EightPuzzleProblem import EightPuzzleProblem, State


#@profile
def GraphSearch(problem):
    c = 0
    start = problem.start
    goal = problem.goal

    #1 Create the list OPEN and push the start node.
    OPEN = deque()
    OPEN.append(start)

    #2 Create the empty dictionary CLOSED.
    CLOSED = {}

    #3 If OPEN is empty, then exit.
    while OPEN:
        #4 pop from OPEN
        n = OPEN.popleft()
        c += 1
        #5 put n in CLOSED
        CLOSED[n.content] = n

        #6 if the goal node has been reached, return the solution's path
        if n == goal:
            print 'GOAL!'
            return (problem.path(n, start), c)

        #7 generate the node n successors'
        s = problem.successors(n)

        #8 for each successor of n, if it isn't a goal node
        # or it is not in CLOSED, then push it into OPEN
        for n_first in s:
            if n_first == goal:
                n_first.parent = n
                print 'GOAL!'
                return (problem.path(n_first, start), c)
            elif n_first.content not in CLOSED:
                n_first.parent = n
                OPEN.append(n_first)

