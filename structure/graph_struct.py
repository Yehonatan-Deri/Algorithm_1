import listnode


class kodkod(listnode.Node):
    def __init__(self, name=None, data=None, prev=None, next=None, pi=None, color=None, i=None, f=None, d=None):
        super().__init__(name, data, prev, next)
        self.pi, self.color, self.i, self.d, self.f = pi, color, i, d, f

    def __str__(self) -> str:
        return super().__str__()
