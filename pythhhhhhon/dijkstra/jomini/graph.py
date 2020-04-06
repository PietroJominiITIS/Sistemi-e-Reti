"""
@author: Pietro Jomini
@last_modified: 23/03/20

I felt the need to encapsulate all my graphs stuff in a wrapper class,
to keep everything organized

TODO:
[ ] - reafctor __repr__
[ ] - migrate dijkstra pool from set to dict
[ ] - find a better way to use that list in shortest_path
[ ] - fix shortest_path for non-existent path
[ ] - networkx repr
"""

from collections import namedtuple
from math import inf


class Graph:

    Edge = namedtuple('Edge', ['start', 'end', 'weight'])

    @staticmethod
    def from_edges(*edges):
        edges = {Graph.Edge(*edge) for edge in edges}
        nodes = {e.start for e in edges} | {e.end for e in edges}
        return Graph(edges=edges, nodes=nodes)

    @staticmethod
    def from_admat(admat, _validate=None, _key=None):
        validate = _validate or (lambda w: w < inf)
        key = _key or (lambda mat, start: mat[start].items())
        edges = set()
        for start in admat:
            edges |= {Graph.Edge(start, end, weight)
                      for end, weight in key(admat, start)
                      if validate(weight)}
        return Graph(edges=edges, nodes=set(admat))

    @staticmethod
    def from_addict(addict):
        validate = (lambda _: True)
        key = (lambda mat, start: mat[start])
        return Graph.from_admat(addict, _validate=validate, _key=key)

    def __init__(self, nodes=set(), edges=set()):
        self.__v__ = 0

        self.nodes = nodes
        self.edges = edges

        self._addict = None
        self._admat = None
        self._addict__v__ = self.__v__
        self._admat__v__ = self.__v__

    def __repr__(self):
        edges = '\n\t\t'.join([''] + [str(edge)
                              for edge in self.edges] if self.edges else [])
        return f'Graph(\n\tnodes:{self.nodes},\n\tedges:{edges})'

    @property
    def admat(self):
        if self._admat is None or self._admat__v__ < self.__v__:
            self._admat = {n: {k: inf for k in self.nodes} for n in self.nodes}
            for start, end, weight in self.edges:
                self._admat[start][end] = weight
            self._admat__v__ = self.__v__
        return self._admat

    @property
    def addict(self):
        if self._addict is None or self._addict__v__ < self.__v__:
            self._addict = {node: set() for node in self.nodes}
            for start, end, cost in self.edges:
                self._addict[start].add((end, cost))
            self._addict__v__ = self.__v__
        return self._addict

    def add_edge(self, start, end, weight):
        self.edges.add(Graph.Edge(start, end, weight))
        self.add_nodes(start, end)

    def add_nodes(self, *nodes):
        for node in nodes:
            self.nodes.add(node)
        self.__v__ += 1

    def dijkstra(self, start):
        """
        dist: store optimal dist from start node to each node
        previous: store previous node, in optimal path, for each node
                  used to build a path from start ot end
        """
        dist = {n: inf for n in self.nodes}
        previous = {n: None for n in self.nodes}
        pool = {(start, 0)} if start in self.nodes else False
        while pool:
            name, bias = min(pool, key=lambda node: node[1])
            pool = {node for node in pool if not node[0] == name}
            for neighb, weight in self.addict[name]:
                diff = bias + weight
                if diff < dist[neighb]:
                    dist[neighb] = diff
                    previous[neighb] = name
                    pool.add((neighb, diff))
        return dist, previous

    def shortest_path(self, start, end):
        """
        If we got an end to reach we can build a path from start to end
        using our previous data
        """
        dist, previous = self.dijkstra(start)
        path = [end]
        while previous[end] is not None and end != start:
            path.append(previous[end])
            end = previous[end]
        path.reverse()
        return path
