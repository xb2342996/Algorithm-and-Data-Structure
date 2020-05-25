## written by xiongbiao
## date 2020-5-25

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
'''

class Solution(object):
    '''
    快慢指针 + 虚拟头结点，确保头结点可以删除第一个头结点
    '''
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None and n == 1:
            return None
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        node, cur = dummy, dummy
        while node:
            if count > n:
                cur = cur.next
            node = node.next
            count += 1

        cur.next = cur.next.next
        return dummy.next


l = make_linkedlist([1])
show_linkedlist(Solution().removeNthFromEnd(l, 1))