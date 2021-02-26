from Algorithm_1.structure.graph_struct import Graph, GraphNotAimed, Edge, Vertice
import copy


# efficiency: O(V+E)
def dfs(G: Graph) -> tuple:  # -> tuple(dict, dict, dict)
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


# efficiency: O(V+E)
def bfs(G: Graph):
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
def topology(G: Graph):
    pi, d, f = dfs(G)
    f.sort()


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
    print(bfs(G))
