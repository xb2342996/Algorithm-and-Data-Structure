## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。
你可以假设这个整数除了 0 本身，没有任何前导的 0。
这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。
'''

class Solution(object):
    '''
    找到最右边不为9的节点加1，将后面的节点全部变为0，如果虚拟头节点为0返回next，为1返回dummy
    时间复杂度O（N） 空间复杂度O（1）
    '''
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        nine = dummy
        while head:
            if head.val != 9:
                nine = head
            head = head.next

        node = nine.next
        while node:
            node.val = 0
            node = node.next

        nine.val += 1

        return dummy if dummy.val == 1 else dummy.next


l = make_linkedlist([1, 2, 3])
show_linkedlist(Solution().plusOne(l))
