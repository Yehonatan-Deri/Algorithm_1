from Algorithm_1.structure.graph_struct import Graph, GraphNotAimed, Edge, Vertice
import copy
import numpy as np
from typing import Union, Tuple, List


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
    return pi, d, f,


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


# efficiency: O(V+E)
def topology(G: Graph) -> list:
    _, _, f = dfs(G)
    topology_order = list(f.items())
    topology_order.sort(key=lambda item: item[1], reverse=True)
    return [item[0] for item in topology_order]


# strongly connected component graph
def sccg(G):
    pass


def roots(G):
    pass


if __name__ == '__main__':
    V = [Vertice(name=str(i)) for i in range(10)]
    r = Edge(from_=V[0], to=V[1], weight=3)
    G = Graph(V=V)
    G.connect(from_=V[1], to=V[2], weight=1)
    G.connect(from_=V[2], to=V[1], weight=1)
    G.connect(e=r)

    # topology(G)
    print(topology(G))

    # print(c)
    #
    # Vector = List[float]
    # print(Vector)
    #
    #
    # def scale(scalar: float, vector: Vector) -> Vector:
    #     return [scalar * num for num in vector]
    #
    #
    # # typechecks; a list of floats qualifies as a Vector.
    # new_vector = scale(2.0, [1.0, -4.2, 5.4])
    # print(new_vector)
