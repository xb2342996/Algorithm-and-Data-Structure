## written by xiongbiao
## date 2020-5-19

from List.linkedlist import List
from List.doublelinkedlist import Node


class CycleDoubleLinkedList(List):
    def __init__(self, nums=None):
        super().__init__()
        self.__head = None
        self.__tail = None
        if nums:
            for n in nums:
                self.add_value(n)
    '''
    双向循环链表单独处理插入尾部，链表为空与不空状况，其他状况连接prev和next即可，插入头部修改头结点指针
    '''
    def add_value_at(self, value, index):

        if index == self._size:
            new_node = Node(value, self.__tail, self.__head)
            if self._size == 0:
                self.__head = new_node
                new_node.prev = new_node
                new_node.next = new_node
            else:
                self.__tail.next = new_node
                self.__head.prev = new_node
            self.__tail = new_node
        else:
            next = self._get_node(index)
            prev = next.prev
            new_node = Node(value, prev, next)
            next.prev = new_node
            prev.next = new_node
            if index == 0:
                self.__head = new_node

        self._size += 1

    '''
    删除节点，特殊处理只有一个节点情况的链表，删除其他节点注意改变头尾节点位置
    '''
    def remove_value_at(self, index):
        self._range_check(index)

        if self._size == 1:
            self.__head, self.__tail = None, None
        else:
            node = self._get_node(index)
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            if index == 0:
                self.__head = next
            elif index == self._size - 1:
                self.__tail = prev

        self._size -= 1

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
                s += '{}(prev:{}, next:{})'.format(node.value, node.prev.value, node.next.value)
            else:
                s += ', {}(prev:{}, next:{})'.format(node.value, node.prev.value, node.next.value)
            node = node.next
        s += '], Size: {}'.format(self._size)

        return s
nums = [1,2,3,4,5,6,7,8,9]
cycledouble = CycleDoubleLinkedList(nums)
cycledouble.add_value_at(100, 0)
print(cycledouble)
cycledouble.remove_value_at(0)
print(cycledouble)
cycledouble.remove_value_at(8)
for _ in range(cycledouble.size()):
    cycledouble.remove_value_at(0)
print(cycledouble)

