class ListNode:
    def __init__(self, name=None, data=None, prev=None, next_=None):
        self.name = name, self.data, self.prev, self.next_ = name, data, prev, next_

    def __str__(self) -> str:
        return f'data: {self.data}, prev: {None if self.prev is None else self.prev.data}, next: {None if self.next_ is None else self.next_.data}'

    def __repr__(self):
        return f'{self.data}'


class List:
    def __init__(self, head=None, last=None, name=None, other=None):
        if other:  # copy constructor
            pass
        else:
            self.head, self.last, self.name, self.n = head, last, name, 0

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

    def __str__(self):
        p, s = self.head, 'head'
        while p:
            s += '->' + repr(p)
            p = p.next_
        s += '->last'
        return s

    def __repr__(self) -> str:
        p = self.head
        s = "--------------------------  list details  ----------------\n"
        while p is not None:
            s += p.__str__() + "\n"
            p = p.next_
        s += "---------------------------  n = {}  -----------------\n".format(self.n)
        return s

    def __add__(self, other, add_to_end=False):
        self.n += 1
        if self.head is None:
            self.head = self.last = other
        elif add_to_end:
            other.next_ = self.head
            self.head.prev = other
            self.head = other
        else:
            other.prev = self.last
            self.last.next_ = other
            self.last = other
        return self

    @staticmethod
    def arr_to_list(array):
        if len(array) == 0:
            return
        l = List()
        for item in array:
            l += ListNode(data=item)
        return l


if __name__ == '__main__':
    import copy

    a = [1, 3, 4]
    # # l = List(7)
    lis = List.arr_to_list([3, 4, 7, 8, 9])
    print(repr(lis))
    n1 = ListNode(data=8)
    lis.head = n1
    print(lis)
    #
    # lis1 = copy.deepcopy(lis)
    # print(lis1)

    # xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # zs = copy.deepcopy(xs)
    # print(xs)
    # zs[1] = 1
    # print('after:\n')
    # print(xs)
    # print(zs)

