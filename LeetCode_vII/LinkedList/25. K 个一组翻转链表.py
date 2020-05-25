## written by xiongbiao
## date 2020-5-25

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''

class Solution(object):
    '''
    使用栈存储要反转的部分，当栈内元素数量与要反转的数量一样时，将栈内所有元素出栈，重新拼成一个新的链表拼接时将每个拼接的节点的next置为None
    时间复杂度O（N)，空间复杂度O(K)
    '''
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        stack = []
        dummy = ListNode(0)
        new_head = dummy
        node = head
        while node:
            stack.append(node)
            node = node.next
            if len(stack) == k:
                for i in range(k):
                    poped = stack.pop()
                    poped.next = None
                    dummy.next = poped
                    dummy = dummy.next

        if len(stack) != 0:
            dummy.next = stack.pop(0)

        return new_head.next
    '''
    K个一组翻转链表，子问题位翻转链表问题，遍历链表，将要反转的链表区域传递进去，翻转后拼接头尾，并返回尾结点作为下一次拼接的头结点
    时间复杂度O(N)， 空间复杂度O（1）
    '''
    # def reverseKGroup(self, head, k):
    #     """
    #     :type head: ListNode
    #     :type k: int
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #     if k == 0 or k == 1:
    #         return head
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     start = dummy
    #     end = head
    #     count = 0
    #     while end:
    #         count += 1
    #         if count % k == 0:
    #             start = self.reverseList(start, end)
    #             end = start.next
    #         else:
    #             end = end.next
    #     return dummy.next
    #
    # def reverseList(self, start, end):
    #     prev = start
    #     tail = end.next
    #     head, cur = start.next, start.next
    #     next = cur.next
    #     while cur is not end:
    #         head.next = next.next
    #         next.next = cur
    #         cur = next
    #         next = head.next
    #     prev.next = cur
    #     head.next = tail
    #     return head


l = make_linkedlist([1,2,3,4,5,6])
l = Solution().reverseKGroup(l, 4)
show_linkedlist(l)