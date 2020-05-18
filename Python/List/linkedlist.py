

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, nums=None):
        self._size = 0
        self.head = None
        if nums is not None:
            for i, n in enumerate(nums):
                self.add_value_at(n, i)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def clear(self):
        self.head = None
        self._size = 0

    def add_value(self, value):
        self.add_value_at(value, self._size)

    def add_value_at(self, value, index):
        self.__range_check_for_add(index)

        if index == 0:
            self.head = Node(value, self.head)
        else:
            node = self.__get_node(index - 1)
            node.next = Node(value, node.next)

        self._size += 1

    def remove_at_index(self, index):
        self.__range_check(index)

        if index == 0:
            value = self.head.value
            self.head = self.head.next
        else:
            node = self.__get_node(index - 1)
            value = node.next.value
            node.next = node.next.next

        self._size -= 1
        return value

    def remove_value(self, value):
        if self.head is None:
            return
        dummy = Node(0, self.head)
        node = dummy
        while node and node.next:
            if node.next.value == value:
                node.next = node.next.next
                self._size -= 1
            else:
                node = node.next
        self.head = dummy.next

    def reverse(self):
        cur = self.head
        next = cur.next
        while next:
            self.head.next = next.next
            next.next = cur
            cur = next
            next = self.head.next
        self.head = cur

    def get_middle(self):
        slow, fast = self.head, self.head
        index = 0
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            index += 1

        return slow, index

    def value_at(self, value):
        node = self.head
        nodes = []
        for i in range(self._size):
            if value == node.value:
                nodes.append(i)
            node = node.next
        return nodes

    def get_value(self, index):
        self.__range_check(index)
        node = self.__get_node(index)
        return node.value

    def set_value(self, index, value):
        self.__range_check(index)

        node = self.__get_node(index)
        old_value = node.value
        node.value = value
        return old_value

    def contains_value(self, value):
        return False if not self.value_at(value) else True

    def __get_node(self, index):
        node = self.head
        for i in range(index):
            node = node.next

        return node

    def __range_check(self, index):
        if index >= self._size or index < 0:
            raise IndexError('Index is out of range, Index must be in [0, ' + str(self._size) + ')')

    def __range_check_for_add(self, index):
        if index > self._size or index < 0:
            raise IndexError('Index is out of range, Index must be in [0, ' + str(self._size) + ']')

    def __repr__(self):

        s = 'LinkedList=['
        node = self.head
        s += str(node.value)
        for i in range(1, self._size):
            node = node.next
            s += ', {}'.format(node.value)
        s += '], Size: {}'.format(self._size)

        return s



nums1 = [3, 3, 1, 4, 5, 3, 3, 3, 3, 2, 6, 3, 3, 3, 3]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = LinkedList(nums2)
# containsvalue
# print(list.contains_value(100))
# print(list.contains_value(1))
# print(list.contains_value(89))
# setvalue
# print(list.set_value(0, 100))
# print(list.set_value(len(list) - 1, 44))
# getvalue
# print(list.get_value(len(list) - 1))
# print(list.get_value(0))
# reverse
# list.reverse()
# getmiddle
# print(list.get_middle())
# indexof
# print(list.value_at(3))
# remove
# list.remove_value(3)
# list.remove_at_index(0)
# list.remove_at_index(0)
# list.remove_at_index(0)
# list.remove_at_index(len(list) - 1)
# list.remove_at_index(2)
# add
# list.add_value(100)
# list.add_value_at(15, 0)
# list.add_value_at(867, 6)

print(list)