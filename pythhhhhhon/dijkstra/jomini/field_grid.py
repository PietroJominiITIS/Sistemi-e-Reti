# Jomini Pietro
# 4/3/2020

# Cloned from https://github.com/My-Students/Python-robotics


def pad(_grid, shape):
    """
    Pad a given matrix `_grid` with a series of `shape` elements \n
    """
    """
    EG:
                          -------------
         ---------        | 8 8 8 8 8 |
         | 1 0 1 |        | 8 1 0 1 8 |
    pad( | 2 1 3 |, 8) -> | 8 2 1 3 8 |
         | 1 0 2 |        | 8 1 0 2 8 |
         ---------        | 8 8 8 8 8 |
                          -------------
    """

    width = 2 + max(len(row) for row in _grid)
    height = 2 + len(_grid)

    grid = [[shape for i in range(width)] for i in range(height)]

    for y in range(len(grid[1:-1])):
        for x in range(len(grid[y+1][1:-1])):
            grid[y+1][x+1] = _grid[y][x]

    return grid


def index(_grid, toIndex):
    """
    Indexes elements equal to `toIndex` in a given matrix `_grid` \n
    """
    """
    EG:
           ---------        ---------
           | 0 0 3 |        | 0 1 3 |
    index( | 1 0 7 |, 0) -> | 1 2 7 |
           | 4 1 0 |        | 4 1 3 |
           ---------        ---------
    """

    k = 0

    grid = _grid[:]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                grid[y][x] = k
                k += 1

    return grid


def grid2adj(_grid):
    """
    Generate an adjacency dictionary from a given boolean grid `_grid`,
    where each cell is considered busy if False, free if True
    """
    """
    EG:
                                         |{
              ---------------------      |  0: [ 1 ]
              | False True  False |      |  1: [ 0, 4, 2 ]
    grid2adj( | False True  True  | ) -> |  2: [ 1 ]
              | True  True  False |      |  3: [ 4 ]
              ---------------------      |  4: [ 1, 3 ]
                                         |}
    """

    adj = {}
    grid = pad(index(_grid, True), False)

    for y, row in enumerate(grid[1:-1]):
        for x, cell in enumerate(row[1:-1]):
            if cell is not False:
                neigh = [(y, x+1), (y+2, x+1), (y+1, x), (y+1, x+2)]
                links = [(grid[a][b], 1)
                         for a, b in neigh if grid[a][b] is not False]
                adj[grid[y+1][x+1]] = links

    return adj
