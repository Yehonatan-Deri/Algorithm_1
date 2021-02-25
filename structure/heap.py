import copy


class BinaryHeap:

    def __init__(self, arr=None, max_=True) -> None:
        self.max_, self.arr = max_, arr

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
        self.__arr = copy.deepcopy(arr)
        for i in range(len(arr) // 2, -1, -1):
            self.heapify_down(i)

    # efficiency: O(log n)
    def heapify_up(self, i):
        if self.max_:
            while i > 0:
                father = self.father(i)
                self.arr[i], self.arr[father], i = min(self.arr[i], self.arr[father]), max(self.arr[i],
                                                                                           self.arr[father]), father
        else:
            while i > 0:
                father = self.father(i)
                self.arr[i], self.arr[father], i = max(self.arr[i], self.arr[father]), min(self.arr[i],
                                                                                           self.arr[father]), father

    # efficiency: O(log n)
    def heapify_down(self, i):
        if self.max_:  # True or
            while i < len(self.arr) // 2:
                left, right = self.left(i), self.right(i)
                max_val = i if self.arr[i] > self.arr[left] else left
                self.arr[i], self.arr[left] = max(self.arr[i], self.arr[left]), min(self.arr[i], self.arr[left])
                if right:
                    max_val = max_val if self.arr[i] > self.arr[right] else right
                    self.arr[i], self.arr[right] = max(self.arr[i], self.arr[right]), min(self.arr[i], self.arr[right])
                if i == max_val:
                    break
                else:
                    i = max_val
        else:
            while i < len(self.arr) // 2:
                left, right = self.left(i), self.right(i)
                min_val = i if self.arr[i] < self.arr[left] else left
                self.arr[i], self.arr[left] = min(self.arr[i], self.arr[left]), max(self.arr[i], self.arr[left])
                if right:
                    min_val = min_val if self.arr[i] < self.arr[right] else right
                    self.arr[i], self.arr[right] = min(self.arr[i], self.arr[right]), max(self.arr[i], self.arr[right])
                if i == min_val:
                    break
                else:
                    i = min_val

    @staticmethod
    def is_heap(h, max_=True):
        h_ = BinaryHeap(max_=max_)
        h_.arr, h_.n = h, len(h)
        if max_:
            for father in range(len(h) // 2):
                if h_.arr[father] < h_.arr[h_.left(father)] or (
                        h_.right(father) and h_.arr[father] < h_.arr[h_.left(father)]):
                    return False
        else:
            for father in range(len(h) // 2):
                if h_.arr[father] > h_.arr[h_.left(father)] or (
                        h_.right(father) < h_.n and h_.arr[father] > h_.arr[h_.left(father)]):
                    return False
        return True

    # efficiency: O(nlog n)
    @staticmethod
    def heap_sort(arr, max_=True):
        h = BinaryHeap(arr=arr, max_=max_)
        l = [h.extract() for i in range(len(arr) - 1, -1, -1)]
        return l

    def __str__(self):
        return 'size=' + str(len(self.arr)) + ', H=' + str(self.arr)


if __name__ == '__main__':
    # for i in range(9, 0, -1):
    #     print(i)
    a = [1, 4, 0, 9, 3, 5, 7, -9, 89]
    b = BinaryHeap(arr=a)

    print(BinaryHeap(arr=a, max_=True))
    print(a)
    print(BinaryHeap.heap_sort(a))
    h = BinaryHeap()
    h.arr = a
    print(h)
    print(a)
