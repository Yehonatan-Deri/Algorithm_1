class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f'data: {self.data}, prev: {None if self.prev is None else self.prev.data}, next: {None if self.next is None else self.next.data}'


class List:
    def __init__(self, head=None, last=None, n=0, other=None):
        self.head = head
        self.last = last
        self.n = 0

    @property
    def head(self):
        return self.head

    @head.setter
    def head(self, node):
        self.head = node

    # @head.getter
    # def head(self):
    #     return

    # @property

    # def last(self):
    #     return self.last
    #
    # @property
    # def n(self):
    #     return self.n

    def __str__(self) -> str:
        p = self.head
        s = "--------------------------  list details  ----------------\n"
        while p is not None:
            s += p.__str__() + "\n"
            p = p.next
        s += "-------------------------------------------------------\n"
        return s

    def __add__(self, other, add_to_end=False):
        self.n += 1
        if self.head is None:
            self.head = self.last = other
            return List()
        # if add_to_end:
        #
        # self.head.next = other

    @staticmethod
    def create_list(array):
        lis = List()
        p = Node(array[0])
        lis.head = p
        for item in array[1:]:
            p.next = Node(item, prev=p)
            p = p.next
        return lis


if __name__ == '__main__':
    a = [1, 3, 4]
    # lis = List.create_list(a)
    n1 = Node(4)
    # lis += n1
    print(n1)
