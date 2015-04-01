#!/usr/bin/env python

# WARNING: this implementation should be fixed.

"""
Iterative Deeping A* Algorithm (IDA*)

See the A* implementation for the algorithm descritpion.
This implementation is an iterative version described by Professor Richard Korf in 1985.
It repeats a bounded depth-first search to cut path that are longer than a function f(n).
If no solution is found, then it increases the maximum bound and try to find a solution again.
It expands more nodes but it avoids resource's saturation and it finds the best path
using the same time of the classic A* algorithm.

"""

import heapq

from EightPuzzleProblem import EightPuzzleProblem, State


def IDAstar(problem):
    global c
    c = 0
    start = problem.start
    goal = problem.goal
    start.g = 0
    start.f = problem.f(start)
    solution = start.f
    while type(solution) is int:
        solution = dfs(start, goal, solution, problem)

    return (problem.path(solution, start), c)


def dfs(node, goal, cost, problem):
    global c
    if node == goal:
        print 'GOAL!'
        return node

    c += 1

    children = problem.successors(node)
    new_cost = 50
    for child in children:
        child.g = node.g + 1
        child.f = problem.f(child)
        child.parent = node

        if child.f <= cost:
            result = dfs(child, goal, cost, problem)
            if type(result) is not int:
                return result
            else:
                new_cost = min(result, new_cost)
        else:
            new_cost = min(new_cost, child.f)
    return new_cost
