#  written by xiongbiao
#  date: 2020-5-18

from List.list import List

'''
链表思路：
1. 虚拟头结点
2. 快慢指针
3. 无法获得节点时，value覆盖
4。 多指针
5.  长短不同的链表，多个链表拼在一起
'''

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList(List):
    def __init__(self, nums=None):
        super().__init__()
        self.__head = None
        if nums:
            for i, n in enumerate(nums):
                self.add_value(n)

    def clear(self):
        self.__head = None
        self._size = 0

    '''
    添加一个值在链表中，边界条件检测，区分插入位置，头部修改拼接头结点，其他位置获取插入节点前一个节点，修改节点参数，修改元素个数
    '''
    def add_value_at(self, value, index):
        self._range_check_for_add(index)

        if index == 0:
            self.__head = Node(value, self.__head)
        else:
            node = self._get_node(index - 1)
            node.next = Node(value, node.next)

        self._size += 1

    '''
    移除链表中的一个值，边界条件检测，区分移除位置，头部修改头结点，其他位置获取插入节点前一个节点，修改节点参数，元素个数 -1
    '''
    def remove_value_at(self, index):
        self._range_check(index)

        if index == 0:
            value = self.__head.value
            self.__head = self.__head.next
        else:
            node = self._get_node(index - 1)
            value = node.next.value
            node.next = node.next.next

        self._size -= 1
        return value

    '''
    移除链表中的某个值，使用虚头结点，从虚头结点遍历，如果节点的下一个节点等于要删除的值，修改节点的next值，node不变，元素个数-1
    否则继续遍历下一个节点，
    '''
    def remove_value(self, value):
        if self.head is None:
            return
        dummy = Node(0, self.__head)
        node = dummy
        while node and node.next:
            if node.next.value == value:
                node.next = node.next.next
                self._size -= 1
            else:
                node = node.next
        self.__head = dummy.next

    '''
    反转链表，3指针head，cur，next，head不动，head的next指向next的next，next指向cur，cur和next向后移动
    '''
    def reverse(self):
        cur = self.__head
        next = cur.next
        while next:
            self.head.next = next.next
            next.next = cur
            cur = next
            next = self.__head.next
        self.__head = cur

    '''
    获取链表的中间点索引和node，快慢指针，当快指针的next和next.next不空，快指针走2步，慢指针走一步
    '''
    def get_middle(self):
        slow, fast = self.__head, self.__head
        index = 0
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            index += 1

        return slow, index

    '''
    返回链表中等于value的所有节点
    '''
    def value_at(self, value):
        node = self.__head
        nodes = []
        for i in range(self._size):
            if value == node.value:
                nodes.append(i)
            node = node.next
        return nodes

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

    def contains_value(self, value):
        return False if not self.value_at(value) else True

    def _get_node(self, index):
        node = self.__head
        for i in range(index):
            node = node.next

        return node

    def __repr__(self):
        s = 'LinkedList=['
        node = self.__head

        for i in range(1, self._size):
            if i == 0:
                s += str(node.value)
            else:
                s += ', {}'.format(node.value)
            node = node.next

        s += '], Size: {}'.format(self._size)

        return s

def test_func():
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

# test_func()