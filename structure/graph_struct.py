import copy


class Rainbow:

    def __init__(self, from_, to, weight=1) -> None:
        self.from_, self.to, self.weight = from_, to, weight
        # Kodkod.connect(self)

    def __str__(self):
        return f'({self.from_.name}->{self.to.name},w={self.weight})'

    def __repr__(self):
        return f'({self.from_.name}->{self.to.name},w={self.weight})'


class Kodkod():
    def __init__(self, name=None, data=None, Adj=None, rainbow=None):
        self.name, self.data, self.Adj, self.rainbow = name, data, Adj, rainbow
        self.Adj = Adj if Adj else []
        self.rainbow = rainbow if rainbow else []

    def connect(self, v=None, weight=1, e=None):
        if e:
            if e.to not in self.Adj:
                self.Adj.append(e.to)
                self.rainbow.append(e)
        elif v:
            if v not in self.Adj:
                self.Adj.append(v)
                e = Rainbow(self, v, weight=weight)
                self.rainbow.append(e)
        return e

    def disconnect(self, v):
        if v in self.Adj:
            i = self.Adj.index(v)
            self.Adj -= v
            del self.rainbow[i]

    def is_connect(self, v):
        return v in self.Adj

    def __str__(self) -> str:
        return f'name: {self.name}, Adj: {self.Adj}, rainbow: {self.rainbow}'

    def __repr__(self) -> str:
        return f'(name: {self.name}, Adj: {self.Adj}, rainbow: {self.rainbow})'

    # def Adj_str(self):
    #     return '[' + ','.join([v.name for v in self.Adj]) + ']'


class KodkodDFS(Kodkod):

    def __init__(self, name=None, data=None, pi=None, color=None, i=None, f=None, d=None):
        super().__init__(name, data)
        self.pi, self.color, self.i, self.d, self.f = pi, color, i, d, f


class KodkodBFS(Kodkod):

    def __init__(self, name=None, data=None, pi=None, color=None, i=None, layer=None):
        super().__init__(name, data)
        self.pi, self.color, self.i, self.layer = pi, color, i, layer


class Graph:

    def __init__(self, E=None, V=None) -> None:
        # if V is None:
        #     V = []
        # if E is None:
        #     E = []
        self.E, self.V = E, V

    def connect(self, from_=None, to=None, weight=1, e=None):
        if e:
            from_, to, weight = e.from_, e.to, e.weight
        else:
            e = from_.connect(v=to, weight=weight)
        from_.connect(v=to, weight=weight)
        if e not in self.E:
            self.E.append(e)
        if from_ not in self.V:
            self.V.append(from_)
        if to not in self.V:
            self.V.append(to)

    def __str__(self):
        s = '------------------  graph  -----------------\n'
        s += 'V=[' + ','.join([v.name for v in self.V]) + ']\n'
        s += 'E=' + ','.join([str(e) for e in self.E]) + '\n'
        s += '|V|={} |E|={}'.format(len(self.V), len(self.E)) + '\n'
        s += '--------------------------------------------'
        return s

    def transpose(self):
        G = Graph()
        G.V = [Kodkod(name=v.name, data=v.data) for v in self.V]
        G.E = [Rainbow(G.V[self.V.index(e.to)], G.V[self.V.index(e.from_)], weight=e.weight) for e in self.E]
        # G.V = V
        # G.E = E
        # for e in G.E:
        #     G.connect(e=e)
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
        if not E:
            return
        for e in E:
            self.connect(e=e)


class GraphAimed:
    pass


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
    V = [Kodkod(name=str(i)) for i in range(10)]
    r = Rainbow(from_=V[0], to=V[1], weight=3)
    G = Graph(V=V)
    G.connect(from_=V[1], to=V[2], weight=1)
    G.connect(from_=V[2], to=V[1], weight=1)
    G.connect(e=r)
    print(G)
    print(G.transpose())
    # print(V[1].Adj_str())
