from Algorithm_1.structure.graph_struct import Graph, GraphNotAimed, Edge, Vertice
import copy
import numpy as np
from typing import Union, Tuple, List


def bfs(G: Graph) -> Tuple[dict, dict]:
    """
    efficiency: O(V+E)
    """
    pi, color, layer, Q = {v: None for v in G.V}, {v: 'white' for v in G.V}, {G.V[0]: 1}, [G.V[0]]

    while len(Q):
        v = Q.pop()
        for u in v.Adj:
            if color[u] == 'white':
                pi[u], color[u], layer[u] = v, 'gray', layer[v] + 1
                Q.append(u)
        color[v] = 'black'

    return pi, layer


def dfs(G: Graph) -> Tuple[dict, dict, dict]:
    """
    efficiency: O(V+E)
    """
    time = 0
    pi, color, d, f = {v: None for v in G.V}, {v: 'white' for v in G.V}, {}, {}

    def dfs_visit(v: Vertice):
        nonlocal time
        color[v], time, d[v] = 'gray', time + 1, time + 1
        for u in v.Adj:
            if color[u] == 'white':
                pi[u] = v
                dfs_visit(u)
        color[v] = 'black'
        time, f[v] = time + 1, time + 1

    for v in G.V:
        if color[v] == 'white':
            dfs_visit(v)
    return pi, d, f


def search_circle(G: Graph) -> Union[bool, dict]:  # -> tuple(dict, dict, dict)
    """
    search circle with dfs
    return: dict of exit time if circle not found or False if circle found
    efficiency: O(V+E)
    """
    time = 0
    color, f = {v: 'white' for v in G.V}, {}

    def dfs_visit(v: Vertice):
        nonlocal time
        color[v], time = 'gray', time + 1
        for u in v.Adj:
            if color[u] == 'white':
                dfs_visit(u)
            elif color == 'white':
                return False

            color[v] = 'black'

        time, f[v] = time + 1, time + 1

    for v in G.V:
        if color[v] == 'white':
            if not dfs_visit(v):
                return False
    return f


def forest(G, v):
    pass


def topology(G: Graph) -> Union[list, None]:
    """
    efficiency: O(V+E)
    """
    f = search_circle(G)
    if not f:
        print('there is a circle in the graph')
        return
    topology_order = list(f.items())
    topology_order.sort(key=lambda item: item[1], reverse=True)
    return [item[0] for item in topology_order]


# @robuz
def sccg(G: Graph):
    """
    strongly connected component graph
    efficiency: O(V+E)
    """
    _, _, f = dfs(G)
    f = [(item[0], item[1], G.V.index(item[0])) for item in f.items()]
    f.sort(key=lambda item: item[1], reverse=True)
    G_t = G.transpose()

    def dfs_visit(v: Vertice):
        color[v] = 'gray'
        for u in v.Adj:
            if color[u] == 'white':
                tie_well[len(tie_well) - 1].append(u)
                dfs_visit(u)
        color[v] = 'black'

    color, tie_well, index_order = {v: 'white' for v in G_t.V}, [], [item[2] for item in f]
    V = np.array(G_t.V)
    for v in V[index_order]:
        if color[v] == 'white':
            tie_well.append([v])
            dfs_visit(v)

    return tie_well


def roots(G):
    pass


if __name__ == '__main__':
    V = [Vertice(name=str(i)) for i in range(4)]
    r = Edge(from_=V[0], to=V[1], weight=3)
    G = Graph(V=V)
    G.connect(from_=V[1], to=V[2], weight=1)
    G.connect(from_=V[2], to=V[1], weight=1)
    G.connect(e=r)

    print(G)
    # topology(G)
    # print(topology(G))
    print(sccg(G))
