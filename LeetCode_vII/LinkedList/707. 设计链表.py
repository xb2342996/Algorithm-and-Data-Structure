## written by xiongbiao
## date 2020-5-25

'''

设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
在链表类中实现这些功能：
get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
'''


class MyLinkedList(object):

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    '''
    基本链表操作
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index == 0:
            return self.head.val

        node = self.head
        for i in range(self.size):
            if i == index:
                return node.val
            node = node.next
        return -1


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return

        new_node = MyLinkedList.ListNode(val)
        if self.size == 0:
            self.head = new_node
            self.size += 1
            return

        if index <= 0:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node

        self.size += 1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            node.next = node.next.next

        self.size -= 1

    def print(self):

        node = self.head
        for i in range(self.size):
            print(node.val)
            node = node.next


obj = MyLinkedList()
obj.addAtHead(2)
obj.deleteAtIndex(1)
obj.addAtHead(2)
obj.addAtHead(7)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(5)
obj.addAtTail(5)
obj.get(6)
obj.deleteAtIndex(6)
obj.deleteAtIndex(4)
obj.print()
