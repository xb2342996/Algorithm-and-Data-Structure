## written by xiong biao
## date 2020-5-24

import random

class SkipList(object):

    class Node(object):
        def __init__(self, key, value, level):
            self.key = key
            self.value = value
            self.nexts = [None] * level
            # random.seed(10)

    def __init__(self):
        self._levels = 0
        self._size = 0
        self.MAX_LEVEL = 32
        self.probablity = 0.25
        self.__first = SkipList.Node(None, None, self.MAX_LEVEL)

    def put(self, key, value):
        self.__check_key(key)
        node = self.__first
        prevs = [None] * self._levels
        for i in range(self._levels)[::-1]:
            if node.nexts[i]:
                cmp = node.nexts[i].key - key
            else:
                cmp = -1
            while node.nexts[i] and cmp < 0:
                node = node.nexts[i]
                cmp = node.key - key

            if cmp == 0:
                old_value = node.nexts[i].value
                node.nexts[i].value = value
                return old_value

            prevs[i] = node

        new_level = self.random_level()
        new_node = SkipList.Node(key, value, new_level)

        for i in range(new_level):

            if i >= self._levels:
                self.__first.nexts[i] = new_node
            else:
                new_node.nexts[i] = prevs[i].nexts[i]
                prevs[i].nexts[i] = new_node

        self._size += 1
        self._levels = max(new_level, self._levels)
        return None

    def random_level(self):
        level = 1
        while random.uniform(0, 1) < self.probablity and level < self.MAX_LEVEL:
            level += 1

        return level


    def get(self, key):
        self.__check_key(key)
        node = self.__first
        for i in range(self._levels)[::-1]:
            while node.nexts[i]:
                if node.nexts[i].key == key:
                    return node.nexts[i].value
                if node.nexts[i].key < key:
                    node = node.nexts[i]
        return None

    def remove(self, key):
        self.__check_key(key)
        node = self.__first
        prevs = [None] * self._levels
        exits = False
        for i in range(self._levels)[::-1]:
            if node.nexts[i]:
                cmp = node.nexts[i].key - key
            else:
                cmp = -1
            while node.nexts[i] and cmp < 0:
                node = node.nexts[i]
                cmp = node.key - key

            if cmp == 0:
                exits = True
            prevs[i] = node

        if not exits:
            return None

        remove_node = node.nexts[0]
        for i in range(len(remove_node.nexts)):
            prevs[i].nexts[i] = remove_node.nexts[i]

        new_level = self._levels
        while new_level > 0 and self.__first.nexts[new_level]:
            self._levels = new_level
            new_level -= 1

        self._size -= 1
        return remove_node.value

    def __check_key(self, key):
        if not key:
            raise ValueError('key cannot be None')

    def __repr__(self):
        s = ''

        for i in range(self._levels)[::-1]:
            node = self.__first
            while node.nexts[i]:
                s += str(node.nexts[i].key) + '-' + str(node.nexts[i].value) + '('+str(len(node.nexts[i].nexts))+'), '
                node = node.nexts[i]
            s += '\n'
        return s

sl = SkipList()

for i in range(16):
    sl.put(i, i + 10)

print(sl)
sl.remove(10)
print(sl)