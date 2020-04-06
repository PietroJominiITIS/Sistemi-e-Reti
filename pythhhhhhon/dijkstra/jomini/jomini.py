"""

@author: Pietro Jomini
@exercise: https://github.com/My-Students/Dijkstra

Splitted in three files:
- jomini.py: main
- graph.py: Graph class and Dijkstra algorithm
- field_grid.py: integration of previous exercise
    (https://github.com/My-Students/Python-robotics)

"""


from graph import Graph
from pprint import pprint as pp
from field_grid import grid2adj

if __name__ == '__main__':
    grid_loop = [[False, True,  True, False, False],
                 [True,  False, True, True,  True],
                 [True,  True,  True, False, True],
                 [False, False, True, True,  True]]

    grid = grid2adj(grid_loop)
    graph = Graph.from_addict(grid)
    pp(graph.shortest_path(0, 5))
