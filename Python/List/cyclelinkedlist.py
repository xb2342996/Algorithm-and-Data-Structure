
## written by xiongbiao
## date 2020-5-19


from List.list import List
from List.linkedlist import Node

class CycleLinkedList(List):
    def __init__(self, nums=None):
        super().__init__()
        self.__head = None
        if nums:
            for n in nums:
                self.add_value(n)
    '''
    添加节点，空链表，插入头结点，其他节点
    '''
    def add_value_at(self, value, index):
        self._range_check_for_add(index)
        if index == 0:
            last = self._get_node(self._size - 1)

            new_node = Node(value, self.__head)
            if last is None:
                new_node.next = new_node
            else:
                last.next = new_node
            self.__head = new_node
        else:
            node = self._get_node(index - 1)
            new_node = Node(value, node.next)
            node.next = new_node

        self._size += 1
    '''
    删除某个位置节点，删除头结点，当节点只有一个元素和节点有多于一个元素特殊处理；删除其他节点
    '''
    def remove_value_at(self, index):
        self._range_check(index)
        if index == 0:
            value = self.__head.value
            if self._size == 1:
                self.__head = None
            else:
                last = self._get_node(self._size - 1)
                self.__head = self.__head.next
                last.next = self.__head
        else:
            prev = self._get_node(index - 1)
            value = prev.next.value
            prev.next = prev.next.next

        self._size -= 1

        return value

    def _get_node(self, index):
        node = self.__head
        for i in range(index):
            node = node.next

        return node

    '''
        获取index的value
        '''

    def get_value(self, index):
        self._range_check(index)
        node = self._get_node(index)
        return node.value

    '''
    修改index的value
    '''

    def set_value(self, index, value):
        self._range_check(index)

        node = self._get_node(index)
        old_value = node.value
        node.value = value
        return old_value

    def __repr__(self):
        s = 'LinkedList=['
        node = self.__head

        for i in range(0, self._size):
            if i == 0:
                s += '{}(next: {})'.format(node.value, node.next.value)
            else:
                s += ', {}(next: {})'.format(node.value, node.next.value)
            node = node.next
        s += '], Size: {}'.format(self._size)

        return s


cycle = CycleLinkedList([1,2,3,4,5,6,7,8])
# cycle.add_value_at(10, 0)
# cycle.add_value_at(15, 9)
cycle.remove_value_at(0)
cycle.remove_value_at(0)
cycle.remove_value_at(0)
cycle.remove_value_at(0)
cycle.remove_value_at(0)
cycle.remove_value_at(0)
cycle.remove_value_at(0)
cycle.remove_value_at(0)
# cycle.remove_value_at(0)

print(cycle)