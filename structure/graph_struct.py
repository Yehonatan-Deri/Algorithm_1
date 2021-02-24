import listnode
import copy


# import dllist
class Rainbow:

    def __init__(self, from_, to, weight=1) -> None:
        self.from_, self.to, self.weight = from_, to, weight
        # Kodkod.connect(self)

    def __str__(self):
        return f'({self.from_.name}->{self.to.name},w={self.weight}'


class Kodkod():
    def __init__(self, name=None, data=None, Adj=None, rainbow=None):
        if rainbow is None:
            rainbow = []
        if Adj is None:
            Adj = []
        self.name, self.data, self.Adj, self.rainbow = name, data, Adj, rainbow

    def connect(self, v=None, weight=1, e=None):
        if e:
            if e.to not in self.Adj:
                self.Adj += e.to
                self.rainbow += e
        elif v:
            self.Adj += v
            e = Rainbow(self, v, weight=weight)
            self.rainbow += e
        return e

    def disconnect(self, v):
        if v in self.Adj:
            i = self.Adj.index(v)
            self.Adj -= v
            del self.rainbow[i]

    def is_connect(self, v):
        return v in self.Adj

    def __str__(self) -> str:
        return f'name: {self.name}, Adj: {self.Adj}'
    #
    # @staticmethod
    # def connect(e):
    #     e.ffrom.Adj += e.to.Adj
    #     e.ffrom.rainbow.


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
        if V is None:
            V = []
        if E is None:
            E = []
        self.E, self.V = E, V

    def connect(self, from_=None, to=None, weight=1, e=None):
        if e:
            if e not in self.E:
                self.E += e
                e.from_.connect(e)
        else:
            self.E += from_.connect(from_=from_, to=to, weight=weight)
            from_.connect(to)
        if e.from_ not in self.V:
            self.V += e.from_
        if e.to not in self.V:
            self.V += e.to


# def __add__(self, v):
#     self.V += v


class GraphAimed:
    pass


class GraphNotAimed(Graph):

    def __init__(self, E=None, V=None) -> None:
        super().__init__(E, V)

    def connect(self, from_=None, to=None, weight=1, e=None):
        super().connect(from_, to, weight, e)
        if e:
            e.to.connect(v=from_, weight=e.weight)
        else:
            super().connect(from_=to, to=from_, weight=weight)

    def transpose(self):
        G = Graph(V=copy.deepcopy(self.V))
        for e in self.E:
            G.connect(from_=e.to, to=e.from_, weight=e.weight)

        return G


if __name__ == '__main__':
    G = Graph()
