import copy
import numpy as np
import operator


class BinaryHeap:
    """
    @compare: define function for compare: max() for heap max or min() for heap mean
    """

    def __init__(self, arr=None, compare=max) -> None:
        self.compare, self.arr = compare, arr

    def father(self, i):
        if i < 0 or i >= len(self.arr) - 1:
            return False
        return i / 2 - 1 if i % 2 == 0 else i / 2

    def left(self, i):
        if i < 0 or i >= len(self.arr):
            return False
        return i * 2 + 1

    def right(self, i):
        if i < 0 or i >= len(self.arr):
            return False
        right = i * 2 + 2
        return right if right < len(self.arr) else False

    # efficiency: O(log n)
    def add(self, data):
        self.arr.append(data)
        self.heapify_up(len(self.arr) - 1)

    # efficiency: O(log n)
    def pop(self, i):
        data = self.arr[i]
        self.arr[i] = self.arr[0] + 1
        self.heapify_up(i)
        self.extract()
        return data

    # efficiency: O(log n)
    def extract(self):
        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]
        data = self.arr.pop(len(self.arr) - 1)
        self.heapify_down(0)
        return data

    # efficiency: O(n)
    @property
    def arr(self):
        return self.__arr

    # efficiency: O(n)
    @arr.setter
    def arr(self, arr):
        if not arr:
            self.__arr = []
            return
        self.__arr = copy.copy(arr)
        for i in range(len(arr) // 2, -1, -1):
            self.heapify_down(i)

    # efficiency: O(log n)
    def heapify_up(self, i):
        while i > 0:
            i_max = self.arr.index(self.compare(self.arr[i], self.arr[self.father(i)]))
            if i != i_max:
                self.arr[i], self.arr[self.father(i)], i = self.arr[self.father(i)], self.arr[i], i_max
            else:
                return

    # efficiency: O(log n)
    def heapify_down(self, i):
        while i < len(self.arr) // 2:
            r, l = self.left(i), self.right(i)  # indexes of right and left suns
            i_max = self.arr.index(self.compare([self.arr[x] for x in [i, r, l] if x is not False]))
            if i_max != i:
                self.arr[i], self.arr[i_max], i = self.arr[i_max], self.arr[i], i_max
            else:
                return

    @staticmethod
    def is_heap(arr, compare=max):
        for father in range(len(arr) // 2):
            l, r = father * 2 + 1, father * 2 + 2 if father * 2 + 2 < len(arr) else False
            if compare([arr[x] for x in [father, r, l] if x is not False]) != arr[father]:
                return False
        return True

    # efficiency: O(nlog n)
    @staticmethod
    def heap_sort(arr, compare=max):
        h = BinaryHeap(arr=arr, compare=compare)
        sort_arr = [h.extract() for i in range(len(arr) - 1, -1, -1)]
        return sort_arr

    def __str__(self):
        return 'size=' + str(len(self.arr)) + ', H=' + str(self.arr)


if __name__ == '__main__':
    a = [1, 4, 0, 9, 3, 5]
    a1 = [9, 5, 4, 3, 1, 0]
    b = BinaryHeap(arr=a, compare=max)
    print(b)
    print(BinaryHeap.heap_sort(a, compare=max))
    print(BinaryHeap.is_heap(a1, compare=min))
