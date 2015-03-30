#!/usr/bin/env python


class Node(object):
    """
    Nodo del grafo di un problema di ricerca.
    """

    def __init__(self, content=None):
        self.__content = content
        self.__parent = None
        self.__g = 0
        self.__f = 0

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, cost):
        self.__g = cost

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, cost):
        self.__f = cost

    def __repr__(self):
        return str(self.__content)

    def __str__(self):
        return str(self.__content)

    def __eq__(self, node):
        return self.__content == node.content

    def __neq__(self, node):
        return self.__content != node.content

    def __lt__(self, node):
        return self.__f < node.f

    def __gt__(self, node):
        return self.__f > node.f

    def __le__(self, node):
        if self.__f == node.f:
            return self.__g > node.g
        else:
            return self.__f < node.f

    def __ge__(self, node):
        if self.__f == node.f:
            return self.__g < node.g
        else:
            return self.__f > node.f
