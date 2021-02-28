from typing import List

from Algorithm_1.structure.graph_struct import Graph, GraphNotAimed, Vertex, Edge
from Algorithm_1.structure.list_struct import ListNode, List
from Algorithm_1.structure.heap import BinaryHeap
import copy


# @robuz
def kruskal(G, s, restore=False):
    """
    kruskal algorithm
    efficiency: O(Vlog V)
    """
    # if len()

    pi = {v: None for v in G.V}
    for v in G.V:
        v.data = {'key': float('inf'), 'in heap': True}
    s.data['key'] = 0
    Q = BinaryHeapPrim(arr=G.V, compare=min, key=lambda v: v.data['key'])

    while Q.arr:
        v, v.data['in heap'] = Q.extract(), False
        for e in v.edges:
            if e.to.data['in heap'] and e.weight < e.to.data['key']:
                pi[e.to], e.to.data['key'] = v, e.weight
                Q.add(Q.pop(e.to.data['i']))

    if restore:
        V = {v: Vertex(name=v.name, data=v.data) for v in G.V}
        G_mst = GraphNotAimed()
        for v, u in pi.items():
            if u:
                G_mst.connect(from_=V[v], to=V[u], weight=v.data['key'])
        return pi, G_mst

    return pi


def prim(G):
    pass


class BinaryHeapPrim(BinaryHeap):
    """
    this class is for kruskal algorithm only , the vertex in this class contain 'i' => index of the object
        in the heap so we can add/pop element in O(1) if we have the element itself (=instead of O(n))
        the 'i' stored in dict in Vertex.data['i']
    """

    def __init__(self, arr: [Vertex] = None, compare=max, key=None) -> None:
        super().__init__(arr, compare, key)
        for v, i in zip(self.arr, range(len(self.arr))):
            v.data['i'] = i

    # efficiency: O(log n)
    def heapify_up(self, i):
        while i > 0:
            i_max = self.arr.index(self.compare(self.arr[i], self.arr[self.father(i)], key=self.key))
            if i == i_max:
                # added for prim ----------------------------------
                temp = self.arr[i].data['i']
                self.arr[i].data['i'] = self.arr[self.father(i)].data['i']
                self.arr[self.father(i)].data['i'] = temp
                # added for prim ----------------------------------
                self.arr[i], self.arr[self.father(i)], i = self.arr[self.father(i)], self.arr[i], self.father(i)
            else:
                return

    # efficiency: O(log n)
    def heapify_down(self, i):
        while i < len(self.arr) // 2:
            r, l = self.left(i), self.right(i)  # indexes of right and left suns
            i_max = self.arr.index(self.compare([self.arr[x] for x in [i, r, l] if x is not False], key=self.key))
            if i_max != i:
                # added for prim ----------------------------------
                temp = self.arr[i].data['i']
                self.arr[i].data['i'] = self.arr[i_max].data['i']
                self.arr[i_max].data['i'] = temp
                # added for prim ----------------------------------
                self.arr[i], self.arr[i_max], i = self.arr[i_max], self.arr[i], i_max
            else:
                return

    # efficiency: O(log n)
    def pop(self, i):
        self.arr[i], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[i]
        # added for prim ----------------------------------
        temp = self.arr[i].data['i']
        self.arr[i].data['i'] = self.arr[len(self.arr) - 1].data['i']
        self.arr[len(self.arr) - 1].data['i'] = temp
        # added for prim ----------------------------------
        data = self.arr.pop()
        if i < len(self.arr):
            self.heapify_down(i)
        return data

    # efficiency: O(log n)
    def extract(self):
        return self.pop(0)

    # efficiency: O(log n)
    def add(self, data):
        self.arr.append(data)
        # added for prim ----------------------------------
        self.arr[len(self.arr) - 1].data['i'] = len(self.arr) - 1
        # added for prim ----------------------------------
        self.heapify_up(len(self.arr) - 1)


if __name__ == '__main__':
    V = [Vertex(name=str(i)) for i in range(6)]
    V[0].name, V[1].name, V[2].name, V[3].name, V[4].name, V[5].name = 'a', 'b', 'c', 'd', 'e', 'f'
    # r = Edge(from_=V[0], to=V[1], weight=3)
    G = GraphNotAimed(V=V)
    G.connect(from_=V[0], to=V[1], weight=4)
    G.connect(from_=V[0], to=V[4], weight=3)
    G.connect(from_=V[0], to=V[3], weight=2)
    G.connect(from_=V[1], to=V[2], weight=5)
    G.connect(from_=V[1], to=V[4], weight=4)
    G.connect(from_=V[1], to=V[5], weight=6)
    G.connect(from_=V[2], to=V[5], weight=1)
    G.connect(from_=V[3], to=V[4], weight=6)
    G.connect(from_=V[4], to=V[5], weight=8)

    print(G)
    print(kruskal(G, G.V[0], restore=True)[1])
