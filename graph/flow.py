from Algorithm_1.structure.graph_struct import Graph, GraphNotAimed, Vertex, Edge
import copy


def ford_fulkerson(G, s, t, func=None):
    """
    ford fulkerson algorithm:
        found max flow in the graph from s to t
          if the weight are irrational numbers the algorithm is not sure the algorithm will converge
          if the weight are rational numbers we can multiple all weight with common factor

    @params:
        @G: graph
        @s: vertex to start
        @t: vertex to end

    return:

    the algorithm:


    efficiency:
        if func is dfs: O(|E||f*|) when |f*| is max flow
        if func is bfs: O(|V||E|^2)
        if func is scaling: O(log(C_max)*|E|)
    """

    def restore_way(pi_edges):
        add_way, min_flow = [pi_edges[t]], pi_edges[t].weight
        while add_way[0].from_ != s:
            add_way.insert(0, pi_edges[add_way[0].from_])
            min_flow = min(min_flow, add_way[0].weight)

        return add_way, min_flow

    G_r, s, t = init(G, s, t)
    # G_r = G
    while True:
        way = dfs(G_r, s, t)
        if way:
            add_way, min_flow = restore_way(way)
            calc_G_r(G_r, add_way, min_flow)
        else:
            break

    # G_max=
    print(G_r)


def init(G, s, t):
    # G_r = copy.deepcopy(G)
    G_r = Graph()
    V = [Vertex(name=v.name + '(r)') for v in G.V]
    dic = {}
    for v1, v2 in zip(G.V, V):
        dic[v1] = v2

    for e in G.E:
        G_r.connect(from_=dic[e.from_], to=dic[e.to], weight=e.weight)

    return G_r, dic[s], dic[t]


def calc_G_r(G_r, add_way, min_flow):
    for e in add_way:
        if e.weight - min_flow <= 0:
            G_r.disconnect(e=e)
        else:
            e.weight -= min_flow
        if e.from_ in e.to.Adj:
            for e_ in e.to.edges:
                if e_.to == e.from_:
                    e_.weight += min_flow
                    break
        else:
            print(e.from_ in G.V)
            G_r.connect(from_=e.to, to=e.from_, weight=min_flow)


def dfs(G, s, t):
    pi_edges, color = {v: None for v in G.V}, {v: 'white' for v in G.V}

    def dfs_visit(v):
        color[v] = 'gray'
        for e in v.edges:
            if color[e.to] == 'white':  # and e.weight > 0
                pi_edges[e.to] = e
                if e.to == t:
                    return True
                return True if e.to == t else dfs_visit(e.to)
        return False

    return pi_edges if dfs_visit(s) else False


def bfs(G, s, t):
    """
    @params:
        @G: graph
        @s: vertex to start bfs
        @t: vertex to end bfs

    efficiency: O(V+E)
    """
    pi, color, Q = {v: None for v in G.V}, {v: 'white' for v in G.V}, [s if s else G.V[0]]

    while len(Q):
        v = Q.pop(0)
        for u in v.Adj:
            if color[u] == 'white':
                pi[u], color[u] = v, 'gray'
                if u == t:
                    return pi
                Q.append(u)

    return False


def scaling(G):
    pass


def flow_bfs(G):
    pass


def pairs(G):
    pass


if __name__ == '__main__':
    V = [Vertex(name=str(i)) for i in range(8)]
    V[0].name, V[1].name, V[2].name, V[3].name, V[4].name, V[5].name, V[6].name, V[7].name = \
        's', '1', '2', '3', '4', '5', '6', 't'
    G = Graph()
    # G.V.append(V[:8])
    for i in range(8):
        G.V.append(V[i])
    G.connect(from_=V[0], to=V[1], weight=3)
    G.connect(from_=V[0], to=V[2], weight=3)
    G.connect(from_=V[1], to=V[2], weight=1)
    G.connect(from_=V[1], to=V[3], weight=3)
    G.connect(from_=V[2], to=V[3], weight=1)
    G.connect(from_=V[2], to=V[4], weight=3)
    G.connect(from_=V[3], to=V[4], weight=2)
    G.connect(from_=V[3], to=V[5], weight=3)
    G.connect(from_=V[4], to=V[5], weight=2)
    G.connect(from_=V[4], to=V[6], weight=3)
    G.connect(from_=V[5], to=V[6], weight=3)
    G.connect(from_=V[5], to=V[7], weight=3)
    G.connect(from_=V[6], to=V[7], weight=3)
    ford_fulkerson(G, V[0], V[7])
    # print(init(G))
    print(G)
    # print(G)
    # e = Edge(from_=V[0], to=V[1], weight=355)
    # print(G)
    # G.connect(e=e)
    # G.connect(e=e)
    # print(G)
