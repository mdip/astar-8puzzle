#!/usr/bin/env python

"""
Rappresentazione del gioco dell'otto.
"""

from Node import Node


class State(object):
    """
    Rappresentazione di uno stato del problema.
    """

    def __init__(self, config=None):
        self.__config = []
        self.__config.extend(config)

    @property
    def config(self):
        return self.__config

    def __str__(self):
        return str(self.__config)

    def __repr__(self):
        return str(self.__config)

    def show(self):
        s = ' -------------\n'
        for i in xrange(len(self.__config)):
            s += ' | ' + str(self.__config[i])
            if (i+1) % 3 == 0:
                s += ' |\n'
                s += ' -------------\n'
        return s

    def __eq__(self, other):
        return self.__config == other.__config

    def __hash__(self):
        """
        Hash della configurazione corrente
        """
        return hash(tuple(self.__config))


class EightPuzzleProblem(object):
    """
    Rappresentazione del problema, della funzione successori,
    della funzione costo del cammino, della funzione euristica e
    della funzione che restituisce la soluzione del problema.
    """

    def __init__(self, start, goal):
        self.start = Node(start)
        self.goal = Node(goal)
        self.h = self.manhattan

    def set_heuristic(self, heuristic_id):
        if heuristic_id == 1:
            self.h = self.misplaced_tiles
        else:
            self.h = self.manhattan

    def get_ideal_coord(self, num):
        if num is 0:
            return (2, 2)
        elif num is 1:
            return (1, 1)
        elif num is 2:
            return (1, 2)
        elif num is 3:
            return (1, 3)
        elif num is 4:
            return (2, 3)
        elif num is 5:
            return (3, 3)
        elif num is 6:
            return (3, 2)
        elif num is 7:
            return (3, 1)
        elif num is 8:
            return (2, 1)

    def get_current_coord(self, pos):
        '''
            Data una posizione in un array
            restituisce le coordinate della
            board per il gioco dell'otto.
        '''
        y = pos % 3 + 1
        x = pos / 3 + 1
        return (x, y)

    def get_list_pos(self, x, y):
        '''
           Date le coordinate, ritorna la posizione dell'elemento
           associato alle coordinate all'interno di una lista.
        '''
        pos = ((x - 1) * 3) + (y - 1)
        return pos

    def heuristic(self, n):
        return self.h(n)

    def manhattan(self, n):
        """
            Distanza di Manhattan
        """
        dist = 0
        values = n.content.config
        for v in values:
            x1, y1 = self.get_current_coord(values.index(v))
            x2, y2 = self.get_ideal_coord(v)
            d = abs(x1 - x2) + abs(y1 - y2)
            dist += d
        return dist

    def misplaced_tiles(self, n):
        """
            Tasselli fuoriposto
        """
        dist = 0
        values = n.content.config
        for v in values:
            if self.get_current_coord(values.index(v)) != self.get_ideal_coord(v):
                dist += 1
        return dist

    def f(self, n):
        """
            f(n) = g(n) + h(n)
            in questo caso h = manhattan
        """
        return (n.g + self.heuristic(n))

    # Path dalla soluzione allo stato di partenza
    def path(self, goal, start):
        if goal == start:
            return [goal]
        elif goal.parent is not None:
            return self.path(goal.parent, start) + [goal]
        else:
            return []

    # Funzione successori definita in base al contesto, in questo caso il gioco dell'8
    def successors(self, node):
        succ_list = []
        state = node.content
        empty = state.config.index(0)
        x, y = self.get_current_coord(empty)

        # up
        if x > 1:
            new_x = x - 1
            new_y = y
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.config[idx]
            new_state = State(state.config)
            new_state.config[idx] = 0
            new_state.config[empty] = swap_value
            n = Node(new_state)
            succ_list.append(n)
            #print 'UP'

        if x < 3:
            new_x = x + 1
            new_y = y
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.config[idx]
            new_state = State(state.config)
            new_state.config[idx] = 0
            new_state.config[empty] = swap_value
            n = Node(new_state)
            succ_list.append(n)
            #print 'DOWN'

        if y > 1:
            new_x = x
            new_y = y - 1
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.config[idx]
            new_state = State(state.config)
            new_state.config[idx] = 0
            new_state.config[empty] = swap_value
            n = Node(new_state)
            succ_list.append(n)
            #print 'LEFT'

        if y < 3:
            new_x = x
            new_y = y+1
            idx = self.get_list_pos(new_x, new_y)
            swap_value = state.config[idx]
            new_state = State(state.config)
            new_state.config[idx] = 0
            new_state.config[empty] = swap_value
            n = Node(new_state)
            succ_list.append(n)
            #print 'RIGHT'

        #genera successori in base alle mosse possibili
        return succ_list

