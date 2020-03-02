import networkx as nx
import matplotlib.pyplot as plt


def netPrintDict(dg):
    g = nx.Graph()

    g.add_nodes_from(range(len(dg.keys())))
    for orig in dg.keys():
        for dests in dg[orig]:
            dest, weight = dests
            g.add_edge(orig, dest, weight=weight)

    nx.draw(g, with_labels=True)
    plt.show()


def user2adj():
    V = range(int(input("|V| - ")))
    graph = [[0 for i in V] for k in V]

    for i in V:
        for n in [int(k) for k in input(f'Node linked to {i}: ').split(',') if k != '']:
            graph[i][n] = 1

    return graph


def adj2adjw(adj):
    graph = adj[:]
    for orig, dests in enumerate(graph):
        for dindex, dest in enumerate(dests):
            if dest == 1:
                graph[orig][dindex] = int(input(f'W({orig}, {dindex}): '))
    return graph


def adj2dict(graph):
    dg = {}
    for orig, dests in enumerate(graph):
        dg[orig] = [(index, i) for index, i in enumerate(dests) if i != 0]
    return dg


def dict2adj(dg):
    V = range(len(dg.keys()))
    graph = [[0 for i in V] for k in V]

    for orig, dests in enumerate(dg.values()):
        for v, w in dests:
            graph[orig][v] = w

    return graph


if __name__ == "__main__":

    mat = user2adj()
    matg = adj2adjw(mat)
    dg = adj2dict(matg)
    matr = dict2adj(dg)

    # print(mat)
    # print(dg)
    # print(matr)

    netPrintDict(dg)
