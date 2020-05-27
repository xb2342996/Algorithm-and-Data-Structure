## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
class Solution(object):
    '''
    2个一组翻转链表，获取要反转的起始位置的前一个节点和翻转的最后一个节点，翻转后拼接到原链表上，前一个节点等于翻转后的尾结点
    时间复杂度O（N）空间复杂度O（1）
    '''
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        count = 0
        node = prev.next
        while node:
            count += 1
            if count % 2 == 0:
                prev = self.swap(prev, node)
                node = prev.next
            else:
                node = node.next

        show_linkedlist(dummy.next)


    def swap(self, start, end):
        prev = start
        head = start.next
        tail = end.next
        cur, next = head, head.next

        while cur is not end:
            head.next = next.next
            next.next = cur
            cur = next
            next = head.next
        prev.next = cur
        head.next = tail
        return head

l = make_linkedlist([1,2,3,4,5])
Solution().swapPairs(l)