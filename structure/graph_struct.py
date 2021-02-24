import listnode


# import dllist
class Rainbow:

    def __init__(self, ffrom, to, weight=1) -> None:
        self.ffrom, self.to, self.weight = ffrom, to, weight

    def __str__(self):
        return f'({self.ffrom.name}->{self.to.name},w={self.weight}'


class Kodkod():
    def __init__(self, name=None, data=None, Adj=None):
        if Adj is None:
            Adj = []
        self.name, self.data, self.Adj = name, data, Adj

    def connect(self, v):
        if v not in self.Adj:
            self.Adj += v

    def disconnect(self, v):
        if v in self.Adj:
            self.Adj -= v

    def __str__(self) -> str:
        return f'name: {self.name}, Adj: {self.Adj}'


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

    # def __add__(self, v):
    #     self.V += v



class GraphAimed:
    pass


class GraphNotAimed(Graph):

    def __init__(self, E=None, V=None) -> None:
        super().__init__(E, V)


if __name__ == '__main__':
    a = ['a', 'b']
    a.remove('d')
    print(a)
