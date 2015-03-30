#!/usr/bin/env python

"""
Iterative Deeping A* Algorithm (IDA*)

Ripete una depth first search limitata scartando i rami che superano
un determinato costo basato su f(n). Se al termine della ricerca un goal
non e' stato trovato, incrementa il limite e ricomincia.
Rispetto ad A* il numero di nodi espansi e' maggiore ma evita la saturazione
delle risorse e produce il cammino migliore in un tempo equivalente ad A*.

La funzione f(n) = g(n) + h(n) e' alla base dell'algoritmo:
- g(n) indica la distanza di <n> dal nodo start di partenza.
- h(n) stima la distanza da <n> al nodo goal di arrivo.

f(n) rappresenta il cammino meno costoso dal nodo <start> al nodo <goal>.

h(n) e' una funzione euristica che stima il costo
di un cammino dal nodo <n> al nodo <goal>.
La funzione si dice ammissibile se non sovrastima il costo.

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
