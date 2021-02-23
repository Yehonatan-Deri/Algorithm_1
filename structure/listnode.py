class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f'data: {self.data}, prev: {None if self.prev is None else self.prev.data}, next: {None if self.next is None else self.next.data}'


class List:
    def __init__(self, head=None, last=None, other=None):
        self.head = head
        self.last = last
        self.n = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.__head = head

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, last):
        self.__last = last

    def __str__(self) -> str:
        p = self.head
        s = "--------------------------  list details  ----------------\n"
        while p is not None:
            s += p.__str__() + "\n"
            p = p.next
        s += "---------------------------  n = {}  -----------------\n".format(self.n)
        return s

    def __add__(self, other, add_to_end=False):
        self.n += 1
        if self.head is None:
            self.head = self.last = other
        if add_to_end:
            other.prev = self.last
            self.last.next = other
            self.last = other
        else:
            other.next = self.head
            self.head.prev = other
            self.head = other
        return self

    @staticmethod
    def create_list(array):
        if len(array) == 0:
            return
        l = List()
        for item in array:
            l += Node(item)
            # p.next = Node(item, prev=p)
            # p = p.next
        return l


if __name__ == '__main__':
    a = [1, 3, 4]
    l = List(7)
    lis = List.create_list(a)
    n1 = Node(4)
    lis += n1
    print(lis)
