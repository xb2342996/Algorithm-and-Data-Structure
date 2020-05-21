## written by xiong biao
## date 2020-5-21

from Tree.rbtree import RedBlackTree

class TreeSet(object):
    def __init__(self):
        self.tree = RedBlackTree()

    def clear(self):
        self.tree.clear()

    def is_empty(self):
        self.tree.is_empty()

    def size(self):
        return self.tree.size()

    def add(self, value):
        self.tree.add_value(value)

    def contains(self, value):
        return self.tree.contains(value)

    def remove(self, value):
        self.tree.remove_value(value)

    def traversal(self):
        return self.tree.inorder_traversal()


def test_func():
    nums = [1, 2, 34, 4, 5, 6, 7, 7, 4, 32, 21, 1, 2]
    list_set = TreeSet()
    for n in nums:
        list_set.add(n)
    print(list_set.traversal())
    list_set.remove(7)
    print(list_set.contains(7))
    print(list_set.traversal())

test_func()