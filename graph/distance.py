from Algorithm_1.structure.graph_struct import GraphNotAimed, Vertex, Graph
from Algorithm_1.structure.list_struct import TwoWayList
from Algorithm_1.structure.heap import BinaryHeap
from Algorithm_1.graph.mst import BinaryHeapPrim
from Algorithm_1.graph.dfs import topology


def dijkstra(G, s):
    """
    dijkstra algorithm:
        if |E| * 0.75  < |V|^2 : the struct will be min heap
        else:                    the struct will be array

        this method work only with positive edges

    @params:
        @G: graph
        @s: vertex to start

    return:
        return pi dict
        if restore=True the mst graph (=Minimal spreadsheet graph) will be return also

    efficiency:
        if |E| * 0.75  < |V|^2: => O(Vlog V)
        if |E| * 0.75  > |V|^2: => O(E) = O(|V|^2)
    """
    struct = 'heap' if len(G.E) < (len(G.V) ** 2) * 0.75 else 'array'
    pi = {v: None for v in G.V}
    _init(G, s)
    key = lambda v: v.data['key']
    Q = BinaryHeapPrim(arr=G.V, compare=min, key=key) if struct == 'heap' else [v for v in G.V]

    while struct == 'heap' and Q.arr or struct == 'array' and Q:
        v, v.data['in heap'] = Q.extract() if struct == 'heap' else Q.pop(Q.index(min(Q, key=key))), False
        for e in v.edges:
            if e.to.data['in heap']:
                relax(e, pi)
                if struct == 'heap':
                    Q.add(Q.pop(e.to.data['i']))

    return pi


def bellman_ford(G, s):
    """
        bellman ford algorithm:
            found distance between s and all other vertex
            this method work also with negative edges

        @params:
            @G: graph
            @s: vertex to start

        return:
            return pi dict or False if there is negative circle in the graph

        efficiency: O(|E|*|V|)
        """
    pi = {v: None for v in G.V}
    _init(G, s)

    for i in range(len(G.V) - 1):
        for e in G.E:
            relax(e, pi)
    for e in G.E:
        if e.to.data['key'] > e.from_.data['key'] + e.weight:
            print('negative circle in the graph')
            return False

    return pi


def dag(G, s):
    """
    dag algorithm:
        found distance between s and all other vertex
        this method work only with graph without circle

    @params:
        @G: graph
        @s: vertex to start

    return:
        return pi dict or False if there is circle in the graph

    efficiency: O(|E|+|V|)
    """
    topology_order = topology(G)
    if not topology_order:
        return
    pi = {v: None for v in G.V}
    _init(G, s)
    for v in topology_order:
        for e in v.edges:
            relax(e, pi)
    return pi


def relax(e, pi):
    if e.to.data['key'] > e.weight + e.from_.data['key']:
        e.to.data['key'], pi[e.to] = e.weight + e.from_.data['key'], e.from_


def _init(G, s):
    '''
    help method for bellman_ford() and dijkstra()
    init all vertex in G:
        insert dictionary with key=inf , and in heap=True
        the key in the start vertex (=s) will be 0

    @param:
        G: graph
        s: vertex to start from
    '''
    for v in G.V:
        v.data = {'key': float('inf'), 'in heap': True}
    s.data['key'] = 0


'''------------------------------   all pairs distance  -------------------------------------'''


def floyd_warshall(G):
    pass


def all_pairs_dijkstra(G):
    pass


def all_pairs_bellman_ford(G):
    pass


def all_pairs_dynamic_slow(G):
    pass


def all_pairs_dynamic_fast(G):
    pass


def johnson(G):
    pass


if __name__ == '__main__':
    V = [Vertex(name=str(i)) for i in range(6)]
    V[0].name, V[1].name, V[2].name, V[3].name, V[4].name, V[5].name = 'a', 'b', 'c', 'd', 'e', 'f'
    # r = Edge(from_=V[0], to=V[1], weight=3)
    # G = GraphNotAimed(V=V)
    # G.connect(from_=V[0], to=V[1], weight=4)
    # G.connect(from_=V[0], to=V[4], weight=3)
    # G.connect(from_=V[0], to=V[3], weight=2)
    # G.connect(from_=V[1], to=V[2], weight=5)
    # G.connect(from_=V[1], to=V[4], weight=4)
    # G.connect(from_=V[1], to=V[5], weight=6)
    # G.connect(from_=V[2], to=V[5], weight=1)
    # G.connect(from_=V[3], to=V[4], weight=6)
    # G.connect(from_=V[4], to=V[5], weight=8)
    # ---------------------
    # G.connect(from_=V[0], to=V[2], weight=8)
    # G.connect(from_=V[0], to=V[5], weight=8)
    # G.connect(from_=V[1], to=V[0], weight=8)
    # G.connect(from_=V[1], to=V[3], weight=8)
    # G.connect(from_=V[2], to=V[3], weight=8)
    # G.connect(from_=V[2], to=V[4], weight=8)
    # pi = dijkstra(G, G.V[0])
    # print('------------------------')
    # print([v.data['key'] for v in G.V])
    # print(pi.values())
    # pi = bellman_ford(G, G.V[0])
    # print('------------------------')
    # print([v.data['key'] for v in G.V])
    # print(pi.values())
    G = Graph()
    G.connect(from_=V[0], to=V[1], weight=2)
    G.connect(from_=V[1], to=V[2], weight=4)
    G.connect(from_=V[2], to=V[3], weight=2)
    G.connect(from_=V[3], to=V[4], weight=6)
    G.connect(from_=V[4], to=V[5], weight=2)
    G.connect(from_=V[0], to=V[2], weight=2)
    pi = dag(G, V[0])
    print([v.data['key'] for v in G.V])
    print(pi.values())
