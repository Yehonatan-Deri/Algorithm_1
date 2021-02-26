from Algorithm_1.structure.graph_struct import Graph, Edge, Vertice
import numpy as np
from typing import Union, Tuple


def bfs(G: Graph, v=None) -> Tuple[dict, dict]:
    """
    params:
        v: vertice to start bfs , by default is G.V[0]
    efficiency: O(V+E)
    """
    v = v if v else V[0]
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


# @robuz
def forest(G, v=None):
    """
    Classification of the edges in G:

    param:
        v: vertice to start bfs , by default is G.V[0]
    efficiency: O(V+E)
    """
    v = v if v else V[0]
    time = 0
    pi, color, d, f = {v: None for v in G.V}, {v: 'white' for v in G.V}, {}, {}
    return_edge, cross_edge, forest_edge, forward_edge = [], [], [], []

    def dfs_visit(v: Vertice):
        nonlocal time
        color[v], time, d[v] = 'gray', time + 1, time + 1
        for e in v.edges:
            if color[e.to] == 'white':
                forest_edge.append(e)
                # pi[e.to] = v
                dfs_visit(e.to)
            elif color[e.to] == 'gray':
                return_edge.append(e)
            elif color[e.to] == 'black':
                if d[e.to] > d[v]:
                    forest_edge.append(e)
                elif d[e.to] < d[v]:
                    cross_edge.append(e)
        color[v] = 'black'
        time, f[v] = time + 1, time + 1

    # for v in G.V:
    #     if color[v] == 'white':
    dfs_visit(v)
    return return_edge, cross_edge, forest_edge, forward_edge


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

    color, tie_well, index_order = {v: 'white' for v in G_t.V}, [], [item[2] for item in f]
    for v in np.array(G_t.V)[index_order]:
        if color[v] == 'white':
            tie_well.append([v])
            dfs_visit(v)

    return tie_well


def roots(G):
    pass


if __name__ == '__main__':
    V = [Vertice(name=str(i)) for i in range(5)]
    # r = Edge(from_=V[0], to=V[1], weight=3)
    G = Graph(V=V)
    # G.connect(from_=V[1], to=V[2], weight=1)
    # G.connect(from_=V[2], to=V[1], weight=1)
    # G.connect(e=r)
    G.connect(from_=V[5], to=V[6])
    G.connect(from_=V[6], to=V[6])

    print(G)
    topology(G)
    print(topology(G))
    print(sccg(G))
