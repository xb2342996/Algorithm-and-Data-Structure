## written by xiong
## date 2020-5-18

from List.list import List

class Node(object):
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedList(List):
    def __init__(self, nums):
        super().__init__()
        self.__head = None
        self.__tail = None
        if nums:
            for n in nums:
                self.add_value(n)

    def clear(self):
        self._size = 0
        self.__head = None
        self.__tail = None

    def add_value_at(self, value, index):
        self._range_check_for_add(index)

        if index == self._size:
            new_node = Node(value, self.__tail, None)
            if self._size == 0:
                self.__head = new_node
            else:
                self.__tail.next = new_node
            self.__tail = new_node
        else:
            next = self._get_node(index)
            prev = next.prev

            new_node = Node(value, prev, next)
            if index == 0:
                self.__head = new_node
            else:
                prev.next = new_node
            next.prev = new_node

        self._size += 1

    def remove_value_at(self, index):
        self._range_check(index)

        if index == 0:
            self.__head = self.__head.next
            self.__head.prev = None
        elif index == self._size - 1:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            node = self._get_node(index)
            prev = node.prev
            next = node.next

            prev.next = next
            next.prev = prev

        self._size -= 1

