## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        dummy = ListNode(0)

        extra = 0
        while stack1 or stack2:
            n1 = stack1.pop() if stack1 else 0
            n2 = stack2.pop() if stack2 else 0

            sum = n1 + n2 + extra
            node = ListNode(sum % 10)
            extra = sum // 10
            node.next = dummy.next
            dummy.next = node

        if extra != 0:
            node = ListNode(extra)
            node.next = dummy.next
            dummy.next = node
        return dummy.next


l1 = make_linkedlist([9,9,9,9,9])
l2 = make_linkedlist([5,6,4])
show_linkedlist(Solution().addTwoNumbers(l1, l2))