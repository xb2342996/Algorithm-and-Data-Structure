## written by xiongbiao
## date 2020-5-28
'''
设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。
注意: 允许出现重复元素。
insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关
'''


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.list = []
        self.index = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.index[val].add(len(self.list))
        self.list.append(val)
        return len(self.index[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.index[val]:
            return False
        remove, last = self.index[val].pop(), self.list[-1]
        self.list[remove] = last
        self.index[last].add(remove)
        self.index[last].discard(len(self.list) - 1)
        self.list.pop()
        return True


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        from random import choice
        return choice(self.list)