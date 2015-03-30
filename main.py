#!/usr/bin/env python

import time

from Astar import Astar
#from IDAstar import IDAstar
from BestFirst import BestFirstSearch
from GraphSearch import GraphSearch

from EightPuzzleProblem import EightPuzzleProblem, State

if __name__ == '__main__':

    selection = -1
    while selection < 0:
        print '************************'
        print '*** 8-puzzle problem ***'
        print '************************\n'

        g = State([1, 2, 3, 8, 0, 4, 7, 6, 5])

        easy_s = State([1, 3, 4, 8, 6, 2, 7, 0, 5])
        medium_s = State([2, 8, 1, 0, 4, 3, 7, 6, 5])
        hard_s = State([2, 8, 1, 4, 6, 3, 0, 7, 5])
        worst_s = State([5, 6, 7, 4, 0, 8, 3, 2, 1])
        icse_s = State([2, 1, 6, 4, 0, 8, 7, 5, 3])

        states = [easy_s, medium_s, hard_s, worst_s, icse_s]

        algorithms = [GraphSearch, BestFirstSearch, Astar]

        print 'Select a problem state for the puzzle:\n'
        print ' 1) Easy'
        print ' 2) Medium'
        print ' 3) Hard'
        print ' 4) Worst'
        print ' 5) Icse slides'

        selection = raw_input('\nPlease, enter the state number: ')
        try:
            selection = int(selection)
        except Exception:
            selection = -1
            continue

        if selection > 0 and selection < 6:
            s = states[selection-1]
        else:
            s = states[1]

        problem = EightPuzzleProblem(s, g)

        print 'START:'
        print problem.start.content.show()

        print 'Select an algorithm to run:\n'
        print ' 1) Graph Search'
        print ' 2) Best First Search'
        #print ' 3) IDAstar Search'
        print ' 3) Astar Search'
        selection = raw_input('\nPlease, enter the algorithm number: ')
        print ''

        try:
            selection = int(selection)
        except Exception:
            selection = -1

        if selection != 1:
            print 'Select an heuristic to use:\n'
            print ' 1) Misplaced tiles'
            print ' 2) Manhattan distance (default)'
            #print ' 3) Nilsson\'s Sequence Score (not admissible)'
            heuristic = raw_input('\nPlease, enter the heuristic number: ')
            print ''

        if selection in range(1, 4):
            g = False
            algorithm = algorithms[selection-1]
            if selection in [3]:
                g = True

            try:
                heuristic = int(heuristic)
            except Exception:
                heuristic = 2

            problem.set_heuristic(heuristic)

            print 'Trying to solve...'
            start_time = time.time()
            (solution, checked_nodes) = algorithm(problem)

            if type(solution) is list:
                i = 1
                solution = solution[1:]
                for move in solution:
                    print 'Move', i+1
                    if g is True:
                        print 'Distance from start:', move.g
                    print 'Distance from goal:', move.f - move.g
                    print move.content.show()
                    i += 1

                print 'Number of moves (L):', (len(solution) + 1)
                print 'Number of expanded nodes (T):', checked_nodes
                print 'Penetrance (L/T):', float((len(solution) + 1)) / (checked_nodes - 1)
                #print 'Problem branching factor: 1.67'

            print 'Elapsed time:', (time.time() - start_time), 'seconds'
        else:
            print 'Wrong algorithm number!'

        print '\n'
        s = raw_input('Exit?(y/n): ')
        if s == 'y':
            selection = 1000
        else:
            selection = -1
            print '\n\n'
