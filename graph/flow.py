from Algorithm_1.structure.graph_struct import Graph, GraphNotAimed, Vertex, Edge
import copy
import math

def dfs(G, s, t, theta=None):
    pi_edges, color = {v: None for v in G.V}, {v: 'white' for v in G.V}

    def dfs_visit(v):
        color[v] = 'gray'
        for e in v.edges:
            if color[e.to] == 'white':  # and e.weight > 0
                if theta and e.weight < theta:
                    continue
                pi_edges[e.to] = e
                return True if e.to == t else dfs_visit(e.to)
        return False

    return pi_edges if dfs_visit(s) else False


def bfs(G, s, t, theta=None):
    """
    @params:
        @G: graph
        @s: vertex to start bfs
        @t: vertex to end bfs

    efficiency: O(V+E)
    """
    pi_edges, color, Q = {v: None for v in G.V}, {v: 'white' for v in G.V}, [s]

    while len(Q):
        v = Q.pop(0)
        for e in v.edges:
            if color[e.to] == 'white':
                if theta and e.weight < theta:
                    continue
                pi_edges[e.to], color[e.to] = e, 'gray'
                if e.to == t:
                    return pi_edges
                Q.append(e.to)

    return False


def ford_fulkerson(G, s, t, func=dfs):
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
    G_r, dic = init(G, s, t)
    s, t = dic[s], dic[t]
    while True:
        way = func(G_r, s, t)
        if way:
            add_way, min_flow = restore_way(way, s, t)
            calc_G_r(G_r, add_way, min_flow)
        else:
            break

    # G_max=
    for
    print(G_r)


def init(G, s, t):
    G_r = Graph()
    V = [Vertex(name=v.name) for v in G.V]
    dic = {}
    for v1, v2 in zip(G.V, V):
        dic[v1] = v2

    for e in G.E:
        G_r.connect(from_=dic[e.from_], to=dic[e.to], weight=e.weight)

    return G_r, dic


def calc_G_r(G_r, add_way, min_flow):
    for e in add_way:
        if e.weight - min_flow <= 0:
            G_r.disconnect(e=e)
        else:
            e.weight -= min_flow
        if e.from_ in e.to.Adj:
            e.to.Adj[e.from_].weight += min_flow
        else:
            G_r.connect(from_=e.to, to=e.from_, weight=min_flow)




def scaling(G, s, t):
    C_max = max(G.E, key=lambda e: e.weight).weight
    theta = 2 ** int(math.log(C_max, 2))
    G_r, dic = init(G, s, t)
    s, t = dic[s], dic[t]
    while theta >= 1:
        while True:
            way = dfs(G_r, s, t, theta=theta)
            if way:
                add_way, min_flow = restore_way(way, s, t)
                calc_G_r(G_r, add_way, min_flow)
            else:
                theta /= 2
                # print(G_r)
                break


def restore_way(pi_edges, s, t):
    add_way, min_flow = [pi_edges[t]], pi_edges[t].weight
    while add_way[0].from_ != s:
        add_way.insert(0, pi_edges[add_way[0].from_])
        min_flow = min(min_flow, add_way[0].weight)

    return add_way, min_flow


def init_(G):
    # G_r = copy.deepcopy(G)
    G_r = Graph()
    V = [Vertex(name=v.name + '(r)') for v in G.V]
    dic = {}
    for v1, v2 in zip(G.V, V):
        dic[v1] = v2

    for e in G.E:
        G_r.connect(from_=dic[e.from_], to=dic[e.to], weight=e.weight)

    return G_r


def pairs(G):
    pass


if __name__ == '__main__':
    V = [Vertex(name=str(i)) for i in range(8)]
    V[0].name, V[1].name, V[2].name, V[3].name, V[4].name, V[5].name, V[6].name, V[7].name = \
        's', '1', '2', '3', '4', '5', '6', 't'
    G = Graph()
    for i in range(8):
        G.V[V[i]] = None
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
    print('--------------------  scalling  ------------------------')
    V = [Vertex(name=str(i)) for i in range(6)]
    V[0].name, V[1].name, V[2].name, V[3].name, V[4].name, V[5].name = 's', '1', '2', '3', '4', 't'
    G = Graph()
    # G.V.append(V[:8])
    for i in range(6):
        G.V[V[i]] = None
    G.connect(from_=V[0], to=V[1], weight=25)
    G.connect(from_=V[0], to=V[3], weight=20)
    G.connect(from_=V[1], to=V[2], weight=20)
    G.connect(from_=V[2], to=V[3], weight=15)
    G.connect(from_=V[2], to=V[5], weight=16)
    G.connect(from_=V[3], to=V[4], weight=25)
    G.connect(from_=V[4], to=V[5], weight=30)
    # G.connect(from_=V[3], to=V[5], weight=3)
    # G.connect(from_=V[4], to=V[5], weight=2)
    # G.connect(from_=V[4], to=V[6], weight=3)
    # G.connect(from_=V[5], to=V[6], weight=3)
    # G.connect(from_=V[5], to=V[7], weight=3)
    # G.connect(from_=V[6], to=V[7], weight=3)
    # ford_fulkerson(G, V[0], V[7])
    print(scaling(G, V[0], V[5]))
    print(G)
