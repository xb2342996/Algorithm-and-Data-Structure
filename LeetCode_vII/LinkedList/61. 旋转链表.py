## written by xiongbiao
## date 2020-5-26
from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

class Solution(object):
    '''
    找到链表的头部和尾部将头尾节点相连，一个节点指向头部一个节点指向尾部，计算头结点需要移动的距离=长度-移动的次数，移动头尾节点，将头尾节点断开，返回头结点
    时间复杂度O（N）空间复杂度O(1)
    '''
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None or k == 0:
            return head
        node = head
        size = 0
        while node.next:
            size += 1
            node = node.next
        size += 1
        times = k % size
        tail = node
        tail.next = head
        for _ in range(size - times):
            head = head.next
            tail = tail.next
        tail.next = None
        return head

    '''
    虚拟头结点的头插法，将尾结点插入头结点，循环K次，如果K很大需要对K取模
    时间复杂度O（KN）空间复杂度O(1)
    '''
    # def rotateRight(self, head, k):
    #     """
    #     :type head: ListNode
    #     :type k: int
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #     if head.next is None or k == 0:
    #         return head
    #     node = head
    #     size = 0
    #     while node:
    #         node = node.next
    #         size += 1
    #     times = k % size
    #
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     for i in range(times):
    #         dummy = self.rotateOnce(dummy)
    #
    #     return dummy.next
    #
    # def rotateOnce(self, head):
    #     node = head
    #     while node.next.next:
    #         node = node.next
    #     tail = node.next
    #     node.next = tail.next
    #     tail.next = head.next
    #     head.next = tail
    #     return head

l = make_linkedlist([1,2,3,4,5])
show_linkedlist(Solution().rotateRight(l, 2))




