import copy
from typing import List


class Edge:

    def __init__(self, from_, to, weight=1) -> None:
        self.from_, self.to, self.weight = from_, to, weight
        # Kodkod.connect(self)

    def __str__(self):
        return f'({self.from_.name}->{self.to.name},w={self.weight})'

    def __repr__(self):
        return f'({self.from_.name}->{self.to.name},w={self.weight})'


class Vertice:
    def __init__(self, name=None, data=None, Adj=None, edges=None):
        self.Adj: List[Vertice]
        self.edges: List[Edge]
        self.name, self.data, self.Adj, self.edges = name, data, Adj, edges
        self.Adj = Adj if Adj else []
        self.edges = edges if edges else []

    def connect(self, v=None, weight=1, e=None):
        if e:
            if e.to not in self.Adj:
                self.Adj.append(e.to)
                self.edges.append(e)
        elif v:
            if v is self:
                return
            if v not in self.Adj:
                self.Adj.append(v)
                e = Edge(self, v, weight=weight)
                self.edges.append(e)
        return e

    def disconnect(self, v):
        if v in self.Adj:
            i = self.Adj.index(v)
            self.Adj.remove(v)
            del self.edges[i]

    def is_connect(self, v):
        return v in self.Adj

    def __str__(self) -> str:
        return f'name: {self.name}, Adj: {self.Adj}, rainbow: {self.edges}'

    def __repr__(self) -> str:
        return f'{self.name}'


class Graph:
    E: [Edge]
    V: [Vertice]

    def __init__(self, E: [Edge] = None, V: [Vertice] = None) -> None:
        self.E, self.V = E, V

    def connect(self, from_: Vertice = None, to: Vertice = None, weight=1, e: Edge = None):
        if e:
            from_, to, weight = e.from_, e.to, e.weight
        elif from_ and to and from_ is not to:
            e = from_.connect(v=to, weight=weight)
        else:
            print('ERROR : must pass @from_,@to OR @e parameters')
            return
        from_.connect(v=to, weight=weight)
        if e not in self.E:
            self.E.append(e)
        if from_ not in self.V:
            self.V.append(from_)
        if to not in self.V:
            self.V.append(to)

    def disconnect(self, from_: Vertice = None, to: Vertice = None, e: Edge = None):
        if e:
            from_, to = e.from_, e.to
        elif not from_ or not to:
            print('ERROR : must pass @from_,@to OR @e parameters')
            return
        from_.disconnect(v=to)
        for edg in self.E:
            if edg.from_ == from_ and edg.to == to:
                self.E.remove(edg)
                return

    def __str__(self):
        s = '------------------  graph  -----------------\n'
        s += 'V=[' + ','.join([v.name for v in self.V]) + ']\n'
        s += 'E=' + ','.join([str(e) for e in self.E]) + '\n'
        s += '|V|={} |E|={}'.format(len(self.V), len(self.E)) + '\n'
        s += '--------------------------------------------'
        return s

    # return new G' transpose graph
    def transpose(self):
        G = Graph()
        G.V = [Vertice(name=v.name, data=v.data) for v in self.V]
        G.E = [Edge(G.V[self.V.index(e.to)], G.V[self.V.index(e.from_)], weight=e.weight) for e in self.E]
        return G

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        self.__V = V if V is not None else []

    @property
    def E(self):
        return self.__E

    @E.setter
    def E(self, E):
        self.__E = E if E is not None else []
        # self.V = []
        if not E:
            return
        for e in E:
            self.connect(e=e)


class GraphNotAimed(Graph):

    def __init__(self, E=None, V=None) -> None:
        super().__init__(E, V)

    def connect(self, from_=None, to=None, weight=1, e=None):
        super().connect(from_, to, weight, e)
        if e:
            e.to.connect(v=from_, weight=e.weight)
        elif from_ and to:
            super().connect(from_=to, to=from_, weight=weight)


if __name__ == '__main__':
    V = [Vertice(name=str(i)) for i in range(10)]
    r = Edge(from_=V[0], to=V[1], weight=3)
    G = Graph(V=V)
    G.connect(from_=V[1], to=V[2], weight=1)
    G.connect(from_=V[2], to=V[1], weight=1)
    G.connect(e=r)
    print(G)
    G.disconnect(from_=V[1], to=V[0])
    print(G)
    # print(G.transpose())
