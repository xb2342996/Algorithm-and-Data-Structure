## written by xiong
## date 2020-5-18

from List.list import List

class Node(object):
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedList(List):
    def __init__(self, nums=None):
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
    '''
    添加元素，四种情况，插入空链表，插入非空头结点，插入非空尾结点，插入中间
    '''
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

    '''
    删除元素，四种情况，删除非空头结点，删除非空尾结点，删除中间
    '''
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

    def get_value(self, index):
        return self._get_node(index).value

    def set_value(self, index, value):
        node = self._get_node(index)
        old_value = node.value
        node.value = value
        return old_value
    '''
    查找索引的节点，大于size一半从尾部开始找，小于size从头部开始找，增加效率
    '''
    def _get_node(self, index):

        if index > (self._size >> 1):
            node = self.__tail
            for _ in range(self._size-1, index):
                node = node.prev
        else:
            node = self.__head
            for _ in range(index):
                node = node.next

        return node

    def __repr__(self):
        s = 'LinkedList=['
        node = self.__head

        for i in range(0, self._size):
            if i == 0:
                s += '{}(prev: {}, next:{})'.format(node.value, None, node.next.value)
            if not node.next:
                s += ', {}(prev: {}, next:{})'.format(node.value, node.prev.value, node.next.value)
            else:
                s += ', {}(prev: {}, next:{})'.format(node.value, node.prev.value, None)
            node = node.next
        s += '], Size: {}'.format(self._size)

        return s


# doublelink = DoubleLinkedList([1,2,3,4,5,6,7,8])
# doublelink.remove_value_at(1)
# doublelink.remove_value_at(0)
# doublelink.remove_value_at(5)
# doublelink.add_value_at(10, 0)
# doublelink.add_value_at(19, 6)
# doublelink.add_value_at(72, 3)
#
# print(doublelink)




