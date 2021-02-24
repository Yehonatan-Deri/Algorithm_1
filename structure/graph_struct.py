import listnode


# import dllist
class Rainbow:

    def __init__(self, ffrom, to, weight=1) -> None:
        self.ffrom, self.to, self.weight = ffrom, to, weight
        # Kodkod.connect(self)

    def __str__(self):
        return f'({self.ffrom.name}->{self.to.name},w={self.weight}'


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

    def connect(self, ffrom=None, to=None, weight=1, e=None):
        if e:
            if e not in self.E:
                self.E += e
                e.ffrom.connect(e)
        else:
            self.E += ffrom.connect(ffrom=ffrom, to=to, weight=weight)
            ffrom.connect(to)
        if e.ffrom not in self.V:
            self.V += e.ffrom
        if e.to not in self.V:
            self.V += e.to


# def __add__(self, v):
#     self.V += v


class GraphAimed:
    pass


class GraphNotAimed(Graph):

    def __init__(self, E=None, V=None) -> None:
        super().__init__(E, V)

    def connect(self, ffrom=None, to=None, weight=1, e=None):
        super().connect(ffrom, to, weight, e)
        if e:
            e.to.connect(v=ffrom, weight=e.weight)
        else:
            super().connect(ffrom=to, to=ffrom, weight=weight)


if __name__ == '__main__':
    a = ['a', 'b']
    a.remove('d')
    print(a)
