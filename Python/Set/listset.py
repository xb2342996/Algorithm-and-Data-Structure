## written by xiongbiao
## date 2020-5-21

from List.linkedlist import LinkedList

class ListSet(object):
    def __init__(self):
        self.list = LinkedList()

    def size(self):
        return self.list.size()

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.list.clear()

    def add(self, value):
        if self.contains(value):
            return
        self.list.add_value(value)

    def remove(self, value):
        index = self.list.index_of(value)
        if index != -1:
            self.list.remove_value(value)

    def contains(self, value):
        return self.list.contains_value(value)

    def traversal(self):
        sets = []
        size = self.size()
        for i in range(size):
            sets.append(self.list.get_value(i))

        return sets

def test_fun():
    nums = [1,2,34,4,5,6,7,7,4,32,21,1,2]
    list_set = ListSet()
    for n in nums:
        list_set.add(n)

    list_set.remove(7)
    print(list_set.contains(7))
    print(list_set.traversal())


test_fun()


