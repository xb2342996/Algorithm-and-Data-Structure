## written by xiong biao
## date 2020-5-22

class UnionFind():
    def __init__(self, capacity=None):

        if capacity < 0 or capacity is None:
            raise ValueError('capacity must be greater than 0')

        self._parents = [0] * capacity
        for i in range(capacity):
            self._parents[i] = i

    def show(self):
        print(self._parents)

    def find(self, index):
        return NotImplemented

    def union(self, index_1, index_2):
        return NotImplemented

    def is_same(self, index_1, index_2):
        return NotImplemented

    def _range_check(self, index):
        if index > len(self._parents) or index < 0:
            raise IndexError('index is out of range')

'''
Quick Find所有的节点都连在root上
'''
class UnionFind_QF(UnionFind):
    def __init__(self, capacity=None):
        super().__init__(capacity)

    def find(self, index):
        self._range_check(index)
        return self._parents[index]

    def union(self, index_1, index_2):
        p1 = self._parents[index_1]
        p2 = self._parents[index_2]
        for i in range(len(self._parents)):
            if self._parents[i] == p1:
                self._parents[i] = p2

    def is_same(self, index_1, index_2):
        return self.find(index_1) == self.find(index_2)

class UnionFind_QU(UnionFind):
    def __init__(self, capacity=None):
        super().__init__(capacity)

    def find(self, index):
        self._range_check(index)
        while self._parents[index] != index:
            index = self._parents[index]

        return index

    def union(self, index_1, index_2):
        p1 = self.find(index_1)
        p2 = self.find(index_2)
        if p1 == p2:
            return
        self._parents[p1] = p2

class UnionFind_QU_size(UnionFind_QU):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.__size = [1] * capacity


    def union(self, index_1, index_2):

        p1 = self.find(index_1)
        p2 = self.find(index_2)
        if p1 == p2:
            return

        if self.__size[p1] > self.__size[p2]:
            self._parents[p2] = p1
            self.__size[p1] += self.__size[p2]
        else:
            self._parents[p1] = p2
            self.__size[p2] += self.__size[p1]

    def show(self):
        super().show()
        print(self.__size)

class UnionFind_QU_rank(UnionFind_QU):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.__ranks = [1] * capacity

    def union(self, index_1, index_2):
        p1 = self.find(index_1)
        p2 = self.find(index_2)
        if p1 == p2:
            return

        if self.__ranks[p1] > self.__ranks[p2]:
            self._parents[p2] = p1
        elif self.__ranks[p1] < self.__ranks[p2]:
            self._parents[p1] = p2
        else:
            self._parents[p1] = p2
            self.__ranks[p2] += 1

    def show(self):
        super().show()
        print(self.__ranks)

class UnionFind_PC(UnionFind_QU_rank):
    def __init__(self, capacity):
        super().__init__(capacity)

    def find(self, index):
        self._range_check(index)
        if self._parents[index] != index:
            self._parents[index] = self.find(self._parents[index])

        return self._parents[index]

    def show(self):
        print(self._parents)

class UnionFind_PS(UnionFind_QU_rank):
    def __init__(self, capacity):
        super().__init__(capacity)

    def find(self, index):
        self._range_check(index)
        while index != self._parents[index]:
            p = self._parents[index]
            self._parents[index] = self._parents[p]
            index = p
        return index

    def show(self):
        print(self._parents)

class UnionFind_PH(UnionFind_QU_rank):
    def __init__(self, capacity):
        super().__init__(capacity)

    def find(self, index):
        self._range_check(index)
        while index != self._parents[index]:
            self._parents[index] = self._parents[self._parents[index]]
            index = self._parents[index]
        return index

    def show(self):
        print(self._parents)

def test_func_uf_ps():
    uf = UnionFind_PS(capacity=7)
    uf.union(1, 0)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)
    uf.union(4, 5)
    uf.union(5, 6)
    uf.show()
    print(uf.find(2))

def test_func_uf_pc():
    uf = UnionFind_PC(capacity=7)
    uf.union(1, 0)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(3, 1)
    uf.show()

def test_func_qu_r():
    uf = UnionFind_QU_rank(capacity=7)
    uf.union(1, 0)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(3, 1)
    uf.show()


def test_func_qu_s():
    uf = UnionFind_QU_size(capacity=7)
    uf.union(1, 0)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(3, 1)
    uf.show()

def test_func_qu():
    uf = UnionFind_QU(capacity=7)
    uf.union(1, 0)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(3, 1)
    uf.show()

def test_func_qf():
    uf = UnionFind_QF(capacity=7)
    uf.union(1, 0)
    uf.union(0, 2)
    uf.union(3, 1)
    print(uf.is_same(4, 1))
    uf.show()

test_func_uf_ps()