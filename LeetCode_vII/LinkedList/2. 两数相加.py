## written by xiongbiao
## date 2020-5-25

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

class Solution(object):
    '''
    创建一个虚拟头结点，按位遍历两个链表，如果其中一个有值另一个为空则另一个为0，相加处理进位值，循环解释后若进位值为1，在拼接一位
    '''
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        extra = 0
        dummy = ListNode(0)
        head = dummy
        while l1 or l2:
            if l1:
                n1 = l1.val
            else:
                n1 = 0
            if l2:
                n2 = l2.val
            else:
                n2 = 0

            res = (n1 + n2 + extra) % 10
            extra = (n1 + n2 + extra) // 10
            dummy.next = ListNode(res)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            dummy = dummy.next

        if extra != 0:
            dummy.next = ListNode(extra)
        return head.next


l1 = make_linkedlist([9, 9])
l2 = make_linkedlist([1])
l3 = Solution().addTwoNumbers(l1, l2)
show_linkedlist(l3)